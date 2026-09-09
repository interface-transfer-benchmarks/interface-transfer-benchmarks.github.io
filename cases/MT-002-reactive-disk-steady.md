---
id: MT-002
title: Steady reactive uptake outside a disk
short_title: Reactive disk
status: ready
benchmark_class: MT

physics:
  - mass-transfer
  - reaction-diffusion

process:
  - interfacial-mass-transfer
  - homogeneous-reaction

dimension: 2D
geometry: disk
interface_motion: static
reference_type: exact-solution
numerical_challenge: logarithmic far field that is only regularised by reaction

quantities_of_interest:
  - uptake_rate
  - concentration_profile
  - convergence_rate

has_exact_solution: true
has_reference_data: true
reference_data:
  - data/MT-002/reference.csv
figures:
  - figures/MT-002-reference.svg

references:
  - frankkamenetskii1969
  - Crank1975
---

# MT-002 - Steady reactive uptake outside a disk

## Purpose

The two-dimensional counterpart of MT-001, and the case that exposes the
two-dimensional far-field trap: without reaction the exterior problem has no
bounded solution, so a Sherwood number normalised on the non-reactive limit
does not exist in 2D.

## Physical Configuration

A disk of radius $R_0$ at concentration $C_s$ in a quiescent plane that
consumes the species at rate $\nu C$.

## Governing Equations

For $r > R_0$,

$$
D \nabla^2 C = \nu C .
$$

## Boundary And Initial Conditions

$$
C(R_0) = C_s, \qquad C(r \to \infty) = 0 .
$$

## Material Parameters

| Parameter | Symbol | Value |
|---|---:|---:|
| disk radius | $R_0$ | 1 |
| diffusivity | $D$ | 1 |
| surface concentration | $C_s$ | 1 |
| Damkohler number | $\mathrm{Da}=\nu R_0^2/D$ | 0.25 to 100 |

## Reference Solution

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

![MT-002 reference](../figures/MT-002-reference.svg)

## Recommended Numerical Setup

Report the uptake $F$ directly rather than a normalised enhancement. Steady
exterior diffusion around a circle admits only $a + b\ln r$, so the flux decays
like $1/\ln(L/R_0)$ and never converges as the box opens; this is the diffusive
analogue of Stokes' paradox. Reaction restores well-posedness through the $K_0$
decay, so the case is legitimate for $\mathrm{Da} \gtrsim 1$ and illegitimate
as $\mathrm{Da} \to 0$.

## Quantities To Report

- $F$ at each $\mathrm{Da}$ and its relative error,
- radial profile against $K_0(mr)/K_0(mR_0)$,
- observed convergence rate,
- the drift of $F$ with box size at fixed $h$, at low and high $\mathrm{Da}$.

## Known Difficulties

- quoting an enhancement factor $E = \mathrm{Sh}(\mathrm{Da})/\mathrm{Sh}(0)$,
  which diverges as the box opens,
- taking the 2D case as a cheap stand-in for 3D.

## References

@frankkamenetskii1969
@Crank1975
