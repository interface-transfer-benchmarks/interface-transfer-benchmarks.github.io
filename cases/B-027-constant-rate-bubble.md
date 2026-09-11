---
id: B-027
title: Constant-rate dissolving bubble
short_title: Constant-rate bubble
status: ready

process:
  - dissolution
  - verification
interface_motion: prescribed
interface_condition:
  - imposed-flux
domains: 2
domain: sphere
dimension: 3D
equations:
  - navier-stokes

reference: closed-form
reference_note: exact kinematic law
numerical_challenge: prescribed mass-transfer shrinkage

quantities_of_interest:
  - bubble_radius
  - phase_area
  - phase_volume
  - radial_symmetry_error
has_reference_data: true
reference_data:
  - data/B-027/reference.csv

references:
  - Gennari2022
  - BasiliskGennariConstant2D
  - BasiliskGennariConstantAxi
---

# B-027 - Constant-rate dissolving bubble

## Problem

A circular or spherical bubble dissolves at a constant interfacial mass flux.
The Basilisk sandbox provides both a planar 2D circle and an axisymmetric
sphere variant.

For a constant mass-transfer rate $\dot m$ and dispersed-phase density
$\rho_d$, the radius evolves as

$$
R(t)=R_0+\frac{\dot m}{\rho_d}t.
$$

The reference case uses a dissolving bubble, so $\dot m<0$.

## Parameters

| Parameter | Symbol |
|---|---|
| initial radius | $R_0$ |
| continuous-phase density | $\rho_c$ |
| density ratio | $\rho_c/\rho_d$ |
| dispersed density | $\rho_d$ |
| mass-transfer rate | $\dot m$ |
| final time | $t_\mathrm{end}$ |

## Reference

For these values,

$$
R(t)=1-t.
$$

The two-dimensional area and axisymmetric volume references are

$$
A(t)=\pi R(t)^2,
\qquad
V(t)=\frac{4\pi}{3}R(t)^3.
$$

The file `data/B-027/reference.csv` tabulates radius, area, and volume.

![B-027 constant-rate bubble reference](../figures/B-027-reference.svg)

## Report

- equivalent radius $R_h(t)$,
- phase area for 2D or phase volume for axisymmetric/3D runs,
- radial symmetry error,
- final radius error.

## References

@Gennari2022
@BasiliskGennariConstant2D
@BasiliskGennariConstantAxi
