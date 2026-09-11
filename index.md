# Benchmark index

| ID | Benchmark | Process | Motion | Interface | Domains | Domain | Equations | Reference | Status |
|---|---|---|---|---|---|---|---|---|---|
| B-001 | [Newman internal transient in a stagnant drop](cases/B-001-newman-stagnant-drop.md) | interfacial-transfer | fixed | imposed-value | 1 (monophasic) | 3D sphere | species-diffusion | series | ready |
| B-002 | [Annulus with a temperature-dependent conductivity](cases/B-002-kirchhoff-annulus.md) | interfacial-transfer | fixed | imposed-value | 1 (monophasic) | 2D annulus | heat-diffusion | closed-form | ready |
| B-003 | [Unsteady diffusion to a sphere](cases/B-003-unsteady-sphere-diffusion.md) | interfacial-transfer | fixed | imposed-value | 1 (monophasic) | 3D sphere | species-diffusion | closed-form | ready |
| B-004 | [Steady reaction-diffusion outside a sphere](cases/B-004-reactive-sphere-steady.md) | reaction | fixed | imposed-value | 1 (monophasic) | 3D sphere | species-diffusion, volume-reaction | closed-form | ready |
| B-005 | [Steady reactive uptake outside a disk](cases/B-005-reactive-disk-steady.md) | reaction | fixed | imposed-value | 1 (monophasic) | 2D disk | species-diffusion, volume-reaction | closed-form | ready |
| B-006 | [Unsteady diffusion with a first-order reaction outside a sphere](cases/B-006-unsteady-reactive-sphere.md) | reaction | fixed | imposed-value | 1 (monophasic) | 3D sphere | species-diffusion, volume-reaction | closed-form | ready |
| B-007 | [Isothermal catalyst pellet, cylinder](cases/B-007-pellet-cylinder.md) | reaction | fixed | imposed-value | 1 (monophasic) | 2D disk | species-diffusion, volume-reaction | closed-form | ready |
| B-008 | [Isothermal catalyst pellet, sphere](cases/B-008-pellet-sphere.md) | reaction | fixed | imposed-value | 1 (monophasic) | 3D sphere | species-diffusion, volume-reaction | closed-form | ready |
| B-009 | [Nonlinear kinetics outside a disk](cases/B-009-nonlinear-kinetics-disk.md) | reaction | fixed | imposed-value | 1 (monophasic) | 2D disk | species-diffusion, volume-reaction | quadrature | ready |
| B-010 | [n-th order pellet and the generalized Thiele modulus](cases/B-010-order-n-pellet.md) | reaction | fixed | imposed-value | 1 (monophasic) | 2D disk | species-diffusion, volume-reaction | quadrature | ready |
| B-011 | [Kronig-Brink circulating drop](cases/B-011-kronig-brink-circulating-drop.md) | interfacial-transfer | fixed | imposed-value | 1 (monophasic) | 3D sphere | species-diffusion, advection | series | ready |
| B-012 | [Leveque entrance region in a channel](cases/B-012-leveque-entrance.md) | interfacial-transfer | fixed | imposed-value | 1 (monophasic) | 2D channel | species-diffusion, advection | asymptotic | ready |
| B-013 | [Non-isothermal pellet, Weisz-Hicks](cases/B-013-weisz-hicks-pellet.md) | reaction | fixed | imposed-value | 1 (monophasic) | 2D disk | species-diffusion, heat-diffusion, volume-reaction | quadrature | ready |
| B-014 | [Plug-flow reactive Graetz problem](cases/B-014-plug-flow-reactive-graetz.md) | reaction | fixed | imposed-value | 1 (monophasic) | 2D channel | species-diffusion, volume-reaction, advection | closed-form | ready |
| B-015 | [Rotation invariance of the uptake by a reactive disk](cases/B-015-rotation-invariance-reactive-disk.md) | verification, reaction | fixed | imposed-value | 1 (monophasic) | 2D disk | species-diffusion, volume-reaction, advection | closed-form | ready |
| B-016 | [First-order surface kinetics on a sphere](cases/B-016-surface-kinetics-sphere.md) | reaction | fixed | kinetic | 1 (monophasic) | 3D sphere | species-diffusion | closed-form | ready |
| B-017 | [Catalyst pellet with an external film](cases/B-017-pellet-external-film.md) | reaction | fixed | kinetic | 1 (monophasic) | 3D sphere | species-diffusion, volume-reaction | closed-form | ready |
| B-018 | [Reactive Graetz problem with a reacting wall](cases/B-018-graetz-robin-wall.md) | reaction | fixed | kinetic | 1 (monophasic) | 2D channel | species-diffusion, advection | series | ready |
| B-019 | [Epstein-Plesset steady-radius dissolution](cases/B-019-epstein-plesset-steady-radius-dissolution.md) | dissolution | fixed | equilibrium | 1 (monophasic) | 3D sphere | species-diffusion | closed-form | ready |
| B-020 | [Planar partition between two half-spaces](cases/B-020-planar-partition-two-phases.md) | absorption | fixed | conjugate | 2 (diphasic) | 1D half-space | species-diffusion | closed-form | ready |
| B-021 | [Steady composite slab with an interfacial partition](cases/B-021-composite-slab-partition.md) | absorption | fixed | conjugate | 2 (diphasic) | 1D slab | species-diffusion | closed-form | ready |
| B-022 | [Static circle with a Henry jump](cases/B-022-static-circle-henry.md) | absorption | fixed | conjugate | 2 (diphasic) | 2D disk | species-diffusion | closed-form | ready |
| B-023 | [Static bubble with a Henry jump](cases/B-023-static-bubble-henry-sphere.md) | absorption | fixed | conjugate | 2 (diphasic) | 3D sphere | species-diffusion | closed-form | ready |
| B-024 | [Resistance additivity across a conjugate interface](cases/B-024-resistance-additivity.md) | verification, absorption | fixed | conjugate | 2 (diphasic) | 3D sphere | species-diffusion | closed-form | ready |
| B-025 | [Reactive absorption into a droplet](cases/B-025-reactive-absorption-droplet.md) | absorption, reaction | fixed | conjugate | 2 (diphasic) | 2D disk | species-diffusion, volume-reaction | closed-form | ready |
| B-026 | [Constant-speed planar solidification](cases/B-026-constant-speed-planar-solidification.md) | solidification, verification | prescribed | imposed-value | 1 (monophasic) | 1D slab | heat-diffusion | closed-form | ready |
| B-027 | [Constant-rate dissolving bubble](cases/B-027-constant-rate-bubble.md) | dissolution, verification | prescribed | imposed-flux | 2 (diphasic) | 3D sphere | navier-stokes | closed-form | ready |
| B-028 | [Planar one-phase Stefan problem](cases/B-028-planar-one-phase-stefan.md) | melting, solidification | free | equilibrium | 1 (monophasic) | 1D half-space | heat-diffusion | closed-form | ready |
| B-029 | [Frank disk](cases/B-029-frank-disk.md) | solidification | free | equilibrium | 1 (monophasic) | 2D disk | heat-diffusion | closed-form | ready |
| B-030 | [Frank sphere](cases/B-030-frank-sphere.md) | solidification | free | equilibrium | 1 (monophasic) | 3D sphere | heat-diffusion | closed-form | ready |
| B-031 | [Static evaporating film](cases/B-031-static-evaporating-film.md) | evaporation | free | equilibrium | 1 (monophasic) | 1D film | species-diffusion | asymptotic | ready |
| B-032 | [Species-diffusion Stefan problem](cases/B-032-species-diffusion-stefan.md) | dissolution | free | equilibrium | 1 (monophasic) | 1D half-space | species-diffusion | closed-form | ready |
| B-033 | [Epstein-Plesset dissolving bubble](cases/B-033-epstein-plesset-dissolving-bubble.md) | dissolution | free | equilibrium | 1 (monophasic) | 3D sphere | species-diffusion | quadrature | ready |
| B-034 | [Planar two-phase Stefan problem](cases/B-034-planar-two-phase-stefan.md) | melting, solidification | free | equilibrium | 2 (diphasic) | 1D half-space | heat-diffusion | closed-form | ready |
| B-035 | [Nusselt laminar film condensation](cases/B-035-nusselt-film-condensation.md) | condensation | free | equilibrium | 1 (monophasic) | 2D plate | heat-diffusion, navier-stokes | asymptotic | ready |
| B-036 | [Gallium melting in a side-heated cavity](cases/B-036-gallium-melting-cavity.md) | melting | free | equilibrium | 2 (diphasic) | 2D cavity | heat-diffusion, navier-stokes | data | draft |
| B-037 | [Binary-alloy solidification (Rubinstein problem)](cases/B-037-binary-alloy-solidification.md) | solidification | free | equilibrium, conjugate | 2 (diphasic) | 1D half-space | heat-diffusion, species-diffusion | closed-form | ready |
| B-038 | [Sucking interface problem](cases/B-038-sucking-interface.md) | boiling, evaporation | free | equilibrium, volume-change | 1 (monophasic) | 1D half-space | heat-diffusion, advection | closed-form | ready |
| B-039 | [Scriven spherical vapor bubble growth](cases/B-039-scriven-spherical-bubble-growth.md) | boiling, evaporation | free | equilibrium, volume-change | 1 (monophasic) | 3D sphere | heat-diffusion, advection | closed-form | ready |
| B-040 | [d2-law evaporating droplet](cases/B-040-d2-law-droplet-evaporation.md) | evaporation | free | equilibrium, volume-change | 1 (monophasic) | 3D sphere | species-diffusion, advection | asymptotic | ready |
| B-041 | [Film boiling on a horizontal wall](cases/B-041-film-boiling-horizontal-wall.md) | boiling, evaporation | free | equilibrium, volume-change, capillary | 2 (diphasic) | 2D wall | heat-diffusion, navier-stokes | data | ready |

Reference data is under `data/<ID>/`, submitted results under `results/<solver>/`.

Figures are not stored; they are drawn from that data when the site is built.

Generated by `scripts/generate_index.jl`.
