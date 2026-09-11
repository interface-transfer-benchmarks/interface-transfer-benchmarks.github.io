---
id: B-041
title: Film boiling on a horizontal wall
short_title: Film boiling
status: ready

process:
  - boiling
  - evaporation
interface_motion: free
interface_condition:
  - equilibrium
  - volume-change
  - capillary
domains: 2
domain: wall
dimension: 2D
equations:
  - heat-diffusion
  - navier-stokes

reference: data
reference_note: published simulations and the Berenson correlation
numerical_challenge: vapor-film instability and bubble release

quantities_of_interest:
  - space_averaged_nusselt
  - bubble_release_period
  - interface_shape
  - vapor_volume
has_reference_data: true
reference_data:
  - data/B-041/reference.csv

references:
  - WelchWilson2000
  - JuricTryggvason1998
  - EsmaeeliTryggvason2004
  - Berenson1961
  - Rajkotwala2019
  - BoydLing2023
---

# B-041 - Film boiling on a horizontal wall

## Problem

A two-dimensional periodic strip of width $\lambda_d$ (the most dangerous
Taylor wavelength) contains a vapor layer on a horizontal superheated wall
below saturated liquid. The initial interface is a small single-mode
perturbation of the flat film:

$$
y_\Gamma(x)
=
\frac{\lambda_d}{128}
\left[
4 + \cos\!\left(\frac{2\pi x}{\lambda_d}\right)
\right],
\qquad
\lambda_d = 2\pi\sqrt{\frac{3\,\sigma}{g\,(\rho_l-\rho_g)}} .
$$

The wall is isothermal at $T_\mathrm{sat}+\Delta T$; the liquid and interface are at
$T_\mathrm{sat}$. Side boundaries are periodic; the top is an outflow far from the
film (domain height $\geq 3\lambda_d$).

Incompressible Navier-Stokes in both phases with surface tension and gravity;
energy equation with the interface held at $T_\mathrm{sat}$; interfacial mass flux
from the conductive jump

$$
\dot m''
=
\frac{\big[\![\,\kappa\,\nabla T\cdot\mathbf n\,]\!\big]}{L},
$$

which drives the velocity jump $[\![\mathbf u\cdot\mathbf n]\!] =
\dot m''\,[\![1/\rho]\!]$ across the front.

## Parameters

The artificial-fluid property set widely used in the film-boiling
verification literature (moderate density ratio, thick thermal layers) is
adopted so results are directly comparable to published simulations. This
set is sometimes referred to as the "phantom fluid" and is conventionally
run at a saturation temperature of 500 K with a wall at 505 K.

| Parameter | Symbol |
|---|---|
| liquid density | $\rho_l$ |
| vapor density | $\rho_g$ |
| liquid viscosity | $\mu_l$ |
| vapor viscosity | $\mu_g$ |
| liquid conductivity | $\kappa_l$ |
| vapor conductivity | $\kappa_g$ |
| liquid heat capacity | $c_{p,l}$ |
| vapor heat capacity | $c_{p,g}$ |
| latent heat | $L$ |
| surface tension | $\sigma$ |
| gravity | $g$ |
| saturation temperature | $T_\mathrm{sat}$ |
| wall superheat | $\Delta T$ |

Derived scales: capillary length $\lambda_0 = \sqrt{\sigma/(g(\rho_l-\rho_g))}$,
most dangerous wavelength $\lambda_d = 2\pi\sqrt3\,\lambda_0$, vapor Jakob
number $\mathrm{Ja} = c_{p,g}\Delta T/L = 0.1$, vapor Prandtl number
$\mathrm{Pr}_g = c_{p,g}\mu_g/\kappa_g = 1$.

## Reference

The wall Nusselt number, space-averaged over the strip and based on
$\lambda_0$,

$$
\mathrm{Nu}(t)
=
\frac{\lambda_0}{\lambda_d\,\Delta T}
\int_0^{\lambda_d}
\left.\frac{\partial T}{\partial y}\right|_\mathrm{wall} dx ,
$$

oscillates with the bubble release cycle around a quasi-periodic mean.
The Berenson correlation predicts

$$
\overline{\mathrm{Nu}}_\mathrm{Ber}
=
0.425
\left[
\frac{\rho_g\,(\rho_l-\rho_g)\,g\,L'\,\lambda_0^{3}}
     {\kappa_g\,\mu_g\,\Delta T}
\right]^{1/4},
\qquad
L' = L + 0.5\,c_{p,g}\,\Delta T ,
$$

and published grid-converged simulations of this configuration report
time-averaged Nusselt numbers within roughly 10-20% of it. The file
`data/B-041/reference.csv` records the derived scales and the Berenson
values for the parameter set above. Results should additionally be compared
qualitatively (bubble pinch-off morphology, release period) to the cited
simulation studies.

![B-041 film boiling reference](../figures/B-041-reference.svg)

## Report

- $\mathrm{Nu}(t)$ history and its quasi-periodic time average,
- comparison of the mean against Berenson and against published simulations,
- bubble release period and interface snapshots over one cycle,
- vapor volume history and global mass/energy balances.

## References

@WelchWilson2000
@JuricTryggvason1998
@EsmaeeliTryggvason2004
@Berenson1961
@Rajkotwala2019
@BoydLing2023
