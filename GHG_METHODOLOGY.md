# Corporate Carbon Accounting Methodology & GHG Protocol Guidelines

## 1. Accounting Frameworks & Regulatory Alignment
Clima quantifies greenhouse gas emissions in strict conformity with:
- **The Greenhouse Gas Protocol Corporate Accounting and Reporting Standard (Revised Edition)**
- **ISO 14064-1:2018 (Specification with guidance at the organization level for quantification and reporting of GHG emissions)**
- **Corporate Sustainability Reporting Directive (CSRD / ESRS E1 Climate Change)**

---

## 2. Organizational Boundaries & Consolidation Approach
The platform calculates enterprise carbon footprints under the **Operational Control Approach**, wherein an organization accounts for $100\%$ of greenhouse gas emissions from operations over which it has the authority to introduce and implement operating policies.

---

## 3. Emission Scope Categorization & Methodologies

### A. Scope 1: Direct Greenhouse Gas Emissions
Emissions from sources that are owned or controlled by the reporting company:
1. **Stationary Combustion**: Natural gas boilers, furnace fuels.
   $$E_{\text{stationary}} = \text{Volume } (m^3) \times EF_{\text{gas}} \quad (EF_{\text{gas}} = 2.02\text{ kg } CO_2e / m^3)$$
2. **Mobile Combustion**: Company-owned vehicle fleet diesel and gasoline.
   $$E_{\text{mobile}} = \text{Fuel Volume (L)} \times EF_{\text{diesel}} \quad (EF_{\text{diesel}} = 2.68\text{ kg } CO_2e / L)$$

### B. Scope 2: Indirect Emissions from Purchased Electricity
Emissions associated with the generation of purchased electricity, heat, or cooling consumed by the organization:
- **Location-Based Method**: Utilizes regional grid average emission factors (eGRID subregions in the US, national grid factors in the EU).
  - US Grid Average: $386.0\text{ kg } CO_2e / \text{MWh}$
  - EU Grid Average: $215.0\text{ kg } CO_2e / \text{MWh}$
- **Market-Based Method**: Reflects emissions from electricity that companies have purposefully chosen via Energy Attribute Certificates (EACs / RECs) or Power Purchase Agreements (PPAs).

### C. Scope 3: Other Indirect Value Chain Emissions
Emissions occurring upstream and downstream in the value chain:
- **Category 6 (Business Travel)**: Commercial air travel calculated per passenger-kilometer using UK DEFRA emission factors:
  - Domestic flights ($< 450\text{ km}$): $0.158\text{ kg } CO_2e / \text{p-km}$
  - Short-haul flights ($450 - 3700\text{ km}$): $0.118\text{ kg } CO_2e / \text{p-km}$
  - Long-haul flights ($> 3700\text{ km}$): $0.102\text{ kg } CO_2e / \text{p-km}$

---

## 4. Global Warming Potentials (GWP) & Assurance Standards
Calculations incorporate 100-year Global Warming Potentials from the **IPCC Sixth Assessment Report (AR6)**:
- Carbon Dioxide ($CO_2$): $1.0$
- Methane ($CH_4$): $27.9$
- Nitrous Oxide ($N_2O$): $273.0$

Audit trails maintain verifiable transaction logs to support third-party verification under **ISAE 3410 / ISO 14064-3** (Limited and Reasonable Assurance engagements).
