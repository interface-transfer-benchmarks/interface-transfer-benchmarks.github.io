---
id: B-037
title: Binary-alloy solidification (Rubinstein problem)
short_title: Rubinstein binary alloy
status: ready

process:
  - solidification
interface_motion: free
interface_condition:
  - equilibrium
  - conjugate
domains: 2
domain: half-space
dimension: 1D
equations:
  - heat-diffusion
  - species-diffusion

reference: closed-form
reference_note: exact similarity solution
numerical_challenge: coupled heat and solute balance at the interface

quantities_of_interest:
  - interface_position
  - interface_temperature
  - interface_concentration
  - temperature_profile
  - concentration_profile
  - solute_conservation
has_reference_data: true
reference_data:
  - data/B-037/reference.csv

references:
  - Rubinstein1971
  - AlexiadesSolomon1993
---

# B-037 - Binary-alloy solidification (Rubinstein problem)

## Problem

A semi-infinite binary melt occupies $x > 0$ with uniform initial temperature
$T_\infty$ and solute concentration $C_\infty$. At $t=0$ the wall $x=0$ is
brought to $T_0$ below the solidus, and a planar solid layer
$0 < x < s(t)$ grows into the melt. Solute diffuses only in the liquid
($D_s = 0$) and is rejected at the front with equilibrium partition
coefficient $H$, so that $C_s^\Gamma = H\,C_l^\Gamma$. The interface
temperature follows the linear liquidus

$$
T_\Gamma = T_m + m\,C_l^\Gamma ,
\qquad m < 0 .
$$

Heat diffusion in each phase,

$$
\partial_t T_s = \alpha_s\,\partial_{xx} T_s \quad (0<x<s),
\qquad
\partial_t T_l = \alpha_l\,\partial_{xx} T_l \quad (x>s),
$$

solute diffusion in the liquid,

$$
\partial_t C = D\,\partial_{xx} C \quad (x>s),
$$

with the interface conditions at $x = s(t)$:

$$
T_s = T_l = T_m + m\,C^\Gamma,
\qquad
\rho L\,\dot s = \kappa_s\,\partial_x T_s - \kappa_l\,\partial_x T_l,
\qquad
(1-H)\,C^\Gamma\,\dot s = -\,D\,\partial_x C .
$$

## Parameters

All quantities are non-dimensional. Equal thermal properties are used in both
phases; the Lewis number $\mathrm{Le} = \alpha/D = 20$ produces a solutal
boundary layer much thinner than the thermal one, which is the physically
relevant and numerically demanding regime.

| Parameter | Symbol |
|---|---|
| density | $\rho$ |
| heat capacity | $c_p$ |
| conductivities | $\kappa_s = \kappa_l$ |
| thermal diffusivities | $\alpha_s = \alpha_l$ |
| solute diffusivity (liquid) | $D$ |
| latent heat | $L$ |
| pure-solvent melting point | $T_m$ |
| liquidus slope | $m$ |
| partition coefficient | $H$ |
| initial concentration | $C_\infty$ |
| initial melt temperature | $T_\infty$ |
| wall temperature | $T_0$ |

The initial melt is above its liquidus $T_m + mC_\infty = -0.5$ and the wall
is well below it, so a solid layer nucleates at the wall and grows.

## Reference

With $s(t) = 2\lambda\sqrt{D t}$ and $\varepsilon_s = \sqrt{D/\alpha_s}$,
$\varepsilon_l = \sqrt{D/\alpha_l}$, the fields are

$$
T_s(x,t) = T_0 + (T_\Gamma - T_0)\,
\frac{\operatorname{erf}\!\big(x/(2\sqrt{\alpha_s t})\big)}
     {\operatorname{erf}(\lambda\varepsilon_s)},
\qquad
T_l(x,t) = T_\infty + (T_\Gamma - T_\infty)\,
\frac{\operatorname{erfc}\!\big(x/(2\sqrt{\alpha_l t})\big)}
     {\operatorname{erfc}(\lambda\varepsilon_l)},
$$

$$
C(x,t) = C_\infty + (C^\Gamma - C_\infty)\,
\frac{\operatorname{erfc}\!\big(x/(2\sqrt{D t})\big)}
     {\operatorname{erfc}(\lambda)} .
$$

The solute balance gives the interface concentration in closed form,

$$
C^\Gamma(\lambda)
=
\frac{C_\infty}
{1 - (1-H)\,F(\lambda)},
\qquad
F(\lambda) = \sqrt{\pi}\,\lambda\,e^{\lambda^2}\operatorname{erfc}(\lambda),
$$

and the Stefan condition closes the problem with one transcendental equation
for $\lambda$:

$$
\rho L\,\lambda\sqrt{D}
=
\frac{\kappa_s\,\big(T_\Gamma(\lambda) - T_0\big)\,
      e^{-\lambda^2\varepsilon_s^2}}
     {\sqrt{\pi\alpha_s}\,\operatorname{erf}(\lambda\varepsilon_s)}
-
\frac{\kappa_l\,\big(T_\infty - T_\Gamma(\lambda)\big)\,
      e^{-\lambda^2\varepsilon_l^2}}
     {\sqrt{\pi\alpha_l}\,\operatorname{erfc}(\lambda\varepsilon_l)},
\qquad
T_\Gamma(\lambda) = T_m + m\,C^\Gamma(\lambda).
$$

## Report

- front position $s(t)$ and error against $2\lambda\sqrt{Dt}$,
- interface temperature and concentration histories against
  $T_\Gamma$, $C^\Gamma$,
- temperature and concentration profiles at selected times,
- global solute conservation (rejected solute vs. liquid enrichment).

## References

@Rubinstein1971
@AlexiadesSolomon1993
