#!/usr/bin/env python3
"""Figures from the reactive-case CSVs.

Reads every ``run/reactive/result/*.csv`` written by ``run/reactive/case-csv.h`` and
draws, per case:

  <case>-sh.{png,pdf}           the observable against what the case swept,
                                with the closed form as a line
  <case>-convergence.{png,pdf}  the relative error against cells per layer,
                                one series per sweep point

plus ``reactive-convergence.{png,pdf}`` overlaying the cases whose abscissa
is a reaction layer, and a three-panel figure for every ``*-field-*.dat``.

Two rules keep the figures honest, both learned by getting them wrong:

* **the abscissa is the `x` column, never a guess.** B6 sweeps the Fourier
  number at two Damkohler numbers, C6 the Biot number at one Thiele modulus,
  B7 a surface Damkohler. Plotting any of those against the `Da` column
  gives a picture that looks like data and is not.
* **2D and 3D rows are never joined.** One case file compiled in two
  dimensions writes two sets of rows with the same case name and different
  references; drawing one line through both is meaningless.

Run from the repository root:  python3 run/reactive/result/plot.py
"""

import csv
import glob
import math
import os
import sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RESULTS = os.path.join(ROOT, "results")
FIGURES = os.path.join(ROOT, "figures", "results")

LAW = {                         # what the case is measured against
    "B1": r"$Sh = 2(1+\sqrt{Da})$, sphere",
    "B2": r"$Sh = 2\sqrt{Da}\,K_1/K_0$, disk",
    "B5": r"$Sh = 2 + 2/\sqrt{\pi Fo}$, unsteady sphere",
    "B6": r"$Sh = 2[1+\sqrt{Da}\,\mathrm{erf}\sqrt{DaFo} + e^{-DaFo}/\sqrt{\pi Fo}]$",
    "B7": r"$Sh_{ov} = 2Da_s/(1+Da_s)$, surface kinetics",
    "B7b": r"$Sh = 2(1+\sqrt{Da})$ from a Robin datum",
    "C1": r"$\eta = 2I_1/(\phi I_0)$, disk pellet",
    "C2": r"$\eta = (3/\phi^2)(\phi\coth\phi - 1)$, sphere pellet",
    "C6": r"$\eta_{ov} = \eta/(1+\phi^2\eta/(d\,Bi))$, pellet behind a film",
    "D8": r"Henry circle: $I^+(t_f)$ against the published closed form",
    "D8lam": r"the Henry sweep: $I^+(t_f)$ over four decades of $\lambda$",
    "D1": r"two half-spaces: $c_1^\gamma = k\sqrt{D_1}/(\sqrt{D_2}+k\sqrt{D_1})$",
    "D1D": r"the same, swept in the diffusivity contrast $D_1/D_2$",
    "D2": r"Newman's sphere: $Sh_i \to 2\pi^2/3$",
    "D3": r"Kronig--Brink: Newman below, $32\lambda_1/3 = 17.90$ above",
    "D9": r"Farsoiya's static bubble, Laplace form inverted by Gaver--Stehfest",
    "D6": r"$1/Sh = 1/Sh_i + kD^*/Sh_e$, resistances in series",
    "B1d": r"opening the box: $Sh \to 2$ like $R_0/L_0$, at fixed $\Delta$",
    "B1dh": r"the same at half the spacing: a box error, not a mesh error",
    "D4": r"$F = 2\pi D_1\lambda\,qR_0I_1/I_0$, reactive droplet",
    "D4lam": r"the same, swept in the Henry ratio $\lambda$",
    "A7": r"solid-body rotation: $F$ must not move with $\Omega$",
    "G2a": r"plug flow, reactive walls: $Sh = \pi^2$ at every $Da$",
    "E2": r"absorbing sphere, Stokes: reference is $Sh = 2$ at $Pe = 0$ only",
    "E2b": r"clean bubble, potential flow (Levich $1.13\,Pe^{1/2}$ needs $Pe \gtrsim 10^3$)",
    "E2c": r"clean bubble, creeping flow (Levich $0.65\,Pe^{1/2}$ needs $Pe \gtrsim 10^3$)",
    "G2": r"reactive Graetz: $Sh_\infty(Da_w)$ against a 1D eigensolve",
    "G4": r"Taylor--Aris: $D_{\rm eff}/D = 1 + Pe^2/210$",
    "G3": r"Lev\^eque: prefactor of $Sh_x \sim x^{-1/3}$",
    "B3": r"$R = kc^2$ outside a disk, against a radial BVP",
    "B4n": r"$R = kc^n$: the order sweep at $Da = 16$",
    "B4lh": r"$R = kc/(1+Kc)^2$: non-monotone in $c$, peak at $Kc = 1$",
    "C5": r"$n$-th order pellet; Aris' $\Phi = \phi\sqrt{(n+1)/2}$",
    "C3": r"Weisz--Hicks: an exothermic pellet has $\eta > 1$",
    "F4": r"$\kappa(T) = 1+\beta T$; Kirchhoff makes the answer exact",
    "C4": r"$\bar C_s/C_\infty$ against Sulaiman Eq. (12)",
    "A1": r"sphere moments: $|\Gamma| = 4\pi R_0^2$, $V = \frac{4}{3}\pi R_0^3$",
    "A1d": r"disk moments: $|\Gamma| = 2\pi R_0$, $V = \pi R_0^2$",
    "A5": r"advected Gaussian: peak $= \sigma_0^2/\sigma^2$, translation",
    "A5r": r"advected Gaussian: peak $= \sigma_0^2/\sigma^2$, rotation",
    "A6": r"shear dispersion: $\hat k \to \frac{2}{3} D\dot S^2$",
    "D7": r"Kapitza: $F = \pi R_0^2S$, independent of $R_K$",
    "D9b": r"static bubble, cut cell: $c_g(0.5)$ against Farsoiya",
    "D9bVOF": r"the same bubble, Basilisk's own VOF/Haroun test",
    "F1": r"$A\to B$: $Sh_A = 2(1+\sqrt{Da})$, $A+B$ harmonic",
    "E2d": r"Robin on a Stokes sphere: $Sh_{ov}=2Da_s/(1+Da_s)$ at $Pe=0$",
}

