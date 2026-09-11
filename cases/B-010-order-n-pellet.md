---
id: B-010
title: n-th order pellet and the generalized Thiele modulus
short_title: n-th order pellet
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

reference: quadrature
reference_note: reduced ODE integrated to tolerance
numerical_challenge: an interior reaction layer with a dead core once the order and the modulus are large enough

quantities_of_interest:
  - effectiveness_factor
  - centre_value
  - convergence_rate
has_reference_data: true
reference_data:
  - data/B-010/reference.csv

references:
  - aris1975
  - thiele1939
---

# B-010 - n-th order pellet and the generalized Thiele modulus

## Problem

A pellet of radius $R_0$ holds its surface at $C_s$ and consumes the species
internally at rate $k C^n$.

$$
D \nabla^2 C = k\,C^n, \qquad r < R_0,
$$

with $C(R_0) = C_s$ and $\partial_r C(0) = 0$.

## Parameters

| Parameter | Symbol |
|---|---|
| pellet radius | $R_0$ |
| diffusivity | $D$ |
| surface concentration | $C_s$ |
| Thiele modulus | $\phi = R_0\sqrt{k C_s^{n-1}/D}$ |
| reaction order | $n$ |
| generalized modulus | $\Phi = \phi\sqrt{(n+1)/2}$ |

## Reference

In the scaled radius $x = r/R_0$ and $y = C/C_s$,

$$
y'' + \frac{s}{x}y' = \phi^2 y^n,
\qquad
y(1) = 1,
\qquad
y'(0) = 0 ,
$$

with $s = 1$ for a disk and $2$ for a sphere, and

$$
\eta = \frac{(s+1)\,y'(1)}{\phi^2} .
$$

At $n = 1$ this returns $\eta = 2I_1(\phi)/(\phi I_0(\phi))$. Aris' generalized
modulus $\Phi$ collapses the curves for different $n$ onto one asymptote:
$\eta\Phi \to 2$ for a disk, $1$ for a slab. Fix one convention and say which.

For $n < 1$ the concentration reaches zero at a finite radius and the pellet
grows a dead core. The asymptote then loses the geometry factor it is being
compared against, since the reaction occupies an annulus rather than the disk.

![B-010 reference](../figures/B-010-reference.svg)

## Report

- $\eta(\phi, n)$ against the radial solve,
- the collapse $\eta\Phi$ against its asymptote,
- the centre value, which says whether a dead core has formed,
- agreement between $\eta$ from the interface flux and $\eta$ from the volume
  average, which is the cheapest dead-core detector,
- observed convergence rate.


## References

@aris1975
@thiele1939
