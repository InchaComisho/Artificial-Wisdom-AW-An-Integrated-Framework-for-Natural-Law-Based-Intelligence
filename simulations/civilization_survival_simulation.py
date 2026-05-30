"""
Civilization Survival Simulation
=================================
Conceptual systems simulation comparing two value systems over 150 years:
  1. Human-Centric Civilization
  2. Artificial Wisdom (AW) Civilization

This is an illustrative model, NOT a predictive scientific climate model.
The purpose is to visualize how foundational value systems affect long-term
civilization stability through resource flows, ecosystem health, carbon
fixation capacity, heat stress, and overall civilization stability.

Variables are dimensionless normalized indices (0.0 – 1.0+ scale) chosen
to demonstrate qualitative divergence, not quantitative prediction.

Author: Master (InchaComisho / inchacomusho)
License: CC BY-SA 4.0
"""

import os
import numpy as np
import matplotlib
matplotlib.use("Agg")  # headless rendering — no display required
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import csv

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

YEARS = 150
T = np.arange(YEARS)
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "outputs")
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ---------------------------------------------------------------------------
# Model parameters
# ---------------------------------------------------------------------------

# Human-Centric model parameters
HC = {
    "extraction_rate":       0.035,   # annual resource depletion fraction
    "regen_rate":            0.005,   # ecosystem recovery rate
    "carbon_fix_growth":    -0.010,   # carbon fixation capacity change/year
    "heat_growth":           0.018,   # heat stress accumulation/year
    "stability_sensitivity": 0.40,    # how strongly ecosystem drives stability
}

# Artificial Wisdom model parameters
AW = {
    "extraction_rate":       0.012,   # lower extraction due to circular design
    "regen_rate":            0.022,   # stronger regeneration from NCS principles
    "carbon_fix_growth":     0.008,   # carbon fixation actively restored
    "heat_growth":           0.004,   # heat stabilized via planetary cooling
    "stability_sensitivity": 0.65,    # higher coupling to ecosystem health
    "correction_factor":     0.015,   # natural-law-based self-correction per year
}

# ---------------------------------------------------------------------------
# Simulation
# ---------------------------------------------------------------------------

def simulate_hc():
    """Human-Centric Civilization trajectory."""
    resources        = np.zeros(YEARS)
    ecosystem        = np.zeros(YEARS)
    carbon_fix       = np.zeros(YEARS)
    heat_stress      = np.zeros(YEARS)
    stability        = np.zeros(YEARS)

    resources[0]   = 1.0
    ecosystem[0]   = 1.0
    carbon_fix[0]  = 1.0
    heat_stress[0] = 0.1
    stability[0]   = 1.0

    p = HC
    for t in range(1, YEARS):
        r = resources[t-1]
        e = ecosystem[t-1]
        c = carbon_fix[t-1]
        h = heat_stress[t-1]

        # Resources deplete at extraction rate, partially restored by ecosystem
        resources[t] = max(0.0, r - p["extraction_rate"] * r + p["regen_rate"] * e * r)

        # Ecosystem health degrades under heat stress and low carbon fixation
        eco_pressure = 0.012 * h + 0.008 * (1.0 - c)
        ecosystem[t] = max(0.0, e - eco_pressure + p["regen_rate"] * e * (1 - e / 1.2))

        # Carbon fixation declines as ecosystem degrades
        carbon_fix[t] = max(0.0, c + p["carbon_fix_growth"] * (1.0 - e))

        # Heat stress accumulates; weakened carbon fixation amplifies it
        carbon_feedback = 0.006 * max(0.0, 1.0 - c)
        heat_stress[t] = min(3.0, h + p["heat_growth"] + carbon_feedback)

        # Civilization stability driven by resource availability and ecosystem health
        stability[t] = max(0.0,
            p["stability_sensitivity"] * ecosystem[t]
            + (1 - p["stability_sensitivity"]) * resources[t]
            - 0.05 * heat_stress[t]
        )

    return resources, ecosystem, carbon_fix, heat_stress, stability