XSYM = {"Da": r"$Da = kR_0^2/D$",
        "Da_s": r"surface Damköhler $Da_s = k_sR_0/D$",
        "phi": r"Thiele modulus $\phi = R_0\sqrt{k/D}$",
        "Bi": r"Biot number $Bi = k_gR_0/D$",
        "Fo": r"Fourier number $Fo = Dt/R_0^2$",
        "h": r"grid spacing $h$",
        "lambda": r"Henry ratio $\lambda$",
        "k": r"Henry ratio $k$",
        "D1/D2": r"diffusivity ratio $D_1/D_2$",
        "Fo_s": r"Fourier number $Fo$",
        "t": r"time $t$",
        "n": r"reaction order $n$",
        "K": r"Langmuir constant $K$",
        "beta": r"conductivity slope $\beta$",
        "gamma": r"reaction strength $\gamma$",
        "L0/R0": r"box size $L_0/R_0$",
        "Da_w": r"wall Damk\"ohler $Da_w = k_wW/D$",
        "Pe": "P\u00e9clet number $Pe$",
        "Pe_i": "internal P\u00e9clet number $Pe_i$",
        "Pe_omega": "rotational P\u00e9clet number $Pe_\\Omega$",
        "Pe_sig": "Péclet number $Pe_\\sigma = U\\sigma_0/D$",
        "Pe_S": "shear Péclet number $Pe_S = \\dot S\\sigma_0^2/D$",
        "R_K": r"Kapitza resistance $R_K$",
        "d0/dx": r"cells per diameter $d_0/\Delta x$"}

YSYM = {"G4": r"$D_{\rm eff}/D$",
        "A1": r"wet volume $V$",
        "A1d": r"wet volume $V$",
        "A5": r"peak amplitude",
        "A5r": r"peak amplitude",
        "A6": r"$\hat k$, the $t^3$ coefficient",
        "D7": r"interface flux $F$",
        "D9b": r"$c_g$ at $r = 0.5$",
        "D9bVOF": r"$c_g$ at $r = 0.5$",
        "E2d": r"$Sh_{ov}$",
        "F1": r"$Sh_A$",
        "G2": r"$Sh_\infty = D_h q_w/(D(c_b-c_w))$",
        "G3": r"prefactor of $Sh_x$ against Lev\^eque",
        "C1": r"effectiveness factor $\eta$",
        "C2": r"effectiveness factor $\eta$",
        "C6": r"overall effectiveness factor $\eta_{ov}$",
        "D8": r"interfacial flux $I^+(t_f)$",
        "D8lam": r"interfacial flux $I^+(t_f)$",
        "D1": r"interface value $c_1^\gamma$",
        "D1D": r"interface value $c_1^\gamma$",
        "D9": r"interfacial flux $F$",
        "B1d": r"$Sh = 2R_0F/(|\Gamma_h|D\Delta c)$",
        "B1dh": r"$Sh = 2R_0F/(|\Gamma_h|D\Delta c)$",
        "D4": r"uptake $F$", "D4lam": r"uptake $F$",
        "B3": r"uptake $F$", "B4n": r"uptake $F$", "B4lh": r"uptake $F$",
        "C5": r"effectiveness factor $\eta$",
        "C3": r"effectiveness factor $\eta$",
        "F4": r"conduction through the inner circle",
        "C4": r"surface concentration $\bar C_s$"}
