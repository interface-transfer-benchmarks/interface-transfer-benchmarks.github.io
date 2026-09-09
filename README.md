# Interface Transfer Benchmarks

Benchmark definitions, reference data, and the website for numerical methods
for interfacial heat and mass transfer.

Site: https://interface-transfer-benchmarks.github.io/

Each benchmark is one Markdown file in `cases/` with a stable identifier.
Its YAML front matter is the single source of truth: [`index.md`](index.md)
and the coverage table in [`taxonomy.md`](taxonomy.md) are generated from it
by `scripts/generate_index.jl`, and `scripts/validate.jl` gates it in CI.

## Goals

Not to promote one numerical method, but to define reproducible test cases for
comparing sharp-interface, front-tracking, level-set, VOF, cut-cell,
ghost-fluid, immersed-boundary, enthalpy, and phase-field methods.

## Identifiers

Following the historical InterfaceTracking collection.

| Prefix | Meaning |
|---|---|
| `N` | Purely numerical test-case |
| `PA` | Compared to an analytical solution |
| `PN` | Compared to a numerical reference method |
| `PE` | Compared to an experiment |
| `PC` | Test of coherence |

## Layout

```text
cases/          Benchmark descriptions
data/           Reference data
figures/        Reference plots
scripts/        Case loading, validation, index and site generation
docs/           Website source
references.bib  Bibliography
```

## Build the site

```bash
julia --project=docs -e 'using Pkg; Pkg.instantiate()'
julia --project=docs docs/make.jl
```

Output in `docs/build/`. See `CONTRIBUTING.md` and `benchmark-template.md`.
