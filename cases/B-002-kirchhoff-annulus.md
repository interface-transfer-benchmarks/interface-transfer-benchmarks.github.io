---
id: B-002
title: Annulus with a temperature-dependent conductivity
short_title: Kirchhoff annulus
status: ready

process:
  - interfacial-transfer
interface_motion: fixed
interface_condition:
  - imposed-value
domains: 1
domain: annulus
dimension: 2D
equations:
  - heat-diffusion

reference: closed-form
reference_note: exact solution through a Kirchhoff transform
numerical_challenge: a nonlinear conductivity linearised by a transform the discretisation does not know about

quantities_of_interest:
  - interfacial_flux
  - temperature_profile
  - convergence_rate
has_reference_data: true
reference_data:
  - data/B-002/reference.csv

references:
  - carslaw1959
  - Crank1975
---

# B-002 - Annulus with a temperature-dependent conductivity

## Problem

Steady conduction in an annulus whose conductivity varies with the temperature,

$$
\nabla\cdot\left(\kappa(T)\nabla T\right) = 0,
\qquad
\kappa(T) = \kappa_0\left(1 + \beta T\right) ,
$$

with $T = 1$ on the inner circle and $T = 0$ on the outer one.

## Parameters

| Parameter | Symbol |
|---|---|
| inner radius | $R_\mathrm{in}$ |
| outer radius | $R_\mathrm{out}$ |
| reference conductivity | $\kappa_0$ |
| conductivity slope | $\beta$ |

## Reference

The Kirchhoff transform

$$
\theta = T + \frac{\beta T^2}{2}
$$

makes $\theta$ harmonic, so it is the logarithmic profile of the linear
problem,

$$
\theta(r) = \theta_\mathrm{in}
\left(1 - \frac{\ln(r/R_\mathrm{in})}{\ln(R_\mathrm{out}/R_\mathrm{in})}\right),
\qquad
T = \frac{\sqrt{1 + 2\beta\theta} - 1}{\beta} .
$$

The flux through the annulus therefore scales exactly,

$$
\frac{F(\beta)}{F(0)} = 1 + \frac{\beta}{2} ,
$$

which is a one-line reference the nonlinear solve has no way of knowing.

![B-002 reference](../figures/B-002-reference.svg)

## Report

- the flux against $F(0)(1 + \beta/2)$,
- the in/out balance across the annulus,
- the temperature profile,
- the iteration count against the conductivity contrast,
- observed convergence rate.


## References

@carslaw1959
@Crank1975
