---
id: B-011
title: Kronig-Brink circulating drop
short_title: Kronig-Brink drop
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
  - advection

reference: series
reference_note: eigenfunction series
numerical_challenge: internal circulation transported without numerical diffusion

quantities_of_interest:
  - internal_sherwood_number
  - concentration_profile
  - convergence_rate
has_reference_data: true
reference_data:
  - data/B-011/reference.csv

references:
  - kronig1951
  - colombet2013
---

# B-011 - Kronig-Brink circulating drop

## Problem

B-001's drop, with the Hadamard-Rybczynski internal circulation imposed as a
prescribed steady velocity field in the creeping-flow limit
$\mathrm{Re}\to 0$, at large internal Peclet number. No momentum solve is
needed.

For $r<R_0$,

$$
\partial_t C + \mathbf{u}\cdot\nabla C = D \nabla^2 C ,
$$

with $\mathbf{u}$ the Hadamard interior field, whose streamlines are the
Hill spherical vortex.

$$
C(R_0,t) = 0, \qquad C(r,0) = C_0 .
$$

## Parameters

| Parameter | Symbol |
|---|---|
| drop radius | $R_0$ |
| diffusivity | $D$ |
| initial concentration | $C_0$ |
| internal Peclet number | $\mathrm{Pe}$ |

## Reference

At large $\mathrm{Pe}$ the mean concentration decays as
$\bar C \propto \exp(-64\lambda_1 D t/d^2)$, and with the same definition used
in B-001, $\mathrm{Sh}_i = -(d^2/6D)\,d\ln \bar C/dt$,

$$
\mathrm{Sh}_i \to \frac{32\lambda_1}{3} = 17.90,
\qquad \lambda_1 = 1.678 .
$$

Quote the constant with its $\lambda_1$: the frequently cited 17.66 is the same
formula at the truncation $\lambda_1 = 1.656$, not a different definition. The
full $\mathrm{Sh}_i(\mathrm{Pe})$ curve interpolating between B-001's 6.58 and
this value is given by the reference below, and is the target for a Peclet
sweep.

![B-011 reference](../figures/B-011-reference.svg)

## Report

- $\mathrm{Sh}_i$ at large $\mathrm{Pe}$ against $32\lambda_1/3$,
- recovery of B-001's 6.58 as $\mathrm{Pe}\to 0$,
- $\mathrm{Sh}_i(\mathrm{Pe})$ across the interpolation range,
- observed convergence rate.


## References

@kronig1951
@colombet2013
