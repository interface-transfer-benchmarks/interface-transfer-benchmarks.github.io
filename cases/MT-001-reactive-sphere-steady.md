---
id: MT-001
title: Steady reaction-diffusion outside a sphere
short_title: Reactive sphere
status: ready
benchmark_class: MT

physics:
  - mass-transfer
  - reaction-diffusion

process:
  - interfacial-mass-transfer
  - homogeneous-reaction

dimension: 3D
geometry: sphere
interface_motion: static
reference_type: exact-solution
numerical_challenge: resolving the reaction layer of thickness R0/sqrt(Da)

quantities_of_interest:
  - sherwood_number
  - concentration_profile
  - convergence_rate

has_exact_solution: true
has_reference_data: true
reference_data:
  - data/MT-001/reference.csv
figures:
  - figures/MT-001-reference.svg

references:
  - frankkamenetskii1969
  - fogler2016
---

# MT-001 - Steady reaction-diffusion outside a sphere

## Problem

A sphere of radius $R_0$ holds its surface at concentration $C_s$. The
surrounding medium is quiescent and consumes the species at rate $\nu C$.

For $r > R_0$,

$$
D \nabla^2 C = \nu C .
$$

$$
C(R_0) = C_s, \qquad C(r \to \infty) = 0 .
$$

## Parameters

| Parameter | Symbol |
|---|---|
| sphere radius | $R_0$ |
| diffusivity | $D$ |
| surface concentration | $C_s$ |
| Damkohler number | $\mathrm{Da}=\nu R_0^2/D$ |

## Reference

$$
\frac{C(r)}{C_s} = \frac{R_0}{r}
\exp\left(-\sqrt{\mathrm{Da}}\,\frac{r-R_0}{R_0}\right),
$$

and the diameter-based Sherwood number is

$$
\mathrm{Sh} = \frac{2 R_0 k_c}{D} = 2\left(1+\sqrt{\mathrm{Da}}\right).
$$

The conventions matter: $\mathrm{Sh}$ is diameter-based, so $\mathrm{Sh}\to 2$
at $\mathrm{Da}=0$, while $\mathrm{Da}$ is radius-based. A diameter-based
Damkohler number would give $2(1+\phi/2)$ and look like a factor-of-two error.

![MT-001 reference](../figures/MT-001-reference.svg)

## Report

- $\mathrm{Sh}$ at each $\mathrm{Da}$ and its relative error,
- radial concentration profile at $\mathrm{Da} = 1$ and $100$,
- observed convergence rate under grid refinement,
- cells per reaction layer at which 1% on $\mathrm{Sh}$ is reached.

## Results

### Two-fluid cut-cell method

L. Libat, C. Selçuk, E. Chénier, V. Le Chenadec. Measured 2026-09-09.

Uniform grid, N = 128, 8 MPI ranks; also run on an octree and an adaptive octree. Da = 0, 1, 4, 10, 100, 1000.

| Da | 0 | 1 | 4 | 10 | 100 | 1000 |
|---|---|---|---|---|---|---|
| n/l | inf | 25.6 | 12.8 | 8.1 | 2.6 | 0.8 |
| rel. error | 4.7e-4 | 7.7e-4 | 1.5e-3 | 2.6e-3 | 1.5e-2 | 9.3e-2 |
| order | 2.03 | 2.00 | 1.96 | 1.93 | 1.76 | 1.33 |

The error is set by `n/l`, not by Da: second order is retained while the layer
is resolved and degrades once it is not.

![MT-001 convergence](../results/two-fluid-cut-cell/MT-001-convergence.png)

![MT-001 observable](../results/two-fluid-cut-cell/MT-001-sh.png)

## References

@frankkamenetskii1969
@fogler2016
