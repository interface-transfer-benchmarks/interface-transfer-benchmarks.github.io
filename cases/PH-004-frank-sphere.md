---
id: PH-004
title: Frank sphere
short_title: Frank sphere
status: ready
benchmark_class: PH

physics:
  - phase-change
  - heat-diffusion
  - radial-symmetry

process:
  - solidification

dimension: 3D
geometry: sphere
interface_motion: moving

reference_type: exact-similarity
numerical_challenge: surface integration, isotropy, and volume conservation
has_exact_solution: true
has_reference_data: true
reference_data:
  - data/PH-004/reference.csv
figures:
  - figures/PH-004-reference.svg

quantities_of_interest:
  - interface_radius
  - temperature_profile
  - phase_volume
  - radial_symmetry_error
  - energy_balance

references:
  - Frank1950
  - GibouFedkiw2005
  - BernauerHerzog2011
  - WenigerTorrilhon2025
---

# PH-004 - Frank sphere

## Problem

The solid sphere is centered at the origin and the moving interface is

$$
r=R(t).
$$

```text
solid nucleus, T = T_m       liquid, T -> T_inf
r < R(t)                    r > R(t)
```

The analytical reference is radial, but numerical methods should solve the full
three-dimensional problem unless they are specifically radial solvers.

Use the nondimensional heat equation in the thermally active liquid:

$$
\partial_tT=\nabla^2T,
\qquad r>R(t).
$$

In radial form,

$$
\partial_tT
=
\frac{1}{r^2}\partial_r(r^2\partial_rT).
$$

The solid nucleus is held at the phase-change temperature,

$$
T=0,\qquad r\le R(t).
$$

At the moving interface,

$$
T(R(t),t)=0,
$$

and

$$
\frac{dR}{dt}=\mathrm{St}\,\partial_rT(R(t)^+,t).
$$

As in the disk case, $\mathrm{St}<0$ and $T_\infty<0$ produce outward growth.

The infinite-domain reference satisfies

$$
T(r,t)\to T_\infty
\qquad\text{as }r\to\infty.
$$

Initialize at $t_0>0$ with

$$
R(t_0)=S_0\sqrt{t_0}.
$$

Use the exact radial temperature outside the sphere and $T=0$ inside it.

## Parameters

| Parameter | Symbol |
|---|---|
| thermal diffusivity | $\alpha$ |
| phase-change temperature | $T_m$ |
| Stefan coefficient | $\mathrm{St}$ |
| similarity radius | $S_0$ |
| initial time | $t_0$ |
| final time | $t_\mathrm{end}$ |
| far-field temperature | $T_\infty$ |

The full-precision value from the formula below is

$$
T_\infty = -0.821033129452817.
$$

## Reference

The interface radius is

$$
R(t)=S_0\sqrt{t}.
$$

Let

$$
s=\frac{r}{\sqrt{t}},
\qquad
F(s)=\frac{\operatorname{erfc}(s/2)}{s}.
$$

The exact temperature field is

$$
T(r,t)
=
\begin{cases}
0, & s\le S_0,\\
T_\infty\left[1-\dfrac{F(s)}{F(S_0)}\right], & s>S_0.
\end{cases}
$$

The far-field temperature is fixed by the Stefan condition:

$$
T_\infty
=
\frac{S_0F(S_0)}
{-2\mathrm{St}F'(S_0)},
$$

with

$$
F'(s)
=
-\frac{\exp(-s^2/4)}{\sqrt{\pi}s}
-
\frac{\operatorname{erfc}(s/2)}{s^2}.
$$

The file `data/PH-004/reference.csv` tabulates $R(t)$ and $T(r,t)$ for selected
times and normalized radii.

![PH-004 Frank sphere reference temperature profile](../figures/PH-004-reference.svg)

## Report

- volume-equivalent radius $R_h=(3V_h/(4\pi))^{1/3}$,
- interface radius error over reconstructed interface points,
- radial temperature profile sampled on axes and diagonals,
- radial symmetry error,
- phase volume error,
- global energy balance.

## References

@Frank1950
@GibouFedkiw2005
@BernauerHerzog2011
@WenigerTorrilhon2025
