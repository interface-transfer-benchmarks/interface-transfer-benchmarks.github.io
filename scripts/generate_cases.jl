include(joinpath(@__DIR__, "cases.jl"))
include(joinpath(@__DIR__, "references.jl"))
include(joinpath(@__DIR__, "results.jl"))

function canonical_asset_path(path::AbstractString)
    normalized = replace(path, "\\" => "/")
    normalized = replace(normalized, r"^(\.\./)+" => "")
    normalized = replace(normalized, r"^/+" => "")
    return normalized
end

function asset_url(path::AbstractString)
    return "../../" * canonical_asset_path(path)
end

function result_figure_url(case_id::AbstractString)
    directory = joinpath(REPO_ROOT, "figures", "results")
    isdir(directory) || return Tuple{String,String}[]
    names = sort([name for name in readdir(directory)
                  if startswith(name, case_id * "-") && endswith(name, ".svg")])
    # the observable first, then the convergence: the figure that says what the
    # case measures before the one that says how fast it converges
    order = name -> (endswith(name, "-sh.svg") ? 0 : 1, name)
    return [(splitext(name)[1], asset_url(joinpath("figures", "results", name)))
            for name in sort(names; by = order)]
end

function rewrite_relative_links(body::AbstractString)
    return replace(body, r"(\]\(|src=\")(?:\.\./|/)*((?:data|figures|results)/)" => s"\1../../\2")
end

function rewrite_math(body::AbstractString)
    lines = split(body, '\n'; keepempty=true)
    rewritten = String[]
    in_code = false
    in_math = false

    for line in lines
        stripped = strip(line)
        if startswith(stripped, "```") && !in_math
            in_code = !in_code
            push!(rewritten, line)
            continue
        end

        if !in_code && stripped == "\$\$"
            push!(rewritten, in_math ? "```" : "```math")
            in_math = !in_math
            continue
        end

        if !in_code && !in_math
            line = replace(line, r"(?<!\\)\$([^$\n]+?)(?<!\\)\$" => s"``\1``")
        end

        push!(rewritten, line)
    end

    return join(rewritten, "\n")
end

function strip_title(body::AbstractString)
    return replace(body, r"^\s*#\s[^\n]*\n+" => ""; count = 1)
end

function citation_link(key::AbstractString, entries)
    haskey(entries, key) || return "@" * key
    return "[" * citation_label(entries[key]) * "](../references.md#" * key * ")"
end

function rewrite_citations(body::AbstractString, entries)
    body = replace(body, r"^@([A-Za-z][\w.:-]*)[ \t]*$"m =>
        m -> "- " * citation_link(strip(m)[2:end], entries))
    return replace(body, r"(?<![\w`])@([A-Za-z][\w.:-]*)" =>
        m -> citation_link(m[2:end], entries))
end

function rewrite_body(body::AbstractString, entries)
    return rewrite_math(rewrite_citations(rewrite_relative_links(strip_title(body)), entries))
end

function copytree(src::AbstractString, dst::AbstractString)
    isdir(src) || return
    isdir(dst) && rm(dst; recursive=true, force=true)
    mkpath(dirname(dst))
    cp(src, dst; force=true)
    for (root, _, files) in walkdir(dst), file in files
        endswith(lowercase(file), ".md") && rm(joinpath(root, file); force=true)
    end
end

function case_record(path::AbstractString)
    metadata, body = frontmatter(read(path, String), path)
    id = string(getmeta(metadata, "id", splitext(basename(path))[1]))
    title = string(getmeta(metadata, "title", id))
    return (; path, filename = basename(path), metadata, body, id, title)
end