YDEF = r"$Sh = 2R_0F/(|\Gamma_h| D \Delta c)$"

# the symbol a legend entry uses for the swept column
SYM = {"Da": "Da", "Da_s": "Da_s", "phi": r"\phi", "Bi": "Bi", "Fo": "Fo",
       "h": "h", "lambda": r"\lambda", "k": "k", "D1/D2": "D_1/D_2",
       "n": "n", "K": "K", "beta": r"\beta", "gamma": r"\gamma",
       "L0/R0": "L_0/R_0",
       # an xname missing here falls through to the raw column name, and
       # mathtext renders `Pe_sig` as "Pe_s ig" -- a legend that looks like
       # a typo in the data rather than in the plotting script.
       "Pe": "Pe", "Pe_omega": r"Pe_\Omega", "Pe_sig": r"Pe_\sigma",
       "Pe_S": "Pe_S", "Pe_i": "Pe_i", "R_K": "R_K", "Da_w": "Da_w",
       "d0/dx": r"d_0/\Delta x", "alpha": r"\alpha"}

# the layer on the convergence abscissa is not the same layer in every case
LAYER = {"B1": r"cells per reaction layer, $NR_0/\sqrt{Da}$",
         "B2": r"cells per reaction layer, $NR_0/\sqrt{Da}$",
         "B7b": r"cells per reaction layer, $NR_0/\sqrt{Da}$",
         "B5": r"cells per diffusive layer, $NR_0\sqrt{Fo}$",
         "B6": r"cells per diffusive layer, $NR_0\sqrt{Fo}$",
         "C1": r"cells per reaction layer, $NR_0/\phi$",
         "C2": r"cells per reaction layer, $NR_0/\phi$",
         "C6": r"cells per reaction layer, $NR_0/\phi$",
         "D8": r"cells per radius, $NR_0/L_0$",
         "D8lam": r"cells per radius, $NR_0/L_0$",
         "D1": r"cells per diffusive layer, $N\sqrt{D_{min}t_{end}}$",
         "D1D": r"cells per diffusive layer, $N\sqrt{D_{min}t_{end}}$",
         "D2": r"cells per radius, $NR_0$",
         "D3": r"cells per radius, $NR_0$",
         "D9": r"cells per radius, $NR_0/L_0$",
         "D6": r"cells per radius, $NR_0$",
         "B1d": r"box size, $L_0/R_0$",
         "B1dh": r"box size, $L_0/R_0$",
         "G2": r"cells per channel width, $NW$",
         "G3": r"cells per channel width, $NW$",
         "G4": r"cells per channel width, $NW$",
         "A7": r"cells per reaction layer, $NR_0/\sqrt{Da}$",
         # B7's reaction is on the surface: there is no bulk layer, and
         # what sets its error is the resolution of Gamma itself.
         "B7": r"cells per radius, $NR_0$",
         "A1": r"cells per radius, $NR_0$",
         "A1d": r"cells per radius, $NR_0$",
         "A5": r"cells per $\sigma_0$, $N\sigma_0$",
         "A5r": r"cells per $\sigma_0$, $N\sigma_0$",
         "A6": r"cells per $\sigma_0$, $N\sigma_0$",
         "D7": r"cells per radius, $NR_0$",
         "D9b": r"cells per diameter, $d_0/\Delta x$",
         "D9bVOF": r"cells per diameter, $d_0/\Delta x$",
         "E2d": r"cells per concentration layer, $NR_0/\sqrt{Pe}$",
         "F1": r"cells per reaction layer, $NR_0/\sqrt{Da}$",
         "G2a": r"cells per channel width, $NW$",
         "E2": r"cells per concentration layer, $NR_0/\sqrt{Pe}$",
         "E2b": r"cells per concentration layer, $NR_0/\sqrt{Pe}$",
         "E2c": r"cells per concentration layer, $NR_0/\sqrt{Pe}$",
         "D4": r"cells per reaction layer, $NR_0/\sqrt{Da}$",
         "D4lam": r"cells per reaction layer, $NR_0/\sqrt{Da}$",
         "B3": r"cells per reaction layer, $NR_0/\sqrt{Da}$",
         "B4n": r"cells per reaction layer, $NR_0/\sqrt{Da}$",
         "B4lh": r"cells per reaction layer, $NR_0/\sqrt{Da}$",
         "C5": r"cells per reaction layer, $NR_0/\phi$",
         "C3": r"cells per reaction layer, $NR_0/\phi$",
         "F4": r"cells across the annulus, $N(R_o-R_i)$",
         "C4": r"cells per reaction layer, $NR_0/\phi$"}

