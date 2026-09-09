---
id: MT-003
title: Unsteady diffusion to a sphere
short_title: Unsteady sphere
status: ready
benchmark_class: MT

physics:
  - mass-transfer

process:
  - interfacial-mass-transfer

dimension: 3D
geometry: sphere
interface_motion: static
reference_type: exact-solution
numerical_challenge: the singular initial flux and its long-time approach to Sh = 2

quantities_of_interest:
  - sherwood_number
  - concentration_profile
  - convergence_rate

has_exact_solution: true
has_reference_data: true
reference_data:
  - data/MT-003/reference.csv
figures:
  - figures/MT-003-reference.svg

references:
  - Crank1975
---

# MT-003 - Unsteady diffusion to a sphere

## Purpose

The non-reactive transient that MT-004 generalises. It checks the time
discretisation of the interfacial flux against a closed form whose early-time
behaviour is singular and whose late-time limit is the steady value
$\mathrm{Sh}=2$.

## Physical Configuration

A sphere of radius $R_0$ is held at $C=C_s$ from $t=0$ in an infinite medium
initially at $C=0$. There is no flow and no reaction.

## Governing Equations

For $r > R_0$,

$$
\partial_t C = D \nabla^2 C .
$$

## Boundary And Initial Conditions

$$
C(R_0,t) = C_s, \qquad C(r,0) = 0, \qquad C(r\to\infty,t)=0 .
$$

## Material Parameters

| Parameter | Symbol | Value |
|---|---:|---:|
| sphere radius | $R_0$ | 1 |
| diffusivity | $D$ | 1 |
| surface concentration | $C_s$ | 1 |
| Fourier number | $\mathrm{Fo}=Dt/R_0^2$ | 0.001 to 10 |

## Reference Solution

With $\xi = (r-R_0)/R_0$,

$$
\frac{C}{C_s} = \frac{1}{1+\xi}\,
\operatorname{erfc}\!\left(\frac{\xi}{2\sqrt{\mathrm{Fo}}}\right),
$$

and

$$
\mathrm{Sh}(\mathrm{Fo}) = 2 + \frac{2}{\sqrt{\pi \mathrm{Fo}}} .
$$

![MT-003 reference](../figures/MT-003-reference.svg)

## Recommended Numerical Setup

Start at $\mathrm{Fo}_0 = 10^{-3}$ from the reference profile rather than from
a step, so that the initial diffusion layer is resolved. Keep the outer
boundary at $r \ge R_0 + 6\sqrt{D t_\mathrm{end}}$ or impose the reference
value there.

## Quantities To Report

- $\mathrm{Sh}(\mathrm{Fo})$ against the closed form,
- the approach to $\mathrm{Sh}=2$ at large $\mathrm{Fo}$,
- profiles at $\mathrm{Fo}=0.01$, $0.1$ and $1$,
- observed convergence rate in space and in time.

## Known Difficulties

- starting from a discontinuous initial condition,
- an outer boundary reached by the diffusion layer before $t_\mathrm{end}$,
- first-order time stepping masked by the $\mathrm{Fo}^{-1/2}$ transient.

## References

@Crank1975
