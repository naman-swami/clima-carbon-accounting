import json
import argparse
from src.carbon_engine import CorporateCarbonAuditor

def main():
    parser = argparse.ArgumentParser(description="Clima Carbon Accounting CLI")
    parser.add_argument("--demo", action="store_true", help="Run simulated corporate GHG emissions footprint audit")
    args = parser.parse_args()

    auditor = CorporateCarbonAuditor()
    report = auditor.calculate_corporate_footprint(natural_gas_therms=45000, grid_electricity_kwh=1200000, supply_chain_spend_usd=3500000)
    print("="*60)
    print(" CLIMATRACK CORPORATE GHG EMISSIONS AUDIT REPORT")
    print("="*60)
    print(json.dumps(report, indent=2))
    print("="*60)

if __name__ == "__main__":
    main()
