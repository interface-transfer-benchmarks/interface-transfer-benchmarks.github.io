const ACCENTS = Dict(
    ("'", 'a') => "á", ("'", 'e') => "é", ("'", 'i') => "í", ("'", 'o') => "ó",
    ("'", 'u') => "ú", ("'", 'c') => "ć", ("'", 'n') => "ń", ("'", 's') => "ś",
    ("`", 'a') => "à", ("`", 'e') => "è", ("`", 'i') => "ì", ("`", 'o') => "ò",
    ("`", 'u') => "ù",
    ("\"", 'a') => "ä", ("\"", 'e') => "ë", ("\"", 'i') => "ï", ("\"", 'o') => "ö",
    ("\"", 'u') => "ü",
    ("^", 'a') => "â", ("^", 'e') => "ê", ("^", 'i') => "î", ("^", 'o') => "ô",
    ("^", 'u') => "û",
    ("~", 'a') => "ã", ("~", 'n') => "ñ", ("~", 'o') => "õ",
    ("c", 'c') => "ç", ("c", 's') => "ş",
    ("v", 'c') => "č", ("v", 's') => "š", ("v", 'z') => "ž",
    ("=", 'a') => "ā", ("=", 'e') => "ē", ("=", 'o') => "ō",
    (".", 'z') => "ż",
)

function detex(text::AbstractString)
    out = replace(text, r"\{?\\([`'\"^~ckv=.])\s*\{?([A-Za-z])\}?\}?" =>
        m -> begin
            c = match(r"\\([`'\"^~ckv=.])\s*\{?([A-Za-z])", m)
            get(ACCENTS, (String(c.captures[1]), first(c.captures[2])), String(c.captures[2]))
        end)
    out = replace(out, r"\\ss\b" => "ß", r"\\&" => "&", r"\\%" => "%", r"\\_" => "_")
    out = replace(out, "{" => "", "}" => "", "--" => "–")
    return strip(out)
end

function parse_bib(path::AbstractString)
    text = replace(read(path, String), "\r\n" => "\n")
    entries = Dict{String,Dict{String,String}}()
    order = String[]
    for m in eachmatch(r"@(\w+)\s*\{\s*([^,\s]+)\s*,(.*?)\n\}\s*\n"s, text * "\n")
        key = String(m.captures[2])
        fields = Dict{String,String}("entrytype" => lowercase(String(m.captures[1])))
        for f in eachmatch(r"(\w+)\s*=\s*\{((?:[^{}]|\{[^{}]*\})*)\}"s, String(m.captures[3]))
            value = replace(String(f.captures[2]), r"\s+" => " ")
            fields[lowercase(String(f.captures[1]))] = detex(value)
        end
        entries[key] = fields
        push!(order, key)
    end
    return entries, order
end

function author_list(entry::Dict{String,String})
    raw = get(entry, "author", "")
    isempty(raw) && return String[]
    return [strip(a) for a in split(raw, " and ")]
end

function surname(author::AbstractString)
    occursin(",", author) && return strip(first(split(author, ",")))
    parts = split(author)
    return isempty(parts) ? String(author) : String(last(parts))
end

function citation_label(entry::Dict{String,String})
    names = author_list(entry)
    year = get(entry, "year", "")
    who = if isempty(names)
        get(entry, "title", "")
    elseif length(names) == 1
        surname(names[1])
    elseif length(names) == 2
        surname(names[1]) * " & " * surname(names[2])
    else
        surname(names[1]) * " et al."
    end
    return isempty(year) ? who : "$who ($year)"
end

function format_entry(entry::Dict{String,String})
    names = author_list(entry)
    parts = String[]
    isempty(names) || push!(parts, join([surname(n) for n in names], ", "))
    haskey(entry, "year") && push!(parts, "(" * entry["year"] * ")")
    haskey(entry, "title") && push!(parts, "*" * entry["title"] * "*")
    for field in ("journal", "publisher", "series")
        haskey(entry, field) && push!(parts, entry[field])
    end
    if haskey(entry, "volume")
        vol = entry["volume"]
        haskey(entry, "number") && (vol *= "(" * entry["number"] * ")")
        haskey(entry, "pages") && (vol *= ":" * entry["pages"])
        push!(parts, vol)
    end
    if haskey(entry, "doi")
        push!(parts, "[doi:" * entry["doi"] * "](https://doi.org/" * entry["doi"] * ")")
    elseif haskey(entry, "url")
        push!(parts, "[link](" * entry["url"] * ")")
    end
    return join(parts, ". ") * "."
end

function escape_html(text::AbstractString)
    return replace(text, "&" => "&amp;", "<" => "&lt;", ">" => "&gt;")
end

function format_entry_html(entry::Dict{String,String})
    names = author_list(entry)
    parts = String[]
    isempty(names) || push!(parts, escape_html(join([surname(n) for n in names], ", ")))
    haskey(entry, "year") && push!(parts, "(" * escape_html(entry["year"]) * ")")
    haskey(entry, "title") && push!(parts, "<em>" * escape_html(entry["title"]) * "</em>")
    for field in ("journal", "publisher", "series")
        haskey(entry, field) && push!(parts, escape_html(entry[field]))
    end
    if haskey(entry, "volume")
        vol = entry["volume"]
        haskey(entry, "number") && (vol *= "(" * entry["number"] * ")")
        haskey(entry, "pages") && (vol *= ":" * entry["pages"])
        push!(parts, escape_html(vol))
    end
    if haskey(entry, "doi")
        doi = escape_html(entry["doi"])
        push!(parts, "<a href=\"https://doi.org/$doi\">doi:$doi</a>")
    elseif haskey(entry, "url")
        url = escape_html(entry["url"])
        push!(parts, "<a href=\"$url\">link</a>")
    end
    return join(parts, ". ") * "."
end

function write_references_page(entries, order, output_path::AbstractString, cited = nothing)
    # references.bib may hold entries no case cites any more: a benchmark that
    # was retired takes its citations with it. Listing them puts a reference on
    # the site for a case that is not there.
    keys = cited === nothing ? order : [key for key in order if key in cited]
    open(output_path, "w") do io
        println(io, "# References")
        println(io)
        println(io, "````@raw html")
        println(io, "<ul>")
        for key in sort(keys; by = k -> lowercase(k))
            println(io, "<li id=\"", key, "\">", format_entry_html(entries[key]), "</li>")
        end
        println(io, "</ul>")
        println(io, "````")
    end
end
