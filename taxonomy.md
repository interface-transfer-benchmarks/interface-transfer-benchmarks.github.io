# Benchmark taxonomy

In the spirit of the historical interface-tracking test-case collections:
<http://test.interface.free.fr/>.

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
