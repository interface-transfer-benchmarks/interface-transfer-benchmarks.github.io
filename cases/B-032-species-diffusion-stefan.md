---
id: B-032
title: Species-diffusion Stefan problem
short_title: Species Stefan problem
status: ready

process:
  - dissolution
interface_motion: free
interface_condition:
  - equilibrium
domains: 1
domain: half-space
dimension: 1D
equations:
  - species-diffusion

reference: closed-form
reference_note: exact similarity solution
numerical_challenge: species-driven interface displacement

quantities_of_interest:
  - interface_displacement
  - concentration_profile
  - gas_volume
has_reference_data: true
reference_data:
  - data/B-032/reference.csv

references:
  - Gennari2022
  - BasiliskGennariSpeciesStefan
---

# B-032 - Species-diffusion Stefan problem

## Problem

A planar gas-liquid interface releases gas into an initially gas-free liquid.
The concentration at the interface is fixed by Henry's law.

The liquid concentration satisfies

$$
\partial_t C = D\partial_{yy}c.
$$

The interface displacement is

$$
\ell(t)=\frac{2}{H}\sqrt{\frac{Dt}{\pi}}.
$$

The concentration field is

$$
C(y,t)
=
C_s
\left[
1-\operatorname{erf}
\left(
\frac{y-y_\Gamma(t)}{2\sqrt{Dt}}
\right)
\right].
$$

## Parameters

| Parameter | Symbol |
|---|---|
| Schmidt number | $\mathrm{Sc}$ |
| diffusivity | $D$ |
| Henry coefficient | $H$ |
| interface concentration scale | $C_s$ |
| final time | $t_\mathrm{end}$ |

## Reference

For the recommended case,

$$
\ell(t)=\frac{2}{1.2}\sqrt{\frac{0.1t}{\pi}}.
$$

The file `data/B-032/reference.csv` tabulates the displacement and
concentration profile.

![B-032 species Stefan reference](../figures/B-032-reference.svg)

## Report

- interface displacement $\ell_h(t)$,
- gas volume change,
- concentration profile,
- final displacement error.

## References

@Gennari2022
@BasiliskGennariSpeciesStefan