# only these share one abscissa with one meaning, so only these are overlaid
# and only these carry the 1% rule
COMBINED = ("B1", "B2", "C1", "C2")

# not every case is second order in its own abscissa: B1d's box offset falls
# like R0/L0, which is first
SLOPE = {"B1d": 1., "B1dh": 1., "D9bVOF": 1.}

# and not every abscissa is a layer
CTITLE = {"D9bVOF": "VOF/Haroun is first order on this problem",
          "B1d": "the box, not the mesh, sets the error",
          "B1dh": "the box, not the mesh, sets the error",
          "A1": "the moments are fourth order, not second",
          "A1d": "the moments are fourth order, not second",
          "A5": "amplitude: the numerical-diffusion meter",
          "A5r": "amplitude: the numerical-diffusion meter",
          "A6": "order 2 in $\\Delta$, with $\\Delta t \\sim \\Delta^2$",
          "D7": "the field is first order where the flux is exact",
          "D9b": "cut cell on Basilisk's own static bubble",
          "E2d": "a solved surface datum, under flow",
          "B7": "a surface reaction has no layer: $\\Gamma$ sets the error"}

# the symbol for the second parameter a case carries beside the one it sweeps
# The reference is not a closed form everywhere: the nonlinear kinetics are
# gated against a radial two-point BVP on a fine uniform grid -- a different
# discretisation in a different dimension count -- so the legend has to say
# so rather than promise an analytic solution that does not exist.
REFNAME = {"B3": "radial BVP", "B4n": "radial BVP", "B4lh": "radial BVP",
           "C3": "radial BVP", "C33": "radial BVP",
           "C5": "radial BVP", "C53": "radial BVP"}

EXTRA = {"C5": r"\phi", "D3": r"Pe_i", "E2d": r"Da_s"}


def read(path):
    """One submitted file. `id` is the benchmark, `variant` the configuration
    the submitter ran; the label tables below are keyed by `variant` first and
    by `id` second, so a submission that names no variant still gets labelled,
    just generically."""
    with open(path) as f:
        rows = []
        for r in csv.DictReader(f):
            r.setdefault("variant", r.get("id", ""))
            r["case"] = r["variant"] or r["id"]
            for k in ("N", "ranks", "dim", "mg_iters"):
                r[k] = int(r[k])
            for k in ("x", "Da", "n_per_layer", "mg_res", "area", "area_rel",
                      "Sh", "Sh_exact", "rel_err", "F", "F_exact",
                      "id_sum", "id_avg"):
                r[k] = float(r[k])
            r["order"] = float(r["order"]) if r.get("order") else None
            rows.append(r)
        return rows


def label(table, case, default):
    """Fall back from the variant to the benchmark id before giving up, so a
    submission that does not use the article's case names is still labelled."""
    if case in table:
        return table[case]
    return table.get(BENCHMARK.get(case, ""), default)


def run_tag(r):
    """Rows from two different runs are two different measurements. The same
    case compiled serial and under MPI writes two files with the same case
    name and the same `x` values; joining them draws one line through two
    interleaved ladders, which doubles back on itself. This is the same rule
    as "2D and 3D are never joined", applied to the run."""
    return (r["grid"], r["ranks"])


def by(rows, key):
    out = {}
    for r in rows:
        out.setdefault(r[key], []).append(r)
    return out


def finite(rows, key):
    return [r for r in rows if math.isfinite(r[key]) and r[key] > 0.]


