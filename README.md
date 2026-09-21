# Clima Corporate Carbon Accounting Engine

[![OpenGAP](https://img.shields.io/badge/OpenGAP-0.1.0-blue.svg)](agent.yaml)
[![ESG](https://img.shields.io/badge/Domain-Carbon_Accounting_GHG-darkgreen.svg)](docs/ipcc_tier_methodology.md)
[![Protocol](https://img.shields.io/badge/Standard-GHG_Protocol_Corporate-teal.svg)](docs/ipcc_tier_methodology.md)
[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](requirements.txt)
[![CI](https://img.shields.io/badge/CI-Passing-brightgreen.svg)](.github/workflows/ci.yml)

An enterprise greenhouse gas accounting engine computing Scope 1, Scope 2, and Scope 3 carbon inventories in metric tons $\text{CO}_2\text{e}$ conforming to the GHG Protocol Corporate Standard.

```
                    ┌─────────────────────────┐
                    │ Corporate Activity Data │
                    │ (Diesel, KWh, Flights)  │
                    └────────────┬────────────┘
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │ calculators/emissions   │
                    └────────────┬────────────┘
                                 │
                 ┌───────────────┴───────────────┐
                 ▼                               ▼
      ┌─────────────────────┐         ┌─────────────────────┐
      │  Scope 1 & Scope 2  │         │  Scope 3 Upstream   │
      │  (Direct & Utility) │         │   (Business Travel) │
      └──────────┬──────────┘         └──────────┬──────────┘
                 │                               │
                 └───────────────┬───────────────┘
                                 ▼
                    ┌─────────────────────────┐
                    │ CSRD / SEC ESG Report   │
                    │ Total Metric Tons CO2e  │
                    └─────────────────────────┘
```

## Features

- **Multi-Scope Carbon Inventory**: Computes Scope 1 stationary/mobile, Scope 2 regional grid emissions, and Scope 3 flight mileage.
- **IPCC Tier 1 Emission Factors**: Incorporates standard EPA and European Environment Agency emission constants.
- **Corporate Activity Benchmark**: Comes pre-packaged with industrial corporate utility and flight activity fixtures.

## Directory Structure

```
clima-carbon-accounting/
├── agent.yaml                       # OpenGAP 0.1.0 Manifest
├── EXPLAINABILITY.md                # 7-checkpoint ESG carbon provenance
├── calculators/
│   └── emissions_engine.py          # Scope 1, 2, and 3 accounting engine
├── standards/
│   └── ghg_protocol_factors.yaml    # EPA / IPCC emission factors
├── fixtures/
│   └── esg_data/
│       └── corporate_activity_data.json # Benchmark corporate activity data
├── docs/
│   └── ipcc_tier_methodology.md     # GHG protocol standard reference
├── tests/
│   └── test_agent.py                # Carbon calculation test suite
├── account.py                          # Carbon accounting CLI
└── requirements.txt
```

## Quick Start

```bash
# Run carbon calculation tests
pytest tests/ -v

# Audit benchmark corporate activity
python account.py --demo
```
