# Benchmark index

| ID | Benchmark | Process | Geometry | Reference | Challenge | Status |
|---|---|---|---|---|---|---|
| HT-001 | [Planar partition between two half-spaces](cases/HT-001-planar-partition-two-phases.md) | interfacial-partition | 1D planar | exact-solution | a jump condition with a partition coefficient and a diffusivity contrast | ready |
| HT-002 | [Newman internal transient in a stagnant drop](cases/HT-002-newman-stagnant-drop.md) | interfacial-mass-transfer | 3D sphere | series-solution | the long-time eigenvalue of the interior field | ready |
| HT-003 | [Kronig-Brink circulating drop](cases/HT-003-kronig-brink-circulating-drop.md) | interfacial-mass-transfer | axisymmetric sphere | series-solution | internal circulation transported without numerical diffusion | ready |
| HT-004 | [Steady composite slab with an interfacial partition](cases/HT-004-composite-slab-partition.md) | interfacial-partition | 1D planar | exact-solution | a steady flux carried unchanged through a discontinuous interface | ready |
| HT-005 | [Unsteady Henry jump across a circle](cases/HT-005-unsteady-henry-circle.md) | interfacial-partition | 2D disk | exact-solution | a discontinuous initial field carried across a curved interface | ready |
| HT-006 | [Annulus with a temperature-dependent conductivity](cases/HT-006-kirchhoff-annulus.md) | interfacial-partition | 2D annulus | exact-solution | a nonlinear conductivity linearised by a transform the discretisation does not know about | ready |
| HT-007 | [Static bubble with a Henry jump](cases/HT-007-static-bubble-henry-sphere.md) | interfacial-partition | 3D sphere | exact-solution | a diffusivity contrast across a curved interface in three dimensions | ready |
| MT-001 | [Steady reaction-diffusion outside a sphere](cases/MT-001-reactive-sphere-steady.md) | interfacial-mass-transfer, homogeneous-reaction | 3D sphere | exact-solution | resolving the reaction layer of thickness R0/sqrt(Da) | ready |
| MT-002 | [Steady reactive uptake outside a disk](cases/MT-002-reactive-disk-steady.md) | interfacial-mass-transfer, homogeneous-reaction | 2D disk | exact-solution | logarithmic far field that is only regularised by reaction | ready |
| MT-003 | [Unsteady diffusion to a sphere](cases/MT-003-unsteady-sphere-diffusion.md) | interfacial-mass-transfer | 3D sphere | exact-solution | the singular initial flux and its long-time approach to Sh = 2 | ready |
| MT-004 | [Unsteady diffusion with a first-order reaction outside a sphere](cases/MT-004-unsteady-reactive-sphere.md) | interfacial-mass-transfer, homogeneous-reaction | 3D sphere | exact-solution | a transient and a reaction layer resolved at once | ready |
| MT-005 | [First-order surface kinetics on a sphere](cases/MT-005-surface-kinetics-sphere.md) | interfacial-mass-transfer, heterogeneous-reaction | 3D sphere | exact-solution | a Robin interface condition whose surface value is solved, not imposed | ready |
| MT-006 | [Isothermal catalyst pellet, cylinder](cases/MT-006-pellet-cylinder.md) | catalysis, homogeneous-reaction | 2D disk | exact-solution | interior reaction layer and the volume integral of the rate | ready |
| MT-007 | [Isothermal catalyst pellet, sphere](cases/MT-007-pellet-sphere.md) | catalysis, homogeneous-reaction | 3D sphere | exact-solution | interior reaction layer on a curved three-dimensional interface | ready |
| MT-008 | [Catalyst pellet with an external film](cases/MT-008-pellet-external-film.md) | catalysis, homogeneous-reaction | 3D sphere | exact-solution | a Robin condition on the interior field with a finite Biot number | ready |
| MT-009 | [Reactive absorption into a droplet](cases/MT-009-reactive-absorption-droplet.md) | absorption, homogeneous-reaction | 2D disk | exact-solution | a Henry jump and an interior reaction solved together | ready |
| MT-010 | [Plug-flow reactive Graetz problem](cases/MT-010-plug-flow-reactive-graetz.md) | interfacial-mass-transfer, homogeneous-reaction | 2D channel | exact-solution | keeping a bulk reaction out of the convective flux | ready |
| MT-011 | [Reactive Graetz problem with a reacting wall](cases/MT-011-graetz-robin-wall.md) | interfacial-mass-transfer, heterogeneous-reaction | 2D channel | series-solution | a Robin wall condition on an interface that reaches the domain boundary | ready |
| MT-012 | [Leveque entrance region in a channel](cases/MT-012-leveque-entrance.md) | interfacial-mass-transfer | 2D channel | asymptotic-solution | a boundary layer whose thickness is set by the distance from the entrance | ready |
| MT-013 | [Nonlinear kinetics outside a disk](cases/MT-013-nonlinear-kinetics-disk.md) | interfacial-mass-transfer, homogeneous-reaction | 2D disk | semi-analytical-ode | a rate that is not proportional to the concentration, and a free boundary when the order is below one | ready |
| MT-014 | [n-th order pellet and the generalized Thiele modulus](cases/MT-014-order-n-pellet.md) | catalysis, homogeneous-reaction | 2D disk | semi-analytical-ode | an interior reaction layer with a dead core once the order and the modulus are large enough | ready |
| MT-015 | [Non-isothermal pellet, Weisz-Hicks](cases/MT-015-weisz-hicks-pellet.md) | catalysis, homogeneous-reaction | 2D disk | semi-analytical-ode | an effectiveness factor above one, and a branch that ends at a turning point | ready |
| PH-001 | [Planar one-phase Stefan problem](cases/PH-001-planar-one-phase-stefan.md) | melting, solidification | 1D planar | exact-similarity | one-sided gradient and latent-heat balance | ready |
| PH-002 | [Planar two-phase Stefan problem](cases/PH-002-planar-two-phase-stefan.md) | melting, solidification | 1D planar | exact-similarity | two-sided heat-flux jump | ready |
| PH-003 | [Frank disk](cases/PH-003-frank-disk.md) | solidification | 2D disk | exact-similarity | curvature, isotropy, and area conservation | ready |
| PH-004 | [Frank sphere](cases/PH-004-frank-sphere.md) | solidification | 3D sphere | exact-similarity | surface integration, isotropy, and volume conservation | ready |
| PH-005 | [Sucking interface problem](cases/PH-005-sucking-interface.md) | boiling, evaporation | 1D planar | exact-similarity | Stefan flow and phase-volume expansion | ready |
| PH-006 | [Scriven spherical vapor bubble growth](cases/PH-006-scriven-spherical-bubble-growth.md) | boiling, evaporation | 3D sphere | exact-similarity | spherical Stefan flow and large density ratio | ready |
| PH-007 | [Static evaporating film](cases/PH-007-static-evaporating-film.md) | evaporation | 1D planar-film | asymptotic-solution | diffusion transient and film recession | ready |
| PH-008 | [Species-diffusion Stefan problem](cases/PH-008-species-diffusion-stefan.md) | dissolution | 1D planar | exact-similarity | species-driven interface displacement | ready |
| PH-009 | [Epstein-Plesset steady-radius dissolution](cases/PH-009-epstein-plesset-steady-radius-dissolution.md) | dissolution | 3D sphere | exact-similarity | early-time spherical diffusion flux | ready |
| PH-010 | [Epstein-Plesset dissolving bubble](cases/PH-010-epstein-plesset-dissolving-bubble.md) | dissolution | 3D sphere | semi-analytical-ode | coupled radius-concentration ODE and vanishing radius | ready |
| PH-011 | [Binary-alloy solidification (Rubinstein problem)](cases/PH-011-binary-alloy-solidification.md) | solidification | 1D planar | exact-similarity | coupled heat and solute balance at the interface | ready |
| PH-012 | [d2-law evaporating droplet](cases/PH-012-d2-law-droplet-evaporation.md) | evaporation | 3D sphere | quasi-steady-analytical | quasi-steady gas-phase transport and shrinking droplet | ready |
| PH-013 | [Nusselt laminar film condensation](cases/PH-013-nusselt-film-condensation.md) | condensation | 2D vertical-plate | analytical-boundary-layer | thin condensate film and interfacial shear | ready |
| PH-014 | [Film boiling on a horizontal wall](cases/PH-014-film-boiling-horizontal-wall.md) | boiling, evaporation | 2D horizontal-wall | numerical-plus-correlation | vapor-film instability and bubble release | ready |
| PH-015 | [Gallium melting in a side-heated cavity](cases/PH-015-gallium-melting-cavity.md) | melting | 2D rectangular-cavity | experimental | natural convection coupled to a melting front | draft |
| VC-001 | [Constant-speed planar solidification](cases/VC-001-constant-speed-planar-solidification.md) | solidification | 1D planar | exact-solution | prescribed moving Dirichlet boundary | ready |
| VC-002 | [Constant-rate dissolving bubble](cases/VC-002-constant-rate-bubble.md) | dissolution | 2D/axisymmetric circle-sphere | exact-kinematic | prescribed mass-transfer shrinkage | ready |
| VC-003 | [Advected Gaussian in a uniform flow](cases/VC-003-advected-gaussian.md) | transport-verification | 2D periodic-box | exact-solution | separating numerical diffusion from phase error | ready |
| VC-004 | [Sheared Gaussian in a linear shear flow](cases/VC-004-sheared-gaussian.md) | transport-verification | 2D periodic-box | exact-solution | the advection-diffusion cross term, which neither pure limit exposes | ready |
| VC-005 | [Rotation invariance of the uptake by a reactive disk](cases/VC-005-rotation-invariance-reactive-disk.md) | transport-verification, homogeneous-reaction | 2D disk | exact-solution | a flow that must not change an answer it cannot physically change | ready |
| VC-006 | [Resistance additivity across a conjugate interface](cases/VC-006-resistance-additivity.md) | transport-verification, interfacial-partition | 3D sphere | exact-identity | three separately measured transfer coefficients that must compose | ready |
| VC-007 | [Taylor-Aris dispersion in a plane channel](cases/VC-007-taylor-aris-dispersion.md) | transport-verification | 2D channel | exact-solution | an effective transport coefficient, not a flux, measured from a decay rate | ready |

Reference data is under `data/<ID>/`, reference plots under `figures/`.

Generated by `scripts/generate_index.jl`.
