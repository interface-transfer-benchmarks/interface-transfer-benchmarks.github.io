---
id: B-013
title: Non-isothermal pellet, Weisz-Hicks
short_title: Weisz-Hicks pellet
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
  - heat-diffusion
  - volume-reaction

reference: quadrature
reference_note: reduced ODE integrated to tolerance
numerical_challenge: an effectiveness factor above one, and a branch that ends at a turning point

quantities_of_interest:
  - effectiveness_factor
  - centre_value
  - convergence_rate
has_reference_data: true
reference_data:
  - data/B-013/reference.csv

references:
  - weisz1962
  - villadsen1978
  - aris1975
---

# B-013 - Non-isothermal pellet, Weisz-Hicks

## Problem

The pellet of B-010 releases heat as it reacts. Eliminating the temperature
through the Prater relation leaves one equation for the scaled concentration
$y = C/C_s$ with an Arrhenius rate,

$$
y'' + \frac{s}{x}y' =
\phi^2 y \exp\!\left(\frac{\gamma\beta(1-y)}{1 + \beta(1-y)}\right),
\qquad
y(1) = 1,
\qquad
y'(0) = 0 ,
$$

with $s = 1$ for a disk and $2$ for a sphere.

## Parameters

| Parameter | Symbol |
|---|---|
| Thiele modulus | $\phi$ |
| Prater number | $\beta = (-\Delta H) D C_s/(\lambda T_s)$ |
| Arrhenius group | $\gamma = E/(R_g T_s)$ |
| geometry factor | $s$ |

## Reference

The same radial two-point problem as B-010 with the Arrhenius rate, solved by
shooting on the centre value. An exothermic pellet, $\beta > 0$, releases heat
faster than it can conduct it away, so the interior runs hotter than the
surface and

$$
\eta = \frac{(s+1)\,y'(1)}{\phi^2} > 1 .
$$

For large $\gamma\beta$ the curve $\eta(\phi)$ is S-shaped and carries up to
three steady states with ignition and extinction turning points; the
multiplicity count against the geometry factor is the validation target. Past
the turning point the lower branch does not exist, and a solver that shoots for
it has nowhere to go. Following the branch through the fold needs an arclength
continuation, which is a different piece of work.

![B-013 reference](../figures/B-013-reference.svg)

## Report

- $\eta(\phi)$ on the lower branch against the radial solve,
- that $\eta > 1$, and by how much,
- where the branch ends,
- observed convergence rate.


## References

@weisz1962
@villadsen1978
@aris1975
