---
id: HT-003
title: Kronig-Brink circulating drop
short_title: Kronig-Brink drop
status: ready
benchmark_class: HT

physics:
  - conjugate-transfer
  - mass-transfer
  - advection

process:
  - interfacial-mass-transfer

dimension: axisymmetric
geometry: sphere
interface_motion: static
reference_type: series-solution
numerical_challenge: internal circulation transported without numerical diffusion

quantities_of_interest:
  - internal_sherwood_number
  - concentration_profile
  - convergence_rate

has_exact_solution: true
has_reference_data: true
reference_data:
  - data/HT-003/reference.csv
figures:
  - figures/HT-003-reference.svg

references:
  - kronig1951
  - colombet2013
---

# HT-003 - Kronig-Brink circulating drop

## Purpose

The upper bracket of the internal resistance of a drop. Internal circulation
raises the internal Sherwood number from HT-002's stagnant value to a second
pure number, and the ratio between them is a direct measure of how much
numerical diffusion the advection scheme adds.

## Physical Configuration

HT-002's drop, with the Hadamard-Rybczynski internal circulation imposed as a
prescribed steady velocity field in the creeping-flow limit
$\mathrm{Re}\to 0$, at large internal Peclet number. No momentum solve is
needed.

## Governing Equations

For $r<R$,

$$
\partial_t C + \mathbf{u}\cdot\nabla C = D \nabla^2 C ,
$$

with $\mathbf{u}$ the Hadamard interior field, whose streamlines are the
Hill spherical vortex.

## Boundary And Initial Conditions

$$
C(R,t) = 0, \qquad C(r,0) = C_0 .
$$

## Material Parameters

| Parameter | Symbol | Value |
|---|---:|---:|
| drop radius | $R$ | 1 |
| diffusivity | $D$ | 1 |
| initial concentration | $C_0$ | 1 |
| internal Peclet number | $\mathrm{Pe}$ | large |

## Reference Solution

At large $\mathrm{Pe}$ the mean concentration decays as
$\bar C \propto \exp(-64\lambda_1 D t/d^2)$, and with the same definition used
in HT-002, $\mathrm{Sh}_i = -(d^2/6D)\,d\ln \bar C/dt$,

$$
\mathrm{Sh}_i \to \frac{32\lambda_1}{3} = 17.90,
\qquad \lambda_1 = 1.678 .
$$

Quote the constant with its $\lambda_1$: the frequently cited 17.66 is the same
formula at the truncation $\lambda_1 = 1.656$, not a different definition. The
full $\mathrm{Sh}_i(\mathrm{Pe})$ curve interpolating between HT-002's 6.58 and
this value is given by the reference below, and is the target for a Peclet
sweep.

![HT-003 reference](../figures/HT-003-reference.svg)

## Recommended Numerical Setup

Impose the analytic interior velocity field rather than solving for it, and
check that it is discretely divergence-free on the mesh actually used;
otherwise the measured decay mixes transport error with a spurious source.

## Quantities To Report

- $\mathrm{Sh}_i$ at large $\mathrm{Pe}$ against $32\lambda_1/3$,
- recovery of HT-002's 6.58 as $\mathrm{Pe}\to 0$,
- $\mathrm{Sh}_i(\mathrm{Pe})$ across the interpolation range,
- observed convergence rate.

## Known Difficulties

- numerical diffusion, which pushes $\mathrm{Sh}_i$ toward the stagnant value
  and makes the scheme look conservative rather than wrong,
- an interior velocity field that is not discretely solenoidal,
- quoting 17.90 against a computation truncated at $\lambda_1 = 1.656$.

## References

@kronig1951
@colombet2013