def yscale(rows):
    """A log axis silently drops a negative observable — and draws an empty
    figure, which is how D8's interfacial flux (negative: the disk loses what
    it started with) first came out blank. Use a log axis only when every
    value is positive and the range is wide enough to earn one."""
    # A row the case gave no reference for (E2 away from Pe = 0) carries a
    # placeholder in Sh_exact, not an observable, and letting it into the
    # range forced a linear axis. Test rel_err, never the sign of Sh_exact:
    # D9's interfacial flux is legitimately negative and its reference with
    # it, and an earlier version of this filter silently deleted D9's line.
    v = [r["Sh"] for r in rows] + [r["Sh_exact"] for r in rows
                                   if math.isfinite(r["Sh_exact"])]
    if min(v) <= 0.:
        return "linear"
    # A7 spans 4.84 to 23.5 -- a factor 4.86, just under the old threshold of
    # 5 -- and on a linear axis the one unresolved cell-Peclet point flattened
    # the four rungs that sit on the reference into a single line.
    return "log" if max(v)/min(v) > 3. else "linear"


def one_series(rows):
    """True when the case's only sweep *is* the ladder: within one run and one
    dimension, exactly one row per rung and one abscissa per rung.

    Counting distinct values instead — `len({x}) == len({N})` — is a
    coincidence, not a bijection, and it is one that happens constantly: B4lh
    sweeps four Langmuir constants over four rungs, C5 four orders over four
    rungs. Both then get drawn as a single line threaded through every row in
    order of the abscissa, which zigzags between the configurations and looks
    like an unstable method."""
    for d in {r["dim"] for r in rows}:
        for t in {run_tag(r) for r in rows}:
            rs = [r for r in rows if r["dim"] == d and run_tag(r) == t]
            if not rs:
                continue
            if len(rs) != len({r["N"] for r in rs}):
                return False
            if len(rs) != len({r["x"] for r in rs}):
                return False
    return True


def series_key(rows):
    """A case may hold a second parameter beside the one it sweeps: B6 sweeps
    Fo at Da = 1 and 10. Return the column that varies independently, or None."""
    if len({r["Da"] for r in rows}) > 1 and \
       any(abs(r["Da"] - r["x"]) > 1e-12 for r in rows):
        return "Da"
    return None


def dims(rows):
    return sorted({r["dim"] for r in rows})


def set_xscale(ax, rows):
    """`Pe = 0`, `Da = 0` and `Omega = 0` are the rows where the closed form
    is *most* often the one that applies -- E2's `Sh -> 2`, A7's and G2a's
    unperturbed reference -- and a plain log axis dropped every one of them
    without a word. Use symlog below the smallest positive abscissa."""
    xs = [r["x"] for r in rows]
    pos = [x for x in xs if x > 0.]
    if min(xs) <= 0. and pos:
        ax.set_xscale("symlog", linthresh=min(pos))
    else:
        ax.set_xscale("log")


