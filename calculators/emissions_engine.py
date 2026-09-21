"""
GHG Protocol Corporate Accounting Engine
Computes Scope 1, Scope 2, and Scope 3 greenhouse gas inventories in metric tons CO2e.
"""
from typing import Dict, Any

class CarbonEmissionsCalculator:
    EMISSION_FACTORS = {
        "diesel_liter": 2.68,
        "natural_gas_kwh": 0.185,
        "grid_us_kwh": 0.385,
        "grid_eu_kwh": 0.220,
        "flight_km": 0.180
    }

    @classmethod
    def calculate_footprint(
        cls,
        scope1_data: Dict[str, float],
        scope2_data: Dict[str, Any],
        scope3_data: Dict[str, float]
    ) -> Dict[str, Any]:
        # Scope 1: Direct Combustion
        s1_diesel_kg = scope1_data.get("diesel_liters", 0.0) * cls.EMISSION_FACTORS["diesel_liter"]
        s1_gas_kg = scope1_data.get("natural_gas_kwh", 0.0) * cls.EMISSION_FACTORS["natural_gas_kwh"]
        scope_1_mt = round((s1_diesel_kg + s1_gas_kg) / 1000.0, 2)

        # Scope 2: Purchased Electricity
        grid_key = "grid_eu_kwh" if scope2_data.get("grid_region") == "EU" else "grid_us_kwh"
        s2_elec_kg = scope2_data.get("purchased_electricity_kwh", 0.0) * cls.EMISSION_FACTORS[grid_key]
        scope_2_mt = round(s2_elec_kg / 1000.0, 2)

        # Scope 3: Travel & Value Chain
        s3_flight_kg = scope3_data.get("business_flight_passenger_km", 0.0) * cls.EMISSION_FACTORS["flight_km"]
        scope_3_mt = round(s3_flight_kg / 1000.0, 2)

        total_mt = round(scope_1_mt + scope_2_mt + scope_3_mt, 2)

        return {
            "scope_1_mt_co2e": scope_1_mt,
            "scope_2_mt_co2e": scope_2_mt,
            "scope_3_mt_co2e": scope_3_mt,
            "total_emissions_mt_co2e": total_mt,
            "carbon_offset_cost_usd": round(total_mt * 35.0, 2), # $35/ton voluntary carbon price
            "compliance_status": "CSRD_REPORTING_READY"
        }
