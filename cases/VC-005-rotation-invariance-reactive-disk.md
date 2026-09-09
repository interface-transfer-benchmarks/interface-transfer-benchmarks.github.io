---
id: VC-005
title: Rotation invariance of the uptake by a reactive disk
short_title: Rotation invariance
status: ready
benchmark_class: VC

physics:
  - advection
  - mass-transfer
  - reaction-diffusion

process:
  - transport-verification
  - homogeneous-reaction

dimension: 2D
geometry: disk
interface_motion: static
reference_type: exact-solution
numerical_challenge: a flow that must not change an answer it cannot physically change

quantities_of_interest:
  - uptake_rate
  - divergence_residual

has_exact_solution: true
has_reference_data: true
reference_data:
  - data/VC-005/reference.csv
figures:
  - figures/VC-005-reference.svg

references:
  - frankkamenetskii1969
  - Crank1975
---

# VC-005 - Rotation invariance of the uptake by a reactive disk

## Purpose

A null test with a known answer. Solid-body rotation about the centre of an
axisymmetric problem carries no species across any concentration contour, so
the uptake must equal MT-002's stationary value at every rotation rate. Any
dependence on the rotation rate is scheme error, and it is measured against an
exact number rather than against a refined run.

## Physical Configuration

MT-002's reactive disk, with the surrounding medium in solid-body rotation
$\mathbf{u} = \Omega\,\hat{\mathbf{e}}_\theta\, r$ about the disk centre.

## Governing Equations

$$
\mathbf{u}\cdot\nabla C = D \nabla^2 C - \nu C .
$$

Because $C$ is a function of $r$ alone and $\mathbf{u}$ is purely azimuthal,
$\mathbf{u}\cdot\nabla C \equiv 0$ and the steady field is MT-002's exactly.

## Boundary And Initial Conditions

$$
C(R_0) = C_s, \qquad C(r\to\infty) = 0 .
$$

## Material Parameters

| Parameter | Symbol | Value |
|---|---:|---:|
| disk radius | $R_0$ | 1 |
| diffusivity | $D$ | 1 |
| Damkohler number | $\mathrm{Da}$ | 1, 16, 100 |
| rotation rate | $\Omega$ | 0, 1, 10, 100 |

## Reference Solution

The uptake is MT-002's, unchanged by $\Omega$,

$$
F = 2\pi D C_s \sqrt{\mathrm{Da}}\,
\frac{K_1(\sqrt{\mathrm{Da}})}{K_0(\sqrt{\mathrm{Da}})} ,
$$

and the discrete divergence of the velocity field, weighted by the cell volume
fractions, must be at round-off.

![VC-005 reference](../figures/VC-005-reference.svg)

## Recommended Numerical Setup

Impose the rotation as an analytic velocity field. Sweep $\Omega$ over at least
two decades at fixed mesh, so that the cell Peclet number varies while the
exact answer does not.

## Quantities To Report

- $F(\Omega)$ at each $\mathrm{Da}$, and its drift relative to $\Omega=0$,
- the volume-fraction-weighted divergence residual,
- the largest cell Peclet number at which the drift stays below a stated
  tolerance.

## Known Difficulties

- a velocity field that is analytically but not discretely solenoidal, which
  makes the rotation a spurious source,
- upwinding that adds diffusion proportional to $\Omega$, which lowers $F$,
- cut cells where the azimuthal flux is not exactly tangential.

## References

@frankkamenetskii1969
@Crank1975
