import argparse
import json
import os
from calculators.emissions_engine import CarbonEmissionsCalculator

def main():
    parser = argparse.ArgumentParser(description="Clima Corporate Carbon Accounting CLI")
    parser.add_argument("--demo", action="store_true", help="Audit sample corporate GHG activity")
    args = parser.parse_args()

    data_file = os.path.join(os.path.dirname(__file__), "fixtures", "esg_data", "corporate_activity_data.json")

    if args.demo:
        with open(data_file, "r") as f:
            data = json.load(f)
        
        res = CarbonEmissionsCalculator.calculate_footprint(
            scope1_data=data["scope_1_activities"],
            scope2_data=data["scope_2_activities"],
            scope3_data=data["scope_3_activities"]
        )

        print("=== CLIMA CORPORATE CARBON ACCOUNTING INVENTORY ===\n")
        print(f"Company: {data['company_name']} | Reporting Year: {data['reporting_year']}")
        print(f"Scope 1 Direct Emissions: {res['scope_1_mt_co2e']} mt CO2e")
        print(f"Scope 2 Purchased Grid: {res['scope_2_mt_co2e']} mt CO2e")
        print(f"Scope 3 Value Chain / Travel: {res['scope_3_mt_co2e']} mt CO2e")
        print(f"TOTAL GHG EMISSIONS: {res['total_emissions_mt_co2e']} mt CO2e")
        print(f"Estimated Carbon Offset Value ($35/t): ${res['carbon_offset_cost_usd']:,.2f}")
        print(f"Reporting Status: {res['compliance_status']}\n")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
