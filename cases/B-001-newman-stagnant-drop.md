---
id: B-001
title: Newman internal transient in a stagnant drop
short_title: Newman drop
status: ready

process:
  - interfacial-transfer
interface_motion: fixed
interface_condition:
  - imposed-value
domains: 1
domain: sphere
dimension: 3D
equations:
  - species-diffusion

reference: series
reference_note: eigenfunction series
numerical_challenge: the long-time eigenvalue of the interior field

quantities_of_interest:
  - internal_sherwood_number
  - concentration_profile
  - convergence_rate
has_reference_data: true
reference_data:
  - data/B-001/reference.csv

references:
  - newman1931
  - colombet2013
---

# B-001 - Newman internal transient in a stagnant drop

## Problem

A spherical drop of radius $R_0$, initially uniform at $C_0$, with its surface
held at $C=0$. There is no flow inside or outside.

For $r<R_0$,

$$
\partial_t C = \frac{D}{r^2}\,\partial_r\!\left(r^2 \partial_r C\right).
$$

$$
C(R_0,t) = 0, \qquad C(r,0) = C_0, \qquad \partial_r C(0,t)=0 .
$$

## Parameters

| Parameter | Symbol |
|---|---|
| drop radius | $R_0$ |
| diffusivity | $D$ |
| initial concentration | $C_0$ |
| Fourier number | $\mathrm{Fo}=Dt/R_0^2$ |

## Reference

$$
\frac{\bar C(t)}{C_0} = \frac{6}{\pi^2}\sum_{n=1}^{\infty}
\frac{1}{n^2}\exp\!\left(-n^2\pi^2 \mathrm{Fo}\right),
$$

and the internal Sherwood number, defined from the decay of $\bar C$ by
$\mathrm{Sh}_i = -(d^2/6D)\,d\ln\bar C/dt$, tends to

$$
\mathrm{Sh}_i \to \frac{2\pi^2}{3} = 6.5797\ldots
$$

The same definition returns B-011's circulating value from its own decay rate,
so the two bracket the internal resistance on one axis.

![B-001 reference](../figures/B-001-reference.svg)

## Report

- $\bar C(\mathrm{Fo})$ against the series,
- $\mathrm{Sh}_i(\mathrm{Fo})$ and its approach to $2\pi^2/3$,
- observed convergence rate.


## References

@newman1931
@colombet2013
