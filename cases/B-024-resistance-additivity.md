---
id: B-024
title: Resistance additivity across a conjugate interface
short_title: Resistance additivity
status: ready

process:
  - verification
  - absorption
interface_motion: fixed
interface_condition:
  - conjugate
domains: 2
domain: sphere
dimension: 3D
equations:
  - species-diffusion

reference: closed-form
reference_note: exact identity between transfer coefficients
numerical_challenge: three separately measured transfer coefficients that must compose

quantities_of_interest:
  - sherwood_number
  - internal_sherwood_number
  - additivity_residual
has_reference_data: true
reference_data:
  - data/B-024/reference.csv

references:
  - sulaiman2019b
  - froment2011
---

# B-024 - Resistance additivity across a conjugate interface

## Problem

A sphere of radius $R_0$ of phase 1 with diffusivity $D_1$, in a quiescent
exterior of phase 2 with diffusivity $D_2$, coupled by a Henry partition $H$
and flux continuity. No reaction anywhere.

$$
\partial_t C_i = D_i \nabla^2 C_i, \qquad i = 1,2 .
$$

At the interface, $C_1 = H C_2$ with continuous flux. The exterior far field is
fixed, the interior starts uniform.

## Parameters

| Parameter | Symbol |
|---|---|
| sphere radius | $R_0$ |
| diffusivity ratio | $D_1/D_2$ |
| partition coefficient | $H$ |
| box size | $L$ |

## Reference

$$
\frac{1}{\mathrm{Sh}} = \frac{1}{\mathrm{Sh}_i} + \frac{H\,D_1}{D_2\,\mathrm{Sh}_e},
$$

with all three measured from the same solve. The residual is the observable,
and its target is zero to machine precision at any Peclet number.

The identity holds only if $\mathrm{Sh}_e$ is measured, never substituted. For
a quiescent sphere in a finite box the concentric-shell value is
$\mathrm{Sh}_e = 2/(1 - R_0/R_\mathrm{out})$, and $R_\mathrm{out}$ is the
radius of the sphere of the same volume as the box,
$R_\mathrm{out} = (3/4\pi)^{1/3} L = 0.6204\,L$, not $L/2$. Substituting the
infinite-domain value $\mathrm{Sh}_e = 2$ in a box with $R_0/R_\mathrm{out}
= 0.46$ is an 84% error, not a small one.

![B-024 reference](../figures/B-024-reference.svg)

## Report

- the additivity residual, at each $D_1/D_2$ and $H$,
- the three Sherwood numbers separately,
- measured $\mathrm{Sh}_e$ against the concentric-shell value at each box size.


## References

@sulaiman2019b
@froment2011
