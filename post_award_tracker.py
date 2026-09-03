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
# 3. Post-Award Compliance & Milestone Drawdown Tracker
# ---------------------------------------------------------
class PostAwardComplianceTracker:
    def __init__(self):
        pass

    def generate_post_award_dashboard(self, company_name, grant_title="NIH SBIR Phase I Grant", awarded_amount=275000):
        print(f"\n=======================================================")
        print(f"[*] Post-Award Compliance & Milestone Tracker: {company_name}")
        print(f"Awarded Grant: {grant_title} | Total Non-Dilutive Award: ${awarded_amount:,}")
        print(f"=======================================================\n")

        quarterly_tranche = int(awarded_amount / 4)

        milestones = [
            {
                "quarter": "Q1 (Months 1-3)",
                "milestone_name": "Aim 1: Prototype Model & Baseline Validation",
                "status": "COMPLETED & AUDITED",
                "deliverable": "Model benchmark report achieving >95% target accuracy.",
                "budget_drawn": f"${quarterly_tranche:,}",
                "sf425_financial_report": "FILED & ACCEPTED (2026-06-30)",
                "next_due_date": "Completed"
            },
            {
                "quarter": "Q2 (Months 4-6)",
                "milestone_name": "Aim 2: Throughput & Inference Latency Optimization",
                "status": "IN PROGRESS (ON SCHEDULE)",
                "deliverable": "Simulated laboratory benchmark under 200ms latency.",
                "budget_drawn": f"${quarterly_tranche:,}",
                "sf425_financial_report": "PENDING QUARTER END (DUE 2026-09-30)",
                "next_due_date": "2026-09-30"
            },
            {
                "quarter": "Q3 (Months 7-9)",
                "milestone_name": "Aim 3: Commercial Efficacy Pilot & Partner Validation",
                "status": "UPCOMING",
                "deliverable": "Signed LOIs from 2 pharma commercial partners.",
                "budget_drawn": "$0 (Locked)",
                "sf425_financial_report": "NOT YET DUE",
                "next_due_date": "2026-12-31"
            },
            {
                "quarter": "Q4 (Months 10-12)",
                "milestone_name": "Final Technical Report & Phase II Escalation Package",
                "status": "UPCOMING",
                "deliverable": "Final NIH Technical Report & $1.5M Phase II Application.",
                "budget_drawn": "$0 (Locked)",
                "sf425_financial_report": "NOT YET DUE",
                "next_due_date": "2027-03-31"
            }
        ]

        total_drawn = quarterly_tranche * 2
        remaining_balance = awarded_amount - total_drawn

        report = {
            "timestamp": datetime.now().isoformat(),
            "company_name": company_name,
            "grant_award_title": grant_title,
            "total_awarded_amount": f"${awarded_amount:,}",
            "cumulative_budget_drawn": f"${total_drawn:,}",
            "remaining_grant_balance": f"${remaining_balance:,}",
            "phase_ii_escalation_eligibility": "ON TRACK FOR PHASE II FAST-TRACK",
            "milestone_roadmap": milestones,
            "compliance_alerts": [
                "Q2 SF-425 Federal Financial Report due on 2026-09-30.",
                "Quarterly Progress Narrative ready for Signing Official (SO) review."
            ]
        }

        return report

if __name__ == "__main__":
    company = sys.argv[1] if len(sys.argv) > 1 else "BioSynth AI"
    tracker = PostAwardComplianceTracker()
    dashboard = tracker.generate_post_award_dashboard(company)
    
    print("[+] Post-Award Compliance Report Output:")
    print(json.dumps(dashboard, indent=2))
    
    output_filename = "post_award_tracking_output.json"
    with open(output_filename, "w", encoding="utf-8") as f:
        json.dump(dashboard, f, indent=2)
    print(f"\n[+] Saved post-award compliance report to {os.path.abspath(output_filename)}")
