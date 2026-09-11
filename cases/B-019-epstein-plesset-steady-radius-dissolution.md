---
id: B-019
title: Epstein-Plesset steady-radius dissolution
short_title: Epstein-Plesset concentration
status: ready

process:
  - dissolution
interface_motion: fixed
interface_condition:
  - equilibrium
domains: 1
domain: sphere
dimension: 3D
equations:
  - species-diffusion

reference: closed-form
reference_note: exact similarity solution
numerical_challenge: early-time spherical diffusion flux

quantities_of_interest:
  - concentration_profile
  - diffusive_mass_flux
  - bubble_mass_loss_rate
has_reference_data: true
reference_data:
  - data/B-019/reference.csv

references:
  - EpsteinPlesset1950
  - Crank1975
  - Gennari2022
  - BasiliskGennariEpsteinPlesset
---

# B-019 - Epstein-Plesset steady-radius dissolution

## Problem

A spherical bubble of radius $R_0$ is held fixed in a liquid with zero initial and
far-field dissolved gas concentration. The interfacial concentration is fixed by
Henry's law.

For $r>R_0$,

$$
\partial_t C
=
\frac{1}{r^2}
\partial_r
\left(
r^2D\partial_r C
\right).
$$

The conditions are

$$
C(r,0)=C_\infty,
\qquad
C(R_0,t)=C_s,
\qquad
C(r,t)\to C_\infty\quad r\to\infty.
$$

## Parameters

| Parameter | Symbol |
|---|---|
| bubble radius | $R_0$ |
| Schmidt number | $\mathrm{Sc}$ |
| diffusivity | $D$ |
| Henry coefficient | $H$ |
| interfacial concentration | $C_s$ |
| bulk concentration | $C_\infty$ |
| final time | $t_\mathrm{end}$ |

## Reference

The concentration field is

$$
C(r,t)
=
C_\infty
+
(C_s-C_\infty)
\frac{R}{r}
\operatorname{erfc}
\left(
\frac{r-R_0}{2\sqrt{Dt}}
\right).
$$

The Epstein-Plesset mass-flux relation for the corresponding moving-radius
problem is

$$
\frac{dR}{dt}
=
\frac{DM(C_\infty-C_s)}{\rho_d}
\left[
\frac{1}{R}
+
\frac{1}{\sqrt{\pi Dt}}
\right].
$$

The file `data/B-019/reference.csv` tabulates the fixed-radius concentration
profile.

![B-019 Epstein-Plesset reference](../figures/B-019-reference.svg)

## Report

- radial concentration profile,
- concentration at sample radii,
- diffusive mass flux at the interface,
- integrated gas released into the liquid.

## References

@EpsteinPlesset1950
@Crank1975
@Gennari2022
@BasiliskGennariEpsteinPlesset
