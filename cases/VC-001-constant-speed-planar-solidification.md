---
id: VC-001
title: Constant-speed planar solidification
short_title: Constant-speed front
status: ready
benchmark_class: VC

physics:
  - phase-change
  - heat-diffusion
  - prescribed-interface-motion

process:
  - solidification

dimension: 1D
geometry: planar
interface_motion: prescribed

reference_type: exact-solution
numerical_challenge: prescribed moving Dirichlet boundary
has_exact_solution: true
has_reference_data: true
reference_data:
  - data/VC-001/reference.csv
figures:
  - figures/VC-001-reference.svg

quantities_of_interest:
  - interface_position
  - temperature_profile
  - fresh_cell_temperature
  - convergence_rate

references:
  - ChenMerrimanOsherSmereka1997
  - BasiliskAlimareDirichletExpand1D
---

# VC-001 - Constant-speed planar solidification

## Problem

A planar interface moves at prescribed speed $V$ in the positive $x$ direction.
The active phase is ahead of the interface; the region behind the front is held
at equilibrium temperature.

```text
x <= Vt                         x > Vt
solid/equilibrium region         active thermal region
T = 0                            T = -1 + exp[-V(x - Vt)]
```

The benchmark uses an imposed analytical profile, so the interface velocity is
not computed from a Stefan condition:

$$
s(t)=Vt.
$$

The temperature field is

$$
T(x,t)=
\begin{cases}
0, & x\le Vt,\\
-1+\exp[-V(x-Vt)], & x>Vt.
\end{cases}
$$

This is the exact solution used by the Basilisk test case.

Use the analytical temperature profile at $t=0$ and enforce the far active-side
Dirichlet value from the same expression. The Basilisk example uses $V=1$ and
periodic boundaries in the transverse direction for its two-dimensional
implementation.

## Parameters

| Parameter | Symbol |
|---|---|
| interface speed | $V$ |
| equilibrium temperature | $T_\mathrm{eq}$ |
| initial time shift | $t_0$ |
| final time | $t_\mathrm{end}$ |

## Reference

For the recommended value $V=1$,

$$
s(t)=t.
$$

The file `data/VC-001/reference.csv` tabulates $s(t)$ and $T(x,t)$ at selected
times.

![VC-001 constant-speed reference](../figures/VC-001-reference.svg)

Generate the CSV and figure with:

```bash
python3 scripts/plot_reference_figures.py VC-001
```

## Report

- interface position $s_h(t)$,
- error in $s_h(t)$,
- temperature profile at the final time,
- temperature error in newly active cells,
- convergence rate for interface position and temperature.

## References

@ChenMerrimanOsherSmereka1997
@BasiliskAlimareDirichletExpand1D
