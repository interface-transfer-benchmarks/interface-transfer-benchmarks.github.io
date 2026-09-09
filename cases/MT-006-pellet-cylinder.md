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

## Problem

A cylindrical pellet of radius $R$ holds its surface at $C_s$ and consumes the
species internally at rate $k C$.

For $r < R$,

$$
D \nabla^2 C = k C .
$$

$$
C(R) = C_s, \qquad \partial_r C(0) = 0 .
$$

## Parameters

| Parameter | Symbol | Value |
|---|---:|---:|
| pellet radius | $R$ | 1 |
| diffusivity | $D$ | 1 |
| surface concentration | $C_s$ | 1 |
| Thiele modulus | $\phi = R\sqrt{k/D}$ | 0.1 to 20 |

## Reference

$$
\frac{C(r)}{C_s} = \frac{I_0(\phi r/R)}{I_0(\phi)},
\qquad
\eta = \frac{2 I_1(\phi)}{\phi I_0(\phi)} .
$$

The asymptote is $\eta \to 2/\phi$.

![MT-006 reference](../figures/MT-006-reference.svg)

## Report

- $\eta(\phi)$ and its relative error,
- agreement of the two routes to $\eta$,
- radial profile at $\phi=5$,
- observed convergence rate.

## Results

Measured with the `basilisk-libat` cut-cell solver, 2026-09-09.

N = 128 uniform, 2D, 16 ranks.

| phi | 0.5 | 1 | 2 | 5 | 10 | 20 |
|---|---|---|---|---|---|---|
| rel. error | 1.3e-5 | 5.3e-5 | 2.2e-4 | 1.5e-3 | 6.2e-3 | 2.3e-2 |
| order | 2.04 | 2.04 | 2.01 | 1.94 | 1.83 | 1.65 |

## References

@thiele1939
@aris1975
