---
id: B-012
title: Leveque entrance region in a channel
short_title: Leveque entrance
status: ready

process:
  - interfacial-transfer
interface_motion: fixed
interface_condition:
  - imposed-value
domains: 1
domain: channel
dimension: 2D
equations:
  - species-diffusion
  - advection

reference: asymptotic
reference_note: Leveque entrance-region limit
numerical_challenge: a boundary layer whose thickness is set by the distance from the entrance

quantities_of_interest:
  - sherwood_number
  - convergence_rate
has_reference_data: true
reference_data:
  - data/B-012/reference.csv

references:
  - leveque1928
  - shah1978
---

# B-012 - Leveque entrance region in a channel

## Problem

A uniform stream enters a channel whose walls are held at $C = 0$. Near the
entrance the concentration layer is thin, sees only the wall shear rate, and
grows like $x^{1/3}$.

$$
u(y)\,\partial_x C = D\,\partial_y^2 C,
\qquad
C(x, \pm W/2) = 0,
\qquad
C(0, y) = C_0 .
$$

## Parameters

| Parameter | Symbol |
|---|---|
| channel width | $W$ |
| hydraulic diameter | $D_h = 2W$ |
| mean velocity | $\bar{u}$ |
| wall shear rate | $\dot\gamma = 6\bar{u}/W$ |
| diffusivity | $D$ |
| Peclet number | $\mathrm{Pe} = \bar{u}W/D$ |

## Reference

While the layer is thin against $W$,

$$
\mathrm{Sh}_x = \frac{D_h}{\Gamma(4/3)}
\left(\frac{\dot\gamma}{9 D x}\right)^{1/3} ,
$$

so a log-log fit of the local transfer coefficient against $x$ has prefactor
$D_h\,(\dot\gamma/9D)^{1/3}/\Gamma(4/3)$ and exponent $-1/3$. The two are not
equally easy to measure: the prefactor is an amplitude, the exponent is a slope
that competes with the $O(\delta/W)$ correction still present in any affordable
window.

![B-012 reference](../figures/B-012-reference.svg)

## Report

- the fitted prefactor against the closed form,
- the fitted exponent against $-1/3$,
- the fit window, fixed in $x$ and not keyed on the layer thickness,
- observed convergence rate of the prefactor.


## References

@leveque1928
@shah1978
