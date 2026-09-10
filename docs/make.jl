using Documenter

repo_root = normpath(joinpath(@__DIR__, ".."))

include(joinpath(repo_root, "scripts", "generate_cases.jl"))

generate_cases()

generated_cases_dir = joinpath(@__DIR__, "src", "generated", "cases")

case_pages = sort([
    joinpath("generated", "cases", basename(path))
    for path in readdir(generated_cases_dir; join=true)
    if endswith(path, ".md")
])

makedocs(;
    sitename = "Interface Transfer Benchmarks",
    repo = Remotes.GitHub("interface-transfer-benchmarks", "interface-transfer-benchmarks.github.io"),
    format = Documenter.HTML(;
        canonical = "https://interface-transfer-benchmarks.github.io",
        prettyurls = true,
        inventory_version = "1",
        edit_link = nothing,
    ),
    pages = [
        "Home" => "index.md",
        "Benchmark index" => "generated/index.md",
        "Taxonomy" => "taxonomy.md",
        "Cases" => case_pages,
        "References" => "generated/references.md",
    ],
)
