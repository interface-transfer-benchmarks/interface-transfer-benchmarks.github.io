---
id: B-005
title: Steady reactive uptake outside a disk
short_title: Reactive disk
status: ready

process:
  - reaction
interface_motion: fixed
interface_condition:
  - imposed-value
domains: 1
domain: disk
dimension: 2D
equations:
  - species-diffusion
  - volume-reaction

reference: closed-form
reference_note: modified Bessel functions
numerical_challenge: logarithmic far field that is only regularised by reaction

quantities_of_interest:
  - uptake_rate
  - concentration_profile
  - convergence_rate
has_reference_data: true
reference_data:
  - data/B-005/reference.csv

references:
  - frankkamenetskii1969
  - Crank1975
---

# B-005 - Steady reactive uptake outside a disk

## Problem

A disk of radius $R_0$ at concentration $C_s$ in a quiescent plane that
consumes the species at rate $k C$.

For $r > R_0$,

$$
D \nabla^2 C = k C .
$$

$$
C(R_0) = C_s, \qquad C(r \to \infty) = 0 .
$$

## Parameters

| Parameter | Symbol |
|---|---|
| disk radius | $R_0$ |
| diffusivity | $D$ |
| surface concentration | $C_s$ |
| Damkohler number | $\mathrm{Da}=k R_0^2/D$ |

## Reference

With $m=\sqrt{\mathrm{Da}}/R_0$,

$$
\frac{C(r)}{C_s} = \frac{K_0(m r)}{K_0(m R_0)},
$$

and the uptake per unit depth is

$$
F = 2\pi R_0 D C_s\, m \,\frac{K_1(m R_0)}{K_0(m R_0)}
  = 2\pi D C_s \sqrt{\mathrm{Da}}\,
    \frac{K_1(\sqrt{\mathrm{Da}})}{K_0(\sqrt{\mathrm{Da}})} .
$$

![B-005 reference](../figures/B-005-reference.svg)

## Report

- $F$ at each $\mathrm{Da}$ and its relative error,
- radial profile against $K_0(mr)/K_0(mR_0)$,
- observed convergence rate,
- the drift of $F$ with box size at fixed $h$, at low and high $\mathrm{Da}$.


## References

@frankkamenetskii1969
@Crank1975