function write_case_page(case, output_path::AbstractString, entries)
    metadata = case.metadata
    open(output_path, "w") do io
        println(io, "# ", case.title)
        println(io)
        facets = [
            table_cell(getmeta(metadata, "process", "")),
            string(table_cell(getmeta(metadata, "interface_motion", "")), " interface"),
            table_cell(getmeta(metadata, "interface_condition", "")),
            domains_cell(metadata),
            geometry_cell(metadata),
            table_cell(getmeta(metadata, "equations", "")),
            table_cell(getmeta(metadata, "reference", "")),
            table_cell(getmeta(metadata, "status", "")),
        ]
        println(io, "`", join(filter(!isempty, facets), "` · `"), "`")
        println(io)
        println(io, "[Source](", REPO_BLOB, "/cases/", case.filename, ")")

        data_files = as_list(getmeta(metadata, "reference_data", ""))
        for file in data_files
            println(io, " · [", basename(file), "](", asset_url(file), ")")
        end

        println(io)
        body = rewrite_body(case.body, entries)
        marker = findlast("\n## References\n", body)
        if marker === nothing
            print(io, body)
            write_results_section(io, case.id, result_figure_url)
        else
            print(io, body[1:first(marker)])
            write_results_section(io, case.id, result_figure_url)
            print(io, body[first(marker)+1:end])
        end
        endswith(case.body, "\n") || println(io)
    end
end

function generate_cases(root::AbstractString = REPO_ROOT)
    repo_root = root
    docs_src = joinpath(repo_root, "docs", "src")
    generated_dir = joinpath(docs_src, "generated")
    generated_cases_dir = joinpath(generated_dir, "cases")

    mkpath(generated_cases_dir)
    for path in readdir(generated_cases_dir; join=true)
        isfile(path) && endswith(path, ".md") && rm(path; force=true)
    end

    copytree(joinpath(repo_root, "data"), joinpath(docs_src, "data"))
    copytree(joinpath(repo_root, "figures"), joinpath(docs_src, "figures"))
    copytree(joinpath(repo_root, "results"), joinpath(docs_src, "results"))

    taxonomy = joinpath(repo_root, "taxonomy.md")
    isfile(taxonomy) && cp(taxonomy, joinpath(docs_src, "taxonomy.md"); force=true)

    entries, order = parse_bib(joinpath(repo_root, "references.bib"))

    cases = load_cases(root)
    cited = Set{String}()
    for case in cases
        union!(cited, as_list(getmeta(case.metadata, "references", "")))
        for m in eachmatch(r"(?<![\w`])@([A-Za-z][\w.:-]*)", case.body)
            push!(cited, String(m.captures[1]))
        end
    end
    for entry in readdir(joinpath(repo_root, "results"); join=true)
        manifest = joinpath(entry, "solver.yml")
        isfile(manifest) || continue
        union!(cited, as_list(getmeta(YAML.load_file(manifest), "references", "")))
    end
    write_references_page(entries, order, joinpath(generated_dir, "references.md"), cited)

    open(joinpath(generated_dir, "index.md"), "w") do io
        println(io, "# Benchmark index")
        println(io)
        println(io, "| ID | Benchmark | Process | Motion | Interface | Domains | Domain | Equations | Reference | Status |")
        println(io, "|---|---|---|---|---|---|---|---|---|---|")
        for case in cases
            metadata = case.metadata
            println(
                io,
                "| [", table_cell(case.id), "](cases/", case.filename, ") | ",
                table_cell(case.title), " | ",
                table_cell(getmeta(metadata, "process", "")), " | ",
                table_cell(getmeta(metadata, "interface_motion", "")), " | ",
                table_cell(getmeta(metadata, "interface_condition", "")), " | ",
                domains_cell(metadata), " | ",
                geometry_cell(metadata), " | ",
                table_cell(getmeta(metadata, "equations", "")), " | ",
                table_cell(getmeta(metadata, "reference", "")), " | ",
                table_cell(getmeta(metadata, "status", "")), " |",
            )
        end
    end

    for case in cases
        write_case_page(case, joinpath(generated_cases_dir, case.filename), entries)
    end

    return cases
end

if abspath(PROGRAM_FILE) == @__FILE__
    generate_cases()
end