def sh_figure(case, rows, out):
    """The observable against what the case swept, per dimension."""
    # `finite()` also demands a positive value, which is right for a layer
    # count and wrong for the abscissa: it deleted every `Da = 0`, `Pe = 0`
    # and `Omega = 0` row -- in several cases the only row whose closed form
    # applies. Keep them and let `set_xscale` place them.
    rows = [r for r in rows if math.isfinite(r["x"])]
    if len({r["x"] for r in rows}) < 2:
        return
    xname = rows[0]["xname"]
    extra = series_key(rows)

    fig, ax = plt.subplots(figsize=(5.4, 4.1))
    fine = max(r["N"] for r in rows)
    nd = len(dims(rows))

    for d in dims(rows):
        dr = [r for r in rows if r["dim"] == d]
        tag = f", {d}D" if nd > 1 else ""

        # the closed form, one curve per value of the second parameter
        for p in (sorted({r[extra] for r in dr}) if extra else [None]):
            pr = [r for r in dr if extra is None or r[extra] == p]
            # a non-finite Sh_exact means the case declined to name a
            # reference for that row. E2 has one at Pe = 0 and none at
            # Pe = 1..50, where Acrivos-Taylor has expired and Levich has not
            # begun; drawing 2 across the sweep gave a line the data had no
            # reason to follow. The test is finiteness and not the sign:
            # D9's reference flux is negative and perfectly real, and testing
            # the sign silently deleted its line.
            ex = sorted({(r["x"], r["Sh_exact"]) for r in pr
                         if math.isfinite(r["Sh_exact"])})
            if not ex:
                continue
            if len({b for _, b in ex}) == 1 and len(ex) > 1:
                # a ladder, not a sweep: one constant reference, so span the
                # abscissa -- but only as far as the rows that *have* that
                # reference. Spanning `pr` instead drew E2's `Sh = 2` clear
                # across a sweep where it holds at Pe = 0 and nowhere else.
                ex = [(min(a for a, _ in ex), ex[0][1]),
                      (max(a for a, _ in ex), ex[0][1])]
            # With a second parameter the marker *shape and colour* are
            # what carry it, so the reference line must carry it too or
            # nothing in the figure connects "Da_s = 10" to the green
            # triangles: E2d shipped with four black-and-grey reference
            # lines and a legend that explained only N, which is a legend
            # describing a different figure. One "closed form" entry says
            # what a line means; the colour says which family it belongs
            # to, and the markers below name the families.
            lab = (label(REFNAME, case, "closed form") + tag) if (not extra or
                   p == min({r[extra] for r in dr})) else "_nolegend_"
            col = f"C{list(sorted({r[extra] for r in dr})).index(p)}" \
                if extra else "k"
            # a reference that exists at a single abscissa is a point, and
            # drawing it as a line of zero length renders nothing at all.
            style = dict(marker="_", ms=14, ls="none") if len(ex) == 1 \
                else dict(ls="-", lw=1.2)
            ax.plot([a for a, _ in ex], [b for _, b in ex],
                    color=col, label=lab, zorder=1, **style)

        if one_series(dr):
            nr = sorted(dr, key=lambda r: r["x"])
            ax.plot([r["x"] for r in nr], [r["Sh"] for r in nr], "o-", ms=5,
                    mfc="none", lw=0.8, label="measured" + tag)
        else:
            # a second parameter must not share a marker with the first: B6
            # sweeps Fo at Da = 1 and 10, and one style for both draws two
            # laws as one cloud.
            marks = ["o", "s", "^", "D", "v"]
            for i, p in enumerate(sorted({r[extra] for r in dr})
                                  if extra else [None]):
                pr = [r for r in dr if extra is None or r[extra] == p]
                for N in sorted({r["N"] for r in pr}):
                    # -1 is the table's "not a measurement" sentinel, and a
                    # marker drawn from one claims the method computed a
                    # value it explicitly refused to. The reference line
                    # stays, so the gap is visible for what it is.
                    #
                    # NaN is the *other* sentinel and means the opposite: the
                    # row is a measurement, there is simply no closed form to
                    # compare it against (E2 at Pe > 0). Those markers must be
                    # drawn -- filtering them left E2-sh an empty frame -- so
                    # test `< 0` rather than `>= 0`, which NaN fails both ways.
                    nr = sorted([r for r in pr if r["N"] == N
                                 and not r["rel_err"] < 0.],
                                key=lambda r: r["x"])
                    if not nr:
                        continue
                    # with a second parameter the legend is the product of
                    # the two sweeps -- four rungs times three moduli is
                    # twelve entries over the data. The marker already says
                    # which modulus (shape and colour, and the reference
                    # lines are labelled with it), so only the first one
                    # names its rungs.
                    # Without a second parameter the marker means the rung,
                    # so the legend names rungs. With one, the marker means
                    # the *parameter* -- shape and colour both -- and the rung
                    # is only its size. Naming rungs then labels three blue
                    # circles "N = 16, 32, 64" and leaves the squares,
                    # triangles and diamonds anonymous, which is what E2d
                    # shipped with. One entry per parameter value instead,
                    # carried by its finest rung so the sample in the legend
                    # is the largest marker of that family.
                    if extra:
                        lab = (f"${label(EXTRA, case, 'Da')} = {p:g}${tag}"
                               if N == max(r["N"] for r in pr)
                               else "_nolegend_")
                    else:
                        lab = f"$N = {N}$" + tag + (
                            " (finest)" if N == fine and nd == 1 else "")
                    ax.plot([r["x"] for r in nr], [r["Sh"] for r in nr],
                            marks[i % len(marks)], ms=4 + 0.5*math.log2(N),
                            mfc="none", color=f"C{i}" if extra else None,
                            label=lab)

    set_xscale(ax, rows)
    ax.set_yscale(yscale (rows))
    ax.set_xlabel(XSYM.get(xname, xname))
    ax.set_ylabel(label(YSYM, case, YDEF))
    ax.set_title(f"{case}: {label(LAW, case, '')}", fontsize=9)
    ax.grid(True, which="both", lw=0.3, alpha=0.5)
    ax.legend(fontsize=7, frameon=False, ncol=1 + (nd > 1),
              title=(r"marker size $\propto N$" if extra else None),
              title_fontsize=7)
    fig.tight_layout()
    save(fig, out)


