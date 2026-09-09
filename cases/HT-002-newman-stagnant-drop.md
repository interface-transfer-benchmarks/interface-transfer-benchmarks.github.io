---
id: HT-002
title: Newman internal transient in a stagnant drop
short_title: Newman drop
status: ready
benchmark_class: HT

physics:
  - conjugate-transfer
  - mass-transfer

process:
  - interfacial-mass-transfer

dimension: 3D
geometry: sphere
interface_motion: static
reference_type: series-solution
numerical_challenge: the long-time eigenvalue of the interior field

quantities_of_interest:
  - internal_sherwood_number
  - concentration_profile
  - convergence_rate

has_exact_solution: true
has_reference_data: true
reference_data:
  - data/HT-002/reference.csv
figures:
  - figures/HT-002-reference.svg

references:
  - newman1931
  - colombet2013
---

# HT-002 - Newman internal transient in a stagnant drop

## Purpose

Fixes the internal resistance of a drop with no internal circulation. The
long-time internal Sherwood number is a pure number, so the case is a sharp
test of the interior solve and of how the internal transfer coefficient is
defined.

## Physical Configuration

A spherical drop of radius $R$, initially uniform at $C_0$, with its surface
held at $C=0$. There is no flow inside or outside.

## Governing Equations

For $r<R$,

$$
\partial_t C = \frac{D}{r^2}\,\partial_r\!\left(r^2 \partial_r C\right).
$$

## Boundary And Initial Conditions

$$
C(R,t) = 0, \qquad C(r,0) = C_0, \qquad \partial_r C(0,t)=0 .
$$

## Material Parameters

| Parameter | Symbol | Value |
|---|---:|---:|
| drop radius | $R$ | 1 |
| diffusivity | $D$ | 1 |
| initial concentration | $C_0$ | 1 |
| Fourier number | $\mathrm{Fo}=Dt/R^2$ | 0.001 to 1 |

## Reference Solution

$$
\frac{\bar C(t)}{C_0} = \frac{6}{\pi^2}\sum_{n=1}^{\infty}
\frac{1}{n^2}\exp\!\left(-n^2\pi^2 \mathrm{Fo}\right),
$$

and the internal Sherwood number, defined from the decay of $\bar C$ by
$\mathrm{Sh}_i = -(d^2/6D)\,d\ln\bar C/dt$, tends to

$$
\mathrm{Sh}_i \to \frac{2\pi^2}{3} = 6.5797\ldots
$$

The same definition returns HT-003's circulating value from its own decay rate,
so the two bracket the internal resistance on one axis.

![HT-002 reference](../figures/HT-002-reference.svg)

## Recommended Numerical Setup

Start from a uniform interior. Reach $\mathrm{Fo}\gtrsim 0.2$ so that the first
mode dominates and the asymptote is visible. Report the definition used for
$\mathrm{Sh}_i$.

## Quantities To Report

- $\bar C(\mathrm{Fo})$ against the series,
- $\mathrm{Sh}_i(\mathrm{Fo})$ and its approach to $2\pi^2/3$,
- observed convergence rate.

## Known Difficulties

- reading the asymptote before the higher modes have decayed,
- a radius- rather than diameter-based transfer coefficient, which changes the
  constant by a factor of two,
- the singular initial flux at $t=0$.

## References

@newman1931
@colombet2013
