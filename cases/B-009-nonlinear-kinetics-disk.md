---
id: B-009
title: Nonlinear kinetics outside a disk
short_title: Nonlinear kinetics
status: ready

process:
  - reaction
interface_motion: fixed
interface_condition:
  - imposed-value
domains: 1
domain: disk
dimension: 2D
equations:
  - species-diffusion
  - volume-reaction

reference: quadrature
reference_note: reduced ODE integrated to tolerance
numerical_challenge: a rate that is not proportional to the concentration, and a free boundary when the order is below one

quantities_of_interest:
  - uptake
  - convergence_rate
has_reference_data: false

references:
  - frankkamenetskii1969
  - aris1975
  - froment2011
---

# B-009 - Nonlinear kinetics outside a disk

## Problem

The steady field outside a disk of radius $R_0$ held at $C_s$ is consumed by a
rate that is not linear in the concentration.

$$
D \nabla^2 C = k\,f(C), \qquad r > R_0,
$$

with $C(R_0) = C_s$ and the far field imposed on the box. Two families:

$$
f(C) = C^n
\qquad\text{and}\qquad
f(C) = \frac{C}{1 + K C} ,
$$

the second a Langmuir-Hinshelwood rate, whose volumetric maximum $k/4K$ is
attained inside the domain whenever $1/K$ is.

## Parameters

| Parameter | Symbol |
|---|---|
| disk radius | $R_0$ |
| diffusivity | $D$ |
| surface concentration | $C_s$ |
| Damkohler number | $\mathrm{Da} = k R_0^2/D$ |
| reaction order | $n$ |
| adsorption constant | $K$ |

## Reference

There is no closed form. The reference is the radial two-point boundary-value
problem

$$
\frac{1}{r}\frac{d}{dr}\left(r\frac{dC}{dr}\right) = \frac{k}{D} f(C),
\qquad
C(R_0) = C_s ,
$$

integrated on a fine uniform grid with the same far-field datum as the run. At
$n = 1$ it must reproduce $F = 2\pi R_0\sqrt{\mathrm{Da}}\,K_1/K_0$, which is what
makes the nonlinear rows mean anything.

Below $n = 1$ the concentration reaches exactly zero at a finite radius and the
problem has a free boundary; a solver that floors the iterate rather than
tracking the front stalls at its cap. That is a property of the problem, not of
the discretisation, and it should be reported rather than gated.

## Report

- the uptake $F$ against the radial solve, over $\mathrm{Da}$ and over $n$,
- the Langmuir-Hinshelwood rate maximum $k/4K$, where it is attained inside
  the box,
- agreement between the interface flux and the volume integral of the rate,
  which detects a front the iterate has walked past,
- observed convergence rate.


## References

@frankkamenetskii1969
@aris1975
@froment2011
