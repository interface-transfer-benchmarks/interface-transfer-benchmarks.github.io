---
id: B-007
title: Isothermal catalyst pellet, cylinder
short_title: Pellet cylinder
status: ready

process:
  - reaction
interface_motion: fixed
interface_condition:
  - imposed-value
domains: 1
domain: disk
dimension: 2D
equations:
  - species-diffusion
  - volume-reaction

reference: closed-form
reference_note: modified Bessel functions
numerical_challenge: interior reaction layer and the volume integral of the rate

quantities_of_interest:
  - effectiveness_factor
  - concentration_profile
  - convergence_rate
has_reference_data: true
reference_data:
  - data/B-007/reference.csv

references:
  - thiele1939
  - aris1975
---

# B-007 - Isothermal catalyst pellet, cylinder

## Problem

A cylindrical pellet of radius $R_0$ holds its surface at $C_s$ and consumes the
species internally at rate $k C$.

For $r < R_0$,

$$
D \nabla^2 C = k C .
$$

$$
C(R_0) = C_s, \qquad \partial_r C(0) = 0 .
$$

## Parameters

| Parameter | Symbol |
|---|---|
| pellet radius | $R_0$ |
| diffusivity | $D$ |
| surface concentration | $C_s$ |
| Thiele modulus | $\phi = R_0\sqrt{k/D}$ |

## Reference

$$
\frac{C(r)}{C_s} = \frac{I_0(\phi r/R_0)}{I_0(\phi)},
\qquad
\eta = \frac{2 I_1(\phi)}{\phi I_0(\phi)} .
$$

The asymptote is $\eta \to 2/\phi$.

![B-007 reference](../figures/B-007-reference.svg)

## Report

- $\eta(\phi)$ and its relative error,
- agreement of the two routes to $\eta$,
- radial profile at $\phi=5$,
- observed convergence rate.


## References

@thiele1939
@aris1975
