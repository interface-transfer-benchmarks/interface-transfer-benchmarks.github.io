---
id: HT-004
title: Steady composite slab with an interfacial partition
short_title: Composite slab
status: ready
benchmark_class: HT

physics:
  - conjugate-transfer
  - mass-transfer

process:
  - interfacial-partition

dimension: 1D
geometry: planar
interface_motion: static
reference_type: exact-solution
numerical_challenge: a steady flux carried unchanged through a discontinuous interface

quantities_of_interest:
  - interfacial_flux
  - interface_jump
  - concentration_profile

has_exact_solution: true
has_reference_data: true
reference_data:
  - data/HT-004/reference.csv
figures:
  - figures/HT-004-reference.svg

references:
  - Crank1975
  - froment2011
---

# HT-004 - Steady composite slab with an interfacial partition

## Purpose

The steady counterpart of HT-001, and the case that states the
resistances-in-series law in its simplest form. Because the exact flux is a
single number, any error in the jump treatment shows up undiluted.

## Physical Configuration

Two slabs in series between $x=0$ and $x=L_1+L_2$. Phase 1 occupies
$0<x<L_1$ with diffusivity $D_1$, phase 2 occupies $L_1<x<L_1+L_2$ with
diffusivity $D_2$. The outer faces are held at fixed values.

## Governing Equations

$$
\partial_x\left(D_i \partial_x C_i\right) = 0, \qquad i = 1,2 .
$$

## Boundary And Initial Conditions

$$
C_1(0) = C_a, \qquad C_2(L_1+L_2) = C_b,
$$

and at $x=L_1$,

$$
C_1 = k\,C_2, \qquad D_1 \partial_x C_1 = D_2 \partial_x C_2 .
$$

## Material Parameters

| Parameter | Symbol | Value |
|---|---:|---:|
| slab thicknesses | $L_1$, $L_2$ | 1, 1 |
| diffusivities | $D_1$, $D_2$ | 1; 1, 0.1, 10 |
| partition coefficient | $k$ | 0.5, 1, 2, 5 |
| face values | $C_a$, $C_b$ | 1, 0 |

## Reference Solution

The flux is constant through both slabs,

$$
J = \frac{C_a - k\,C_b}{L_1/D_1 + k L_2/D_2},
$$

the profile is piecewise linear, and the interfacial values are

$$
C_1(L_1) = C_a - J\,\frac{L_1}{D_1},
\qquad
C_2(L_1) = \frac{1}{k}\left(C_a - J\,\frac{L_1}{D_1}\right).
$$

The denominator is the sum of the two resistances, with the partition
coefficient weighting the second: the same statement as MT-005's
$1/\mathrm{Sh}_\mathrm{ov} = 1/2 + 1/(2\mathrm{Da}_s)$ and MT-008's
$1/\eta_\mathrm{ov} = 1/\eta + \phi^2/(3\mathrm{Bi})$, written across a
composite wall.

![HT-004 reference](../figures/HT-004-reference.svg)

## Recommended Numerical Setup

Place the interface off a cell face. Sweep $k$ at $D_1=D_2$ and then the
diffusivity ratio at $k=1$, so that the two effects are separated.

## Quantities To Report

- $J$ against the closed form, at each $k$ and diffusivity ratio,
- the residual of $C_1 - kC_2$ at the interface,
- the flux measured on each side, which must agree,
- observed convergence rate.

## Known Difficulties

- a partition applied to the flux rather than to the value,
- harmonic averaging of the diffusivity across the interface, which silently
  replaces the partition with a continuous field,
- an interface aligned with a cell face, which hides first-order jump errors.

## References

@Crank1975
@froment2011
