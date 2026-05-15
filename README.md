# Phase-Change Numerical Benchmarks website

This repository builds the public website:

https://phase-change-numerical-benchmarks.github.io/

The benchmark source files live in:

https://github.com/Phase-Change-Numerical-Benchmarks/benchmarks

## Local build

Clone both repositories:

```bash
git clone https://github.com/Phase-Change-Numerical-Benchmarks/phase-change-numerical-benchmarks.github.io
cd phase-change-numerical-benchmarks.github.io

mkdir -p _upstream
git clone https://github.com/Phase-Change-Numerical-Benchmarks/benchmarks _upstream/benchmarks
```

Build:

```bash
julia --project=docs -e 'using Pkg; Pkg.instantiate()'
julia --project=docs docs/make.jl
```

The generated site is written to:

```text
docs/build/
```
