using Documenter

repo_root = normpath(joinpath(@__DIR__, ".."))

include(joinpath(repo_root, "scripts", "generate_cases.jl"))

generate_cases()

generated_cases_dir = joinpath(@__DIR__, "src", "generated", "cases")

const FAMILIES = ["PH" => "Phase change", "MT" => "Mass transfer", "HT" => "Conjugate transfer", "VC" => "Verification"]

case_files = sort([basename(path) for path in readdir(generated_cases_dir) if endswith(path, ".md")])

case_sections = [
    name => [joinpath("generated", "cases", file) for file in case_files if startswith(file, prefix)]
    for (prefix, name) in FAMILIES
]
case_sections = [section for section in case_sections if !isempty(section.second)]

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
        "Cases" => case_sections,
        "References" => "generated/references.md",
    ],
)
