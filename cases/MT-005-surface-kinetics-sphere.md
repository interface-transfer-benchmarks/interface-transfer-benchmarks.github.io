---
id: MT-005
title: First-order surface kinetics on a sphere
short_title: Robin sphere
status: ready
benchmark_class: MT

physics:
  - mass-transfer
  - surface-reaction

process:
  - interfacial-mass-transfer
  - heterogeneous-reaction

dimension: 3D
geometry: sphere
interface_motion: static
reference_type: exact-solution
numerical_challenge: a Robin interface condition whose surface value is solved, not imposed

quantities_of_interest:
  - sherwood_number
  - surface_concentration
  - convergence_rate

has_exact_solution: true
has_reference_data: true
reference_data:
  - data/MT-005/reference.csv
figures:
  - figures/MT-005-reference.svg

references:
  - taylor1963
  - collins1949
  - lu2018
---

# MT-005 - First-order surface kinetics on a sphere

## Problem

A sphere of radius $R_0$ consumes the species at its surface at rate
$k_s C_s$, in a quiescent medium of far-field concentration $C_\infty$. There
is no bulk reaction.

For $r > R_0$,

$$
\nabla^2 C = 0 .
$$

At the surface, consumption balances the diffusive supply,

$$
k_s C(R_0) = D\, \partial_r C(R_0),
$$

and $C(r\to\infty) = C_\infty$.

## Parameters

| Parameter | Symbol | Value |
|---|---:|---:|
| sphere radius | $R_0$ | 1 |
| diffusivity | $D$ | 1 |
| far-field concentration | $C_\infty$ | 1 |
| surface Damkohler number | $\mathrm{Da}_s = k_s R_0/D$ | 0.01 to 100 |

## Reference

$$
\frac{C(r)}{C_\infty} = 1 - \frac{R_0}{r}\,
\frac{\mathrm{Da}_s}{1+\mathrm{Da}_s},
\qquad
\frac{C_s}{C_\infty} = \frac{1}{1+\mathrm{Da}_s},
$$

and the overall Sherwood number obeys a resistances-in-series law,

$$
\mathrm{Sh}_\mathrm{ov} = \frac{2\,\mathrm{Da}_s}{1+\mathrm{Da}_s},
\qquad
\frac{1}{\mathrm{Sh}_\mathrm{ov}} = \frac{1}{2} + \frac{1}{2\,\mathrm{Da}_s} .
$$

The limits bracket every reactive particle: $\mathrm{Da}_s \to \infty$ gives
the diffusion-controlled sphere $\mathrm{Sh}=2$, and $\mathrm{Da}_s \to 0$
gives the kinetics-controlled $\mathrm{Sh}=2\,\mathrm{Da}_s$.

![MT-005 reference](../figures/MT-005-reference.svg)

## Report

- $\mathrm{Sh}_\mathrm{ov}$ across $\mathrm{Da}_s$,
- the solved surface trace $C_s/C_\infty$ against $1/(1+\mathrm{Da}_s)$,
- linearity of $1/\mathrm{Sh}_\mathrm{ov}$ in $1/\mathrm{Da}_s$,
- observed convergence rate.

## Results

Measured with the `basilisk-libat` cut-cell solver, 2026-09-09.

N = 64 uniform, 8 ranks.

| Da_s | 0.1 | 1 | 10 | 100 | 1000 |
|---|---|---|---|---|---|
| rel. error | 2.3e-4 | 9.6e-4 | 1.7e-3 | 1.9e-3 | 1.9e-3 |
| order | 2.20 | 2.21 | 2.23 | 2.24 | 2.24 |

The errors on `Sh_ov` and on the solved `c_s` are the same numbers, because
`Sh_ov = 2 Da_s c_s` with `Da_s` exact: measuring the solved surface
concentration and measuring the transfer are one measurement.

## References

@taylor1963
@collins1949
@lu2018