def finish_convergence(ax, case, rows):
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlabel(label(LAYER, case, "cells per layer"))
    ax.set_ylabel("relative error")
    # CTITLE was defined and never read: every convergence figure carried
    # "the layer, not the parameter, sets the error", including B1d's and
    # B1dh's, whose entries in that dict say the *opposite* -- the box, not
    # the mesh. A default that contradicts the case is worse than a generic
    # one, because it reads as a finding.
    ax.set_title(f"{case}: "
                 + label(CTITLE, case, "the layer, not the parameter, "
                                    "sets the error"),
                 fontsize=10)
    ax.grid(True, which="both", lw=0.3, alpha=0.5)
    ax.legend(fontsize=7, frameon=False, ncol=2)
    ax.figure.tight_layout()


def convergence_figure(case, rows, out):
    """The error against cells per layer, one series per sweep point."""
    rows = finite(rows, "n_per_layer")
    # a table carries -1 where the case refuses to call a configuration
    # measured (C5's dead cores, B3's stalled Newton). A log axis cannot
    # draw it, but an unfiltered series still claims a legend entry, so
    # the figure would list a curve that is not there.
    rows = finite(rows, "rel_err")
    # -1 is "not a measurement" (C5's dead cores, B3's stalled Newton) and now
    # also "no reference exists for this row" (E2 at Pe > 0). Plotting the
    # latter drew the *physical enhancement* Sh(Pe)/Sh(0) as if it were an
    # error, which no refinement can reduce -- hence E2's flat series.
    rows = [r for r in rows if r["rel_err"] >= 0.]
    # Returning silently here is how B7 went without a convergence figure
    # for as long as it has existed: it wrote HUGE_VAL for n_per_layer --
    # honest for a *surface* reaction, which has no bulk layer, but the
    # column is the convergence abscissa, and `finite()` then emptied the
    # list. A figure that is declined must say so, exactly as the
    # single-resolution branch in main() does.
    if not rows:
        print(f"# {case}: no row survives the convergence filter "
              f"(n_per_layer or rel_err) -- no figure", file=sys.stderr)
        return
    xname = rows[0]["xname"]
    extra = series_key(rows)
    nd = len(dims(rows))

    fig, ax = plt.subplots(figsize=(5.4, 4.1))

    # A case whose only sweep is the ladder itself (D9 sweeps h) has one row
    # per rung: grouping it by `x` gives one series of one point per rung —
    # the "only two points" figure. It is one series through every rung.
    if one_series(rows):
        for d, t in [(d, t) for d in dims(rows)
                     for t in sorted({run_tag(r) for r in rows})]:
            rs = sorted([r for r in rows if r["dim"] == d and run_tag(r) == t],
                        key=lambda r: r["n_per_layer"])
            if len(rs) < 2:
                continue
            ax.plot([r["n_per_layer"] for r in rs],
                    [r["rel_err"] for r in rs], "o-", ms=4, lw=1,
                    label="measured" + (f", {d}D" if len(dims(rows)) > 1
                                        else "") + f" [{t[0]}]")
            if len(rs) > 1:
                n0, n1 = rs[0]["n_per_layer"], rs[-1]["n_per_layer"]
                e0 = rs[0]["rel_err"]
                ax.plot([n0, n1], [e0, e0*(n1/n0)**-2], "k--", lw=0.8,
                        label="slope $-2$" if d == dims(rows)[0] else None)
        finish_convergence(ax, case, rows)
        save(fig, out)
        return

    tags = sorted({run_tag(r) for r in rows})
    for d in dims(rows):
        for x in sorted({r["x"] for r in rows if r["dim"] == d}):
            for p in (sorted({r[extra] for r in rows}) if extra else [None]):
                seen = set()
                for t in tags:
                    rs = sorted([r for r in rows if r["dim"] == d
                                 and r["x"] == x and run_tag(r) == t
                                 and (extra is None or r[extra] == p)],
                                key=lambda r: r["n_per_layer"])
                    if len(rs) < 2:
                        continue
                    # serial and MPI agreeing to the last digit is a result,
                    # not two curves: draw it once
                    sig = tuple((round(r["n_per_layer"], 10),
                                 round(r["rel_err"], 12)) for r in rs)
                    if sig in seen:
                        continue
                    seen.add(sig)
                    lab = f"${SYM.get(xname, xname)} = {x:g}$"
                    if extra:
                        lab += f", ${label(EXTRA, case, 'Da')} = {p:g}$"
                    if nd > 1:
                        lab += f", {d}D"
                    if len(tags) > 1 and len(seen) > 1:
                        lab += f" [{t[0]}" + (f"/{t[1]}" if t[1] > 1 else "") + "]"
                    ax.plot([r["n_per_layer"] for r in rs],
                            [r["rel_err"] for r in rs], "o-", ms=4, lw=1,
                            label=lab)

    if case not in COMBINED:
        # a slope-2 guide, anchored on the coarsest point of the whole set,
        # so the reader can read the order off the figure
        pts = sorted((r["n_per_layer"], r["rel_err"]) for r in rows
                     if r["rel_err"] > 0.)
        if len(pts) > 1:
            (n0, e0), (n1, _) = pts[0], pts[-1]
            ax.plot([n0, n1], [e0, e0*(n1/n0)**-2], "k--", lw=0.8,
                    label="slope $-2$")

    if case in COMBINED:
        xg0, xg1 = 2., 60.
        ax.plot([xg0, xg1], [1e-2*(xg0/4.)**-2, 1e-2*(xg1/4.)**-2],
                "k--", lw=0.8, label="slope $-2$")
        ax.axvline(4., color="0.5", lw=0.8, ls=":")
        ax.plot([4.], [1e-2], "k+", ms=8, mew=1.2, zorder=5)
        ax.annotate("1% at $n/\\ell \\approx 4$", (4., 1e-2),
                    textcoords="offset points", xytext=(8, 8), fontsize=7,
                    color="0.3")

    finish_convergence(ax, case, rows)
    save(fig, out)


