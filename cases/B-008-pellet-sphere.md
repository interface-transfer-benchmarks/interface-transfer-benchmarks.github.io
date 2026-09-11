---
id: B-008
title: Isothermal catalyst pellet, sphere
short_title: Pellet sphere
status: ready

process:
  - reaction
interface_motion: fixed
interface_condition:
  - imposed-value
domains: 1
domain: sphere
dimension: 3D
equations:
  - species-diffusion
  - volume-reaction

reference: closed-form
reference_note: exact steady solution
numerical_challenge: interior reaction layer on a curved three-dimensional interface

quantities_of_interest:
  - effectiveness_factor
  - concentration_profile
  - convergence_rate
has_reference_data: true
reference_data:
  - data/B-008/reference.csv

references:
  - thiele1939
  - fogler2016
---

# B-008 - Isothermal catalyst pellet, sphere

## Problem

A spherical pellet of radius $R_0$ at surface concentration $C_s$, consuming the
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
\frac{C(r)}{C_s} = \frac{R}{r}\,\frac{\sinh(\phi r/R_0)}{\sinh \phi},
\qquad
\eta = \frac{3}{\phi^2}\left(\phi \coth \phi - 1\right).
$$

The same result in the characteristic-length convention $L=(R_0/3)\sqrt{k/D}$
reads $\eta = (1/L)\left(1/\tanh(3L) - 1/(3L)\right)$. Fix one convention and
state it: this is the standard source of a factor-of-three disagreement. The
asymptote is $\eta \to 3/\phi$.

![B-008 reference](../figures/B-008-reference.svg)

## Report

- $\eta(\phi)$ and its relative error,
- agreement of the two routes to $\eta$,
- radial profile at $\phi=5$,
- observed convergence rate.


## References

@thiele1939
@fogler2016
