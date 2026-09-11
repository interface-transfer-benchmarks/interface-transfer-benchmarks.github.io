---
id: B-023
title: Static bubble with a Henry jump
short_title: Static bubble
status: ready

process:
  - absorption
interface_motion: fixed
interface_condition:
  - conjugate
domains: 2
domain: sphere
dimension: 3D
equations:
  - species-diffusion

reference: closed-form
reference_note: exact solution
numerical_challenge: a diffusivity contrast across a curved interface in three dimensions

quantities_of_interest:
  - interfacial_flux
  - convergence_rate
has_reference_data: false

references:
  - farsoiya2021
  - libat2025st
---

# B-023 - Static bubble with a Henry jump

## Problem

A sphere of radius $R_0$ holds gas with diffusivity $D_g$, surrounded by liquid
with diffusivity $D_l$. The gas starts uniform at $C_{g0}$, the liquid at zero,
and the bubble does not move.

$$
\partial_t C_g = D_g\nabla^2 C_g,
\qquad
\partial_t C_l = D_l\nabla^2 C_l .
$$

At $r = R_0$,

$$
\frac{C_l}{C_g} = H,
\qquad
D_g\partial_r C_g = D_l\partial_r C_l .
$$

## Parameters

| Parameter | Symbol |
|---|---|
| bubble radius | $R_0$ |
| diffusivity, gas | $D_g$ |
| diffusivity, liquid | $D_l$ |
| Henry coefficient | $H$ |
| initial gas value | $C_{g0}$ |

## Reference

In Laplace space, with $\ell_i = \sqrt{s/D_i}$,

$$
\tilde{C}_g = \frac{C_{g0}}{s}\left(1 - \frac{2\sinh(\ell_g r)}{\zeta r}\right),
\qquad
\tilde{C}_l = \frac{\xi\,C_{g0}\,e^{-\ell_l r}}{s\,\zeta\,r} ,
$$

$$
\xi = \frac{2D_g\left(\ell_g R_0\cosh(\ell_g R_0) - \sinh(\ell_g R_0)\right)}
{D_l e^{-\ell_l R_0}\left(1 + \ell_l R_0\right)},
\qquad
\zeta = \frac{\xi e^{-\ell_l R_0}}{H R_0} + \frac{2\sinh(\ell_g R_0)}{R_0} ,
$$

inverted by a keyhole contour on the branch cut. This is the three-dimensional
counterpart of B-022's Bessel integral, and it is the reference implementation
of the competing volume-of-fluid treatment as much as a closed form: the
observable is the interfacial flux, which is negative, the bubble losing what
it started with.

## Report

- the interfacial flux against the inversion,
- the residual of the Henry condition,
- the conservation budget,
- observed convergence rate.

A test that suppresses a reference line whenever the reference is negative will
silently delete this case's reference; the test for "no reference here" is
finiteness, never a sign.


## References

@farsoiya2021
@libat2025st