def combined_figure(cases, out):
    fig, ax = plt.subplots(figsize=(5.4, 4.1))
    marks = {"B1": "o", "B2": "s", "C1": "v", "C2": "D"}
    colors = {"B1": "C0", "B2": "C3", "C1": "C4", "C2": "C5"}
    for case, rows in sorted(cases.items()):
        if case not in COMBINED:
            continue
        pts = sorted((r["n_per_layer"], r["rel_err"])
                     for r in finite(rows, "n_per_layer"))
        ax.plot([p[0] for p in pts], [p[1] for p in pts], marks[case], ms=4,
                mfc="none", color=colors[case],
                label=f"{case} — {label(LAW, case, '')}")
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlabel(r"cells per reaction layer, $n/\ell$")
    ax.set_ylabel("relative error")
    ax.set_title("Outside and inside, 2D and 3D: one layer, one curve",
                 fontsize=10)
    ax.grid(True, which="both", lw=0.3, alpha=0.5)
    ax.legend(fontsize=7, frameon=False)
    fig.tight_layout()
    save(fig, out)


# --------------------------------------------------------------------- fields

def save(fig, stem):
    os.makedirs(os.path.dirname(stem), exist_ok=True)
    path = f"{stem}.svg"
    fig.savefig(path, format="svg")
    print(os.path.relpath(path, ROOT))
    plt.close(fig)


BENCHMARK = {}


def main():
    paths = sorted(glob.glob(os.path.join(RESULTS, "*", "B-*.csv")))
    if not paths:
        sys.exit("no CSV under results/<solver>/ — nothing to draw")

    cases = {}
    for p in paths:
        for r in read(p):          # one file can hold several variants: B7 and
            BENCHMARK[r["case"]] = r["id"]                # B7b, C2 and C6
            cases.setdefault(r["case"], []).append(r)

    for case, rows in sorted(cases.items()):
        # A case run at a single resolution is a smoke test, not a benchmark,
        # and gets no figure. D3's three rows per sweep point are Fourier
        # times rather than rungs: the convergence figure came out as a
        # vertical line through them, and the Sh figure was squashed flat by
        # the one Pe_i = 1000 row that did not converge (Sh = -92). Both look
        # like data. Refuse rather than mislead.
        if len({r["N"] for r in rows}) < 2:
            print(f"# {case}: one resolution, no figure", file=sys.stderr)
            continue
        stem = os.path.join(FIGURES, f"{rows[0]['id']}-{case}")
        sh_figure(case, rows, f"{stem}-sh")
        convergence_figure(case, rows, f"{stem}-convergence")
    if len([c for c in cases if c in COMBINED]) > 1:
        combined_figure(cases, os.path.join(FIGURES, "combined-convergence"))


if __name__ == "__main__":
    main()
