# ClimaTrack — Corporate Scope 1-3 GHG Carbon Accounting Auditor

[![OpenGAP Compliant](https://img.shields.io/badge/OpenGAP-0.1.0-blue.svg)](https://opengap.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

Automated GHG Protocol compliance agent calculating Scope 1, 2, and 3 emission factors, supply chain carbon intensity, and SEC climate disclosure reports.

## Domain Category
**Data & analytics**

## Architecture
- **OpenGAP Specification**: `0.1.0`
- **Role**: Chief Sustainability Officer & ESG Carbon Auditor
- **Primary Goal**: Standardize multi-facility energy invoices and procurement manifests into audited CO2-equivalent ledger entries following GHG Protocol standards.

## Skills Included
- **`scope12-combustion-audit`**: Computing stationary combustion emissions and market-based Scope 2 electricity grid emission factors (eGRID/IEA).
- **`scope3-spend-category-modeling`**: Applying EEIO spend-based and supplier-specific activity methodologies across all 15 GHG Protocol categories.
- **`sec-esg-disclosure-synthesis`**: Generating audited TCFD and ISSB S2 climate resilience financial disclosure schedules.

## Tools Schema
- **`calculate-scope-emissions`**: Convert fuel consumption, utility kWh, and refrigerant losses into metric tons of CO2 equivalent.
- **`audit-supplier-carbon-intensity`**: Evaluate tier-1 supplier carbon disclosures and identify high-abatement priority vendors.
- **`generate-ghg-audit-trail`**: Export cryptographic hash verification for baseline inventory restatements and offset retirement certificates.

## Explainability & Verification
Full explainability compliance under OpenGAP Checkpoint 2 is detailed in [EXPLAINABILITY.md](EXPLAINABILITY.md), covering:
- Decision Reasoning
- Data Sources and Inputs Used
- Confidence Scoring Methodology
- Source Attribution Protocol
- Bias Awareness
- Limitation Taxonomy per Domain
- Uncertainty Quantification Approach

## Multi-Framework Compatibility
Adapters and visa export configurations are included in `exports/`:
- Anthropic Claude (`claude-system-prompt.txt`)
- OpenAI Assistants (`openai-assistant.json`)
- LangChain (`langchain-agent.json`)
- CrewAI (`crewai-agent.json`)
- AutoGen (`autogen-agent.json`)

## License
MIT License
