---
id: B-025
title: Reactive absorption into a droplet
short_title: Reactive droplet
status: ready

process:
  - absorption
  - reaction
interface_motion: fixed
interface_condition:
  - conjugate
domains: 2
domain: disk
dimension: 2D
equations:
  - species-diffusion
  - volume-reaction

reference: closed-form
reference_note: exact steady solution
numerical_challenge: a Henry jump and an interior reaction solved together

quantities_of_interest:
  - uptake_rate
  - concentration_profile
  - interface_jump
has_reference_data: true
reference_data:
  - data/B-025/reference.csv

references:
  - libat2025st
  - Crank1975
---

# B-025 - Reactive absorption into a droplet

## Problem

A droplet of radius $R_0$ occupies $r<R_0$ with diffusivity $D_1$ and consumes the
species at rate $k C$. The exterior phase has diffusivity $D_2$. The
concentrations are related at the interface by a Henry coefficient $H$.

$$
D_1 \nabla^2 C_1 = k C_1 \quad (r<R_0), \qquad
D_2 \nabla^2 C_2 = 0 \quad (r>R_0).
$$

At $r=R_0$ the concentrations satisfy the partition $C_1 = H C_2$ and the
fluxes are continuous. The exterior far field is set to unity.

## Parameters

| Parameter | Symbol |
|---|---|
| droplet radius | $R_0$ |
| interior diffusivity | $D_1$ |
| exterior diffusivity | $D_2$ |
| Henry coefficient | $H$ |
| Damkohler number | $\mathrm{Da} = k R_0^2/D_1$ |

## Reference

With $q = \sqrt{k/D_1}$, so that $qR = \sqrt{\mathrm{Da}}$,

$$
C_1(r) = H\,\frac{I_0(q r)}{I_0(q R_0)},
\qquad
C_2(r) = 1 + \frac{D_1}{D_2}\,H\, q R_0\,
\frac{I_1(qR)}{I_0(qR)} \ln\frac{r}{R},
$$

and the uptake per unit depth is

$$
F = 2\pi D_1 H\, q R_0\, \frac{I_1(qR)}{I_0(qR)} .
$$

![B-025 reference](../figures/B-025-reference.svg)

## Report

- $F(\mathrm{Da},H)$ and its relative error,
- the interfacial jump $C_1/C_2 - H$ at the interface,
- profiles on both sides at $\mathrm{Da}=4$, $H=2$,
- observed convergence rate.


## References

@libat2025st
@Crank1975
