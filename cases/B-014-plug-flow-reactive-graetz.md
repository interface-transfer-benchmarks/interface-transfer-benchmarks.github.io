---
id: B-014
title: Plug-flow reactive Graetz problem
short_title: Reactive Graetz
status: ready

process:
  - reaction
interface_motion: fixed
interface_condition:
  - imposed-value
domains: 1
domain: channel
dimension: 2D
equations:
  - species-diffusion
  - volume-reaction
  - advection

reference: closed-form
reference_note: exact solution for plug flow
numerical_challenge: keeping a bulk reaction out of the convective flux

quantities_of_interest:
  - sherwood_number
  - axial_decay_rate
  - concentration_profile
has_reference_data: true
reference_data:
  - data/B-014/reference.csv

references:
  - shah1978
  - higuera2023
---

# B-014 - Plug-flow reactive channel

## Problem

Plug flow $U\hat{\mathbf{x}}$ between plane walls a distance $W$ apart, both
held at $C=0$, with a first-order bulk reaction. The full two-dimensional
equation is solved, with no boundary-layer approximation and no entrance-length
assumption:

$$
U \partial_x C = D\left(\partial_x^2 C + \partial_y^2 C\right) - k C .
$$

$$
C(x, \pm W/2) = 0 .
$$

## Parameters

Taking $W=1$ and $D=1$, so that $\mathrm{Pe}=U$ and $\mathrm{Da}=k$.

| Parameter | Symbol |
|---|---|
| wall spacing | $W$ |
| diffusivity | $D$ |
| Peclet number | $\mathrm{Pe} = UW/D$ |
| Damkohler number | $\mathrm{Da} = kW^2/D$ |

## Reference

With $q = \pi/W$, the field

$$
C(x,y) = \cos\!\left(q y\right) e^{-\mu x}
$$

is an exact solution of the full two-dimensional problem, where $\mu$ is the
positive root of

$$
D\mu^2 + U\mu - \left(k + D q^2\right) = 0,
\qquad
\mu = \frac{-U + \sqrt{U^2 + 4D\left(k + Dq^2\right)}}{2D} .
$$

The reaction enters only through the constant term, so it shifts the axial
decay rate without touching the transverse structure. The often-quoted shift
$\mu - \mu(0) = k/U$ is the large-Peclet limit of this root, not its value:
at $\mathrm{Pe}=5$ the two differ by a factor of about three, and the quadratic
root is what should be gated.

The Sherwood number built on the transverse profile is unchanged by the
reaction in the same limit, so its drift with $\mathrm{Da}$ measures how much
reaction is leaking into the convective flux.

![B-014 reference](../figures/B-014-reference.svg)

## Report

- $\mu$ at each $\mathrm{Da}$, against the quadratic root,
- the drift of $\mathrm{Sh}$ with $\mathrm{Da}$, which should be small,
- the transverse profile against $\cos(qy)$,
- observed convergence rate.


## References

@shah1978
@higuera2023
