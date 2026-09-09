---
id: MT-006
title: Isothermal catalyst pellet, cylinder
short_title: Pellet cylinder
status: ready
benchmark_class: MT

physics:
  - mass-transfer
  - reaction-diffusion

process:
  - catalysis
  - homogeneous-reaction

dimension: 2D
geometry: disk
interface_motion: static
reference_type: exact-solution
numerical_challenge: interior reaction layer and the volume integral of the rate

quantities_of_interest:
  - effectiveness_factor
  - concentration_profile
  - convergence_rate

has_exact_solution: true
has_reference_data: true
reference_data:
  - data/MT-006/reference.csv
figures:
  - figures/MT-006-reference.svg

references:
  - thiele1939
  - aris1975
---

# MT-006 - Isothermal catalyst pellet, cylinder

## Purpose

Moves the reaction inside the interface. The observable is the effectiveness
factor, a volume integral of the reaction rate, so the case checks the interior
solve and the integration weights rather than an interfacial flux.

## Physical Configuration

A cylindrical pellet of radius $R$ holds its surface at $C_s$ and consumes the
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
\frac{C(r)}{C_s} = \frac{I_0(\phi r/R)}{I_0(\phi)},
\qquad
\eta = \frac{2 I_1(\phi)}{\phi I_0(\phi)} .
$$

The asymptote is $\eta \to 2/\phi$.

![MT-006 reference](../figures/MT-006-reference.svg)

## Recommended Numerical Setup

Resolve the interior layer of thickness $R/\phi$; report the cells per layer at
which 1% on $\eta$ is reached. Compute $\eta$ both as the volume integral of
the rate and as the surface flux divided by the rate at $C_s$: the two routes
must agree to solver tolerance.

## Quantities To Report

- $\eta(\phi)$ and its relative error,
- agreement of the two routes to $\eta$,
- radial profile at $\phi=5$,
- observed convergence rate.

## Known Difficulties

- radius-based versus half-thickness-based Thiele moduli,
- integration weights in cut cells dominating the error in $\eta$,
- the $\phi \to 0$ limit, where $\eta \to 1$ hides scheme error.

## References

@thiele1939
@aris1975
