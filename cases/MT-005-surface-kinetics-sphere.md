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

## Purpose

The only case in the family whose interface condition is neither Dirichlet nor
Neumann, and the only one where the surface concentration is a result rather
than a datum. The field is harmonic, so the case isolates the Robin condition
from the reaction-layer meshing constraint of MT-001.

## Physical Configuration

A sphere of radius $R_0$ consumes the species at its surface at rate
$k_s C_s$, in a quiescent medium of far-field concentration $C_\infty$. There
is no bulk reaction.

## Governing Equations

For $r > R_0$,

$$
\nabla^2 C = 0 .
$$

## Boundary And Initial Conditions

At the surface, consumption balances the diffusive supply,

$$
k_s C(R_0) = D\, \partial_r C(R_0),
$$

and $C(r\to\infty) = C_\infty$.

## Material Parameters

| Parameter | Symbol | Value |
|---|---:|---:|
| sphere radius | $R_0$ | 1 |
| diffusivity | $D$ | 1 |
| far-field concentration | $C_\infty$ | 1 |
| surface Damkohler number | $\mathrm{Da}_s = k_s R_0/D$ | 0.01 to 100 |

## Reference Solution

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

## Recommended Numerical Setup

A cubic box of side $L \ge 40 R_0$, or the reference profile imposed on the
outer boundary. No reaction layer exists, so the mesh requirement is set by the
interface representation alone.

## Quantities To Report

- $\mathrm{Sh}_\mathrm{ov}$ across $\mathrm{Da}_s$,
- the solved surface trace $C_s/C_\infty$ against $1/(1+\mathrm{Da}_s)$,
- linearity of $1/\mathrm{Sh}_\mathrm{ov}$ in $1/\mathrm{Da}_s$,
- observed convergence rate.

## Known Difficulties

- imposing $C_s$ rather than solving for it,
- a Robin row that degrades to first order at cut cells,
- box truncation, which biases the $\mathrm{Da}_s \to \infty$ end.

## References

@taylor1963
@collins1949
@lu2018
