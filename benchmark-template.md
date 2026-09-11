---
id: B-XXX
title: Benchmark title
short_title: Short title
status: draft

process:
  - melting
interface_motion: free
interface_condition:
  - dirichlet
  - stefan
domains: 1
domain: half-space
dimension: 1D
equations:
  - heat-diffusion

reference: closed-form
reference_note: what the reference is and how it is evaluated
numerical_challenge: the one difficulty this case targets

quantities_of_interest:
  - interface_position
  - temperature_profile
  - energy_error
has_reference_data: false

maintainers:
  - name: Your Name
    affiliation: Your Lab

references:
  - AuthorYear
---

# B-XXX - Benchmark title

## Problem

What the configuration is, the governing equations, and the boundary and
initial conditions.

$$
\partial_t u = \nabla\cdot(k \nabla u).
$$

Use the symbols of the [notation table](taxonomy.md#notation), and the facet
vocabularies of [`taxonomy.md`](taxonomy.md) in the front matter.

## Parameters

| Parameter | Symbol | Value |
|---|---:|---:|
| a length | $L$ | 1 |
| a diffusivity | $D$ | 1 |

## Reference

The closed form, series, or reference dataset, with the conventions stated.

![B-XXX reference](../figures/B-XXX-reference.svg)

## Report

- the primary observable and its error,
- observed convergence rate.

## Results

Optional. One `###` subsection per solver, titled with the method and its
authors, then the date and the run configuration, then the numbers and the
figures. Include runs that did not meet their gate, and say so.

## References

@Key1234
