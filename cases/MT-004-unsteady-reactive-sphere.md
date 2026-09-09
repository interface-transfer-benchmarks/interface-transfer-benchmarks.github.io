---
id: MT-004
title: Unsteady diffusion with a first-order reaction outside a sphere
short_title: Unsteady reactive sphere
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
numerical_challenge: a transient and a reaction layer resolved at once

quantities_of_interest:
  - sherwood_number
  - concentration_profile
  - convergence_rate

has_exact_solution: true
has_reference_data: true
reference_data:
  - data/MT-004/reference.csv
figures:
  - figures/MT-004-reference.svg

references:
  - Crank1975
  - frankkamenetskii1969
---

# MT-004 - Unsteady diffusion with a first-order reaction outside a sphere

## Purpose

Couples MT-001's reaction layer to MT-003's transient. Both limits are
recovered from one closed form, so a scheme cannot pass by being right in time
and wrong in space, or the reverse.

## Physical Configuration

MT-003's sphere in a medium that also consumes the species at rate $\nu C$.

## Governing Equations

For $r > R_0$,

$$
\partial_t C = D \nabla^2 C - \nu C .
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
| Damkohler number | $\mathrm{Da}=\nu R_0^2/D$ | 0, 1, 10 |
| Fourier number | $\mathrm{Fo}=Dt/R_0^2$ | 0.001 to 10 |

## Reference Solution

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
$\hat u = (R_0/s)\exp(-q(r-R_0))$ and $q=\sqrt{(s+\nu)/D}$, the surface
gradient gives $\hat{\mathrm{Sh}} = 2 + (2R_0/\sqrt{D})\sqrt{s+\nu}/s$, whose
inverse is the expression above. MT-001 is the limit
$\mathrm{Fo}\to\infty$ and MT-003 the limit $\mathrm{Da}\to 0$.

![MT-004 reference](../figures/MT-004-reference.svg)

## Recommended Numerical Setup

As MT-003, with the mesh additionally satisfying MT-001's reaction-layer
constraint at the chosen $\mathrm{Da}$.

## Quantities To Report

- $\mathrm{Sh}(\mathrm{Fo})$ at each $\mathrm{Da}$,
- recovery of $2(1+\sqrt{\mathrm{Da}})$ at large $\mathrm{Fo}$,
- recovery of MT-003 at $\mathrm{Da}=0$,
- observed convergence rate in space and in time.

## Known Difficulties

- a time step that resolves the transient but a mesh that does not resolve the
  reaction layer, or the reverse,
- comparing against surface-reaction references, which are a different problem:
  this case has a bulk reaction and no Stefan flow.

## References

@Crank1975
@frankkamenetskii1969
