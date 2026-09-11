# Solver Results

One directory per solver. No figures are stored: the plots are drawn from these
files by `scripts/plot_results.py` when the site is built.

```text
results/<solver-slug>/solver.yml   the method, its authors, its code
results/<solver-slug>/<ID>.csv     one benchmark, the numbers
results/<solver-slug>/<ID>.md      one benchmark, optional commentary
```

## solver.yml

```yaml
name: Two-fluid cut-cell method
authors:
  - A. Author
  - B. Author
code: the solver or repository name
references:
  - BibTeXKey
```

## The CSV

One row per run. Required columns:

| Column | Meaning |
|---|---|
| `id` | the benchmark identifier |
| `xname` | what the run swept: `h`, `Da`, `Fo`, `Bi`, `phi` |
| `x` | the value of that sweep point |
| `N` | cells across the domain |
| `Sh` | the observable the benchmark asks for |
| `Sh_exact` | the reference value at that point |

Recommended columns, used to label the tables and to keep runs apart:
`variant`, `grid`, `ranks`, `dim`, and `n_per_layer` — the cells across
whatever layer sets the error, which is the abscissa of the convergence figure.

`variant` names the configuration inside one benchmark: a case run at two
reaction orders, or a Robin datum beside a Dirichlet one, is two variants of
one benchmark and is drawn as two figures. `scripts/plot_results.py` keys its
axis labels, reference-law captions and convergence abscissa off `variant`,
falling back to the benchmark id and then to generic labels.

Any further columns are carried through untouched; the suite in this repository
also writes `Da`, `n_per_layer`, `mg_iters`, `mg_res`, `area`, `area_rel`,
`rel_err`, `order`, `F`, `F_exact`, `id_sum`, `id_avg`.

**Submit measurements, not errors.** The relative error and the observed order
are computed from `Sh` and `Sh_exact` the same way for every method, so two
solvers are always compared on the same footing. A submitted `rel_err` column is
kept for cross-checking but is not what the site displays.
