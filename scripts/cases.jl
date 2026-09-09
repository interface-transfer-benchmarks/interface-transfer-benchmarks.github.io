using YAML

const REPO = "interface-transfer-benchmarks/interface-transfer-benchmarks.github.io"
const REPO_BLOB = "https://github.com/$(REPO)/blob/main"
const REPO_ROOT = normpath(joinpath(@__DIR__, ".."))

const REQUIRED_FIELDS = [
    "id",
    "title",
    "status",
    "benchmark_class",
    "physics",
    "process",
    "dimension",
    "geometry",
    "interface_motion",
    "reference_type",
    "numerical_challenge",
    "quantities_of_interest",
    "references",
]

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

function case_record(path::AbstractString)
    metadata, body = frontmatter(read(path, String), path)
    id = string(getmeta(metadata, "id", splitext(basename(path))[1]))
    title = string(getmeta(metadata, "title", id))
    return (; path, filename = basename(path), metadata, body, id, title)
end

function load_cases(root::AbstractString = REPO_ROOT)
    cases_dir = joinpath(root, "cases")
    isdir(cases_dir) || error("No case files under $cases_dir.")
    paths = sort([
        path for path in readdir(cases_dir; join=true)
        if isfile(path) && endswith(path, ".md")
    ])
    isempty(paths) && error("No case files under $cases_dir.")
    return sort([case_record(path) for path in paths]; by = case -> case.id)
end
