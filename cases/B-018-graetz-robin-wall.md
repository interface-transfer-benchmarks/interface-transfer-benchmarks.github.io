---
id: B-018
title: Reactive Graetz problem with a reacting wall
short_title: Graetz, Robin wall
status: ready

process:
  - reaction
interface_motion: fixed
interface_condition:
  - kinetic
domains: 1
domain: channel
dimension: 2D
equations:
  - species-diffusion
  - advection

reference: series
reference_note: Graetz eigenfunction series
numerical_challenge: a Robin wall condition on an interface that reaches the domain boundary

quantities_of_interest:
  - sherwood_number
  - decay_rate
  - convergence_rate
has_reference_data: true
reference_data:
  - data/B-018/reference.csv

references:
  - shah1978
  - higuera2023
---

# B-018 - Reactive Graetz problem with a reacting wall

## Problem

Plane Poiseuille flow between walls a distance $W$ apart consumes the species
at the wall by a first-order surface reaction.

$$
u(y)\,\partial_x C = D\left(\partial_x^2 C + \partial_y^2 C\right),
\qquad
u(y) = \frac{3}{2}\bar{u}\left(1 - \left(\frac{2y}{W}\right)^2\right) .
$$

At each wall,

$$
-D\,\partial_n C = k_s C ,
$$

with symmetry on the centreline. The axial diffusion term is kept.

## Parameters

| Parameter | Symbol |
|---|---|
| channel width | $W$ |
| hydraulic diameter | $D_h = 2W$ |
| mean velocity | $\bar{u}$ |
| diffusivity | $D$ |
| Peclet number | $\mathrm{Pe} = \bar{u}W/D$ |
| wall Damkohler number | $\mathrm{Da}_w = k_s W/D$ |

## Reference

Separating $C = Y(y)e^{-\mu x}$ and keeping the axial diffusion leaves an
eigenvalue problem on the half-channel,

$$
Y'' + \left(\mu^2 + \frac{\mu\,u(y)}{D}\right) Y = 0,
\qquad
Y'(0) = 0,
\qquad
D\,Y'(W/2) + k_s Y(W/2) = 0 ,
$$

whose smallest positive root $\mu$ gives an exact solution of the full
two-dimensional problem. The transfer coefficient follows from the same
eigenfunction,

$$
\mathrm{Sh} = \frac{D_h\,q_w}{D\,(C_b - C_w)},
\qquad
C_b = \frac{\int u Y}{\int u} .
$$

As $\mathrm{Pe}\to\infty$ the two limits are the tabulated parallel-plate
values $8.2353$ at $\mathrm{Da}_w\to 0$ and $7.5407$ at
$\mathrm{Da}_w\to\infty$: the wall kinetics move $\mathrm{Sh}$ *down*, from the
constant-flux value to the constant-wall-value one.

![B-018 reference](../figures/B-018-reference.svg)

## Report

- $\mathrm{Sh}(\mathrm{Da}_w)$ and its relative error,
- the decay rate $\mu$,
- the two limits above, reached at large $\mathrm{Pe}$,
- observed convergence rate.

Both observables are differences of nearly equal numbers when the wall reacts
weakly. Report the conditioned error, $\mathrm{Sh}$ divided by the
amplification $C_b/(C_b - C_w)$, and say that you did.


## References

@shah1978
@higuera2023
