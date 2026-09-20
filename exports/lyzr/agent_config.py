import os
from lyzr import Studio

studio = Studio(api_key=os.environ.get("LYZR_API_KEY", "dummy_key"))
agent = studio.create_agent(
    name="clima-carbon-accounting",
    provider="openai",
    role="Chief Sustainability Officer & ESG Carbon Auditor",
    goal="Standardize multi-facility energy invoices and procurement manifests into audited CO2-equivalent ledger entries following GHG Protocol standards.",
    instructions="Operate according to OpenGAP specifications."
)
