using Documenter
using DocumenterVitepress

repo_root = normpath(joinpath(@__DIR__, ".."))

include(joinpath(repo_root, "scripts", "generate_cases.jl"))

generated_cases_dir = joinpath(@__DIR__, "src", "generated", "cases")

case_pages = sort([
    joinpath("generated", "cases", basename(path))
    for path in readdir(generated_cases_dir; join=true)
    if endswith(path, ".md")
])

makedocs(;
    sitename = "Phase-Change Numerical Benchmarks",
    source = "src",
    build = "build",
    format = DocumenterVitepress.MarkdownVitepress(;
        repo = "github.com/Phase-Change-Numerical-Benchmarks/phase-change-numerical-benchmarks.github.io",
        devbranch = "main",
        devurl = "dev",
        deploy_url = "https://phase-change-numerical-benchmarks.github.io",
        inventory_version = "1",
    ),
    pages = [
        "Home" => "index.md",
        "Benchmark index" => "generated/index.md",
        "Taxonomy" => "taxonomy.md",
        "Cases" => case_pages,
    ],
)

versioned_build = joinpath(@__DIR__, "build", "1")
if isdir(versioned_build) && isfile(joinpath(versioned_build, "index.html"))
    for entry in readdir(versioned_build; join=true)
        destination = joinpath(@__DIR__, "build", basename(entry))
        rm(destination; force=true, recursive=true)
        cp(entry, destination; force=true)
    end
end

assets_source = joinpath(@__DIR__, "src", "assets")
assets_destination = joinpath(@__DIR__, "build", "assets")
if isdir(assets_source)
    mkpath(assets_destination)
    for entry in readdir(assets_source; join=true)
        destination = joinpath(assets_destination, basename(entry))
        rm(destination; force=true, recursive=true)
        cp(entry, destination; force=true)
    end
end

html_files = String[]
for (root, _, files) in walkdir(joinpath(@__DIR__, "build"))
    occursin(string(joinpath("build", ".documenter")), root) && continue
    for file in files
        endswith(file, ".html") && push!(html_files, joinpath(root, file))
    end
end

for source in html_files
    alias_dir = joinpath(dirname(source), splitext(basename(source))[1])
    isfile(alias_dir) && rm(alias_dir; force=true)
    mkpath(alias_dir)
    cp(source, joinpath(alias_dir, "index.html"); force=true)
end
