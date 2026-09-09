# Benchmark taxonomy

## By physical process

- melting
- solidification
- evaporation
- condensation
- boiling
- sublimation
- dissolution with phase-equilibrium analogy

## By coupling level

### Diffusion-only phase change

The interface motion is driven only by heat or mass diffusion.

Examples:

- planar Stefan problem
- Frank disk
- Frank sphere

### Phase change with Stefan flow

The interface motion induces a velocity field because of density change.

Examples:

- sucking interface problem
- vaporization with density ratio

### Phase change with hydrodynamics

The full flow field is coupled to the phase-change rate.

Examples:

- growing vapor bubble
- film boiling
- boiling bubble detachment

### Phase change with capillarity

Surface tension affects the interface dynamics.

Examples:

- evaporating droplet
- boiling bubble with surface tension
- capillary-controlled melting/freezing

### Phase change with buoyancy

Natural convection modifies heat transfer.

Examples:

- melting in a cavity
- film boiling
- Rayleigh-Benard-like melting

## By reference type

- exact solution
- similarity solution
- reduced ODE solution
- high-resolution numerical solution
- experimental data

## By numerical challenge

- interface tracking
- curvature computation
- jump conditions
- mass conservation
- latent heat conservation
- large density ratio
- topology change
- thin thermal boundary layer
- fresh/dead cells
- moving contact line

## Current benchmark coverage

| ID | Process | Geometry | Reference type | Primary numerical challenge |
|---|---|---|---|---|
| HT-001 | interfacial-partition | 1D planar | exact-solution | a jump condition with a partition coefficient and a diffusivity contrast |
| HT-002 | interfacial-mass-transfer | 3D sphere | series-solution | the long-time eigenvalue of the interior field |
| HT-003 | interfacial-mass-transfer | axisymmetric sphere | series-solution | internal circulation transported without numerical diffusion |
| HT-004 | interfacial-partition | 1D planar | exact-solution | a steady flux carried unchanged through a discontinuous interface |
| MT-001 | interfacial-mass-transfer, homogeneous-reaction | 3D sphere | exact-solution | resolving the reaction layer of thickness R0/sqrt(Da) |
| MT-002 | interfacial-mass-transfer, homogeneous-reaction | 2D disk | exact-solution | logarithmic far field that is only regularised by reaction |
| MT-003 | interfacial-mass-transfer | 3D sphere | exact-solution | the singular initial flux and its long-time approach to Sh = 2 |
| MT-004 | interfacial-mass-transfer, homogeneous-reaction | 3D sphere | exact-solution | a transient and a reaction layer resolved at once |
| MT-005 | interfacial-mass-transfer, heterogeneous-reaction | 3D sphere | exact-solution | a Robin interface condition whose surface value is solved, not imposed |
| MT-006 | catalysis, homogeneous-reaction | 2D disk | exact-solution | interior reaction layer and the volume integral of the rate |
| MT-007 | catalysis, homogeneous-reaction | 3D sphere | exact-solution | interior reaction layer on a curved three-dimensional interface |
| MT-008 | catalysis, homogeneous-reaction | 3D sphere | exact-solution | a Robin condition on the interior field with a finite Biot number |
| MT-009 | absorption, homogeneous-reaction | 2D disk | exact-solution | a Henry jump and an interior reaction solved together |
| MT-010 | interfacial-mass-transfer, homogeneous-reaction | axisymmetric tube | exact-solution | separating an advective eigenvalue from a reactive shift |
| PH-001 | melting, solidification | 1D planar | exact-similarity | one-sided gradient and latent-heat balance |
| PH-002 | melting, solidification | 1D planar | exact-similarity | two-sided heat-flux jump |
| PH-003 | solidification | 2D disk | exact-similarity | curvature, isotropy, and area conservation |
| PH-004 | solidification | 3D sphere | exact-similarity | surface integration, isotropy, and volume conservation |
| PH-005 | boiling, evaporation | 1D planar | exact-similarity | Stefan flow and phase-volume expansion |
| PH-006 | boiling, evaporation | 3D sphere | exact-similarity | spherical Stefan flow and large density ratio |
| PH-007 | evaporation | 1D planar-film | asymptotic-solution | diffusion transient and film recession |
| PH-008 | dissolution | 1D planar | exact-similarity | species-driven interface displacement |
| PH-009 | dissolution | 3D sphere | exact-similarity | early-time spherical diffusion flux |
| PH-010 | dissolution | 3D sphere | semi-analytical-ode | coupled radius-concentration ODE and vanishing radius |
| PH-011 | solidification | 1D planar | exact-similarity | coupled heat and solute balance at the interface |
| PH-012 | evaporation | 3D sphere | quasi-steady-analytical | quasi-steady gas-phase transport and shrinking droplet |
| PH-013 | condensation | 2D vertical-plate | analytical-boundary-layer | thin condensate film and interfacial shear |
| PH-014 | boiling, evaporation | 2D horizontal-wall | numerical-plus-correlation | vapor-film instability and bubble release |
| PH-015 | melting | 2D rectangular-cavity | experimental | natural convection coupled to a melting front |
| VC-001 | solidification | 1D planar | exact-solution | prescribed moving Dirichlet boundary |
| VC-002 | dissolution | 2D/axisymmetric circle-sphere | exact-kinematic | prescribed mass-transfer shrinkage |
| VC-003 | transport-verification | 2D periodic-box | exact-solution | separating numerical diffusion from phase error |
| VC-004 | transport-verification | 2D periodic-box | exact-solution | the advection-diffusion cross term, which neither pure limit exposes |
| VC-005 | transport-verification, homogeneous-reaction | 2D disk | exact-solution | a flow that must not change an answer it cannot physically change |
| VC-006 | transport-verification, interfacial-partition | 3D sphere | exact-identity | three separately measured transfer coefficients that must compose |

Generated by `scripts/generate_index.jl`.
