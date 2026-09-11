---
id: B-015
title: Rotation invariance of the uptake by a reactive disk
short_title: Rotation invariance
status: ready

process:
  - verification
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
  - advection

reference: closed-form
reference_note: exact steady solution
numerical_challenge: a flow that must not change an answer it cannot physically change

quantities_of_interest:
  - uptake_rate
  - divergence_residual
has_reference_data: true
reference_data:
  - data/B-015/reference.csv

references:
  - frankkamenetskii1969
  - Crank1975
---

# B-015 - Rotation invariance of the uptake by a reactive disk

## Problem

B-005's reactive disk, with the surrounding medium in solid-body rotation
$\mathbf{u} = \Omega\,\hat{\mathbf{e}}_\theta\, r$ about the disk centre.

$$
\mathbf{u}\cdot\nabla C = D \nabla^2 C - k C .
$$

Because $C$ is a function of $r$ alone and $\mathbf{u}$ is purely azimuthal,
$\mathbf{u}\cdot\nabla C \equiv 0$ and the steady field is B-005's exactly.

$$
C(R_0) = C_s, \qquad C(r\to\infty) = 0 .
$$

## Parameters

| Parameter | Symbol |
|---|---|
| disk radius | $R_0$ |
| diffusivity | $D$ |
| Damkohler number | $\mathrm{Da}$ |
| rotation rate | $\Omega$ |

## Reference

The uptake is B-005's, unchanged by $\Omega$,

$$
F = 2\pi D C_s \sqrt{\mathrm{Da}}\,
\frac{K_1(\sqrt{\mathrm{Da}})}{K_0(\sqrt{\mathrm{Da}})} ,
$$

and the discrete divergence of the velocity field, weighted by the cell volume
fractions, must be at round-off.

![B-015 reference](../figures/B-015-reference.svg)

## Report

- $F(\Omega)$ at each $\mathrm{Da}$, and its drift relative to $\Omega=0$,
- the volume-fraction-weighted divergence residual,
- the largest cell Peclet number at which the drift stays below a stated
  tolerance.


## References

@frankkamenetskii1969
@Crank1975
