---
id: PH-XXX
title: Benchmark title
short_title: Short title
status: draft

benchmark_class: PH

physics:
  - phase-change
  - heat-diffusion

process:
  - melting

dimension: 1D
geometry: planar

interface_motion: moving
interface_representation:
  - front-tracking
  - level-set
  - VOF
  - phase-field
  - enthalpy
  - cut-cell

quantities_of_interest:
  - interface_position
  - temperature_profile
  - phase_volume
  - energy_error

has_exact_solution: true
has_reference_data: false

maintainers:
  - name: Your Name
    affiliation: Your Lab

references:
  - key: AuthorYear
---

# PH-XXX - Benchmark title

## Problem

What the configuration is, the governing equations, and the boundary and
initial conditions.

$$
\partial_t u = \nabla\cdot(k \nabla u).
$$

## Parameters

| Parameter | Symbol | Value |
|---|---:|---:|
| a length | $L$ | 1 |
| a diffusivity | $D$ | 1 |

## Reference

The closed form, series, or reference dataset, with the conventions stated.

![PH-XXX reference](../figures/PH-XXX-reference.svg)

## Report

- the primary observable and its error,
- observed convergence rate.

## Results

Optional. One `###` subsection per solver, titled with the method and its
authors, then the date and the run configuration, then the numbers and the
figures. Include runs that did not meet their gate, and say so.

## References

@Key1234
