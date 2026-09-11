using YAML

const RESULTS_DIR = joinpath(REPO_ROOT, "results")
const RESULT_COLUMNS = ["id", "variant", "xname", "x", "grid", "ranks", "dim", "N",
                        "Da", "Sh", "Sh_exact"]

struct Submission
    slug::String
    name::String
    authors::Vector{String}
    code::String
    rows::Vector{Dict{String,String}}
    note::String
end

function read_result_csv(path::AbstractString)
    lines = filter(!isempty, strip.(readlines(path)))
    isempty(lines) && return Dict{String,String}[]
    header = String.(split(lines[1], ','))
    return [Dict(zip(header, String.(split(line, ',')))) for line in lines[2:end]]
end

function submissions(case_id::AbstractString)
    isdir(RESULTS_DIR) || return Submission[]
    found = Submission[]
    for entry in sort(readdir(RESULTS_DIR; join=true))
        isdir(entry) || continue
        csv = joinpath(entry, "$(case_id).csv")
        note = joinpath(entry, "$(case_id).md")
        (isfile(csv) || isfile(note)) || continue
        manifest = isfile(joinpath(entry, "solver.yml")) ?
            YAML.load_file(joinpath(entry, "solver.yml")) : Dict{Any,Any}()
        push!(found, Submission(
            basename(entry),
            string(getmeta(manifest, "name", basename(entry))),
            as_list(getmeta(manifest, "authors", "")),
            string(getmeta(manifest, "code", "")),
            isfile(csv) ? read_result_csv(csv) : Dict{String,String}[],
            isfile(note) ? strip(read(note, String)) : "",
        ))
    end
    return found
end

field(row, key) = strip(get(row, key, ""))
numeric(row, key) = tryparse(Float64, field(row, key))

function signature(row, split_on_da::Bool)
    ranks = field(row, "ranks")
    parts = [field(row, "variant"), field(row, "dim") * "D", field(row, "grid"),
             isempty(ranks) ? "" : (ranks == "1" ? "serial" : ranks * " ranks"),
             split_on_da ? "Da = " * field(row, "Da") : ""]
    return join(filter(!isempty, parts), " ")
end

function splits_on_da(rows)
    any(row -> field(row, "xname") == "Da", rows) && return false
    return length(Set(field(row, "Da") for row in rows)) > 1
end

function trim(value)
    (value === nothing || !isfinite(value)) && return "-"
    return string(round(value; sigdigits=3))
end

function relative_error(row)
    value, reference = numeric(row, "Sh"), numeric(row, "Sh_exact")
    (value === nothing || reference === nothing || reference == 0) && return nothing
    return abs(value - reference) / abs(reference)
end

sortkey(values) = sort(collect(values); by = value -> something(tryparse(Float64, value), Inf))

function block_table(io, rows)
    xname = field(first(rows), "xname")
    xs = sortkey(Set(field(row, "x") for row in rows))
    resolutions = sortkey(Set(field(row, "N") for row in rows))
    cell = Dict((field(row, "x"), field(row, "N")) => row for row in rows)

    if length(resolutions) <= 1 || xname == "h"
        println(io, "| ", xname, " | ", join(xs, " | "), " |")
        println(io, "|---|", repeat("---|", length(xs)))
        picked = [get(cell, (x, first(resolutions)), nothing) for x in xs]
        println(io, "| Sh | ", join([row === nothing ? "-" : trim(numeric(row, "Sh")) for row in picked], " | "), " |")
        println(io, "| reference | ", join([row === nothing ? "-" : trim(numeric(row, "Sh_exact")) for row in picked], " | "), " |")
        errors = [row === nothing ? nothing : relative_error(row) for row in picked]
        println(io, "| rel. error | ", join([trim(error) for error in errors], " | "), " |")
        orders = ["" for _ in xs]
        for index in 2:length(xs)
            x0, x1 = tryparse(Float64, xs[index-1]), tryparse(Float64, xs[index])
            e0, e1 = errors[index-1], errors[index]
            if x0 !== nothing && x1 !== nothing && e0 !== nothing && e1 !== nothing &&
               x0 > 0 && x1 > 0 && e0 > 0 && e1 > 0 && x0 != x1
                orders[index] = string(round(abs(log(e1 / e0) / log(x1 / x0)); digits=2))
            end
        end
        any(!isempty, orders) && println(io, "| order | ", join(orders, " | "), " |")
        println(io)
        return
    end

    println(io, "| ", xname, " | ", join(xs, " | "), " |")
    println(io, "|---|", repeat("---|", length(xs)))
    previous = nothing
    for resolution in resolutions
        errors = [haskey(cell, (x, resolution)) ? relative_error(cell[(x, resolution)]) : nothing for x in xs]
        println(io, "| N = ", resolution, " | ", join([trim(error) for error in errors], " | "), " |")
        if previous !== nothing
            ratio = tryparse(Float64, resolution) / tryparse(Float64, previous[1])
            orders = map(zip(previous[2], errors)) do (before, after)
                (before === nothing || after === nothing || before <= 0 || after <= 0 || ratio <= 1) && return ""
                string(round(log(before / after) / log(ratio); digits=2))
            end
            any(!isempty, orders) && println(io, "| order | ", join(orders, " | "), " |")
        end
        previous = (resolution, errors)
    end
    println(io)
end

function write_results_section(io, case_id::AbstractString, figure_url)
    found = submissions(case_id)
    isempty(found) && return
    println(io, "## Results")
    println(io)
    for submission in found
        heading = isempty(submission.authors) ? submission.name :
            string(submission.name, " - ", join(submission.authors, ", "))
        println(io, "### ", heading)
        println(io)
        if !isempty(submission.note)
            println(io, submission.note)
            println(io)
        end
        blocks = Dict{String,Vector{Dict{String,String}}}()
        split_on_da = splits_on_da(submission.rows)
        for row in submission.rows
            push!(get!(blocks, signature(row, split_on_da), Dict{String,String}[]), row)
        end
        for key in sort(collect(keys(blocks)))
            println(io, "**", key, "**")
            println(io)
            block_table(io, blocks[key])
        end
    end
    for (name, url) in figure_url(case_id)
        println(io, "![", name, "](", url, ")")
        println(io)
    end
    println(io, "Generated from `results/*/", case_id, ".csv`.")
    println(io)
end
