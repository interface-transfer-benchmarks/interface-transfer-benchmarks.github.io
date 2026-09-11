# TODO

## Benchmark Candidates

Numbers are assigned at implementation time, from the position the facets give
the case in the difficulty order.

### Fixed interface

- Unsteady Henry jump across a circle, two-phase Bessel-integral reference.
- Static bubble with a Henry jump in 3D, Laplace-inversion reference.
- Second-order and n-th order kinetics outside a disk, independent BVP reference.
- Non-isothermal pellet with multiplicity and an S-shaped effectiveness curve.
- Leveque entrance region for a reactive wall.
- Curvature computation on static circle and sphere interfaces.
- Sharp-interface jump condition on an oblique interface.

### Prescribed interface

- Global energy-balance closure for a translating interface.
- Phase volume conservation under a prescribed moving interface.
- Fresh-cell and dead-cell consistency near a prescribed front.

### Free interface, closed-form or reduced reference

- Stefan problem with kinetic undercooling.
- Stefan problem with Gibbs-Thomson curvature correction.
- Cylindrical vapor bubble growth with Stefan flow.
- Neumann two-phase Stefan problem with unequal conductivities.
- Ivantsov paraboloidal dendrite tip (Peclet-undercooling relation).
- Mullins-Sekerka dispersion relation for a perturbed planar front.
- Landau ablation problem with imposed surface heat flux.
- High-transfer-number d2-law variant (Y_s = 0.5).
- Latent-heat conservation under grid refinement.
- Stationary interface with equal heat fluxes on both sides.

### Free interface, data reference

- Fixed or deforming vapor bubble growth with full hydrodynamic coupling.
- Vapor bubble rise with phase change and buoyancy.
- Melting in a square cavity with natural convection.
- Freezing and melting around a cold or hot cylinder.
- Dendritic solidification with anisotropic surface energy.
- Two bubbles or droplets with phase-change-driven interaction.
- Two-front collision or bubble coalescence topology change.
- Thin-film evaporation with a moving contact line.
- Bubble detachment from a heated wall.
- Pool boiling single-bubble growth cycle.
- Freezing of water around a cooled cylinder.
- Evaporation of a sessile droplet.
- Leidenfrost droplet lifetime or vapor-film thickness.
- Condensation film on a vertical plate.

## Pending Data Work

- Digitize the Gau & Viskanta melt-front traces for B-036 (state the
  cross-section used; cross-check against Hannoun et al. converged numerics).

## Repository Tasks

- Add a BibTeX lint/check step.
- Add a Markdown link checker.
- Add a facet-vocabulary check to `scripts/validate.jl`.
