---
id: PH-012
title: d2-law evaporating droplet
short_title: d2-law droplet
status: ready
benchmark_class: PH

physics:
  - phase-change
  - mass-diffusion
  - stefan-flow
  - soluble-species

process:
  - evaporation

dimension: 3D
geometry: sphere
interface_motion: moving

reference_type: quasi-steady-analytical
numerical_challenge: quasi-steady gas-phase transport and shrinking droplet
has_exact_solution: true
has_reference_data: true
reference_data:
  - data/PH-012/reference.csv
figures:
  - figures/PH-012-reference.svg

quantities_of_interest:
  - droplet_diameter
  - evaporation_rate
  - vapor_mass_fraction_profile
  - stefan_velocity

references:
  - Spalding1953
  - Law1982
---

# PH-012 - d2-law evaporating droplet

## Problem

A liquid droplet of initial diameter $d_0$ evaporates in a quiescent,
infinite gas. The vapor mass fraction at the surface is fixed at $Y_s$
(isothermal surface at phase equilibrium) and the far field is at $Y_\infty$.
Gas density $\rho_g$ and vapor diffusivity $D_g$ are constant; the gas is
quasi-steady with respect to the slow droplet regression
($\rho_g/\rho_l \ll 1$); gravity and liquid internal motion are neglected.

Quasi-steady gas phase, $r > R(t)$:

$$
\frac{d}{dr}\!\left(\rho_g u r^2\right) = 0,
\qquad
\rho_g u r^2 \frac{dY}{dr}
=
\frac{d}{dr}\!\left(\rho_g D_g r^2 \frac{dY}{dr}\right),
$$

with $Y(R)=Y_s$, $Y(\infty)=Y_\infty$. The interface mass balance is

$$
\dot m
=
4\pi R^2\,\rho_g\left(u - \dot R\right)\Big|_{R}
=
-\,\frac{4\pi R^2\,\rho_g D_g}{1-Y_s}\,
\frac{dY}{dr}\Big|_{R},
\qquad
\rho_l\,\frac{d}{dt}\!\left(\tfrac{4}{3}\pi R^3\right) = -\,\dot m .
$$

## Parameters

Water-like droplet in air at moderate surface saturation.

| Parameter | Symbol |
|---|---|
| initial diameter | $d_0$ |
| liquid density | $\rho_l$ |
| gas density | $\rho_g$ |
| vapor diffusivity | $D_g$ |
| surface mass fraction | $Y_s$ |
| far-field mass fraction | $Y_\infty$ |
| transfer number | $B_M$ |
| evaporation constant | $K$ |
| droplet lifetime | $t_{life}$ |

## Reference

The configuration of the reference, with the values it is stated for:

Water-like droplet in air at moderate surface saturation.

| Parameter | Symbol | Value | Unit |
|---|---:|---:|---|
| initial diameter | $d_0$ | $1\times10^{-3}$ | m |
| liquid density | $\rho_l$ | 1000 | kg/m^3 |
| gas density | $\rho_g$ | 1.0 | kg/m^3 |
| vapor diffusivity | $D_g$ | $2.5\times10^{-5}$ | m^2/s |
| surface mass fraction | $Y_s$ | 0.05 | - |
| far-field mass fraction | $Y_\infty$ | 0 | - |
| transfer number | $B_M$ | 0.052632 | - |
| evaporation constant | $K$ | $1.0258\times10^{-8}$ | m^2/s |
| droplet lifetime | $t_{life}$ | 97.48 | s |


The quasi-steady solution gives

$$
\dot m = 4\pi\,\rho_g D_g\,R\,\ln(1+B_M),
\qquad
B_M = \frac{Y_s - Y_\infty}{1 - Y_s},
$$

$$
1 - Y(r)
=
\left(1 - Y_\infty\right)
\exp\!\left[-\,\frac{\dot m}{4\pi\rho_g D_g\,r}\right]
=
\left(1 - Y_\infty\right)\left(1+B_M\right)^{-R/r},
$$

and the droplet surface area decreases linearly in time (the d2-law):

$$
d^2(t) = d_0^2 - K\,t,
\qquad
K = \frac{8\,\rho_g D_g}{\rho_l}\,\ln(1+B_M),
\qquad
t_{life} = \frac{d_0^2}{K}.
$$

The Stefan (blowing) velocity in the gas is
$u(r) = \dot m / (4\pi\rho_g r^2)$.

Generate the CSV and figure with:

```bash
python3 scripts/plot_reference_figures.py PH-012
```

## Report

- $d^2(t)$, the fitted evaporation constant $K$, and the relative error,
- instantaneous evaporation rate $\dot m(t)$,
- vapor mass-fraction profile against the exponential reference,
- interface-velocity consistency: $\dot R$ vs. $-\dot m /(4\pi\rho_l R^2)$.

## References

@Spalding1953
@Law1982
