# Interface Transfer Benchmarks website

This repository builds the public website:

https://interface-transfer-benchmarks.github.io/

The benchmark source files live in:

https://github.com/interface-transfer-benchmarks/benchmarks

## Local build

Clone both repositories:

```bash
git clone https://github.com/interface-transfer-benchmarks/interface-transfer-benchmarks.github.io
cd interface-transfer-benchmarks.github.io

mkdir -p _upstream
git clone https://github.com/interface-transfer-benchmarks/benchmarks _upstream/benchmarks
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
