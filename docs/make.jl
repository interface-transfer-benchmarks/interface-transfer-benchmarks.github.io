using Documenter

repo_root = normpath(joinpath(@__DIR__, ".."))

include(joinpath(repo_root, "scripts", "generate_cases.jl"))

cases = generate_cases()

const MOTIONS = [
    "fixed" => "Fixed interface",
    "prescribed" => "Prescribed interface",
    "free" => "Free interface",
]

case_sections = [
    name => [
        joinpath("generated", "cases", case.filename) for case in cases
        if string(getmeta(case.metadata, "interface_motion", "")) == motion
    ]
    for (motion, name) in MOTIONS
]
case_sections = [section for section in case_sections if !isempty(section.second)]

let listed = sum(length(section.second) for section in case_sections)
    listed == length(cases) ||
        error("$(length(cases) - listed) case(s) missing from the sidebar; check interface_motion")
end

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
