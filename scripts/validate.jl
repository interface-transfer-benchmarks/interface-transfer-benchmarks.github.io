include(joinpath(@__DIR__, "cases.jl"))

function bib_keys(root::AbstractString)
    text = read(joinpath(root, "references.bib"), String)
    return Set(m.captures[1] for m in eachmatch(r"^@\w+\{([^,]+),"m, text))
end

const RETIRED = [
    r"\\Sigma" => "\\Gamma marks the interface",
    r"h_\{fg\}|h_\{lg\}" => "L is the latent heat",
    r"\\rho_v|k_v\b|c_\{p,v\}|\\mu_v" => "the gas phase is subscript g",
    r"_\{(sat|end|eq|life|qs|wall|bulk)\}" => "a roman subscript takes \\mathrm",
    r"\\mathrm\{St\}(?!e)" => "the Stefan number is \\mathrm{Ste}",
    r"D\^\*" => "the diffusivity ratio is D_1/D_2",
    r"\$He\$" => "the partition coefficient is H",
]

const INLINE_ASSET = r"!\[[^\]]*\]\(\.\./((?:data|figures|results)/[^)\s]+)\)"

function inline_assets(body::AbstractString)
    return [String(m.captures[1]) for m in eachmatch(INLINE_ASSET, body)]
end

const GROUPS = r"(?<![A-Za-z\\{])(Sh|Da|Pe|Fo|Bi|Nu|Sc|Ja|Ste|Ra|Pr)(?![A-Za-z}])"

function notation_problems(body::AbstractString)
    problems = String[]
    for (pattern, message) in RETIRED
        occursin(pattern, body) && push!(problems, message)
    end
    stripped = replace(body, r"\\mathrm\{[^}]*\}" => "")
    for m in eachmatch(r"\$\$(.*?)\$\$|\$([^\$\n]+)\$"s, stripped)
        math = something(m.captures[1], m.captures[2])
        for g in eachmatch(GROUPS, math)
            push!(problems, "$(g.captures[1]) is a dimensionless group and takes \\mathrm")
        end
    end
    return unique(problems)
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

        for asset in inline_assets(case.body)
            isfile(joinpath(root, asset)) ||
                push!(errors, "$rel: image does not exist: $asset")
        end

        for problem in notation_problems(case.body)
            push!(errors, "$rel: notation, $problem")
        end
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
