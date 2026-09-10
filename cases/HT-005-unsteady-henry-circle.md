---
id: HT-005
title: Unsteady Henry jump across a circle
short_title: Unsteady Henry circle
status: ready
benchmark_class: HT

physics:
  - conjugate-transfer
  - mass-diffusion
  - two-phase

process:
  - interfacial-partition

dimension: 2D
geometry: disk
interface_motion: static
reference_type: exact-solution
numerical_challenge: a discontinuous initial field carried across a curved interface

quantities_of_interest:
  - interfacial_flux
  - interface_values
  - interface_jump
  - convergence_rate

has_exact_solution: true
has_reference_data: false

references:
  - libat2025st
  - Crank1975
---

# HT-005 - Unsteady Henry jump across a circle

## Problem

A circle of radius $R_0$ separates two phases with diffusivities $K^+$ inside
and $K^-$ outside. The inner field starts at $\phi_0$, the outer at zero, and
the box carries homogeneous Neumann conditions.

$$
\partial_t \phi^{\pm} = K^{\pm}\nabla^2\phi^{\pm} .
$$

At $r = R_0$,

$$
\phi^+ = \lambda\,\phi^-,
\qquad
K^+\partial_r\phi^+ = K^-\partial_r\phi^- .
$$

## Parameters

| Parameter | Symbol |
|---|---|
| circle radius | $R_0$ |
| diffusivity, inside | $K^+$ |
| diffusivity, outside | $K^-$ |
| Henry ratio | $\lambda$ |
| initial inner value | $\phi_0$ |
| final time | $t_f$ |

## Reference

With $K = \sqrt{K^+/K^-}$ the solution is a Bessel integral on each side,

$$
\phi^+(r,t) = \frac{4\phi_0\lambda K^+ (K^-)^2}{\pi^2 R_0}
\int_0^\infty
\frac{e^{-K^+ u^2 t} J_0(ur) J_1(uR_0)}{u^2\left[\Phi^2 + \Psi^2\right]}\,du ,
$$

$$
\phi^-(r,t) = \frac{2\phi_0\lambda K^+\sqrt{K^-}}{\pi}
\int_0^\infty
\frac{e^{-K^+ u^2 t} J_1(uR_0)\left[J_0(Kur)\Phi - Y_0(Kur)\Psi\right]}
{u\left[\Phi^2 + \Psi^2\right]}\,du ,
$$

with

$$
\Phi = K^+\sqrt{K^-}J_1(R_0u)Y_0(KR_0u) - \lambda K^-\sqrt{K^+}J_0(R_0u)Y_1(KR_0u),
$$

$$
\Psi = K^+\sqrt{K^-}J_1(R_0u)J_0(KR_0u) - \lambda K^-\sqrt{K^+}J_0(R_0u)J_1(KR_0u).
$$

The closed form **jumps** at $r = R_0$. It must be evaluated per phase, or only
at the interface where the observables live; a single radial table interpolated
across the interface returns, in exactly the cut cells, a value belonging to
neither phase, and the error then grows under refinement.

## Report

- the interfacial flux and the two interfacial traces,
- the residual of $\phi^+ - \lambda\phi^-$, which is algebraic and should reach
  zero exactly,
- the conservation budget,
- the same flux error across several decades of $\lambda$,
- observed convergence rate.

A time scheme with a Crank-Nicolson half step reads the initial traces through
its explicit half, where they satisfy no interface row. Two backward-Euler half
steps at the start fix it; without them the budget drifts by 2e-2 instead of by
round-off.

## Results

### Two-fluid cut-cell method - L. Libat, C. Selçuk, E. Chénier, V. Le Chenadec

Measured 2026-09-09. Uniform grid, N = 8 to 256, 16 MPI ranks, $\lambda = 2$,
interfacial flux at $t_f$.

| h | 1 | 0.5 | 0.25 | 0.125 | 0.0625 | 0.03125 |
|---|---|---|---|---|---|---|
| rel. error | 3.3e-1 | 1.6e-1 | 4.3e-2 | 9.4e-3 | 2.2e-3 | 5.7e-4 |
| order | | 1.07 | 1.86 | 2.19 | 2.12 | 1.93 |

Across four decades of the Henry ratio at N = 256 the flux error stays at
5.5e-4 to 5.7e-4: the jump row does not care how large the jump is.

| lambda | 1 | 2 | 10 | 100 |
|---|---|---|---|---|
| rel. error | 5.5e-4 | 5.7e-4 | 5.6e-4 | 5.6e-4 |

The jump row closes at exactly 0.0e+00 at every rung and every $\lambda$, and
the conservation budget holds to 3e-13, which tracks the solver tolerance
rather than the scheme.

![HT-005 convergence](../results/two-fluid-cut-cell/HT-005-convergence.png)

![HT-005 observable](../results/two-fluid-cut-cell/HT-005-sh.png)

![HT-005 Henry sweep](../results/two-fluid-cut-cell/HT-005-henry.png)

## References

@libat2025st
@Crank1975
