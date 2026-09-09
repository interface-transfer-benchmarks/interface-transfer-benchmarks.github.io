---
id: MT-010
title: Plug-flow reactive Graetz problem
short_title: Reactive Graetz
status: ready
benchmark_class: MT

physics:
  - mass-transfer
  - reaction-diffusion
  - advection

process:
  - interfacial-mass-transfer
  - homogeneous-reaction

dimension: axisymmetric
geometry: tube
interface_motion: static
reference_type: exact-solution
numerical_challenge: separating an advective eigenvalue from a reactive shift

quantities_of_interest:
  - sherwood_number
  - axial_decay_rate
  - concentration_profile

has_exact_solution: true
has_reference_data: true
reference_data:
  - data/MT-010/reference.csv
figures:
  - figures/MT-010-reference.svg

references:
  - shah1978
  - higuera2023
---

# MT-010 - Plug-flow reactive Graetz problem

## Purpose

The one case in the family with a flow, and the sharpest available separation
of advection from reaction: a bulk first-order reaction shifts every axial
decay rate by exactly $k/U$ and must leave the asymptotic Sherwood number
unchanged. A scheme that leaks reaction into the transverse eigenvalue fails
visibly.

## Physical Configuration

A circular tube of radius $R$ carries a uniform plug flow $U$. The wall is held
at $C=0$, the inlet carries $C=C_0$, and the fluid consumes the species at rate
$k C$.

## Governing Equations

$$
U \partial_x C
= \frac{D}{r}\,\partial_r\!\left(r\,\partial_r C\right) - k C ,
$$

with axial diffusion neglected, as in the classical Graetz problem.

## Boundary And Initial Conditions

$$
C(x,R) = 0, \qquad \partial_r C(x,0) = 0, \qquad C(0,r) = C_0 .
$$

## Material Parameters

| Parameter | Symbol | Value |
|---|---:|---:|
| tube radius | $R$ | 1 |
| plug velocity | $U$ | 1 |
| diffusivity | $D$ | 1 |
| Damkohler number | $\mathrm{Da} = k R^2/D$ | 0, 1, 4, 16 |

## Reference Solution

Separating variables gives
$C = \sum_n a_n J_0(\lambda_n r/R)\, e^{-\sigma_n x}$, where $\lambda_n$ are
the zeros of $J_0$ and

$$
\sigma_n = \frac{D \lambda_n^2}{U R^2} + \frac{k}{U} .
$$

The reaction shifts every axial decay rate by the same constant $k/U$, so the
transverse eigenvalue problem is untouched. The asymptotic diameter-based
Sherwood number is built from the first eigenvalue alone,

$$
\mathrm{Sh}_\infty = \lambda_0^2 = 5.7831859629\ldots,
\qquad \lambda_0 = 2.4048255577\ldots,
$$

and is therefore independent of $\mathrm{Da}$.

![MT-010 reference](../figures/MT-010-reference.svg)

## Recommended Numerical Setup

Take the velocity as a prescribed analytic field; no momentum solve is needed.
Measure the decay rate by fitting $\ln \bar{C}(x)$ over the fully developed
region, downstream of the entrance length.

## Quantities To Report

- $\sigma_0$ at each $\mathrm{Da}$, against $D\lambda_0^2/(UR^2) + k/U$,
- $\mathrm{Sh}_\infty$ at each $\mathrm{Da}$, which must not move,
- the transverse profile against $J_0(\lambda_0 r/R)$,
- observed convergence rate.

## Known Difficulties

- fitting the decay rate inside the entrance region,
- retaining axial diffusion while comparing against the boundary-layer form,
- a reaction term not exactly balanced by the advective operator, which moves
  $\mathrm{Sh}_\infty$ and is the failure this case detects.

## References

@shah1978
@higuera2023
