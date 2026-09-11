# Benchmark taxonomy

## Interface motion

| Value | Meaning |
|---|---|
| `fixed` | The interface geometry does not change in time |
| `prescribed` | The position follows a law imposed by the case |
| `free` | The position follows from the solved transfer rate |

## Interface condition

How the interfacial value of a transported field is determined. One entry per
field, so a case that solves two fields declares two closures.

| Value | Meaning |
|---|---|
| `imposed-value` | The case gives the value |
| `imposed-flux` | The case gives the flux |
| `kinetic` | A rate law relates flux and value, the value is solved |
| `equilibrium` | A thermodynamic relation fixes the value: melting temperature, Henry, liquidus |
| `conjugate` | Both sides are coupled by a partition and flux continuity, the value is solved |

Two modifiers follow the closures when they apply.

| Value | Meaning |
|---|---|
| `volume-change` | The mass flux drives a velocity jump across the interface |
| `capillary` | Surface tension enters the momentum jump |

A flux jump that sets the interface velocity is not listed here; it is
`interface_motion: free`.

## Domains

`1` monophasic, one domain carries the solved fields. `2` diphasic, two domains
are coupled through the interface condition. A phase held at a uniform value
and not solved does not count as a domain.

## Geometry

`domain` is the shape, `dimension` the number of space dimensions.

`domain`: half-space, slab, film, plate, wall, annulus, disk, sphere, channel,
cavity, periodic-box.

`dimension`: `1D`, `2D`, `3D`. A configuration with an axis of symmetry is `3D`,
whatever mesh it is solved on.

## Equations

What is discretised in the bulk.

| Value | Meaning |
|---|---|
| `heat-diffusion` | An energy equation |
| `species-diffusion` | One or more transported scalars |
| `volume-reaction` | A reaction source inside a phase |
| `advection` | Transport by a velocity field given by the case |
| `navier-stokes` | The velocity field is solved |

Surface reactions are not listed here; they are the `robin` interface
condition.

## Reference

How the reference is evaluated, not what it is called. `reference_note` gives
the specifics.

| Value | Meaning |
|---|---|
| `closed-form` | A formula evaluated to machine precision |
| `series` | An eigenfunction series truncated to tolerance |
| `quadrature` | A reduced ODE or integral solved to tolerance |
| `asymptotic` | Valid only in a stated limit |
| `data` | Published simulation, correlation or measurement |

## Process

The physical process the case represents.

melting, solidification, evaporation, condensation, boiling, dissolution,
absorption, reaction, interfacial-transfer, verification.

The cases that solve for the phase-change rate are those with `stefan` among
their interface conditions.

## Notation

One name per quantity, across every case.

| Quantity | Symbol |
|---|---|
| concentration | $C$, at the surface $C_s$, far field $C_\infty$ |
| temperature | $T$, saturation $T_\mathrm{sat}$, melting $T_m$, far field $T_\infty$ |
| species diffusivity | $D$ |
| thermal diffusivity | $\alpha = \kappa/(\rho c_p)$ |
| thermal conductivity | $\kappa$ |
| heat capacity | $c_p$ |
| latent heat | $L$ |
| Thiele modulus | $\phi$ |
| reaction rate constant | $k$, at a surface $k_s$ |
| partition or Henry coefficient | $H$ |
| wavenumber | $q$ |
| interface | $\Gamma$ |
| radius | $R_0$ fixed or initial, $R(t)$ moving |
| phase subscripts | $l$ liquid, $g$ gas or vapour, $s$ solid |

Dimensionless groups are upright in mathematics, $\mathrm{Sh}$,
$\mathrm{Da}$, $\mathrm{Pe}$, $\mathrm{Fo}$, $\mathrm{Bi}$,
$\mathrm{Ste}$, and plain ASCII in the results tables. Multi-letter roman
subscripts take `\mathrm`, single-letter phase subscripts do not.
