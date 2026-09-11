---
id: B-016
title: First-order surface kinetics on a sphere
short_title: Robin sphere
status: ready

process:
  - reaction
interface_motion: fixed
interface_condition:
  - kinetic
domains: 1
domain: sphere
dimension: 3D
equations:
  - species-diffusion

reference: closed-form
reference_note: exact steady solution
numerical_challenge: a Robin interface condition whose surface value is solved, not imposed

quantities_of_interest:
  - sherwood_number
  - surface_concentration
  - convergence_rate
has_reference_data: true
reference_data:
  - data/B-016/reference.csv

references:
  - taylor1963
  - collins1949
  - lu2018
---

# B-016 - First-order surface kinetics on a sphere

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

| Parameter | Symbol |
|---|---|
| sphere radius | $R_0$ |
| diffusivity | $D$ |
| far-field concentration | $C_\infty$ |
| surface Damkohler number | $\mathrm{Da}_s = k_s R_0/D$ |

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

![B-016 reference](../figures/B-016-reference.svg)

## Report

- $\mathrm{Sh}_\mathrm{ov}$ across $\mathrm{Da}_s$,
- the solved surface trace $C_s/C_\infty$ against $1/(1+\mathrm{Da}_s)$,
- linearity of $1/\mathrm{Sh}_\mathrm{ov}$ in $1/\mathrm{Da}_s$,
- observed convergence rate.


## References

@taylor1963
@collins1949
@lu2018
