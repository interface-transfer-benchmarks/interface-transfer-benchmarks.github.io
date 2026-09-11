---
id: B-004
title: Steady reaction-diffusion outside a sphere
short_title: Reactive sphere
status: ready

process:
  - reaction
interface_motion: fixed
interface_condition:
  - imposed-value
domains: 1
domain: sphere
dimension: 3D
equations:
  - species-diffusion
  - volume-reaction

reference: closed-form
reference_note: exact steady solution
numerical_challenge: resolving the reaction layer of thickness R0/sqrt(Da)

quantities_of_interest:
  - sherwood_number
  - concentration_profile
  - convergence_rate
has_reference_data: true
reference_data:
  - data/B-004/reference.csv

references:
  - frankkamenetskii1969
  - fogler2016
---

# B-004 - Steady reaction-diffusion outside a sphere

## Problem

A sphere of radius $R_0$ holds its surface at concentration $C_s$. The
surrounding medium is quiescent and consumes the species at rate $k C$.

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
| sphere radius | $R_0$ |
| diffusivity | $D$ |
| surface concentration | $C_s$ |
| Damkohler number | $\mathrm{Da}=k R_0^2/D$ |

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

![B-004 reference](../figures/B-004-reference.svg)

## Report

- $\mathrm{Sh}$ at each $\mathrm{Da}$ and its relative error,
- radial concentration profile at $\mathrm{Da} = 1$ and $100$,
- observed convergence rate under grid refinement,
- cells per reaction layer at which 1% on $\mathrm{Sh}$ is reached.


## References

@frankkamenetskii1969
@fogler2016