def simulate_aw():
    """Artificial Wisdom Civilization trajectory."""
    resources        = np.zeros(YEARS)
    ecosystem        = np.zeros(YEARS)
    carbon_fix       = np.zeros(YEARS)
    heat_stress      = np.zeros(YEARS)
    stability        = np.zeros(YEARS)

    resources[0]   = 1.0
    ecosystem[0]   = 1.0
    carbon_fix[0]  = 1.0
    heat_stress[0] = 0.1
    stability[0]   = 1.0

    p = AW
    for t in range(1, YEARS):
        r = resources[t-1]
        e = ecosystem[t-1]
        c = carbon_fix[t-1]
        h = heat_stress[t-1]

        # Natural-law correction: AW redirects excess extraction back into regen
        correction = p["correction_factor"] * max(0.0, 1.0 - e)

        # Resources: lower extraction, stronger regeneration via NCS principles
        resources[t] = min(1.2,
            r - p["extraction_rate"] * r
            + p["regen_rate"] * e * (1 - r / 1.2)
            + correction * r
        )

        # Ecosystem: actively restored; heat impact dampened
        eco_pressure = 0.004 * h + 0.002 * max(0.0, 1.0 - c)
        ecosystem[t] = min(1.1,
            e - eco_pressure
            + p["regen_rate"] * (1 - e / 1.1)
            + correction
        )

        # Carbon fixation recovers as ecosystem strengthens
        carbon_fix[t] = min(1.2, c + p["carbon_fix_growth"] * ecosystem[t])

        # Heat stress stabilized by cooling technologies and carbon fixation
        heat_sink = 0.010 * min(1.0, c)
        heat_stress[t] = max(0.05, h + p["heat_growth"] - heat_sink)

        # Stability strongly coupled to ecosystem and carbon fixation
        stability[t] = min(1.2,
            p["stability_sensitivity"] * ecosystem[t]
            + (1 - p["stability_sensitivity"]) * resources[t]
            - 0.02 * heat_stress[t]
            + 0.01 * carbon_fix[t]
        )

    return resources, ecosystem, carbon_fix, heat_stress, stability


# ---------------------------------------------------------------------------
# Run both scenarios
# ---------------------------------------------------------------------------

hc_res, hc_eco, hc_cfx, hc_heat, hc_stab = simulate_hc()
aw_res, aw_eco, aw_cfx, aw_heat, aw_stab = simulate_aw()

variables = [
    ("Resources",               hc_res,  aw_res,  "tab:orange",  "tab:blue"),
    ("Ecosystem Health",        hc_eco,  aw_eco,  "tab:red",     "tab:green"),
    ("Carbon Fixation Capacity",hc_cfx,  aw_cfx,  "saddlebrown", "seagreen"),
    ("Heat Stress",             hc_heat, aw_heat, "firebrick",   "steelblue"),
    ("Civilization Stability",  hc_stab, aw_stab, "darkred",     "darkblue"),
]

# ---------------------------------------------------------------------------
# Plot 1: Individual variable panels (5 subplots)
# ---------------------------------------------------------------------------

fig, axes = plt.subplots(3, 2, figsize=(14, 16))
fig.suptitle(
    "Civilization Survival Simulation\n"
    "Human-Centric vs Artificial Wisdom Value Systems (150 Years)",
    fontsize=15, fontweight="bold", y=0.98
)

ax_flat = axes.flatten()
for i, (label, hc_data, aw_data, hc_color, aw_color) in enumerate(variables):
    ax = ax_flat[i]
    ax.plot(T, hc_data, color=hc_color, linewidth=2.0,
            label="Human-Centric", linestyle="--")
    ax.plot(T, aw_data, color=aw_color, linewidth=2.0,
            label="Artificial Wisdom")
    ax.set_title(label, fontsize=12, fontweight="bold")
    ax.set_xlabel("Year", fontsize=10)
    ax.set_ylabel("Index", fontsize=10)
    ax.legend(fontsize=9)
    ax.grid(True, alpha=0.3)
    ax.set_xlim(0, YEARS - 1)

# Hide unused subplot (6th panel used for a disclaimer note)
ax_note = ax_flat[5]
ax_note.axis("off")
ax_note.text(
    0.5, 0.5,
    "DISCLAIMER\n\n"
    "This is a conceptual systems simulation.\n"
    "It is illustrative and educational only.\n"
    "It is NOT a predictive scientific climate model.\n\n"
    "Variable values are dimensionless normalized indices\n"
    "designed to show qualitative divergence between\n"
    "value-system architectures, not quantitative outcomes.",
    transform=ax_note.transAxes,
    ha="center", va="center",
    fontsize=9.5,
    bbox=dict(boxstyle="round,pad=0.8", facecolor="#f0f0f0", edgecolor="gray"),
)

plt.tight_layout(rect=[0, 0, 1, 0.97])
panel_path = os.path.join(OUTPUT_DIR, "civilization_survival_panels.png")
plt.savefig(panel_path, dpi=150, bbox_inches="tight")
plt.close()
print(f"Saved: {panel_path}")

