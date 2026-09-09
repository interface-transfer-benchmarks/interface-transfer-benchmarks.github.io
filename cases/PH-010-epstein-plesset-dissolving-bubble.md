---
id: PH-010
title: Epstein-Plesset dissolving bubble
short_title: Epstein-Plesset dissolution
status: ready
benchmark_class: PH

physics:
  - phase-change
  - mass-diffusion
  - soluble-species

process:
  - dissolution

dimension: 3D
geometry: sphere
interface_motion: moving

reference_type: semi-analytical-ode
numerical_challenge: coupled radius-concentration ODE and vanishing radius
has_exact_solution: true
has_reference_data: true
reference_data:
  - data/PH-010/reference.csv
figures:
  - figures/PH-010-reference.svg

quantities_of_interest:
  - bubble_radius
  - dissolution_time
  - concentration_profile
  - gas_mass_conservation

references:
  - EpsteinPlesset1950
  - Gennari2022
  - BasiliskGennariEpsteinPlesset
---

# PH-010 - Epstein-Plesset dissolving bubble

## Problem

A gas bubble of initial radius $R_0$ is immersed in an infinite quiescent
liquid with uniform initial dissolved-gas concentration $c_\infty$ below the
saturation concentration $c_\Sigma$ imposed at the interface by Henry's law.
The bubble shrinks as gas diffuses into the liquid. Gas-side dynamics,
surface tension, and liquid convection (including the small radial Stefan
flow) are neglected, consistent with the Epstein-Plesset model in the dilute
limit $c_\Sigma/\rho_b \ll 1$.

In the liquid, $r > R(t)$,

$$
\partial_t c
=
\frac{D}{r^2}\,
\partial_r\!\left(r^2 \partial_r c\right),
$$

with

$$
c(r,0)=c_\infty,
\qquad
c(R(t),t)=c_\Sigma,
\qquad
c(r,t)\to c_\infty \quad (r\to\infty).
$$

The interface recedes according to the solutal Stefan condition

$$
\rho_b\,\frac{dR}{dt}
=
D\,\partial_r c\big|_{r=R^+},
$$

with $\rho_b$ the gas density inside the bubble (taken constant).

## Parameters

The parameters extend the PH-009 fixed-radius setup to a moving interface.

| Parameter | Symbol |
|---|---|
| initial radius | $R_0$ |
| diffusivity | $D$ |
| interfacial concentration | $c_\Sigma$ |
| bulk concentration | $c_\infty$ |
| bubble gas density | $\rho_b$ |
| uptake parameter | $\beta = (c_\Sigma-c_\infty)/\rho_b$ |
| quasi-steady dissolution time | $t_{qs}$ |

## Reference

Epstein and Plesset obtained, in the quasi-frozen-boundary approximation,

$$
\frac{dR}{dt}
=
-\,\frac{D\,(c_\Sigma-c_\infty)}{\rho_b}
\left[
\frac{1}{R}
+
\frac{1}{\sqrt{\pi D t}}
\right],
$$

an ordinary differential equation that is integrated numerically to machine
precision. Neglecting the transient term $1/\sqrt{\pi D t}$ yields the
closed-form quasi-steady radius

$$
R_{qs}(t)
=
\sqrt{R_0^2 - 2\,\frac{D(c_\Sigma-c_\infty)}{\rho_b}\,t},
$$

which bounds the true radius from above and gives the quasi-steady
dissolution time $t_{qs} = \rho_b R_0^2 / \left(2D(c_\Sigma-c_\infty)\right)$.

Generate the CSV and figure with:

```bash
python3 scripts/plot_reference_figures.py PH-010
```

## Report

- bubble radius $R(t)$ and error against the ODE reference,
- dissolution time (or time to reach $R = 0.2 R_0$),
- radial concentration profiles at selected times,
- integrated gas mass released versus bubble mass lost.

## References

@EpsteinPlesset1950
@Gennari2022
@BasiliskGennariEpsteinPlesset
