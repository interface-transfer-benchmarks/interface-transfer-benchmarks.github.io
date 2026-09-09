---
id: VC-003
title: Advected Gaussian in a uniform flow
short_title: Advected Gaussian
status: ready
benchmark_class: VC

physics:
  - advection
  - mass-transfer

process:
  - transport-verification

dimension: 2D
geometry: periodic-box
interface_motion: static
reference_type: exact-solution
numerical_challenge: separating numerical diffusion from phase error

quantities_of_interest:
  - peak_amplitude
  - centroid_position
  - error_norms

has_exact_solution: true
has_reference_data: true
reference_data:
  - data/VC-003/reference.csv
figures:
  - figures/VC-003-reference.svg

references:
  - Crank1975
---

# VC-003 - Advected Gaussian in a uniform flow

## Problem

A Gaussian blob of initial variance $\sigma_0^2$ is carried by a uniform
velocity $\mathbf{U}$ across a periodic box while it diffuses.

$$
\partial_t C + \mathbf{U}\cdot\nabla C = D \nabla^2 C .
$$

$$
C(\mathbf{x},0) = \frac{1}{2\pi\sigma_0^2}
\exp\!\left(-\frac{|\mathbf{x}-\mathbf{x}_0|^2}{2\sigma_0^2}\right),
$$

periodic on all faces.

## Parameters

| Parameter | Symbol |
|---|---|
| box side | $L$ |
| initial standard deviation | $\sigma_0$ |
| velocity | $\mathbf{U}$ |
| diffusivity | $D$ |
| cell Peclet number | $\mathrm{Pe}_h = \lvert U\rvert h/D$ |

## Reference

The blob translates without change of shape and spreads exactly,

$$
C(\mathbf{x},t) = \frac{1}{2\pi\sigma^2(t)}
\exp\!\left(-\frac{|\mathbf{x}-\mathbf{x}_0-\mathbf{U}t|^2}{2\sigma^2(t)}\right),
\qquad
\sigma^2(t) = \sigma_0^2 + 2Dt ,
$$

so the peak value is $1/(2\pi\sigma^2(t))$ and the centroid is exactly
$\mathbf{x}_0 + \mathbf{U}t$. Solid-body rotation admits the same solution with
$\mathbf{U}$ replaced by the rotating field, provided the blob stays away from
the axis.

![VC-003 reference](../figures/VC-003-reference.svg)

## Report

- peak amplitude against $1/(2\pi\sigma^2(t))$, as a function of
  $\mathrm{Pe}_h$,
- centroid displacement against $\mathbf{U}t$,
- $L_2$ and $L_\infty$ errors against the closed form,
- observed convergence rate.

## References

@Crank1975
