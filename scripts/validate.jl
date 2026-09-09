include(joinpath(@__DIR__, "cases.jl"))

function bib_keys(root::AbstractString)
    text = read(joinpath(root, "references.bib"), String)
    return Set(m.captures[1] for m in eachmatch(r"^@\w+\{([^,]+),"m, text))
end

function validate(root::AbstractString = REPO_ROOT)
    errors = String[]
    bibkeys = bib_keys(root)
    index_text = read(joinpath(root, "index.md"), String)
    seen = Dict{String,String}()

    cases = load_cases(root)
    for case in cases
        rel = joinpath("cases", case.filename)
        metadata = case.metadata

        for field in REQUIRED_FIELDS
            isempty(render_value(getmeta(metadata, field, ""))) &&
                push!(errors, "$rel: missing required field '$field'")
        end

        startswith(case.filename, case.id) ||
            push!(errors, "$rel: id '$(case.id)' does not prefix the filename")
        haskey(seen, case.id) &&
            push!(errors, "$rel: duplicate id '$(case.id)' (also in $(seen[case.id]))")
        seen[case.id] = case.filename

        for field in ("reference_data", "figures"), entry in as_list(getmeta(metadata, field, ""))
            isfile(joinpath(root, entry)) ||
                push!(errors, "$rel: $field path does not exist: $entry")
        end

        if lowercase(render_value(getmeta(metadata, "has_reference_data", "false"))) == "true" &&
           isempty(as_list(getmeta(metadata, "reference_data", "")))
            push!(errors, "$rel: has_reference_data is true but reference_data is empty")
        end

        for key in as_list(getmeta(metadata, "references", ""))
            key in bibkeys || push!(errors, "$rel: reference key not in references.bib: $key")
        end

        occursin("cases/$(case.filename)", index_text) ||
            push!(errors, "$rel: not listed in index.md")
    end

    if !isempty(errors)
        foreach(e -> println(stderr, "ERROR: ", e), errors)
        println(stderr, "$(length(errors)) problem(s) found.")
        exit(1)
    end

    println("$(length(cases)) case files validated, no problems found.")
    return cases
end

if abspath(PROGRAM_FILE) == @__FILE__
    validate()
end
