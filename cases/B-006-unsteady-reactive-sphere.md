---
id: B-006
title: Unsteady diffusion with a first-order reaction outside a sphere
short_title: Unsteady reactive sphere
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
reference_note: exact unsteady solution
numerical_challenge: a transient and a reaction layer resolved at once

quantities_of_interest:
  - sherwood_number
  - concentration_profile
  - convergence_rate
has_reference_data: true
reference_data:
  - data/B-006/reference.csv

references:
  - Crank1975
  - frankkamenetskii1969
---

# B-006 - Unsteady diffusion with a first-order reaction outside a sphere

## Problem

B-003's sphere in a medium that also consumes the species at rate $k C$.

For $r > R_0$,

$$
\partial_t C = D \nabla^2 C - k C .
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
| Damkohler number | $\mathrm{Da}=k R_0^2/D$ |
| Fourier number | $\mathrm{Fo}=Dt/R_0^2$ |

## Reference

With $\xi=(r-R_0)/R_0$ and $m=\sqrt{\mathrm{Da}}$,

$$
\frac{C}{C_s} = \frac{1}{2(1+\xi)}
\left[
e^{-m\xi}\operatorname{erfc}\!\left(\frac{\xi}{2\sqrt{\mathrm{Fo}}}-m\sqrt{\mathrm{Fo}}\right)
+
e^{+m\xi}\operatorname{erfc}\!\left(\frac{\xi}{2\sqrt{\mathrm{Fo}}}+m\sqrt{\mathrm{Fo}}\right)
\right],
$$

and

$$
\mathrm{Sh}(\mathrm{Fo},\mathrm{Da}) = 2\left[
1 + \sqrt{\mathrm{Da}}\,\operatorname{erf}\!\left(\sqrt{\mathrm{Da}\,\mathrm{Fo}}\right)
+ \frac{e^{-\mathrm{Da}\,\mathrm{Fo}}}{\sqrt{\pi \mathrm{Fo}}}
\right].
$$

This follows from the Laplace transform of $u=rC$: with
$\hat u = (R_0/s)\exp(-q(r-R_0))$ and $q=\sqrt{(s+k)/D}$, the surface
gradient gives $\hat{\mathrm{Sh}} = 2 + (2R_0/\sqrt{D})\sqrt{s+k}/s$, whose
inverse is the expression above. B-004 is the limit
$\mathrm{Fo}\to\infty$ and B-003 the limit $\mathrm{Da}\to 0$.

![B-006 reference](../figures/B-006-reference.svg)

## Report

- $\mathrm{Sh}(\mathrm{Fo})$ at each $\mathrm{Da}$,
- recovery of $2(1+\sqrt{\mathrm{Da}})$ at large $\mathrm{Fo}$,
- recovery of B-003 at $\mathrm{Da}=0$,
- observed convergence rate in space and in time.


## References

@Crank1975
@frankkamenetskii1969
