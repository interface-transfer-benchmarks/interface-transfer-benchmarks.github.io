# Contributing

Three things are welcome: results from your own solver, new benchmarks, and
corrections.

## Submitting results

One pull request, two things in it.

1. `results/<your-solver-slug>/` — your figures, named
   `<ID>-convergence.png` and `<ID>-sh.png`. Extra views take a third name,
   for instance `<ID>-henry.png`.
2. In each case file you ran, one subsection appended to `## Results`:

```markdown
### Method name - A. Author, B. Author

Measured 2026-01-01. Uniform grid, N = 128, 8 MPI ranks. Da = 1, 10, 100.

| Da | 1 | 10 | 100 |
|---|---|---|---|
| rel. error | 1e-3 | 2e-3 | 3e-2 |
| order | 2.00 | 1.93 | 1.76 |

![ID convergence](../results/<slug>/<ID>-convergence.png)
```

Nothing else. The front matter, `index.md` and the site are generated.

Three rules:

- One subsection per solver, and you edit only your own.
- Report the runs that missed their gate, and say so. A named failure is worth
  more than a missing row.
- The configuration line must be enough to re-run it: grid, resolution, ranks,
  parameter values, date.

A maintainer checks that the case files still validate, that the figures exist
and are the ones referenced, and that the numbers match the figures. Then it
merges and CI publishes it.

If you would rather not open a pull request, open an issue titled
`Results: <ID>, <method>` with the same table and the figures attached, and a
maintainer will commit it under your name.

## Proposing a benchmark

Open an issue titled `New benchmark proposal: <ID> short title`, with the
configuration, the governing equations, the boundary and initial conditions,
the reference solution or dataset, the quantities of interest, the numerical
difficulty it targets, and the bibliography.

Copy `benchmark-template.md` to `cases/<ID>-short-title.md`. The identifier
prefix names the family: `PH` phase change, `MT` mass transfer with reaction,
`HT` conjugate transfer, `VC` verification and coherence. Use the symbols of
the [notation table](taxonomy.md#notation).

A case merges as `draft` once the physical idea is clear. It is `ready` only
when the equations, the conditions, the parameters and the quantities of
interest are unambiguous and a reference solution or dataset exists.
