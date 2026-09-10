# Benchmark taxonomy

In the spirit of the historical
[interface-tracking test-case collections](http://test.interface.free.fr/).

Every case declares the facets below in its file.

## Benchmark class

The identifier prefix.

| Class | Scope |
|---|---|
| `PH` | Phase change: Stefan problems, melting, solidification, evaporation, condensation, boiling |
| `MT` | Mass transfer with reaction, homogeneous in a phase or heterogeneous at the interface |
| `HT` | Conjugate transfer across an interface, heat or mass, without phase change |
| `VC` | Verification and coherence: the answer is known by construction |

## Process

melting, solidification, evaporation, condensation, boiling, dissolution,
absorption, catalysis, interfacial-mass-transfer, interfacial-partition,
homogeneous-reaction, heterogeneous-reaction, transport-verification.

## Physics

heat-diffusion, mass-diffusion, advection, reaction-diffusion,
surface-reaction, conjugate-transfer, soluble-species, phase-change,
stefan-flow, two-phase, surface-tension, gravity, natural-convection,
hydrodynamic-coupling, thermo-solutal-coupling.

## Interface motion

| Value | Meaning |
|---|---|
| `static` | The interface does not move and its position is exact |
| `fixed` | An internal boundary between two phases, held in place |
| `prescribed` | The interface moves along a law imposed by the case |
| `moving` | The interface velocity comes from the solved transfer rate |

## Geometry and dimension

`1D`, `2D`, `2D/axisymmetric`, `axisymmetric`, `3D`, over planar, planar-film,
annulus, disk, sphere, circle-sphere, channel, periodic-box, vertical-plate,
horizontal-wall, rectangular-cavity.

## Reference type

| Value | Meaning |
|---|---|
| `exact-solution` | Closed form, valid for all times |
| `exact-similarity` | Closed form in a similarity variable |
| `exact-kinematic` | Closed form for a prescribed interface law |
| `exact-identity` | An identity the discretisation must satisfy |
| `series-solution` | Convergent eigenfunction series |
| `semi-analytical-ode` | A reduced ODE integrated to tolerance |
| `quasi-steady-analytical` | Closed form under a quasi-steady assumption |
| `asymptotic-solution` | Valid in a stated limit |
| `analytical-boundary-layer` | Boundary-layer closed form |
| `numerical-plus-correlation` | Published simulation with a correlation |
| `experimental` | Measured data |

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
