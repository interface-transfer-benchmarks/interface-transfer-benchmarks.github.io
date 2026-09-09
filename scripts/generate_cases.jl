using YAML

const METADATA_FIELDS = [
    "id",
    "title",
    "short_title",
    "status",
    "benchmark_class",
    "physics",
    "process",
    "dimension",
    "geometry",
    "interface_motion",
    "quantities_of_interest",
    "has_exact_solution",
    "has_reference_data",
    "reference_data",
    "figures",
    "references",
]

const REPO_BLOB = "https://github.com/interface-transfer-benchmarks/interface-transfer-benchmarks.github.io/blob/main"

function getmeta(metadata, key::AbstractString, default = "")
    if haskey(metadata, key)
        return metadata[key]
    elseif haskey(metadata, Symbol(key))
        return metadata[Symbol(key)]
    else
        return default
    end
end

function frontmatter(markdown::AbstractString, path::AbstractString)
    normalized = replace(markdown, "\r\n" => "\n")
    if !startswith(normalized, "---\n")
        return Dict{Any,Any}(), normalized
    end

    marker = findnext("\n---\n", normalized, 5)
    marker === nothing && error("Unclosed YAML front matter in $path")

    yaml_text = normalized[5:first(marker)-1]
    body = normalized[last(marker)+1:end]
    parsed = YAML.load(yaml_text)
    metadata = parsed isa AbstractDict ? parsed : Dict{Any,Any}()
    return metadata, body
end

function as_list(value)
    if value === nothing || value == ""
        return String[]
    elseif value isa AbstractVector
        return [string(item) for item in value if item !== nothing && string(item) != ""]
    else
        return [string(value)]
    end
end

function render_value(value)
    if value === nothing || value == ""
        return ""
    elseif value isa AbstractVector
        return join([string(item) for item in value], ", ")
    elseif value isa AbstractDict
        return join(["$(key): $(val)" for (key, val) in value], ", ")
    else
        return string(value)
    end
end

function table_cell(value)
    return replace(render_value(value), "|" => "\\|", "\n" => " ")
end

function canonical_asset_path(path::AbstractString)
    normalized = replace(path, "\\" => "/")
    normalized = replace(normalized, r"^(\.\./)+" => "")
    normalized = replace(normalized, r"^/+" => "")
    return normalized
end

function asset_url(path::AbstractString)
    return "../../" * canonical_asset_path(path)
end

function rewrite_relative_links(body::AbstractString)
    return replace(body, r"(\]\(|src=\")(?:\.\./|/)*((?:data|figures)/)" => s"\1../../\2")
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

function rewrite_body(body::AbstractString)
    return rewrite_math(rewrite_relative_links(body))
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

function write_case_page(case, output_path::AbstractString)
    metadata = case.metadata
    open(output_path, "w") do io
        println(io, "# ", case.title)
        println(io)
        println(io, "Source: [", case.filename, "](", REPO_BLOB, "/cases/", case.filename, ")")
        println(io)
        println(io, "| Field | Value |")
        println(io, "|---|---|")
        for key in METADATA_FIELDS
            value = getmeta(metadata, key, "")
            rendered = table_cell(value)
            isempty(rendered) || println(io, "| `", key, "` | ", rendered, " |")
        end

        data_files = as_list(getmeta(metadata, "reference_data", ""))
        if !isempty(data_files)
            println(io)
            println(io, "## Data")
            println(io)
            for file in data_files
                println(io, "- [", basename(file), "](", asset_url(file), ")")
            end
        end

        figure_files = as_list(getmeta(metadata, "figures", ""))
        if !isempty(figure_files)
            println(io)
            println(io, "## Figures")
            println(io)
            for file in figure_files
                alt = splitext(basename(file))[1]
                println(io, "![", alt, "](", asset_url(file), ")")
            end
        end

        println(io)
        println(io, "## Benchmark Definition")
        println(io)
        print(io, rewrite_body(case.body))
        endswith(case.body, "\n") || println(io)
    end
end

function generate_cases()
    repo_root = normpath(joinpath(@__DIR__, ".."))
    cases_dir = joinpath(repo_root, "cases")
    docs_src = joinpath(repo_root, "docs", "src")
    generated_dir = joinpath(docs_src, "generated")
    generated_cases_dir = joinpath(generated_dir, "cases")

    isdir(cases_dir) || error("No case files under $cases_dir.")

    mkpath(generated_cases_dir)
    for path in readdir(generated_cases_dir; join=true)
        isfile(path) && endswith(path, ".md") && rm(path; force=true)
    end

    copytree(joinpath(repo_root, "data"), joinpath(docs_src, "data"))
    copytree(joinpath(repo_root, "figures"), joinpath(docs_src, "figures"))

    taxonomy = joinpath(repo_root, "taxonomy.md")
    isfile(taxonomy) && cp(taxonomy, joinpath(docs_src, "taxonomy.md"); force=true)

    case_paths = sort([
        path for path in readdir(cases_dir; join=true)
        if isfile(path) && endswith(path, ".md")
    ])
    cases = sort([case_record(path) for path in case_paths]; by = case -> case.id)

    open(joinpath(generated_dir, "index.md"), "w") do io
        println(io, "# Benchmark index")
        println(io)
        println(io, "| ID | Title | Class | Status | Dimension | Geometry |")
        println(io, "|---|---|---|---|---|---|")
        for case in cases
            metadata = case.metadata
            class = getmeta(metadata, "benchmark_class", "")
            status = getmeta(metadata, "status", "")
            dimension = getmeta(metadata, "dimension", "")
            geometry = getmeta(metadata, "geometry", "")
            println(
                io,
                "| [", table_cell(case.id), "](cases/", case.filename, ") | ",
                table_cell(case.title), " | ",
                table_cell(class), " | ",
                table_cell(status), " | ",
                table_cell(dimension), " | ",
                table_cell(geometry), " |",
            )
        end
    end

    for case in cases
        write_case_page(case, joinpath(generated_cases_dir, case.filename))
    end

    return cases
end

generate_cases()
