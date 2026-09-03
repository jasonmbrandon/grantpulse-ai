import os
import sys
import json
from datetime import datetime

# Set encoding for Windows standard output safety
if hasattr(sys.stdout, 'reconfigure'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

# ---------------------------------------------------------
# Commercial Subscription Strategy & ARR Financial Model
# ---------------------------------------------------------
class GrantPulseBusinessModel:
    def __init__(self):
        self.pricing_tiers = {
            "starter": {
                "name": "Starter Founder Plan",
                "monthly_price": 499,
                "annual_price": 4900,
                "target_customer": "Early Seed Startups & Small Businesses (1-5 FTEs)",
                "grant_coverage": "Federal SBIR/STTR + State Level Grants",
                "proposal_builds_per_month": 3,
                "openalex_citations_limit": 25,
                "radar_alert_frequency": "Weekly",
                "success_fee_option": "5% on Won Grants"
            },
            "growth": {
                "name": "Growth Pro Plan",
                "monthly_price": 1499,
                "annual_price": 14500,
                "target_customer": "Growth Stage Tech & Biotech Companies (5-25 FTEs)",
                "grant_coverage": "Universal Grants (Federal, State, Foundation, Corporate, Global)",
                "proposal_builds_per_month": 10,
                "openalex_citations_limit": "Unlimited",
                "radar_alert_frequency": "Daily Real-Time",
                "success_fee_option": "3% on Won Grants"
            },
            "enterprise": {
                "name": "Enterprise & Lab Plan",
                "monthly_price": 3999,
                "annual_price": 38000,
                "target_customer": "University Labs, Accelerators & Institutional R&D",
                "grant_coverage": "Universal + Custom RFPs & Private Foundation Submissions",
                "proposal_builds_per_month": "Unlimited",
                "openalex_citations_limit": "Unlimited",
                "radar_alert_frequency": "Instant Real-Time",
                "success_fee_option": "0% Success Fee (Pure SaaS)"
            }
        }

    def calculate_12_month_projections(self):
        """Simulates 12-month ARR growth based on CMO lead radar conversion curves."""
        months = 12
        monthly_data = []
        
        starter_subscribers = 5
        growth_subscribers = 2
        enterprise_subscribers = 1
        
        cumulative_grant_wins_value = 0

        for m in range(1, months + 1):
            # Monthly Subscriber Acquisition Growth
            starter_subscribers += int(3 + (m * 1.5))
            growth_subscribers += int(1 + (m * 0.8))
            if m % 2 == 0:
                enterprise_subscribers += 1

            mrr_starter = starter_subscribers * 499
            mrr_growth = growth_subscribers * 1499
            mrr_enterprise = enterprise_subscribers * 3999
            
            total_mrr = mrr_starter + mrr_growth + mrr_enterprise
            arr = total_mrr * 12
            
            # Estimated Non-Dilutive Funding Secured for Clients ($275k per winning proposal)
            winning_grants_this_month = int(growth_subscribers * 0.4) + int(enterprise_subscribers * 0.8)
            monthly_grant_funding_secured = winning_grants_this_month * 275000
            cumulative_grant_wins_value += monthly_grant_funding_secured

            monthly_data.append({
                "month": f"Month {m}",
                "subscribers": {
                    "starter": starter_subscribers,
                    "growth": growth_subscribers,
                    "enterprise": enterprise_subscribers,
                    "total": starter_subscribers + growth_subscribers + enterprise_subscribers
                },
                "financials": {
                    "mrr": f"${total_mrr:,}",
                    "arr": f"${arr:,}",
                    "monthly_client_funding_won": f"${monthly_grant_funding_secured:,}"
                }
            })

        summary = {
            "timestamp": datetime.now().isoformat(),
            "business_name": "GrantPulse AI Commercial SaaS",
            "model_type": "Hybrid SaaS Subscription + Contingency Success Fee",
            "pricing_tiers": self.pricing_tiers,
            "unit_economics": {
                "average_cac": "$850 (CMO Social Lead Radar Acquisition)",
                "average_ltv": "$18,500 (14-Month Average Retention)",
                "ltv_to_cac_ratio": "21.7x"
            },
            "year_1_milestones": {
                "ending_mrr": monthly_data[-1]["financials"]["mrr"],
                "ending_arr": monthly_data[-1]["financials"]["arr"],
                "total_active_subscribers": monthly_data[-1]["subscribers"]["total"],
                "cumulative_client_funding_secured": f"${cumulative_grant_wins_value:,}"
            },
            "12_month_growth_trajectory": monthly_data
        }
        return summary

if __name__ == "__main__":
    model = GrantPulseBusinessModel()
    projections = model.calculate_12_month_projections()
    
    print("\n=======================================================")
    print("[*] GrantPulse AI Commercial Strategy & ARR Financial Model")
    print(f"Ending Year 1 ARR: {projections['year_1_milestones']['ending_arr']}")
    print(f"Total Client Non-Dilutive Funding Secured: {projections['year_1_milestones']['cumulative_client_funding_secured']}")
    print("=======================================================\n")
    
    output_filename = "business_financial_model.json"
    with open(output_filename, "w", encoding="utf-8") as f:
        json.dump(projections, f, indent=2)
    print(f"[+] Saved business financial model to {os.path.abspath(output_filename)}")
