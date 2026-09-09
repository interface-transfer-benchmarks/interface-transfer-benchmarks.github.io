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

## Purpose

The meter, not the physics. Every transfer number in the `MT` and `HT`
families is a flux, and a flux is an amplitude, so a scheme that damps a
Gaussian under-reports a Sherwood number in exactly the way an unresolved
reaction layer does. This case separates the two causes before any
$\mathrm{Sh}(\mathrm{Pe})$ is quoted: the peak amplitude is the
numerical-diffusion meter and the centroid is the phase-error meter.

## Physical Configuration

A Gaussian blob of initial variance $\sigma_0^2$ is carried by a uniform
velocity $\mathbf{U}$ across a periodic box while it diffuses.

## Governing Equations

$$
\partial_t C + \mathbf{U}\cdot\nabla C = D \nabla^2 C .
$$

## Boundary And Initial Conditions

$$
C(\mathbf{x},0) = \frac{1}{2\pi\sigma_0^2}
\exp\!\left(-\frac{|\mathbf{x}-\mathbf{x}_0|^2}{2\sigma_0^2}\right),
$$

periodic on all faces.

## Material Parameters

| Parameter | Symbol | Value |
|---|---:|---:|
| box side | $L$ | 1 |
| initial standard deviation | $\sigma_0$ | 0.05 |
| velocity | $\mathbf{U}$ | (1, 0) |
| diffusivity | $D$ | $10^{-4}$ |
| cell Peclet number | $\mathrm{Pe}_h = |U| h/D$ | swept |

## Reference Solution

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

## Recommended Numerical Setup

Sweep the cell Peclet number at fixed resolution by varying $D$, and sweep the
Courant number at fixed $\mathrm{Pe}_h$. Report peak amplitude and centroid
separately: a scheme can be exact in one and poor in the other.

## Quantities To Report

- peak amplitude against $1/(2\pi\sigma^2(t))$, as a function of
  $\mathrm{Pe}_h$,
- centroid displacement against $\mathbf{U}t$,
- $L_2$ and $L_\infty$ errors against the closed form,
- observed convergence rate.

## Known Difficulties

- reporting only a norm, which merges amplitude loss with phase error,
- an initial blob too narrow for the mesh, so that the initial condition itself
  is under-resolved,
- diffusion small enough that the exact spreading is below the scheme's own
  numerical diffusion, which makes the meter unreadable.

## References

@Crank1975
