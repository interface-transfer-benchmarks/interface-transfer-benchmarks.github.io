---
id: MT-007
title: Isothermal catalyst pellet, sphere
short_title: Pellet sphere
status: ready
benchmark_class: MT

physics:
  - mass-transfer
  - reaction-diffusion

process:
  - catalysis
  - homogeneous-reaction

dimension: 3D
geometry: sphere
interface_motion: static
reference_type: exact-solution
numerical_challenge: interior reaction layer on a curved three-dimensional interface

quantities_of_interest:
  - effectiveness_factor
  - concentration_profile
  - convergence_rate

has_exact_solution: true
has_reference_data: true
reference_data:
  - data/MT-007/reference.csv
figures:
  - figures/MT-007-reference.svg

references:
  - thiele1939
  - fogler2016
---

# MT-007 - Isothermal catalyst pellet, sphere

## Purpose

The three-dimensional form of MT-006, and the case where the classical
factor-of-three convention error appears.

## Physical Configuration

A spherical pellet of radius $R$ at surface concentration $C_s$, consuming the
species internally at rate $k C$.

## Governing Equations

For $r < R$,

$$
D \nabla^2 C = k C .
$$

## Boundary And Initial Conditions

$$
C(R) = C_s, \qquad \partial_r C(0) = 0 .
$$

## Material Parameters

| Parameter | Symbol | Value |
|---|---:|---:|
| pellet radius | $R$ | 1 |
| diffusivity | $D$ | 1 |
| surface concentration | $C_s$ | 1 |
| Thiele modulus | $\phi = R\sqrt{k/D}$ | 0.1 to 20 |

## Reference Solution

$$
\frac{C(r)}{C_s} = \frac{R}{r}\,\frac{\sinh(\phi r/R)}{\sinh \phi},
\qquad
\eta = \frac{3}{\phi^2}\left(\phi \coth \phi - 1\right).
$$

The same result in the characteristic-length convention $L=(R/3)\sqrt{k/D}$
reads $\eta = (1/L)\left(1/\tanh(3L) - 1/(3L)\right)$. Fix one convention and
state it: this is the standard source of a factor-of-three disagreement. The
asymptote is $\eta \to 3/\phi$.

![MT-007 reference](../figures/MT-007-reference.svg)

## Recommended Numerical Setup

As MT-006, in three dimensions. Report $\eta$ by both the volume-integral and
the surface-flux route.

## Quantities To Report

- $\eta(\phi)$ and its relative error,
- agreement of the two routes to $\eta$,
- radial profile at $\phi=5$,
- observed convergence rate.

## Known Difficulties

- the radius-based versus characteristic-length Thiele modulus,
- surface-integration error on a curved interface entering $\eta$ directly.

## References

@thiele1939
@fogler2016
