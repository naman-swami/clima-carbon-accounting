# Clima Corporate Carbon Accounting Engine

> **GHG Protocol & ISO 14064-1 Compliant Multi-Scope Emissions Ledger**  
> Quantifying Scope 1 (Direct), Scope 2 (Grid Electricity), and Scope 3 (Supply Chain) Footprints.

---

### GHG Protocol Calculation Standards

Emissions calculations adhere to IPCC Sixth Assessment Report (AR6) Global Warming Potentials ($GWP_{100}$):

$$E = \sum_{i} \left( A_i \times EF_i \times \frac{GWP_i}{1000} \right) \quad [\text{Metric Tonnes } CO_2e]$$
Where $A_i$ represents activity volume (liters fuel, MWh power, passenger-km), and $EF_i$ represents the emission factor.

---

### Scope Breakdown & Verified Emission Factors

```
                           Enterprise Activity
                                   │
         ┌─────────────────────────┼─────────────────────────┐
         ▼                         ▼                         ▼
   [SCOPE 1: Direct]      [SCOPE 2: Electricity]     [SCOPE 3: Upstream]
   Stationary Fuel        US Grid: 0.386 t/MWh       Air Travel (Long-haul):
   Natural Gas:           EU Grid: 0.215 t/MWh       0.102 kg CO2e / p-km
   2.02 kg CO2e / m³
```

| Scope Classification | Activity Source | Default Factor ($EF$) | Reporting Unit |
| :--- | :--- | :--- | :--- |
| **Scope 1** | Diesel Fleet Combustion | $2.68$ | $\text{kg } CO_2e / \text{liter}$ |
| **Scope 1** | Natural Gas Boilers | $2.02$ | $\text{kg } CO_2e / \text{m}^3$ |
| **Scope 2** | Substation Power (US Avg) | $386.0$ | $\text{kg } CO_2e / \text{MWh}$ |
| **Scope 3** | Commercial Aviation | $0.102$ | $\text{kg } CO_2e / \text{passenger-km}$ |

---

### Running the Carbon Accounting Ledger

```bash
# Calculate corporate emissions ledger for benchmark fiscal quarter
python account.py --demo

# Execute ISO assurance test suite
pytest tests/ -v
```

Activity payloads, audit assurance methodology, and IPCC emission factor lookups are configured in [GHG_METHODOLOGY.md](GHG_METHODOLOGY.md) and `standards/ghg_protocol_factors.yaml`.
