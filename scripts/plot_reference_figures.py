#!/usr/bin/env python3
"""Generate analytical reference data and figures for benchmark cases."""

from __future__ import annotations

import argparse
import csv
import math
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import mpmath as mp


ROOT = Path(__file__).resolve().parents[1]
CURVE_POINTS = 401


def write_csv(path: Path, header: list[str], rows: list[list[object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="") as handle:
        writer = csv.writer(handle, lineterminator="\n")
        writer.writerow(header)
        writer.writerows(rows)


def save_figure(path: Path, title: str, xlabel: str, ylabel: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True, color="0.88", linewidth=0.8)
    plt.tight_layout()
    plt.savefig(path, format="svg")
    plt.close()


def linspace(start: float, stop: float, count: int) -> list[float]:
    if count < 2:
        return [start]
    step = (stop - start) / (count - 1)
    return [start + index * step for index in range(count)]


def generate_ph001() -> None:
    lambda_ = float(
        mp.findroot(
            lambda value: mp.sqrt(mp.pi)
            * value
            * mp.e** (value * value)
            * mp.erf(value)
            - 1,
            0.6,
        )
    )

    rows: list[list[object]] = []
    for time in [0.01, 0.1, 0.4, 1.0]:
        interface_position = 2 * lambda_ * math.sqrt(time)
        for x_over_s in [0, 0.125, 0.25, 0.375, 0.5, 0.625, 0.75, 0.875, 1.0]:
            x = x_over_s * interface_position
            temperature = 1 - math.erf(x / (2 * math.sqrt(time))) / math.erf(lambda_)
            rows.append([time, x_over_s, x, interface_position, temperature])

    write_csv(
        ROOT / "data/PH-001/reference.csv",
        ["time", "x_over_s", "x", "interface_position", "temperature"],
        rows,
    )

    times = linspace(0.01, 1.0, CURVE_POINTS)
    positions = [2 * lambda_ * math.sqrt(time) for time in times]
    plt.figure(figsize=(7.2, 4.3))
    plt.plot(times, positions, color="#1f77b4", linewidth=2.2, label="s(t)")
    plt.legend()
    save_figure(
        ROOT / "figures/PH-001-reference.svg",
        "PH-001 one-phase Stefan reference",
        "time",
        "interface position",
    )


def generate_ph002() -> None:
    xi = float(
        mp.findroot(
            lambda value: value
            - (1 / mp.sqrt(mp.pi))
            * mp.e ** (-value * value)
            * (1 / (1 + mp.erf(value)) - 0.25 / mp.erfc(value)),
            0.25,
        )
    )

    rows: list[list[object]] = []
    for time in [0.01, 0.1, 0.4, 1.0]:
        interface_position = 2 * xi * math.sqrt(time)
        span = 2 * math.sqrt(time)
        for eta in [-2, -1.5, -1, -0.5, 0, 0.5, 1, 1.5, 2]:
            x = eta * span
            if x <= interface_position:
                phase = "minus"
                temperature = 1 - (
                    (1 + math.erf(x / (2 * math.sqrt(time)))) / (1 + math.erf(xi))
                )
            else:
                phase = "plus"
                temperature = -0.25 + 0.25 * math.erfc(
                    x / (2 * math.sqrt(time))
                ) / math.erfc(xi)
            rows.append([time, eta, x, interface_position, phase, temperature])

    write_csv(
        ROOT / "data/PH-002/reference.csv",
        ["time", "eta_x_over_2sqrt_t", "x", "interface_position", "phase", "temperature"],
        rows,
    )

    times = linspace(0.01, 1.0, CURVE_POINTS)
    positions = [2 * xi * math.sqrt(time) for time in times]
    plt.figure(figsize=(7.2, 4.3))
    plt.plot(times, positions, color="#d62728", linewidth=2.2, label="s(t)")
    plt.legend()
    save_figure(
        ROOT / "figures/PH-002-reference.svg",
        "PH-002 two-phase Stefan reference",
        "time",
        "interface position",
    )


def frank_disk_f(similarity_radius: float) -> mp.mpf:
    return mp.e1(similarity_radius * similarity_radius / 4)


def frank_disk_f_prime(similarity_radius: float) -> mp.mpf:
    return -2 * mp.e ** (-similarity_radius * similarity_radius / 4) / similarity_radius


def frank_sphere_f(similarity_radius: float) -> mp.mpf:
    return mp.erfc(similarity_radius / 2) / similarity_radius


def frank_sphere_f_prime(similarity_radius: float) -> mp.mpf:
    return -mp.e ** (-similarity_radius * similarity_radius / 4) / (
        mp.sqrt(mp.pi) * similarity_radius
    ) - mp.erfc(similarity_radius / 2) / (similarity_radius * similarity_radius)


def generate_frank_case(
    case_id: str,
    title: str,
    f,
    f_prime,
    color: str,
) -> None:
    stefan_coefficient = -0.4
    similarity_radius_0 = 1.2
    temperature_inf = float(
        similarity_radius_0
        * f(similarity_radius_0)
        / (-2 * stefan_coefficient * f_prime(similarity_radius_0))
    )

    rows: list[list[object]] = []
    for time in [0.1, 0.25, 0.5, 1.0]:
        interface_radius = similarity_radius_0 * math.sqrt(time)
        for r_over_r in [0, 0.5, 1.0, 1.05, 1.25, 1.5, 2.0, 2.5, 3.0]:
            radius = r_over_r * interface_radius
            similarity_radius = radius / math.sqrt(time)
            if similarity_radius <= similarity_radius_0:
                phase = "solid"
                temperature = 0.0
            else:
                phase = "liquid"
                temperature = float(
                    temperature_inf
                    * (1 - f(similarity_radius) / f(similarity_radius_0))
                )
            rows.append(
                [
                    time,
                    r_over_r,
                    radius,
                    interface_radius,
                    similarity_radius,
                    phase,
                    temperature,
                ]
            )

    write_csv(
        ROOT / f"data/{case_id}/reference.csv",
        [
            "time",
            "r_over_R",
            "r",
            "interface_radius",
            "similarity_radius",
            "phase",
            "temperature",
        ],
        rows,
    )

    radii = linspace(0.0, 3.6, CURVE_POINTS)
    temperatures = [
        0.0
        if radius <= similarity_radius_0
        else float(temperature_inf * (1 - f(radius) / f(similarity_radius_0)))
        for radius in radii
    ]
    plt.figure(figsize=(7.2, 4.3))
    plt.plot(radii, temperatures, color=color, linewidth=2.2, label="T(r, t=1)")
    plt.axvline(
        similarity_radius_0,
        color="0.35",
        linestyle="--",
        linewidth=1.2,
        label="interface",
    )
    plt.legend()
    save_figure(
        ROOT / f"figures/{case_id}-reference.svg",
        f"{case_id} {title} temperature reference",
        "radius",
        "temperature",
    )


def generate_ph003() -> None:
    generate_frank_case("PH-003", "Frank disk", frank_disk_f, frank_disk_f_prime, "#2ca02c")


def generate_ph004() -> None:
    generate_frank_case(
        "PH-004", "Frank sphere", frank_sphere_f, frank_sphere_f_prime, "#9467bd"
    )


def generate_ph005() -> None:
    rho_l = 958.4
    rho_g = 0.597
    k_l = 0.679
    k_g = 0.025
    cp_l = 4216.0
    cp_g = 2030.0
    h_lg = 2.26e6
    t_sat = 373.15
    t_bulk = 378.15
    alpha_l = k_l / (rho_l * cp_l)
    alpha_g = k_g / (rho_g * cp_g)

    def residual(beta: mp.mpf) -> mp.mpf:
        beta = mp.mpf(beta)
        density_diffusion_ratio = (
            rho_g * mp.sqrt(alpha_g) / (rho_l * mp.sqrt(alpha_l))
        )
        return beta - (
            (t_bulk - t_sat)
            * cp_g
            * k_l
            * mp.sqrt(alpha_g)
            * mp.e
            ** (
                -(beta * beta)
                * rho_g
                * rho_g
                * alpha_g
                / (rho_l * rho_l * alpha_l)
            )
        ) / (
            h_lg
            * k_g
            * mp.sqrt(mp.pi * alpha_l)
            * mp.erfc(beta * density_diffusion_ratio)
        )

    beta = float(mp.findroot(residual, 0.8))

    def interface_position(time: float) -> float:
        return 2 * beta * math.sqrt(alpha_g * time)

    def liquid_velocity(time: float) -> float:
        return (1 - rho_g / rho_l) * beta * math.sqrt(alpha_g / time)

    def temperature(x: float, time: float) -> float:
        density_diffusion_ratio = rho_g * math.sqrt(alpha_g) / (
            rho_l * math.sqrt(alpha_l)
        )
        argument = x / (2 * math.sqrt(alpha_l * time)) + beta * (
            rho_g - rho_l
        ) / rho_l * math.sqrt(alpha_g / alpha_l)
        return t_bulk - (t_bulk - t_sat) / math.erfc(
            beta * density_diffusion_ratio
        ) * math.erfc(argument)

    rows: list[list[object]] = []
    for time in [0.1, 0.25, 0.5, 1.0]:
        delta = interface_position(time)
        velocity = liquid_velocity(time)
        for x_over_delta in [0, 0.5, 1.0, 1.05, 1.25, 1.5, 2.0, 3.0, 4.0]:
            x = x_over_delta * delta
            phase = "vapor" if x <= delta else "liquid"
            temp = t_sat if x <= delta else temperature(x, time)
            rows.append([time, x_over_delta, x, delta, velocity, phase, temp])

    write_csv(
        ROOT / "data/PH-005/reference.csv",
        [
            "time",
            "x_over_delta",
            "x",
            "interface_position",
            "liquid_velocity",
            "phase",
            "temperature",
        ],
        rows,
    )

    times = linspace(0.1, 1.0, CURVE_POINTS)
    positions = [interface_position(time) for time in times]
    velocities = [liquid_velocity(time) for time in times]

    figure, axis_position = plt.subplots(figsize=(7.2, 4.3))
    axis_velocity = axis_position.twinx()

    position_line = axis_position.plot(
        times,
        positions,
        color="#8c564b",
        linewidth=2.2,
        label="delta(t)",
    )[0]
    velocity_line = axis_velocity.plot(
        times,
        velocities,
        color="#17becf",
        linewidth=2.2,
        label="u_l(t)",
    )[0]

    axis_position.set_title("PH-005 sucking-interface reference")
    axis_position.set_xlabel("time")
    axis_position.set_ylabel("vapor-layer thickness")
    axis_velocity.set_ylabel("liquid velocity")
    axis_position.grid(True, color="0.88", linewidth=0.8)
    axis_position.legend(
        [position_line, velocity_line],
        [position_line.get_label(), velocity_line.get_label()],
        loc="best",
    )
    figure.tight_layout()
    figure.savefig(ROOT / "figures/PH-005-reference.svg", format="svg")
    plt.close(figure)


def scriven_integral(
    lower: float,
    beta: float,
    rho_l: float,
    rho_g: float,
) -> mp.mpf:
    if lower >= 1:
        return mp.mpf("0")
    lower = max(0.0, lower)

    def integrand(x: mp.mpf) -> mp.mpf:
        return mp.e ** (
            -(beta * beta)
            * ((1 - x) ** -2 - 2 * (1 - rho_g / rho_l) * x - 1)
        )

    points = [lower]
    for point in [0.5, 0.9, 0.99, 0.999, 1.0]:
        if point > lower:
            points.append(point)
    return mp.quad(integrand, points)


def generate_ph006() -> None:
    rho_l = 958.0
    rho_g = 0.59
    k_l = 0.6
    cp_l = 4216.0
    cp_g = 2034.0
    h_lg = 2.257e6
    t_sat = 373.0
    jakob = 3.0
    t_bulk = t_sat + h_lg * rho_g * jakob / (rho_l * cp_l)
    alpha_l = k_l / (rho_l * cp_l)

    lhs = rho_l * cp_l * (t_bulk - t_sat) / (
        rho_g * (h_lg + (cp_l - cp_g) * (t_bulk - t_sat))
    )

    def residual(beta: mp.mpf) -> mp.mpf:
        return 2 * beta * beta * scriven_integral(0.0, float(beta), rho_l, rho_g) - lhs

    beta = float(mp.findroot(residual, (3.0, 4.0)))

    def radius(time: float) -> float:
        return 2 * beta * math.sqrt(alpha_l * time)

    energy_scale = rho_g * (h_lg + (cp_l - cp_g) * (t_bulk - t_sat)) / (
        rho_l * cp_l
    )

    def temperature(r: float, time: float) -> float:
        interface_radius = radius(time)
        if r <= interface_radius:
            return t_sat
        lower = 1 - interface_radius / r
        return float(
            t_bulk
            - 2
            * beta
            * beta
            * energy_scale
            * scriven_integral(lower, beta, rho_l, rho_g)
        )

    rows: list[list[object]] = []
    for time in [0.152088195917732, 0.25, 0.5, 1.0]:
        interface_radius = radius(time)
        for r_over_r in [0, 0.5, 1.0, 1.05, 1.25, 1.5, 2.0, 3.0, 4.0]:
            r = r_over_r * interface_radius
            phase = "vapor" if r <= interface_radius else "liquid"
            rows.append(
                [
                    time,
                    r_over_r,
                    r,
                    interface_radius,
                    phase,
                    temperature(r, time),
                ]
            )

    write_csv(
        ROOT / "data/PH-006/reference.csv",
        ["time", "r_over_R", "r", "bubble_radius", "phase", "temperature"],
        rows,
    )

    times = linspace(0.152088195917732, 1.0, CURVE_POINTS)
    radii = [radius(time) for time in times]
    plt.figure(figsize=(7.2, 4.3))
    plt.plot(times, radii, color="#e377c2", linewidth=2.2, label="R(t)")
    plt.legend()
    save_figure(
        ROOT / "figures/PH-006-reference.svg",
        "PH-006 Scriven spherical bubble reference",
        "time",
        "bubble radius",
    )


def generate_vc001() -> None:
    speed = 1.0

    def interface_position(time: float) -> float:
        return speed * time

    def temperature(x: float, time: float) -> float:
        if x <= interface_position(time):
            return 0.0
        return -1.0 + math.exp(-speed * (x - interface_position(time)))

    rows: list[list[object]] = []
    for time in [0.0, 0.05, 0.1, 0.2]:
        position = interface_position(time)
        for x in linspace(0.0, 0.5, 11):
            phase = "solid" if x <= position else "active"
            rows.append([time, x, position, phase, temperature(x, time)])

    write_csv(
        ROOT / "data/VC-001/reference.csv",
        ["time", "x", "interface_position", "phase", "temperature"],
        rows,
    )

    xs = linspace(0.0, 0.5, CURVE_POINTS)
    plt.figure(figsize=(7.2, 4.3))
    for time, color in [(0.0, "#1f77b4"), (0.1, "#ff7f0e"), (0.2, "#2ca02c")]:
        plt.plot(
            xs,
            [temperature(x, time) for x in xs],
            color=color,
            linewidth=2.0,
            label=f"T(x,{time:g})",
        )
    plt.legend()
    save_figure(
        ROOT / "figures/VC-001-reference.svg",
        "VC-001 constant-speed solidification reference",
        "x",
        "temperature",
    )


def generate_ph007() -> None:
    h0 = 1.0
    domain_height = 10.0
    diffusivity = 1.0
    mu = 0.001 * 0.8
    t_shift = 0.05
    quasi_static_speed = -mu * diffusivity / (domain_height - h0)

    def h_quasi_static(time: float) -> float:
        return h0 + quasi_static_speed * time

    def h_transient(time: float) -> float:
        return h0 + 2 * mu * (
            math.sqrt(t_shift / math.pi) - math.sqrt((time + t_shift) / math.pi)
        )

    def v_transient(time: float) -> float:
        return -mu * math.sqrt(diffusivity / (math.pi * (time + t_shift)))

    rows: list[list[object]] = []
    for time in [0.0, 1.0, 10.0, 25.0, 50.0, 100.0]:
        rows.append(
            [
                time,
                h_quasi_static(time),
                quasi_static_speed,
                h_transient(time),
                v_transient(time),
            ]
        )

    write_csv(
        ROOT / "data/PH-007/reference.csv",
        [
            "time",
            "quasi_static_thickness",
            "quasi_static_velocity",
            "transient_thickness",
            "transient_velocity",
        ],
        rows,
    )

    times = linspace(0.0, 100.0, CURVE_POINTS)
    plt.figure(figsize=(7.2, 4.3))
    plt.plot(times, [h_quasi_static(t) for t in times], label="quasi-static")
    plt.plot(times, [h_transient(t) for t in times], label="early transient")
    plt.legend()
    save_figure(
        ROOT / "figures/PH-007-reference.svg",
        "PH-007 static evaporating film reference",
        "time",
        "film thickness",
    )


def generate_vc002() -> None:
    initial_radius = 1.0
    density_dispersed = 0.001
    mass_transfer_rate = -1.0e-3

    def radius(time: float) -> float:
        return initial_radius + mass_transfer_rate / density_dispersed * time

    rows: list[list[object]] = []
    for time in [0.0, 0.25, 0.5, 0.75, 0.9]:
        r = radius(time)
        rows.append([time, r, math.pi * r * r, 4 * math.pi * r**3 / 3])

    write_csv(
        ROOT / "data/VC-002/reference.csv",
        ["time", "radius", "area_2d", "volume_3d"],
        rows,
    )

    times = linspace(0.0, 0.95, CURVE_POINTS)
    plt.figure(figsize=(7.2, 4.3))
    plt.plot(times, [radius(t) for t in times], label="R(t)", color="#7f7f7f")
    plt.legend()
    save_figure(
        ROOT / "figures/VC-002-reference.svg",
        "VC-002 constant-rate bubble reference",
        "time",
        "radius",
    )


def generate_ph008() -> None:
    diffusivity = 0.1
    henry = 1.2
    c_sigma = 1.0

    def displacement(time: float) -> float:
        return 2 / henry * math.sqrt(time * diffusivity / math.pi)

    def concentration(distance_from_interface: float, time: float) -> float:
        if time <= 0:
            return 0.0
        return c_sigma * math.erfc(distance_from_interface / (2 * math.sqrt(diffusivity * time)))

    rows: list[list[object]] = []
    for time in [1.0, 10.0, 50.0, 175.0]:
        ell = displacement(time)
        for eta in [0, 0.25, 0.5, 1.0, 2.0, 4.0]:
            distance = eta * 2 * math.sqrt(diffusivity * time)
            rows.append([time, ell, eta, distance, concentration(distance, time)])

    write_csv(
        ROOT / "data/PH-008/reference.csv",
        ["time", "interface_displacement", "eta", "distance_from_interface", "concentration"],
        rows,
    )

    times = linspace(0.0, 175.0, CURVE_POINTS)
    plt.figure(figsize=(7.2, 4.3))
    plt.plot(times, [displacement(t) for t in times], label="ell(t)", color="#17becf")
    plt.legend()
    save_figure(
        ROOT / "figures/PH-008-reference.svg",
        "PH-008 species-diffusion Stefan reference",
        "time",
        "interface displacement",
    )


def generate_ph009() -> None:
    radius = 0.5
    diffusivity = 1.0 / 0.0526
    c_sigma = 0.2
    c_bulk = 0.0

    def concentration(r: float, time: float) -> float:
        if r <= radius:
            return c_sigma
        return c_bulk + (c_sigma - c_bulk) * radius / r * math.erfc(
            (r - radius) / (2 * math.sqrt(diffusivity * time))
        )

    rows: list[list[object]] = []
    for time in [1.0e-5, 1.0e-4, 1.0e-3, 1.0e-2]:
        for r_over_r in [1.0, 1.1, 1.2, 1.5, 2.0, 3.0]:
            r = r_over_r * radius
            rows.append([time, r_over_r, r, concentration(r, time)])

    write_csv(
        ROOT / "data/PH-009/reference.csv",
        ["time", "r_over_R", "r", "concentration"],
        rows,
    )

    radii = linspace(radius, 2.0, CURVE_POINTS)
    plt.figure(figsize=(7.2, 4.3))
    for time, color in [(1.0e-4, "#1f77b4"), (1.0e-3, "#ff7f0e"), (1.0e-2, "#2ca02c")]:
        plt.plot(
            radii,
            [concentration(r, time) for r in radii],
            label=f"t={time:g}",
            color=color,
        )
    plt.legend()
    save_figure(
        ROOT / "figures/PH-009-reference.svg",
        "PH-009 Epstein-Plesset concentration reference",
        "radius",
        "concentration",
    )


def generate_ph010() -> None:
    radius_0 = 0.5
    diffusivity = 1.0
    beta = 0.2  # (c_sigma - c_inf) / rho_b

    # Integrate dR/dt = -D*beta*(1/R + 1/sqrt(pi D t)) with t = tau^2
    # so that dR/dtau = -2 D beta (tau/R + 1/sqrt(pi D)) is regular at 0.
    sqrt_pi_d = math.sqrt(math.pi * diffusivity)

    def rhs(tau: float, radius: float) -> float:
        return -2.0 * diffusivity * beta * (tau / radius + 1.0 / sqrt_pi_d)

    tau = 0.0
    radius = radius_0
    dtau = 1.0e-4
    history: list[tuple[float, float]] = [(0.0, radius_0)]
    while radius > 0.02 * radius_0:
        k1 = rhs(tau, radius)
        k2 = rhs(tau + 0.5 * dtau, radius + 0.5 * dtau * k1)
        k3 = rhs(tau + 0.5 * dtau, radius + 0.5 * dtau * k2)
        k4 = rhs(tau + dtau, radius + dtau * k3)
        radius += dtau / 6.0 * (k1 + 2 * k2 + 2 * k3 + k4)
        tau += dtau
        history.append((tau * tau, radius))

    def quasi_steady(time: float) -> float:
        value = radius_0**2 - 2 * diffusivity * beta * time
        return math.sqrt(value) if value > 0 else 0.0

    final_time = history[-1][0]
    sample_times = [t for t in [0.0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35] if t < final_time]
    sample_times.append(final_time)
    rows: list[list[object]] = []
    index = 0
    for target in sample_times:
        while index < len(history) - 1 and history[index][0] < target:
            index += 1
        time, radius_ode = history[index]
        rows.append([time, radius_ode, quasi_steady(time)])

    write_csv(
        ROOT / "data/PH-010/reference.csv",
        ["time", "radius_epstein_plesset", "radius_quasi_steady"],
        rows,
    )

    times = [point[0] for point in history]
    radii = [point[1] for point in history]
    plt.figure(figsize=(7.2, 4.3))
    plt.plot(times, radii, label="Epstein-Plesset ODE", color="#1f77b4")
    plt.plot(
        times,
        [quasi_steady(t) for t in times],
        label="quasi-steady",
        color="#ff7f0e",
        linestyle="--",
    )
    plt.legend()
    save_figure(
        ROOT / "figures/PH-010-reference.svg",
        "PH-010 Epstein-Plesset dissolving bubble",
        "time",
        "bubble radius",
    )


def generate_ph011() -> None:
    diffusivity = mp.mpf("0.05")
    alpha = mp.mpf("1.0")
    conductivity = mp.mpf("1.0")
    rho_latent = mp.mpf("1.0")  # rho * L
    t_melt = mp.mpf("0.0")
    liquidus_slope = mp.mpf("-0.5")
    partition = mp.mpf("0.2")
    c_inf = mp.mpf("1.0")
    t_inf = mp.mpf("-0.3")
    t_wall = mp.mpf("-1.5")
    epsilon = mp.sqrt(diffusivity / alpha)

    def c_interface(lam: mp.mpf) -> mp.mpf:
        f_lambda = mp.sqrt(mp.pi) * lam * mp.exp(lam**2) * mp.erfc(lam)
        return c_inf / (1 - (1 - partition) * f_lambda)

    def t_interface(lam: mp.mpf) -> mp.mpf:
        return t_melt + liquidus_slope * c_interface(lam)

    def residual(lam: mp.mpf) -> mp.mpf:
        t_gamma = t_interface(lam)
        arg = lam * epsilon
        solid_flux = (
            conductivity
            * (t_gamma - t_wall)
            * mp.exp(-(arg**2))
            / (mp.sqrt(mp.pi * alpha) * mp.erf(arg))
        )
        liquid_flux = (
            conductivity
            * (t_inf - t_gamma)
            * mp.exp(-(arg**2))
            / (mp.sqrt(mp.pi * alpha) * mp.erfc(arg))
        )
        return rho_latent * lam * mp.sqrt(diffusivity) - solid_flux + liquid_flux

    lam = mp.findroot(residual, mp.mpf("0.5"))
    c_gamma = c_interface(lam)
    t_gamma = t_interface(lam)

    def front(time: float) -> float:
        return float(2 * lam * mp.sqrt(diffusivity * time))

    def temperature(x: float, time: float) -> float:
        s = front(time)
        if x <= s:
            return float(
                t_wall
                + (t_gamma - t_wall)
                * mp.erf(x / (2 * mp.sqrt(alpha * time)))
                / mp.erf(lam * epsilon)
            )
        return float(
            t_inf
            + (t_gamma - t_inf)
            * mp.erfc(x / (2 * mp.sqrt(alpha * time)))
            / mp.erfc(lam * epsilon)
        )

    def concentration(x: float, time: float) -> float:
        s = front(time)
        if x <= s:
            return float(partition * c_gamma)
        return float(
            c_inf
            + (c_gamma - c_inf)
            * mp.erfc(x / (2 * mp.sqrt(diffusivity * time)))
            / mp.erfc(lam)
        )

    rows: list[list[object]] = [
        ["lambda", float(lam), "", "", ""],
        ["C_gamma", float(c_gamma), "", "", ""],
        ["T_gamma", float(t_gamma), "", "", ""],
    ]
    for time in [1.0, 4.0, 10.0]:
        s = front(time)
        rows.append(["front_position", time, s, "", ""])
        for x in [0.0, 0.5 * s, s, s + 0.05, s + 0.25, s + 1.0, s + 3.0]:
            rows.append(["profile", time, x, temperature(x, time), concentration(x, time)])

    write_csv(
        ROOT / "data/PH-011/reference.csv",
        ["record", "time_or_value", "x_or_front", "temperature", "concentration"],
        rows,
    )

    time_plot = 4.0
    s_plot = front(time_plot)
    positions = linspace(0.0, s_plot + 4.0, CURVE_POINTS)
    figure, (axis_t, axis_c) = plt.subplots(1, 2, figsize=(9.6, 4.3))
    axis_t.plot(positions, [temperature(x, time_plot) for x in positions], color="#1f77b4")
    axis_t.axvline(s_plot, color="0.6", linestyle=":")
    axis_t.set_title("temperature, t = 4")
    axis_t.set_xlabel("x")
    axis_t.grid(True, color="0.88", linewidth=0.8)
    axis_c.plot(positions, [concentration(x, time_plot) for x in positions], color="#d62728")
    axis_c.axvline(s_plot, color="0.6", linestyle=":")
    axis_c.set_title("concentration, t = 4")
    axis_c.set_xlabel("x")
    axis_c.grid(True, color="0.88", linewidth=0.8)
    figure.suptitle("PH-011 Rubinstein binary-alloy reference")
    figure.tight_layout()
    figure.savefig(ROOT / "figures/PH-011-reference.svg", format="svg")
    plt.close(figure)


def generate_ph012() -> None:
    diameter_0 = 1.0e-3
    rho_liquid = 1000.0
    rho_gas = 1.0
    diffusivity = 2.5e-5
    y_surface = 0.05
    y_far = 0.0

    transfer_number = (y_surface - y_far) / (1.0 - y_surface)
    evaporation_constant = (
        8.0 * rho_gas * diffusivity / rho_liquid * math.log1p(transfer_number)
    )
    lifetime = diameter_0**2 / evaporation_constant

    def diameter(time: float) -> float:
        value = diameter_0**2 - evaporation_constant * time
        return math.sqrt(value) if value > 0 else 0.0

    def mass_rate(time: float) -> float:
        radius = 0.5 * diameter(time)
        return 4.0 * math.pi * rho_gas * diffusivity * radius * math.log1p(transfer_number)

    def mass_fraction(r_over_radius: float) -> float:
        return 1.0 - (1.0 - y_far) * (1.0 + transfer_number) ** (-1.0 / r_over_radius)

    rows: list[list[object]] = [
        ["B_M", transfer_number, ""],
        ["K", evaporation_constant, ""],
        ["t_life", lifetime, ""],
    ]
    for fraction in [0.0, 0.1, 0.25, 0.5, 0.75, 0.9]:
        time = fraction * lifetime
        rows.append(["d2_history", time, diameter(time) ** 2])
        rows.append(["mdot_history", time, mass_rate(time)])
    for r_over_radius in [1.0, 1.25, 1.5, 2.0, 3.0, 5.0, 10.0]:
        rows.append(["Y_profile", r_over_radius, mass_fraction(r_over_radius)])

    write_csv(
        ROOT / "data/PH-012/reference.csv",
        ["record", "time_or_r_over_R", "value"],
        rows,
    )

    times = linspace(0.0, lifetime, CURVE_POINTS)
    figure, (axis_d, axis_y) = plt.subplots(1, 2, figsize=(9.6, 4.3))
    axis_d.plot(times, [diameter(t) ** 2 * 1e6 for t in times], color="#1f77b4")
    axis_d.set_title("d2 history")
    axis_d.set_xlabel("time [s]")
    axis_d.set_ylabel("d^2 [mm^2]")
    axis_d.grid(True, color="0.88", linewidth=0.8)
    ratios = linspace(1.0, 10.0, CURVE_POINTS)
    axis_y.plot(ratios, [mass_fraction(r) for r in ratios], color="#d62728")
    axis_y.set_title("vapor mass fraction")
    axis_y.set_xlabel("r / R")
    axis_y.set_ylabel("Y")
    axis_y.grid(True, color="0.88", linewidth=0.8)
    figure.suptitle("PH-012 d2-law reference")
    figure.tight_layout()
    figure.savefig(ROOT / "figures/PH-012-reference.svg", format="svg")
    plt.close(figure)


def generate_ph013() -> None:
    plate_height = 0.1
    delta_t = 10.0
    rho_liquid = 958.4
    rho_vapor = 0.60
    mu_liquid = 2.82e-4
    k_liquid = 0.68
    h_fg = 2.257e6
    gravity = 9.81

    factor = (
        4.0
        * k_liquid
        * mu_liquid
        * delta_t
        / (gravity * rho_liquid * (rho_liquid - rho_vapor) * h_fg)
    )

    def thickness(x: float) -> float:
        return (factor * x) ** 0.25 if x > 0 else 0.0

    def heat_coefficient(x: float) -> float:
        return k_liquid / thickness(x)

    def mass_flow(x: float) -> float:
        return (
            gravity
            * rho_liquid
            * (rho_liquid - rho_vapor)
            * thickness(x) ** 3
            / (3.0 * mu_liquid)
        )

    mean_h = 4.0 / 3.0 * heat_coefficient(plate_height)
    mean_nu = mean_h * plate_height / k_liquid

    rows: list[list[object]] = [
        ["mean_h", mean_h, "", ""],
        ["mean_Nu_L", mean_nu, "", ""],
    ]
    for fraction in [0.05, 0.1, 0.25, 0.5, 0.75, 1.0]:
        x = fraction * plate_height
        rows.append(
            [
                "profile",
                x,
                thickness(x),
                4.0 * mass_flow(x) / mu_liquid,
            ]
        )

    write_csv(
        ROOT / "data/PH-013/reference.csv",
        ["record", "x_or_value", "film_thickness", "film_reynolds"],
        rows,
    )

    positions = linspace(1.0e-4 * plate_height, plate_height, CURVE_POINTS)
    figure, (axis_d, axis_h) = plt.subplots(1, 2, figsize=(9.6, 4.3))
    axis_d.plot(positions, [thickness(x) * 1e3 for x in positions], color="#1f77b4")
    axis_d.set_title("film thickness")
    axis_d.set_xlabel("x [m]")
    axis_d.set_ylabel("delta [mm]")
    axis_d.grid(True, color="0.88", linewidth=0.8)
    axis_h.plot(positions, [heat_coefficient(x) for x in positions], color="#d62728")
    axis_h.set_title("local heat transfer coefficient")
    axis_h.set_xlabel("x [m]")
    axis_h.set_ylabel("h [W/(m^2 K)]")
    axis_h.grid(True, color="0.88", linewidth=0.8)
    figure.suptitle("PH-013 Nusselt film condensation reference")
    figure.tight_layout()
    figure.savefig(ROOT / "figures/PH-013-reference.svg", format="svg")
    plt.close(figure)


def generate_ph014() -> None:
    rho_liquid = 200.0
    rho_vapor = 5.0
    mu_vapor = 0.005
    k_vapor = 1.0
    cp_vapor = 200.0
    h_fg = 1.0e4
    sigma = 0.1
    gravity = 9.81
    delta_t = 5.0

    delta_rho = rho_liquid - rho_vapor
    lambda_0 = math.sqrt(sigma / (gravity * delta_rho))
    lambda_c = 2.0 * math.pi * lambda_0
    lambda_d = math.sqrt(3.0) * lambda_c
    h_fg_prime = h_fg + 0.5 * cp_vapor * delta_t
    nu_berenson = 0.425 * (
        rho_vapor * delta_rho * gravity * h_fg_prime * lambda_0**3 / (k_vapor * mu_vapor * delta_t)
    ) ** 0.25
    h_berenson = nu_berenson * k_vapor / lambda_0
    grashof = rho_vapor * delta_rho * gravity * lambda_0**3 / mu_vapor**2
    jakob = cp_vapor * delta_t / h_fg

    write_csv(
        ROOT / "data/PH-014/reference.csv",
        ["quantity", "value"],
        [
            ["capillary_length_lambda0", lambda_0],
            ["critical_wavelength_lambda_c", lambda_c],
            ["most_dangerous_wavelength_lambda_d", lambda_d],
            ["grashof_number", grashof],
            ["vapor_jakob_number", jakob],
            ["berenson_mean_nusselt_lambda0", nu_berenson],
            ["berenson_heat_transfer_coefficient", h_berenson],
        ],
    )

    superheats = linspace(1.0, 25.0, CURVE_POINTS)
    values = [
        0.425
        * (
            rho_vapor
            * delta_rho
            * gravity
            * (h_fg + 0.5 * cp_vapor * dt)
            * lambda_0**3
            / (k_vapor * mu_vapor * dt)
        )
        ** 0.25
        for dt in superheats
    ]
    plt.figure(figsize=(7.2, 4.3))
    plt.plot(superheats, values, color="#1f77b4", label="Berenson mean Nu")
    plt.axvline(delta_t, color="0.6", linestyle=":", label="benchmark superheat")
    plt.legend()
    save_figure(
        ROOT / "figures/PH-014-reference.svg",
        "PH-014 film boiling Berenson anchor",
        "wall superheat",
        "mean Nusselt number (lambda0)",
    )



def generate_mt001() -> None:
    da_values = [0.0, 0.25, 1.0, 4.0, 16.0, 100.0]
    rows = [[da, 2 * (1 + math.sqrt(da))] for da in da_values]
    write_csv(ROOT / "data/MT-001/reference.csv", ["damkohler", "sherwood"], rows)

    radii = linspace(1.0, 6.0, CURVE_POINTS)
    plt.figure(figsize=(7.2, 4.3))
    for da in [0.0, 1.0, 16.0, 100.0]:
        profile = [math.exp(-math.sqrt(da) * (r - 1.0)) / r for r in radii]
        plt.plot(radii, profile, linewidth=2.0, label=f"Da = {da:g}")
    plt.legend()
    save_figure(
        ROOT / "figures/MT-001-reference.svg",
        "MT-001 reaction-diffusion outside a sphere",
        "r / R0",
        "C / Cs",
    )


def generate_mt002() -> None:
    da_values = [0.25, 1.0, 4.0, 16.0, 64.0, 100.0]
    rows = []
    for da in da_values:
        m = mp.sqrt(da)
        flux = 2 * mp.pi * m * mp.besselk(1, m) / mp.besselk(0, m)
        rows.append([da, float(flux)])
    write_csv(ROOT / "data/MT-002/reference.csv", ["damkohler", "uptake"], rows)

    sweep = [0.05 * 1.15**index for index in range(60)]
    fluxes = [
        float(2 * mp.pi * mp.sqrt(da) * mp.besselk(1, mp.sqrt(da)) / mp.besselk(0, mp.sqrt(da)))
        for da in sweep
    ]
    plt.figure(figsize=(7.2, 4.3))
    plt.plot(sweep, fluxes, color="#1f77b4", linewidth=2.2, label="F(Da)")
    plt.xscale("log")
    plt.legend()
    save_figure(
        ROOT / "figures/MT-002-reference.svg",
        "MT-002 reactive uptake outside a disk",
        "Da",
        "F / (D Cs)",
    )


def generate_mt003() -> None:
    fo_values = [0.001, 0.01, 0.1, 1.0, 10.0]
    rows = [[fo, 2 + 2 / math.sqrt(math.pi * fo)] for fo in fo_values]
    write_csv(ROOT / "data/MT-003/reference.csv", ["fourier", "sherwood"], rows)

    sweep = [0.001 * 1.2**index for index in range(55)]
    plt.figure(figsize=(7.2, 4.3))
    plt.plot(
        sweep,
        [2 + 2 / math.sqrt(math.pi * fo) for fo in sweep],
        color="#1f77b4",
        linewidth=2.2,
        label="Sh(Fo)",
    )
    plt.axhline(2.0, color="0.5", linewidth=1.2, label="Sh = 2")
    plt.xscale("log")
    plt.yscale("log")
    plt.legend()
    save_figure(
        ROOT / "figures/MT-003-reference.svg",
        "MT-003 unsteady diffusion to a sphere",
        "Fo",
        "Sh",
    )


def mt004_sherwood(fourier: float, damkohler: float) -> float:
    return float(
        2
        * (
            1
            + mp.sqrt(damkohler) * mp.erf(mp.sqrt(damkohler * fourier))
            + mp.e ** (-damkohler * fourier) / mp.sqrt(mp.pi * fourier)
        )
    )


def generate_mt004() -> None:
    rows = []
    for da in [0.0, 1.0, 10.0]:
        for fo in [0.001, 0.01, 0.1, 1.0, 10.0]:
            rows.append([da, fo, mt004_sherwood(fo, da)])
    write_csv(ROOT / "data/MT-004/reference.csv", ["damkohler", "fourier", "sherwood"], rows)

    sweep = [0.001 * 1.2**index for index in range(55)]
    plt.figure(figsize=(7.2, 4.3))
    for da in [0.0, 1.0, 10.0]:
        plt.plot(
            sweep,
            [mt004_sherwood(fo, da) for fo in sweep],
            linewidth=2.0,
            label=f"Da = {da:g}",
        )
        plt.axhline(2 * (1 + math.sqrt(da)), color="0.75", linewidth=1.0)
    plt.xscale("log")
    plt.yscale("log")
    plt.legend()
    save_figure(
        ROOT / "figures/MT-004-reference.svg",
        "MT-004 unsteady reaction-diffusion outside a sphere",
        "Fo",
        "Sh",
    )


def generate_mt005() -> None:
    das = [0.01, 0.1, 1.0, 10.0, 100.0]
    rows = [[da, 1 / (1 + da), 2 * da / (1 + da)] for da in das]
    write_csv(
        ROOT / "data/MT-005/reference.csv",
        ["surface_damkohler", "surface_concentration", "sherwood"],
        rows,
    )

    sweep = [0.01 * 1.2**index for index in range(56)]
    plt.figure(figsize=(7.2, 4.3))
    plt.plot(sweep, [2 * da / (1 + da) for da in sweep], linewidth=2.2, label="Sh_ov")
    plt.plot(sweep, [1 / (1 + da) for da in sweep], linewidth=2.2, label="Cs / Cinf")
    plt.axhline(2.0, color="0.5", linewidth=1.2, label="Sh = 2")
    plt.xscale("log")
    plt.legend()
    save_figure(
        ROOT / "figures/MT-005-reference.svg",
        "MT-005 first-order surface kinetics on a sphere",
        "Da_s",
        "Sh_ov, Cs / Cinf",
    )



def pellet_cylinder_eta(phi: float) -> float:
    return float(2 * mp.besseli(1, phi) / (phi * mp.besseli(0, phi)))


def pellet_sphere_eta(phi: float) -> float:
    return float(3 * (phi / mp.tanh(phi) - 1) / phi**2)


def generate_mt006() -> None:
    phis = [0.1, 0.5, 1.0, 2.0, 5.0, 10.0, 20.0]
    rows = [[phi, pellet_cylinder_eta(phi)] for phi in phis]
    write_csv(ROOT / "data/MT-006/reference.csv", ["thiele", "effectiveness"], rows)

    sweep = [0.05 * 1.15**index for index in range(60)]
    plt.figure(figsize=(7.2, 4.3))
    plt.plot(sweep, [pellet_cylinder_eta(phi) for phi in sweep], linewidth=2.2, label="eta(phi)")
    plt.plot(sweep, [min(1.0, 2 / phi) for phi in sweep], "--", color="0.5", linewidth=1.4, label="2 / phi")
    plt.xscale("log")
    plt.yscale("log")
    plt.legend()
    save_figure(
        ROOT / "figures/MT-006-reference.svg",
        "MT-006 isothermal pellet, cylinder",
        "phi",
        "eta",
    )


def generate_mt007() -> None:
    phis = [0.1, 0.5, 1.0, 2.0, 5.0, 10.0, 20.0]
    rows = [[phi, pellet_sphere_eta(phi)] for phi in phis]
    write_csv(ROOT / "data/MT-007/reference.csv", ["thiele", "effectiveness"], rows)

    sweep = [0.05 * 1.15**index for index in range(60)]
    plt.figure(figsize=(7.2, 4.3))
    plt.plot(sweep, [pellet_sphere_eta(phi) for phi in sweep], linewidth=2.2, label="eta(phi)")
    plt.plot(sweep, [min(1.0, 3 / phi) for phi in sweep], "--", color="0.5", linewidth=1.4, label="3 / phi")
    plt.xscale("log")
    plt.yscale("log")
    plt.legend()
    save_figure(
        ROOT / "figures/MT-007-reference.svg",
        "MT-007 isothermal pellet, sphere",
        "phi",
        "eta",
    )


def generate_mt008() -> None:
    rows = []
    for biot in [0.1, 1.0, 10.0, 100.0]:
        for phi in [0.1, 1.0, 5.0, 20.0]:
            eta = pellet_sphere_eta(phi)
            eta_ov = eta / (1 + phi**2 * eta / (3 * biot))
            surface = float(1 / (1 + (phi / mp.tanh(phi) - 1) / biot))
            rows.append([biot, phi, surface, eta_ov])
    write_csv(
        ROOT / "data/MT-008/reference.csv",
        ["biot", "thiele", "surface_concentration", "effectiveness_overall"],
        rows,
    )

    sweep = [0.05 * 1.15**index for index in range(60)]
    plt.figure(figsize=(7.2, 4.3))
    for biot in [0.1, 1.0, 10.0, 100.0]:
        values = [
            pellet_sphere_eta(phi) / (1 + phi**2 * pellet_sphere_eta(phi) / (3 * biot))
            for phi in sweep
        ]
        plt.plot(sweep, values, linewidth=2.0, label=f"Bi = {biot:g}")
    plt.plot(sweep, [pellet_sphere_eta(phi) for phi in sweep], "--", color="0.5", linewidth=1.4, label="Bi -> inf")
    plt.xscale("log")
    plt.yscale("log")
    plt.legend()
    save_figure(
        ROOT / "figures/MT-008-reference.svg",
        "MT-008 pellet with an external film",
        "phi",
        "eta_ov",
    )


def mt009_uptake(damkohler: float, henry: float) -> float:
    q = mp.sqrt(damkohler)
    return float(2 * mp.pi * henry * q * mp.besseli(1, q) / mp.besseli(0, q))


def generate_mt009() -> None:
    rows = []
    for henry in [1.0, 2.0, 4.0]:
        for da in [0.25, 1.0, 4.0, 16.0, 64.0]:
            rows.append([henry, da, mt009_uptake(da, henry)])
    write_csv(ROOT / "data/MT-009/reference.csv", ["henry", "damkohler", "uptake"], rows)

    sweep = [0.1 * 1.15**index for index in range(50)]
    plt.figure(figsize=(7.2, 4.3))
    for henry in [1.0, 2.0, 4.0]:
        plt.plot(sweep, [mt009_uptake(da, henry) for da in sweep], linewidth=2.0, label=f"lambda = {henry:g}")
    plt.xscale("log")
    plt.yscale("log")
    plt.legend()
    save_figure(
        ROOT / "figures/MT-009-reference.svg",
        "MT-009 reactive absorption into a droplet",
        "Da",
        "F / D1",
    )


def generate_mt010() -> None:
    lambda0 = float(mp.findroot(lambda value: mp.besselj(0, value), 2.4))
    sherwood = lambda0**2
    rows = [[da, lambda0, sherwood, sherwood + da] for da in [0.0, 1.0, 4.0, 16.0]]
    write_csv(
        ROOT / "data/MT-010/reference.csv",
        ["damkohler", "eigenvalue", "sherwood_infinity", "axial_decay_rate"],
        rows,
    )

    radii = linspace(0.0, 1.0, CURVE_POINTS)
    figure, axes = plt.subplots(1, 2, figsize=(9.6, 4.0))
    axes[0].plot(radii, [float(mp.besselj(0, lambda0 * r)) for r in radii], linewidth=2.2)
    axes[0].set_xlabel("r / R")
    axes[0].set_ylabel("J0(lambda0 r / R)")
    axes[0].grid(True, color="0.88", linewidth=0.8)
    das = linspace(0.0, 16.0, 65)
    axes[1].plot(das, [sherwood + da for da in das], linewidth=2.2, label="sigma_0")
    axes[1].plot(das, [sherwood for _ in das], "--", linewidth=1.8, label="Sh_inf")
    axes[1].set_xlabel("Da")
    axes[1].grid(True, color="0.88", linewidth=0.8)
    axes[1].legend()
    figure.suptitle("MT-010 plug-flow reactive Graetz problem")
    figure.tight_layout()
    figure.savefig(ROOT / "figures/MT-010-reference.svg", format="svg")
    plt.close(figure)



def ht001_interface_values(henry: float, ratio: float) -> tuple[float, float]:
    denominator = math.sqrt(ratio) + henry
    return henry / denominator, 1.0 / denominator


def generate_ht001() -> None:
    rows = []
    for ratio in [0.1, 1.0, 10.0]:
        for henry in [0.5, 1.0, 2.0, 5.0]:
            first, second = ht001_interface_values(henry, ratio)
            rows.append([ratio, henry, first, second])
    write_csv(
        ROOT / "data/HT-001/reference.csv",
        ["diffusivity_ratio", "henry", "interface_value_phase1", "interface_value_phase2"],
        rows,
    )

    sweep = [0.1 * 1.1**index for index in range(50)]
    plt.figure(figsize=(7.2, 4.3))
    for ratio in [0.1, 1.0, 10.0]:
        plt.plot(
            sweep,
            [ht001_interface_values(henry, ratio)[0] for henry in sweep],
            linewidth=2.0,
            label=f"D2/D1 = {ratio:g}",
        )
    plt.xscale("log")
    plt.legend()
    save_figure(
        ROOT / "figures/HT-001-reference.svg",
        "HT-001 planar partition between two half-spaces",
        "k",
        "C1 at the interface",
    )


def newman_mean(fourier: float, terms: int = 200) -> float:
    total = mp.mpf(0)
    for n in range(1, terms + 1):
        total += mp.e ** (-(n**2) * mp.pi**2 * fourier) / n**2
    return float(6 / mp.pi**2 * total)


def generate_ht002() -> None:
    fos = [0.001, 0.01, 0.05, 0.1, 0.2, 0.5, 1.0]
    rows = [[fo, newman_mean(fo)] for fo in fos]
    rows.append(["sherwood_asymptote", float(2 * mp.pi**2 / 3)])
    write_csv(ROOT / "data/HT-002/reference.csv", ["fourier", "mean_concentration"], rows)

    sweep = [0.001 * 1.15**index for index in range(55)]
    figure, axes = plt.subplots(1, 2, figsize=(9.6, 4.0))
    axes[0].plot(sweep, [newman_mean(fo) for fo in sweep], linewidth=2.2)
    axes[0].set_xscale("log")
    axes[0].set_xlabel("Fo")
    axes[0].set_ylabel("mean C / C0")
    axes[0].grid(True, color="0.88", linewidth=0.8)
    rates = []
    for fo in sweep:
        delta = fo * 1e-4
        rate = -(math.log(newman_mean(fo + delta)) - math.log(newman_mean(fo))) / delta
        rates.append(rate * 4 / 6)
    axes[1].plot(sweep, rates, linewidth=2.2, label="Sh_i(Fo)")
    axes[1].axhline(float(2 * mp.pi**2 / 3), color="0.5", linewidth=1.4, label="2 pi^2 / 3")
    axes[1].set_xscale("log")
    axes[1].set_xlabel("Fo")
    axes[1].set_ylim(0, 20)
    axes[1].grid(True, color="0.88", linewidth=0.8)
    axes[1].legend()
    figure.suptitle("HT-002 Newman internal transient in a stagnant drop")
    figure.tight_layout()
    figure.savefig(ROOT / "figures/HT-002-reference.svg", format="svg")
    plt.close(figure)


def generate_ht003() -> None:
    eigenvalue = 1.678
    sherwood = 32 * eigenvalue / 3
    rows = [
        ["eigenvalue_lambda1", eigenvalue],
        ["sherwood_asymptote", sherwood],
        ["decay_rate_over_D_per_d2", 64 * eigenvalue],
        ["newman_asymptote", float(2 * mp.pi**2 / 3)],
    ]
    write_csv(ROOT / "data/HT-003/reference.csv", ["quantity", "value"], rows)

    times = linspace(0.0, 0.08, CURVE_POINTS)
    plt.figure(figsize=(7.2, 4.3))
    plt.plot(
        times,
        [math.exp(-64 * eigenvalue * t / 4.0) for t in times],
        linewidth=2.2,
        label="Kronig-Brink, Sh_i = 17.90",
    )
    plt.plot(
        times,
        [newman_mean(t) for t in times],
        linewidth=2.2,
        label="Newman, Sh_i = 6.58",
    )
    plt.yscale("log")
    plt.legend()
    save_figure(
        ROOT / "figures/HT-003-reference.svg",
        "HT-003 Kronig-Brink circulating drop",
        "Fo",
        "mean C / C0",
    )


def ht004_flux(henry: float, ratio: float) -> float:
    return 1.0 / (1.0 + henry / ratio)


def generate_ht004() -> None:
    rows = []
    for ratio in [0.1, 1.0, 10.0]:
        for henry in [0.5, 1.0, 2.0, 5.0]:
            flux = ht004_flux(henry, ratio)
            rows.append([ratio, henry, flux, 1.0 - flux, (1.0 - flux) / henry])
    write_csv(
        ROOT / "data/HT-004/reference.csv",
        ["diffusivity_ratio", "henry", "flux", "interface_value_phase1", "interface_value_phase2"],
        rows,
    )

    sweep = [0.1 * 1.1**index for index in range(50)]
    plt.figure(figsize=(7.2, 4.3))
    for ratio in [0.1, 1.0, 10.0]:
        plt.plot(sweep, [ht004_flux(henry, ratio) for henry in sweep], linewidth=2.0, label=f"D2/D1 = {ratio:g}")
    plt.xscale("log")
    plt.legend()
    save_figure(
        ROOT / "figures/HT-004-reference.svg",
        "HT-004 steady composite slab with an interfacial partition",
        "k",
        "J L1 / (D1 Ca)",
    )



def generate_vc003() -> None:
    sigma0, diffusivity, speed = 0.05, 1e-4, 1.0
    rows = []
    for time in [0.0, 0.1, 0.25, 0.5, 1.0]:
        variance = sigma0**2 + 2 * diffusivity * time
        rows.append([time, variance, 1 / (2 * math.pi * variance), speed * time])
    write_csv(
        ROOT / "data/VC-003/reference.csv",
        ["time", "variance", "peak_amplitude", "centroid_x"],
        rows,
    )

    times = linspace(0.0, 1.0, CURVE_POINTS)
    figure, axes = plt.subplots(1, 2, figsize=(9.6, 4.0))
    axes[0].plot(
        times,
        [1 / (2 * math.pi * (sigma0**2 + 2 * diffusivity * t)) for t in times],
        linewidth=2.2,
    )
    axes[0].set_xlabel("t")
    axes[0].set_ylabel("peak amplitude")
    axes[0].grid(True, color="0.88", linewidth=0.8)
    axes[1].plot(times, [speed * t for t in times], linewidth=2.2)
    axes[1].set_xlabel("t")
    axes[1].set_ylabel("centroid x")
    axes[1].grid(True, color="0.88", linewidth=0.8)
    figure.suptitle("VC-003 advected Gaussian in a uniform flow")
    figure.tight_layout()
    figure.savefig(ROOT / "figures/VC-003-reference.svg", format="svg")
    plt.close(figure)


def vc004_moments(time: float, sigma0: float, diffusivity: float, shear: float):
    yy = sigma0**2 + 2 * diffusivity * time
    xy = shear * (sigma0**2 * time + diffusivity * time**2)
    xx = (
        sigma0**2
        + 2 * diffusivity * time
        + shear**2 * (sigma0**2 * time**2 + 2 * diffusivity * time**3 / 3)
    )
    return xx, yy, xy


def generate_vc004() -> None:
    sigma0, diffusivity, shear = 0.05, 1e-3, 1.0
    rows = []
    for time in [0.0, 0.25, 0.5, 1.0, 2.0]:
        xx, yy, xy = vc004_moments(time, sigma0, diffusivity, shear)
        dispersion = 2 * shear**2 * diffusivity * time**3 / 3
        rows.append([time, xx, yy, xy, dispersion])
    write_csv(
        ROOT / "data/VC-004/reference.csv",
        ["time", "sigma_xx", "sigma_yy", "sigma_xy", "shear_dispersion_term"],
        rows,
    )

    times = linspace(0.0, 2.0, CURVE_POINTS)
    plt.figure(figsize=(7.2, 4.3))
    plt.plot(times, [vc004_moments(t, sigma0, diffusivity, shear)[0] for t in times], linewidth=2.2, label="sigma_xx")
    plt.plot(times, [vc004_moments(t, sigma0, diffusivity, shear)[1] for t in times], linewidth=2.2, label="sigma_yy")
    plt.plot(times, [vc004_moments(t, sigma0, diffusivity, shear)[2] for t in times], linewidth=2.2, label="sigma_xy")
    plt.plot(
        times,
        [2 * shear**2 * diffusivity * t**3 / 3 for t in times],
        "--",
        color="0.4",
        linewidth=1.8,
        label="(2/3) D gamma^2 t^3",
    )
    plt.legend()
    save_figure(
        ROOT / "figures/VC-004-reference.svg",
        "VC-004 sheared Gaussian in a linear shear flow",
        "t",
        "second moments",
    )


def generate_vc005() -> None:
    rows = []
    for da in [1.0, 16.0, 100.0]:
        m = mp.sqrt(da)
        flux = float(2 * mp.pi * m * mp.besselk(1, m) / mp.besselk(0, m))
        for omega in [0.0, 1.0, 10.0, 100.0]:
            rows.append([da, omega, flux])
    write_csv(ROOT / "data/VC-005/reference.csv", ["damkohler", "rotation_rate", "uptake"], rows)

    omegas = linspace(0.0, 100.0, CURVE_POINTS)
    plt.figure(figsize=(7.2, 4.3))
    for da in [1.0, 16.0, 100.0]:
        m = mp.sqrt(da)
        flux = float(2 * mp.pi * m * mp.besselk(1, m) / mp.besselk(0, m))
        plt.plot(omegas, [flux for _ in omegas], linewidth=2.2, label=f"Da = {da:g}")
    plt.legend()
    save_figure(
        ROOT / "figures/VC-005-reference.svg",
        "VC-005 rotation invariance of the uptake by a reactive disk",
        "Omega",
        "F / (D Cs)",
    )


def generate_vc006() -> None:
    rows = [["additivity_residual_target", 0.0]]
    for outer in [2.0, 5.0, 10.0, 20.0, 50.0]:
        rows.append([f"shell_sherwood_Rout_over_R0_{outer:g}", 2 / (1 - 1 / outer)])
    rows.append(["shell_sherwood_infinite", 2.0])
    rows.append(["equal_volume_radius_over_box_side", (3 / (4 * math.pi)) ** (1 / 3)])
    write_csv(ROOT / "data/VC-006/reference.csv", ["quantity", "value"], rows)

    ratios = linspace(1.5, 50.0, CURVE_POINTS)
    plt.figure(figsize=(7.2, 4.3))
    plt.plot(ratios, [2 / (1 - 1 / ratio) for ratio in ratios], linewidth=2.2, label="Sh_e shell")
    plt.axhline(2.0, color="0.5", linewidth=1.4, label="Sh_e = 2")
    plt.xscale("log")
    plt.legend()
    save_figure(
        ROOT / "figures/VC-006-reference.svg",
        "VC-006 external Sherwood number in a finite domain",
        "Rout / R0",
        "Sh_e",
    )


GENERATORS = {
    "PH-001": generate_ph001,
    "PH-002": generate_ph002,
    "PH-003": generate_ph003,
    "PH-004": generate_ph004,
    "PH-005": generate_ph005,
    "PH-006": generate_ph006,
    "PH-007": generate_ph007,
    "PH-008": generate_ph008,
    "PH-009": generate_ph009,
    "PH-010": generate_ph010,
    "PH-011": generate_ph011,
    "PH-012": generate_ph012,
    "PH-013": generate_ph013,
    "PH-014": generate_ph014,
    "VC-001": generate_vc001,
    "VC-002": generate_vc002,
    "MT-001": generate_mt001,
    "MT-002": generate_mt002,
    "MT-003": generate_mt003,
    "MT-004": generate_mt004,
    "MT-005": generate_mt005,
    "MT-006": generate_mt006,
    "MT-007": generate_mt007,
    "MT-008": generate_mt008,
    "MT-009": generate_mt009,
    "MT-010": generate_mt010,
    "HT-001": generate_ht001,
    "HT-002": generate_ht002,
    "HT-003": generate_ht003,
    "HT-004": generate_ht004,
    "VC-003": generate_vc003,
    "VC-004": generate_vc004,
    "VC-005": generate_vc005,
    "VC-006": generate_vc006,
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate benchmark reference CSV files and SVG figures."
    )
    parser.add_argument(
        "cases",
        nargs="*",
        help="Case IDs to generate. Omit to generate all cases.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    cases = args.cases or sorted(GENERATORS)
    unknown_cases = sorted(set(cases) - set(GENERATORS))
    if unknown_cases:
        valid_cases = ", ".join(sorted(GENERATORS))
        raise SystemExit(
            f"unknown case ID(s): {', '.join(unknown_cases)}. "
            f"Valid case IDs: {valid_cases}"
        )
    for case_id in cases:
        GENERATORS[case_id]()
        print(f"generated {case_id}")


if __name__ == "__main__":
    main()
