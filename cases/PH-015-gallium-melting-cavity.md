---
id: PH-015
title: Gallium melting in a side-heated cavity
short_title: Gallium melting
status: draft
benchmark_class: PH

physics:
  - phase-change
  - heat-diffusion
  - natural-convection
  - gravity
  - hydrodynamic-coupling

process:
  - melting

dimension: 2D
geometry: rectangular-cavity
interface_motion: moving

reference_type: experimental
numerical_challenge: natural convection coupled to a melting front
has_exact_solution: false
has_reference_data: false

quantities_of_interest:
  - melt_front_position
  - liquid_fraction
  - flow_structure
  - wall_heat_flux

references:
  - GauViskanta1986
  - Brent1988
  - Hannoun2003
---

# PH-015 - Gallium melting in a side-heated cavity

## Problem

Solid gallium initially fills a rectangular cavity at (or marginally below)
its melting temperature. At $t = 0$ the left vertical wall is raised to
$T_h$ above the melting point while the right wall is held at $T_c$ slightly
below it; horizontal walls are adiabatic. A melt layer forms at the hot wall
and natural convection progressively tilts the front, melting the top faster
than the bottom.

Gau & Viskanta's cavity is 8.89 cm long and 6.35 cm high (depth 3.81 cm);
the standard two-dimensional model uses the vertical mid-plane.
Following the configuration fixed by Brent, Voller & Reid:

| Quantity | Symbol | Value | Unit |
|---|---:|---:|---|
| cavity length | $W$ | 0.0889 | m |
| cavity height | $H$ | 0.0635 | m |
| hot wall | $T_h$ | 311.0 | K |
| cold wall | $T_c$ | 301.3 | K |
| melting temperature | $T_m$ | 302.78 | K |
| initial temperature | $T_i$ | 301.3 | K |

Incompressible Navier-Stokes with Boussinesq buoyancy in the melt, no slip on
all walls and on the front; energy equation in both phases; melting front at
$T = T_m$ with the Stefan condition

$$
\rho L\,V_\Gamma
=
\big[\![\,\kappa\,\nabla T\cdot\mathbf n\,]\!\big].
$$

Density change on melting and solid motion are neglected.

## Parameters

Gallium properties as used in the enthalpy-porosity literature:

| Parameter | Symbol |
|---|---|
| density | $\rho$ |
| viscosity | $\mu$ |
| conductivity | $\kappa$ |
| heat capacity | $c_p$ |
| latent heat | $L$ |
| thermal expansion | $\beta$ |
| gravity | $g$ |

The commonly quoted dimensionless groups for this configuration are
$\mathrm{Pr} \approx 0.0216$, $\mathrm{Ste} = c_p (T_h - T_m)/L \approx 0.039$, and
$\mathrm{Ra} = g\beta(T_h - T_m)H^3 \rho^2 c_p/(\mu \kappa) \approx 6\times10^{5}$
(Boussinesq in the melt only).

## Reference

The configuration of the reference, with the values it is stated for:

Gallium properties as used in the enthalpy-porosity literature:

| Parameter | Symbol | Value | Unit |
|---|---:|---:|---|
| density | $\rho$ | 6093 | kg/m^3 |
| viscosity | $\mu$ | $1.81\times10^{-3}$ | Pa s |
| conductivity | $\kappa$ | 32 | W/(m K) |
| heat capacity | $c_p$ | 381.5 | J/(kg K) |
| latent heat | $L$ | $80\,160$ | J/kg |
| thermal expansion | $\beta$ | $1.2\times10^{-4}$ | 1/K |
| gravity | $g$ | 9.81 | m/s^2 |

The commonly quoted dimensionless groups for this configuration are
$\mathrm{Pr} \approx 0.0216$, $\mathrm{Ste} = c_p (T_h - T_m)/L \approx 0.039$, and
$\mathrm{Ra} = g\beta(T_h - T_m)H^3 \rho^2 c_p/(\mu \kappa) \approx 6\times10^{5}$
(Boussinesq in the melt only).


The primary reference is the sequence of melt-front shapes measured by
Gau & Viskanta with the pour-out method at approximately
$t = 2,\,6,\,10,\,12.5,\,17$ and $19\ \mathrm{min}$, published as front
traces (their Fig. 7) and reproduced throughout the modelling literature
starting with Brent, Voller & Reid.

Digitized front coordinates are **not yet included** in `data/PH-015/`:
the original data exist only as figures, and a curated digitization (with an
explicit statement of which cross-section is used, see below) is a pending
contribution. Until then, contributors should compare against the published
figures and against the grid-converged fixed-grid simulations of
Hannoun, Alexiades & Mai, which serve as the de facto numerical reference for
the same configuration.

## Report

- melt front position at the experimental times,
- liquid volume fraction history,
- number and evolution of convective rolls in the melt,
- hot-wall Nusselt number history.

## References

@GauViskanta1986
@Brent1988
@Hannoun2003
