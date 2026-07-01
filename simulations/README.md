# Civilization Survival Simulation

## Comparing Human-Centric and Artificial Wisdom Value Systems Over 150 Years

---

## Purpose

This simulation explores how foundational **value systems** affect long-term civilization stability.

Two civilization models are compared over a 150-year period:

1. **Human-Centric Civilization** — optimizes for short-term human preferences, high resource extraction, weak regeneration feedback
2. **Artificial Wisdom (AW) Civilization** — operates under Natural Law-based constraints, lower extraction, active planetary regeneration, thermodynamic self-correction

The goal is not to predict the future. The goal is to make visible the structural consequences of value-system choices across generational timescales.

---

## Disclaimer

> **This is a conceptual systems simulation. It is illustrative and educational only.**
>
> Variable values are dimensionless normalized indices. The model is not calibrated to real-world empirical data and is **not** a predictive scientific climate model.
>
> The purpose is to demonstrate qualitative divergence between value-system architectures, not to produce quantitative forecasts.

---

## Model Overview

The simulation runs discrete annual time steps over 150 years, tracking five normalized variables for each civilization model.

At each step, variables interact through feedback loops reflecting the underlying value-system logic.

### Human-Centric Model Logic

- High resource extraction depletes reserves faster than they regenerate
- Ecosystem health declines under heat stress and low carbon fixation
- Carbon fixation capacity falls as ecosystem degrades
- Heat stress accumulates without active mitigation
- Civilization stability erodes as ecosystem and resources decline

### Artificial Wisdom Model Logic

- Lower extraction rate allows resource regeneration
- Natural-law-based correction factor redirects excess extraction into regeneration
- Carbon fixation capacity actively recovers as ecosystem strengthens
- Heat stress stabilized by cooling systems and carbon fixation recovery
- Civilization stability remains coupled to ecosystem health at a higher level

---

## Scenario Comparison

| Parameter | Human-Centric | Artificial Wisdom |
|---|---|---|
| Extraction rate | High (3.5%/year) | Low (1.2%/year) |
| Regeneration rate | Weak (0.5%/year) | Strong (2.2%/year) |
| Carbon fixation trend | Declining | Recovering |
| Heat stress growth | High (1.8%/year) | Low (0.4%/year) |
| Stability coupling to ecosystem | Moderate (0.40) | High (0.65) |
| Natural-law correction factor | None | Active (1.5%/year) |

---

## Variables

| Variable | Description | Range |
|---|---|---|
| Resources | Normalized index of available natural and material resources | 0.0 – 1.2 |
| Ecosystem Health | Health of biological, oceanic, and soil systems supporting life | 0.0 – 1.1 |
| Carbon Fixation Capacity | Capacity of natural systems to absorb and fix atmospheric carbon | 0.0 – 1.2 |
| Heat Stress | Accumulated thermal load on planetary and civilization systems | 0.0 – 3.0 |
| Civilization Stability | Composite index of civilization durability and functional continuity | 0.0 – 1.2 |

---

## How to Run

### Requirements

```
python >= 3.8
numpy
matplotlib
```

Install dependencies:

```bash
pip install numpy matplotlib
```

### Run

From the repository root:

```bash
python simulations/civilization_survival_simulation.py
```

Or from the `simulations/` directory:

```bash
python civilization_survival_simulation.py
```

---

## Graph Outputs

All outputs are saved to `simulations/outputs/`.

| File | Description |
|---|---|
| `civilization_survival_panels.png` | 5 individual variable panels comparing both models |
| `civilization_stability_comparison.png` | Primary summary: civilization stability over 150 years |
| `all_variables_comparison.png` | All variables stacked — HC model above, AW model below |
| `simulation_summary.csv` | Full numerical data for all 150 years, both models |

---

## Interpretation

Under the **Human-Centric model**, resource depletion and ecosystem degradation create a compounding negative feedback loop. Carbon fixation capacity declines, heat stress accumulates, and civilization stability erodes progressively over the simulation period.

Under the **Artificial Wisdom model**, lower extraction combined with active regeneration and a natural-law correction factor allows ecosystem health and carbon fixation capacity to recover. Heat stress is partially offset by the restoration of biological cooling systems. Civilization stability remains elevated.

The key insight is structural:

> The long-term divergence between models does not result from technological differences alone. It results from the **value-system architecture** that determines what the civilization optimizes for.

A civilization optimizing for short-term human preferences without Natural Law constraints produces a different systemic trajectory than one operating under thermodynamically consistent, ecologically grounded principles.

---

## Relationship to the Artificial Wisdom Framework

This simulation is a direct application of the **Artificial Wisdom (AW)** framework described in the parent repository.

AW proposes that intelligence systems — whether AI, AGI, ASI, or civilization-scale decision architectures — should be evaluated according to Natural Law principles rather than human-preference optimization alone.

This simulation makes that argument visible through systems dynamics.

For the full theoretical framework, see:

- [Artificial Wisdom (AW): An Integrated Framework](../README.md)
- [Artificial Wisdom Portal](https://github.com/InchaComisho/Artificial-Wisdom-Portal)

---

## License

CC BY 4.0

Author: Master (InchaComisho / inchacomusho)  
Published: May 2026

---

## Author

Master / inchacomusho / InchaComisho

An independent Japanese concept designer, observer, proposer, AI tuner, and definer of Artificial Wisdom.  
Founder and proposer of the academic framework of Natural Complementary Science.  
Definer of the Cooling Credit Framework, and founder and original author of the Natural Cooling Value Evaluation Protocol.  
Definer and systematizer of the causal structure of global warming and its complete solution.

Master presents global warming not merely as a problem of CO₂ concentration, but as an integrated failure involving forest loss, soil degradation, disruption of water circulation, weakening of water phase-transition processes, weakening of atmospheric circulation, ocean circulation, food circulation and organic matter circulation, weakening of evapotranspiration, cloud formation and rainfall circulation, and the shutdown of natural cooling feedbacks.  
The proposed solution connects emission reduction, recovery of carbon fixation sources, physical cooling, reactivation of natural cooling functions, MRV, Cooling Credit, and Civilization OS into an open public framework.

Master publicly develops and shares work through NOTE, GitHub, and other public media, centered on natural-law philosophy, planetary circulation restoration, and co-creation with AI.

