---
id: VC-002
title: Constant-rate dissolving bubble
short_title: Constant-rate bubble
status: ready
benchmark_class: VC

physics:
  - phase-change
  - prescribed-mass-transfer
  - hydrodynamics

process:
  - dissolution

dimension: 2D/axisymmetric
geometry: circle-sphere
interface_motion: moving

reference_type: exact-kinematic
numerical_challenge: prescribed mass-transfer shrinkage
has_exact_solution: true
has_reference_data: true
reference_data:
  - data/VC-002/reference.csv
figures:
  - figures/VC-002-reference.svg

quantities_of_interest:
  - bubble_radius
  - phase_area
  - phase_volume
  - radial_symmetry_error

references:
  - Gennari2022
  - BasiliskGennariConstant2D
  - BasiliskGennariConstantAxi
---

# VC-002 - Constant-rate dissolving bubble

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

Use the Gennari Basilisk setup.

| Parameter | Symbol | Value |
|---|---:|---:|
| initial radius | $R_0$ | 1 |
| continuous-phase density | $\rho_c$ | 1 |
| density ratio | $\rho_c/\rho_d$ | 1000 |
| dispersed density | $\rho_d$ | 0.001 |
| mass-transfer rate | $\dot m$ | $-10^{-3}$ |
| final time | $t_{end}$ | 1 |

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

The file `data/VC-002/reference.csv` tabulates radius, area, and volume.

![VC-002 constant-rate bubble reference](../figures/VC-002-reference.svg)

Generate the CSV and figure with:

```bash
python3 scripts/plot_reference_figures.py VC-002
```

## Report

- equivalent radius $R_h(t)$,
- phase area for 2D or phase volume for axisymmetric/3D runs,
- radial symmetry error,
- final radius error.

## References

@Gennari2022
@BasiliskGennariConstant2D
@BasiliskGennariConstantAxi
