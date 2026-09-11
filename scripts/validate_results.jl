include(joinpath(@__DIR__, "cases.jl"))
include(joinpath(@__DIR__, "results.jl"))

const REQUIRED_RESULT_COLUMNS = ["id", "xname", "x", "N", "Sh", "Sh_exact"]

function validate_results(root::AbstractString = REPO_ROOT)
    errors = String[]
    known = Set(case.id for case in load_cases(root))
    bibkeys = Set(m.captures[1] for m in
        eachmatch(r"^@\w+\{([^,]+),"m, read(joinpath(root, "references.bib"), String)))
    directory = joinpath(root, "results")
    checked = 0

    for entry in sort(readdir(directory; join=true))
        isdir(entry) || continue
        slug = basename(entry)
        manifest = joinpath(entry, "solver.yml")
        if !isfile(manifest)
            push!(errors, "results/$slug: missing solver.yml")
        else
            meta = YAML.load_file(manifest)
            isempty(render_value(getmeta(meta, "name", ""))) &&
                push!(errors, "results/$slug/solver.yml: missing 'name'")
            for key in as_list(getmeta(meta, "references", ""))
                key in bibkeys ||
                    push!(errors, "results/$slug/solver.yml: reference key not in references.bib: $key")
            end
        end

        for path in sort(readdir(entry; join=true))
            endswith(path, ".csv") || continue
            rel = "results/$slug/$(basename(path))"
            case_id = splitext(basename(path))[1]
            case_id in known || push!(errors, "$rel: no benchmark with id '$case_id'")
            rows = read_result_csv(path)
            isempty(rows) && (push!(errors, "$rel: no data rows"); continue)
            for column in REQUIRED_RESULT_COLUMNS
                haskey(first(rows), column) || push!(errors, "$rel: missing column '$column'")
            end
            seen = Set{NTuple{7,String}}()
            for (line, row) in enumerate(rows)
                field(row, "id") == case_id ||
                    push!(errors, "$rel line $(line + 1): id '$(field(row, "id"))' does not match the filename")
                for column in ("x", "Sh", "Sh_exact")
                    haskey(row, column) && !isempty(field(row, column)) &&
                        numeric(row, column) === nothing &&
                        push!(errors, "$rel line $(line + 1): '$column' is not a number: $(field(row, column))")
                end
                key = (field(row, "variant"), field(row, "grid"), field(row, "ranks"),
                       field(row, "dim"), field(row, "N"), field(row, "x"), field(row, "Da"))
                key in seen && push!(errors, "$rel line $(line + 1): duplicate run $(key)")
                push!(seen, key)
            end
            checked += 1
        end
    end

    if !isempty(errors)
        foreach(e -> println(stderr, "ERROR: ", e), errors)
        println(stderr, "$(length(errors)) problem(s) found.")
        exit(1)
    end
    println("$checked result files validated, no problems found.")
end

if abspath(PROGRAM_FILE) == @__FILE__
    validate_results()
end