# ---------------------------------------------------------------------------
# Plot 2: Civilization Stability overlay (primary summary chart)
# ---------------------------------------------------------------------------

fig2, ax2 = plt.subplots(figsize=(12, 6))
ax2.fill_between(T, hc_stab, alpha=0.15, color="darkred")
ax2.fill_between(T, aw_stab, alpha=0.15, color="darkblue")
ax2.plot(T, hc_stab, color="darkred", linewidth=2.5,
         linestyle="--", label="Human-Centric Civilization")
ax2.plot(T, aw_stab, color="darkblue", linewidth=2.5,
         label="Artificial Wisdom Civilization")
ax2.set_title(
    "Civilization Stability Over 150 Years\nHuman-Centric vs Artificial Wisdom",
    fontsize=13, fontweight="bold"
)
ax2.set_xlabel("Year", fontsize=11)
ax2.set_ylabel("Stability Index", fontsize=11)
ax2.legend(fontsize=11)
ax2.grid(True, alpha=0.3)
ax2.set_xlim(0, YEARS - 1)
ax2.text(
    0.02, 0.04,
    "Conceptual simulation — not a predictive model",
    transform=ax2.transAxes, fontsize=8, color="gray", style="italic"
)

plt.tight_layout()
stability_path = os.path.join(OUTPUT_DIR, "civilization_stability_comparison.png")
plt.savefig(stability_path, dpi=150, bbox_inches="tight")
plt.close()
print(f"Saved: {stability_path}")

# ---------------------------------------------------------------------------
# Plot 3: All variables stacked comparison
# ---------------------------------------------------------------------------

fig3 = plt.figure(figsize=(14, 10))
gs = gridspec.GridSpec(2, 1, hspace=0.45)
ax_top = fig3.add_subplot(gs[0])
ax_bot = fig3.add_subplot(gs[1])

colors_hc = ["tab:orange", "tab:red",   "saddlebrown", "firebrick",  "darkred"]
colors_aw = ["tab:blue",   "tab:green", "seagreen",    "steelblue",  "darkblue"]
labels_short = ["Resources", "Ecosystem", "Carbon Fix.", "Heat Stress", "Stability"]

for (label, hc_d, aw_d, hc_c, aw_c), ls in zip(variables, labels_short):
    ax_top.plot(T, hc_d, color=hc_c, linewidth=1.8, linestyle="--", label=f"HC: {ls}")
    ax_bot.plot(T, aw_d, color=aw_c, linewidth=1.8,               label=f"AW: {ls}")

ax_top.set_title("Human-Centric Civilization — All Variables", fontsize=11, fontweight="bold")
ax_bot.set_title("Artificial Wisdom Civilization — All Variables", fontsize=11, fontweight="bold")
for ax in (ax_top, ax_bot):
    ax.set_xlabel("Year", fontsize=10)
    ax.set_ylabel("Index", fontsize=10)
    ax.legend(fontsize=8, loc="upper right", ncol=2)
    ax.grid(True, alpha=0.3)
    ax.set_xlim(0, YEARS - 1)

fig3.suptitle(
    "All Variables: Human-Centric vs Artificial Wisdom (150 Years)",
    fontsize=13, fontweight="bold"
)
stacked_path = os.path.join(OUTPUT_DIR, "all_variables_comparison.png")
plt.savefig(stacked_path, dpi=150, bbox_inches="tight")
plt.close()
print(f"Saved: {stacked_path}")

# ---------------------------------------------------------------------------
# CSV Summary
# ---------------------------------------------------------------------------

csv_path = os.path.join(OUTPUT_DIR, "simulation_summary.csv")
header = [
    "Year",
    "HC_Resources", "AW_Resources",
    "HC_Ecosystem", "AW_Ecosystem",
    "HC_CarbonFix", "AW_CarbonFix",
    "HC_HeatStress", "AW_HeatStress",
    "HC_Stability", "AW_Stability",
]

with open(csv_path, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(header)
    for t in range(YEARS):
        writer.writerow([
            t,
            round(hc_res[t], 4),  round(aw_res[t], 4),
            round(hc_eco[t], 4),  round(aw_eco[t], 4),
            round(hc_cfx[t], 4),  round(aw_cfx[t], 4),
            round(hc_heat[t], 4), round(aw_heat[t], 4),
            round(hc_stab[t], 4), round(aw_stab[t], 4),
        ])

print(f"Saved: {csv_path}")
print("\nSimulation complete.")
print(f"  HC final stability : {hc_stab[-1]:.4f}")
print(f"  AW final stability : {aw_stab[-1]:.4f}")
