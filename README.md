# Interface Transfer Benchmarks

Benchmark definitions, reference data, and the website for numerical methods
for interfacial heat and mass transfer.

Site: https://interface-transfer-benchmarks.github.io/

Each benchmark is one Markdown file in `cases/` with a stable identifier.
Its YAML front matter is the single source of truth: [`index.md`](index.md) is
generated from it by `scripts/generate_index.jl`, and `scripts/validate.jl`
gates it in CI.

Only data is stored. No figure is in the repository: the reference plots and
every results plot are drawn by `scripts/plot_reference_figures.py` and
`scripts/plot_results.py` when the site is built.

## Goals

Not to promote one numerical method, but to define reproducible test cases for
comparing sharp-interface, front-tracking, level-set, VOF, cut-cell,
ghost-fluid, immersed-boundary, enthalpy, and phase-field methods.

## Identifiers

`B-001` to `B-041`. See [`taxonomy.md`](taxonomy.md).

## Layout

```text
cases/          Benchmark descriptions
data/           Reference data
results/        Submitted solver results, one directory per solver
scripts/        Case loading, validation, plotting, index and site generation
docs/           Website source
references.bib  Bibliography
```

## Build the site

```bash
julia --project=docs -e 'using Pkg; Pkg.instantiate()'
julia --project=docs docs/make.jl
```

Output in `docs/build/`. See `CONTRIBUTING.md` and `benchmark-template.md`.
