import os
import pytest
from calculators.emissions_engine import CarbonEmissionsCalculator

def test_scope_1_combustion():
    s1 = {"diesel_liters": 1000.0, "natural_gas_kwh": 10000.0}
    res = CarbonEmissionsCalculator.calculate_footprint(s1, {}, {})
    # diesel: 2680 kg, gas: 1850 kg -> 4530 kg -> 4.53 mt
    assert res["scope_1_mt_co2e"] == 4.53
    assert res["total_emissions_mt_co2e"] == 4.53

def test_corporate_fixture_audit():
    import json
    data_file = os.path.join(os.path.dirname(__file__), "..", "fixtures", "esg_data", "corporate_activity_data.json")
    with open(data_file, "r") as f:
        data = json.load(f)
    res = CarbonEmissionsCalculator.calculate_footprint(
        data["scope_1_activities"],
        data["scope_2_activities"],
        data["scope_3_activities"]
    )
    assert res["total_emissions_mt_co2e"] > 100.0
    assert res["carbon_offset_cost_usd"] > 0
