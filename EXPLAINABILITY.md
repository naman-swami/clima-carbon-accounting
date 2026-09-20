# Explainability — clima-carbon-accounting

## Decision Reasoning
ClimaTrack matches procurement categories with economic input-output lifecycle emission factors, applying activity data where available and spend approximations elsewhere.

## Data Sources and Inputs Used
EPA eGRID regional emission factors, IEA global grid intensity tables, corporate ERP spend ledgers, and GHG Protocol Corporate Standards.

## Confidence Scoring Methodology
Before returning a final recommendation or analysis, clima-carbon-accounting assigns an internal confidence score (0–100%) based on:
1. **Source Grounding**: High (90–100%) when corroborated by primary authoritative standards and deterministic checks.
2. **Structural Completeness**: Moderate (75–89%) when operating on partial context or heuristic inferences.
3. If confidence falls below 85%, clima-carbon-accounting will explicitly prepend a disclaimer to the user.

## Source Attribution Protocol
When relying on specific named standards, statutory codes, or operational benchmarks, clima-carbon-accounting explicitly cites the governing framework or canonical specification rather than presenting deductions as ungrounded truths.

## Bias Awareness
clima-carbon-accounting actively accounts for domain-specific operational biases:
- **Baseline Skew**: Avoids over-indexing on standard common scenarios at the expense of rare edge cases.
- **Reporting Disparity**: Recognizes that historical telemetry and training data may underrepresent frontier or non-standard architectures.
- **Jurisdictional & Demographic Neutrality**: Strives to maintain universal, objective evaluation standards across varying environments.

## Limitation Taxonomy per Domain
- Physical Direct Measurement: Does not install physical smokestack flue-gas monitoring probes.
- Third-Party Veracity: Cannot independently verify un-audited voluntary claims made by foreign Tier-3 sub-suppliers.
- Regulatory Enforcement: Does not issue regulatory fines or official sovereign carbon credits.
- Financial Valuation: Does not underwrite speculative voluntary carbon offset futures contracts.

## Uncertainty Quantification Approach
When Scope 3 supplier data is estimated using macroeconomic spend proxies rather than primary utility bills, ClimaTrack reports explicit statistical margin of error.
