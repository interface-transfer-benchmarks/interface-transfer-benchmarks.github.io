---
id: B-035
title: Nusselt laminar film condensation
short_title: Nusselt condensation
status: ready

process:
  - condensation
interface_motion: free
interface_condition:
  - equilibrium
domains: 1
domain: plate
dimension: 2D
equations:
  - heat-diffusion
  - navier-stokes

reference: asymptotic
reference_note: laminar boundary-layer solution
numerical_challenge: thin condensate film and interfacial shear

quantities_of_interest:
  - film_thickness
  - local_nusselt_number
  - mean_nusselt_number
  - condensate_mass_flow
  - velocity_profile
has_reference_data: true
reference_data:
  - data/B-035/reference.csv

references:
  - Nusselt1916
---

# B-035 - Nusselt laminar film condensation

## Problem

Saturated quiescent vapor at $T_\mathrm{sat}$ condenses on a vertical isothermal
plate of height $L_p$ held at $T_w < T_\mathrm{sat}$. A laminar condensate film
flows down the plate under gravity; the film is thin, inertia and convection
in the film are negligible, the temperature profile across the film is
linear, and the vapor exerts no shear on the interface.

In the film, $0 < y < \delta(x)$ with $x$ measured downward from the leading
edge:

$$
\mu_l\,\partial_{yy} u + g\,(\rho_l - \rho_g) = 0,
\qquad
\partial_{yy} T = 0,
$$

with no slip at the wall, zero interfacial shear
$\partial_y u|_{\delta} = 0$, $T(0)=T_w$, $T(\delta)=T_\mathrm{sat}$. The interface
energy balance converts the conducted heat into condensate:

$$
L\,\frac{d\Gamma}{dx}
=
\frac{\kappa_l\,(T_\mathrm{sat}-T_w)}{\delta(x)},
\qquad
\Gamma(x) = \int_0^{\delta} \rho_l\,u\,dy
= \frac{g\,\rho_l(\rho_l-\rho_g)\,\delta^3}{3\mu_l}.
$$

## Parameters

Saturated steam at atmospheric pressure on a subcooled plate.

| Parameter | Symbol |
|---|---|
| plate height | $L_p$ |
| saturation temperature | $T_\mathrm{sat}$ |
| wall temperature | $T_w$ |
| liquid density | $\rho_l$ |
| vapor density | $\rho_g$ |
| liquid viscosity | $\mu_l$ |
| liquid conductivity | $\kappa_l$ |
| liquid heat capacity | $c_{p,l}$ |
| latent heat | $L$ |
| gravity | $g$ |

## Reference

The configuration of the reference, with the values it is stated for:

Saturated steam at atmospheric pressure on a subcooled plate.

| Parameter | Symbol | Value | Unit |
|---|---:|---:|---|
| plate height | $L_p$ | 0.1 | m |
| saturation temperature | $T_\mathrm{sat}$ | 373.15 | K |
| wall temperature | $T_w$ | 363.15 | K |
| liquid density | $\rho_l$ | 958.4 | kg/m^3 |
| vapor density | $\rho_g$ | 0.60 | kg/m^3 |
| liquid viscosity | $\mu_l$ | $2.82\times10^{-4}$ | Pa s |
| liquid conductivity | $\kappa_l$ | 0.68 | W/(m K) |
| liquid heat capacity | $c_{p,l}$ | 4216 | J/(kg K) |
| latent heat | $L$ | $2.257\times10^{6}$ | J/kg |
| gravity | $g$ | 9.81 | m/s^2 |


The Nusselt solution is

$$
\delta(x)
=
\left[
\frac{4\,\kappa_l\,\mu_l\,(T_\mathrm{sat}-T_w)\,x}
     {g\,\rho_l\,(\rho_l-\rho_g)\,L}
\right]^{1/4},
$$

$$
h(x) = \frac{\kappa_l}{\delta(x)},
\qquad
\overline{h} = \frac{4}{3}\,h(L_p),
\qquad
\overline{Nu}_{L}
=
0.943
\left[
\frac{\rho_l\,g\,(\rho_l-\rho_g)\,L\,L_p^3}
     {\mu_l\,\kappa_l\,(T_\mathrm{sat}-T_w)}
\right]^{1/4},
$$

with film velocity profile
$u(x,y) = \dfrac{g(\rho_l-\rho_g)}{\mu_l}\left(\delta y - y^2/2\right)$ and
film Reynolds number $Re_\delta = 4\Gamma/\mu_l$ (laminar, wave-free below
$Re_\delta \approx 30$). Sensible-heat corrections
($L' = L + 0.68\,c_{p,l}\Delta T$, Rohsenow) shift the result by
under 2% here and are not applied to the reference.

## Report

- steady film thickness $\delta(x)$ against the $x^{1/4}$ law,
- local and mean Nusselt numbers,
- condensate mass flow at the outlet vs. integrated interfacial flux,
- velocity profile across the film at $x = L_p/2$.

## References

@Nusselt1916
