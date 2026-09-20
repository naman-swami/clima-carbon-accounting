import pytest
from src.carbon_engine import CorporateCarbonAuditor

def test_emissions_aggregation():
    auditor = CorporateCarbonAuditor()
    res = auditor.calculate_corporate_footprint(10000, 100000, 50000)
    assert res["total_co2e_metric_tons"] > 0
    assert res["scope1_stationary_combustion_mt"] == 53.0
