---
id: B-017
title: Catalyst pellet with an external film
short_title: Pellet with film
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
  - volume-reaction

reference: closed-form
reference_note: exact steady solution at finite Biot number
numerical_challenge: a Robin condition on the interior field with a finite Biot number

quantities_of_interest:
  - effectiveness_factor
  - surface_concentration
  - convergence_rate
has_reference_data: true
reference_data:
  - data/B-017/reference.csv

references:
  - fogler2016
  - froment2011
  - sulaiman2019b
---

# B-017 - Catalyst pellet with an external film

## Problem

B-008's pellet, with the surface concentration no longer imposed: an external
film of mass-transfer coefficient $k_g$ separates the surface from a bulk at
$C_b$.

For $r < R_0$,

$$
D \nabla^2 C = k C .
$$

$$
k_g\left(C_b - C(R_0)\right) = D\,\partial_r C(R_0), \qquad \partial_r C(0) = 0 .
$$

## Parameters

| Parameter | Symbol |
|---|---|
| pellet radius | $R_0$ |
| diffusivity | $D$ |
| bulk concentration | $C_b$ |
| Thiele modulus | $\phi = R_0\sqrt{k/D}$ |
| Biot number | $\mathrm{Bi} = k_g R_0/D$ |

## Reference

$$
\frac{C_s}{C_b} = \frac{1}{1 + \left(\phi \coth \phi - 1\right)/\mathrm{Bi}},
\qquad
\eta_\mathrm{ov} = \frac{\eta(\phi)}{1 + \phi^2 \eta(\phi)/(3\,\mathrm{Bi})},
$$

with $\eta(\phi)$ from B-008. The limits are B-008 exactly as
$\mathrm{Bi}\to\infty$, and $\eta_\mathrm{ov} \to 3\,\mathrm{Bi}/\phi^2$ as
$\mathrm{Bi}\to 0$.

The identity $1/\eta_\mathrm{ov} = 1/\eta + \phi^2/(3\,\mathrm{Bi})$ is the
same statement as B-016's $1/\mathrm{Sh}_\mathrm{ov} = 1/2 + 1/(2\mathrm{Da}_s)$:
resistances in series, measured on the two sides of the interface.

![B-017 reference](../figures/B-017-reference.svg)

## Report

- $\eta_\mathrm{ov}(\phi,\mathrm{Bi})$ and its relative error,
- the solved surface trace $C_s/C_b$,
- linearity of $1/\eta_\mathrm{ov}$ in $1/\mathrm{Bi}$,
- recovery of B-008 at large $\mathrm{Bi}$.


## References

@fogler2016
@froment2011
@sulaiman2019b
