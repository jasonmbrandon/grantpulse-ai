import os
import sys
import json
import random
from datetime import datetime

# Set encoding for Windows standard output safety
if hasattr(sys.stdout, 'reconfigure'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

class MonthlyFundSelectorEngine:
    def __init__(self):
        self.award_amount = "$10,000"
        
    def run_monthly_draw(self, candidate_subscribers=None):
        if not candidate_subscribers:
            candidate_subscribers = [
                {
                    "company_name": "BioSynth AI",
                    "plan": "Growth Pro ($1,499/mo)",
                    "domain": "AI protein folding for targeted drug discovery",
                    "sam_cleared": True,
                    "impact_score": 19,
                    "entries_weighted": 3
                },
                {
                    "company_name": "NeuroGen Technologies",
                    "plan": "Starter Founder ($499/mo)",
                    "domain": "AI EEG diagnostic headset",
                    "sam_cleared": True,
                    "impact_score": 21,
                    "entries_weighted": 2
                },
                {
                    "company_name": "Quantum CleanEnergy Inc",
                    "plan": "Growth Pro ($1,499/mo)",
                    "domain": "Quantum carbon capture materials",
                    "sam_cleared": True,
                    "impact_score": 18,
                    "entries_weighted": 3
                },
                {
                    "company_name": "OmniCell Therapeutics",
                    "plan": "Enterprise ($3,999/mo)",
                    "domain": "High-throughput cell therapy screening",
                    "sam_cleared": True,
                    "impact_score": 16,
                    "entries_weighted": 5
                }
            ]
            
        print("==========================================================================")
        print("⚡ GrantPulse AI — Automated Monthly $10,000 Founder Grant Selection Draw")
        print("==========================================================================")
        print(f"[*] Candidate Pool Size: {len(candidate_subscribers)} Active Subscribers")
        
        # Weighted random selection based on subscription tier & readiness
        weighted_pool = []
        for sub in candidate_subscribers:
            weights = sub.get("entries_weighted", 1)
            weighted_pool.extend([sub] * weights)
            
        winner = random.choice(weighted_pool)
        
        print(f"\n[+] WINNER SELECTED FOR THIS MONTH: {winner['company_name']}")
        print(f"    Subscription Tier: {winner['plan']}")
        print(f"    Domain: {winner['domain']}")
        print(f"    Award Amount: {self.award_amount} Non-Dilutive Cash Grant")
        
        # Generate formal award certificate / JSON
        award_package = {
            "award_id": f"GP-FUND-{datetime.now().strftime('%Y%m')}-001",
            "timestamp": datetime.now().isoformat(),
            "award_amount": self.award_amount,
            "winner_company": winner["company_name"],
            "subscription_plan": winner["plan"],
            "domain_focus": winner["domain"],
            "disbursement_status": "READY FOR DIRECT WIRE DISBURSEMENT",
            "full_swarm_package_included": True
        }
        
        # Save JSON output
        output_json = "monthly_grant_winner_output.json"
        with open(output_json, "w", encoding="utf-8") as f:
            json.dump(award_package, f, indent=2)
            
        # Save Award Letter Markdown
        output_md = "monthly_grant_award_letter.md"
        with open(output_md, "w", encoding="utf-8") as f:
            f.write(f"""# Official GrantPulse AI Founder Grant Award Letter

**Award ID**: {award_package['award_id']}  
**Date**: {datetime.now().strftime('%B %d, %Y')}  
**Grant Amount**: {self.award_amount} (Non-Dilutive Cash Award)  

---

### Congratulations to **{winner['company_name']}**!

GrantPulse AI Inc. is pleased to formally notify **{winner['company_name']}** that your company has been selected as the official recipient of **The Monthly GrantPulse $10,000 Founder Grant**.

#### Award Details:
- **Recipient Entity**: {winner['company_name']} ({winner['plan']})
- **Technical Focus**: {winner['domain']}
- **Award Structure**: 100% Non-Dilutive Grant ($0 Equity Dilution)
- **Disbursement Method**: Direct ACH / Bank Wire Transfer to Recipient Entity

In addition to your $10,000 non-dilutive cash grant, GrantPulse AI's 3-agent swarm has executed a full Phase I proposal build and OpenAlex scientific literature search for your technology.

*Issued by GrantPulse AI Inc. Selection Committee*
""")
            
        print(f"\n[+] Saved Winner Output to: {os.path.abspath(output_json)}")
        print(f"[+] Saved Winner Award Letter to: {os.path.abspath(output_md)}")
        return award_package

if __name__ == "__main__":
    engine = MonthlyFundSelectorEngine()
    engine.run_monthly_draw()
