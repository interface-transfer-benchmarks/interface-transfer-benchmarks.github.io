---
id: B-039
title: Scriven spherical vapor bubble growth
short_title: Scriven bubble growth
status: ready

process:
  - boiling
  - evaporation
interface_motion: free
interface_condition:
  - equilibrium
  - volume-change
domains: 1
domain: sphere
dimension: 3D
equations:
  - heat-diffusion
  - advection

reference: closed-form
reference_note: exact spherical similarity solution
numerical_challenge: spherical Stefan flow and large density ratio

quantities_of_interest:
  - bubble_radius
  - temperature_profile
  - vapor_volume
  - radial_symmetry_error
  - energy_balance
has_reference_data: true
reference_data:
  - data/B-039/reference.csv

references:
  - Scriven1959
  - Tanguy2014
  - Rajkotwala2019
  - BasiliskScrivenProblem
  - BasiliskGennariScriven
---

# B-039 - Scriven spherical vapor bubble growth

## Problem

A vapor bubble is embedded in an initially quiescent, uniformly superheated
liquid. The interface is spherical:

$$
r=R(t).
$$

```text
vapor bubble, T = T_sat       superheated liquid, T -> T_bulk
r < R(t)                     r > R(t)
```

The gas is at saturation temperature. Heat conducted from the liquid supplies
latent heat at the interface and drives bubble growth.

The liquid temperature satisfies the radial advection-diffusion equation

$$
\partial_tT_l + u_r\partial_rT_l
=
\alpha_l
\frac{1}{r^2}
\partial_r
\left(
r^2\partial_rT_l
\right),
\qquad r>R(t).
$$

The liquid radial velocity comes from phase expansion and is included in the
Scriven similarity solution. At the interface,

$$
T_l(R(t),t)=T_\mathrm{sat}.
$$

The heat flux at the interface balances latent and sensible energy needed to
create vapor. The resulting similarity equation for the growth constant is
given below.

In the infinite-domain reference solution,

$$
T_l(r,t)\to T_\infty
\qquad \text{as } r\to\infty.
$$

For a finite-domain simulation, initialize at $t_0>0$ using

$$
R(t_0)=2\beta\sqrt{\alpha_l t_0}
$$

and set the liquid temperature from the analytical radial profile.

## Parameters

Scriven example.

| Parameter | Symbol |
|---|---|
| liquid density | $\rho_l$ |
| vapor density | $\rho_g$ |
| liquid conductivity | $\kappa_l$ |
| vapor conductivity | $\kappa_g$ |
| liquid heat capacity | $c_{p,l}$ |
| vapor heat capacity | $c_{p,g}$ |
| latent heat | $L$ |
| saturation temperature | $T_\mathrm{sat}$ |
| Jakob number | $\mathrm{Ja}$ |
| bulk liquid temperature | $T_\infty$ |

The liquid thermal diffusivity is

$$
\alpha_l = 1.48554269845860\times10^{-7}\ \mathrm{m^2/s}.
$$

## Reference

The configuration of the reference, with the values it is stated for:

Use the water/vapor setup with Jakob number $\mathrm{Ja}=3$ used in Basilisk's
Scriven example.

| Parameter | Symbol | Value | Unit |
|---|---:|---:|---|
| liquid density | $\rho_l$ | 958 | kg/m^3 |
| vapor density | $\rho_g$ | 0.59 | kg/m^3 |
| liquid conductivity | $\kappa_l$ | 0.6 | W/(m K) |
| vapor conductivity | $\kappa_g$ | 0.026 | W/(m K) |
| liquid heat capacity | $c_{p,l}$ | 4216 | J/(kg K) |
| vapor heat capacity | $c_{p,g}$ | 2034 | J/(kg K) |
| latent heat | $L$ | $2.257\times10^6$ | J/kg |
| saturation temperature | $T_\mathrm{sat}$ | 373 | K |
| Jakob number | $\mathrm{Ja}$ | 3 | - |
| bulk liquid temperature | $T_\infty$ | 373.989096611774 | K |

The liquid thermal diffusivity is

$$
\alpha_l = 1.48554269845860\times10^{-7}\ \mathrm{m^2/s}.
$$


The bubble radius is

$$
R(t)=2\beta\sqrt{\alpha_l t}.
$$

The growth constant $\beta$ solves

$$
\frac{
\rho_l c_{p,l}(T_\infty-T_\mathrm{sat})
}{
\rho_g
\left[
L+(c_{p,l}-c_{p,g})(T_\infty-T_\mathrm{sat})
\right]
}
=
2\beta^2
\int_0^1
\exp
\left[
-\beta^2
\left(
(1-x)^{-2}
-2\left(1-\frac{\rho_g}{\rho_l}\right)x
-1
\right)
\right]\,dx.
$$

For the recommended case,

$$
\beta = 3.32643989498138.
$$

The radial liquid temperature profile is

$$
T_l(r,t)
=
T_\infty
-
2\beta^2
\frac{
\rho_g
\left[
L+(c_{p,l}-c_{p,g})(T_\infty-T_\mathrm{sat})
\right]
}{
\rho_l c_{p,l}
}
\int_{1-R(t)/r}^{1}
\exp
\left[
-\beta^2
\left(
(1-x)^{-2}
-2\left(1-\frac{\rho_g}{\rho_l}\right)x
-1
\right)
\right]\,dx.
$$

Inside the bubble, use $T_g=T_\mathrm{sat}$.

The file `data/B-039/reference.csv` tabulates $R(t)$ and $T_l(r,t)$ for
selected times and radii.

![B-039 Scriven reference](../figures/B-039-reference.svg)

The CSV table intentionally uses a compact set of verification points. The SVG
figure uses 401 plotted points for a smooth curve.

## Note

Scriven's original analytical solution is spherically symmetric. The usual
"2D" numerical implementation is an axisymmetric $(r,z)$ computation, which
represents a three-dimensional sphere. A true two-dimensional cylindrical
analogue can be formulated, but it is not the standard Scriven spherical bubble
benchmark and uses a different radial geometry.

## Report

- bubble radius $R_h(t)$ from vapor volume,
- radial temperature profile at selected times,
- radial symmetry error,
- vapor volume conservation relative to $4\pi R^3/3$,
- interfacial heat flux and latent-heat balance,
- convergence of final-radius error.

## References

@Scriven1959
@Tanguy2014
@Rajkotwala2019
@BasiliskScrivenProblem
@BasiliskGennariScriven
