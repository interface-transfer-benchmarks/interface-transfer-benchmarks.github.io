---
id: B-003
title: Unsteady diffusion to a sphere
short_title: Unsteady sphere
status: ready

process:
  - interfacial-transfer
interface_motion: fixed
interface_condition:
  - imposed-value
domains: 1
domain: sphere
dimension: 3D
equations:
  - species-diffusion

reference: closed-form
reference_note: exact unsteady solution
numerical_challenge: the singular initial flux and its long-time approach to Sh = 2

quantities_of_interest:
  - sherwood_number
  - concentration_profile
  - convergence_rate
has_reference_data: true
reference_data:
  - data/B-003/reference.csv

references:
  - Crank1975
---

# B-003 - Unsteady diffusion to a sphere

## Problem

A sphere of radius $R_0$ is held at $C=C_s$ from $t=0$ in an infinite medium
initially at $C=0$. There is no flow and no reaction.

For $r > R_0$,

$$
\partial_t C = D \nabla^2 C .
$$

$$
C(R_0,t) = C_s, \qquad C(r,0) = 0, \qquad C(r\to\infty,t)=0 .
$$

## Parameters

| Parameter | Symbol |
|---|---|
| sphere radius | $R_0$ |
| diffusivity | $D$ |
| surface concentration | $C_s$ |
| Fourier number | $\mathrm{Fo}=Dt/R_0^2$ |

## Reference

With $\xi = (r-R_0)/R_0$,

$$
\frac{C}{C_s} = \frac{1}{1+\xi}\,
\operatorname{erfc}\!\left(\frac{\xi}{2\sqrt{\mathrm{Fo}}}\right),
$$

and

$$
\mathrm{Sh}(\mathrm{Fo}) = 2 + \frac{2}{\sqrt{\pi \mathrm{Fo}}} .
$$

![B-003 reference](../figures/B-003-reference.svg)

## Report

- $\mathrm{Sh}(\mathrm{Fo})$ against the closed form,
- the approach to $\mathrm{Sh}=2$ at large $\mathrm{Fo}$,
- profiles at $\mathrm{Fo}=0.01$, $0.1$ and $1$,
- observed convergence rate in space and in time.


## References

@Crank1975
