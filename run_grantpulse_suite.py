import os
import sys
import json
import subprocess
from datetime import datetime

# Set encoding for Windows standard output safety
if hasattr(sys.stdout, 'reconfigure'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

PYTHON = sys.executable
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def run_suite():
    print("==========================================================================")
    print("⚡ GrantPulse AI — Complete 7-Module Production Platform Suite Launcher")
    print(f"Timestamp: {datetime.now().isoformat()}")
    print(f"Base Directory: {BASE_DIR}")
    print("==========================================================================\n")

    suite_modules = [
        {
            "name": "Multi-Agent Grant Writing Swarm (CrewAI + OpenAlex)",
            "script": "grantpulse_swarm.py",
            "expected_outputs": ["grant_proposal_output.json", "grant_proposal_document.md"]
        },
        {
            "name": "Universal 5-Pillar Grant Discovery Radar (Federal, State, Foundation, Corporate, Global)",
            "script": "grant_scanner_radar.py",
            "expected_outputs": ["continuous_grant_radar_output.json"]
        },
        {
            "name": "CMO Social Lead Generation Scanner (Agent-Reach Engine)",
            "script": "agent_reach_grant_leads.py",
            "expected_outputs": ["grant_leads_output.json"]
        },
        {
            "name": "Commercial Subscription Strategy & Financial ARR Engine",
            "script": "business_model_strategy.py",
            "expected_outputs": ["business_financial_model.json"]
        },
        {
            "name": "Administrative SAM.gov & Institutional Registration Checker",
            "script": "registration_compliance_checker.py",
            "expected_outputs": ["registration_compliance_output.json"]
        },
        {
            "name": "Mock NIH Study Section Reviewer Panel Simulator",
            "script": "grant_panel_simulator.py",
            "expected_outputs": ["mock_study_section_output.json", "mock_study_section_summary_statement.md"]
        },
        {
            "name": "Post-Award Compliance & Milestone Drawdown Tracker",
            "script": "post_award_tracker.py",
            "expected_outputs": ["post_award_tracking_output.json"]
        }
    ]

    diagnostics = []

    for mod in suite_modules:
        script_path = os.path.join(BASE_DIR, mod["script"])
        print(f"[*] Running Module: {mod['name']}...")
        start_time = datetime.now()
        
        res = subprocess.run([PYTHON, script_path], cwd=BASE_DIR, capture_output=True, text=True)
        duration = round((datetime.now() - start_time).total_seconds(), 2)
        
        status = "PASSED" if res.returncode == 0 else "FAILED"
        print(f"    Status: [{status}] in {duration}s")
        
        verified_files = []
        for out_file in mod["expected_outputs"]:
            out_path = os.path.join(BASE_DIR, out_file)
            exists = os.path.exists(out_path)
            size = os.path.getsize(out_path) if exists else 0
            verified_files.append({"file": out_file, "exists": exists, "size_bytes": size})
            print(f"    Output File '{out_file}': {'[EXISTS ' + str(size) + ' bytes]' if exists else '[MISSING]'}")

        diagnostics.append({
            "module": mod["name"],
            "script": mod["script"],
            "status": status,
            "duration_seconds": duration,
            "verified_outputs": verified_files
        })
        print("--------------------------------------------------------------------------\n")

    suite_summary = {
        "suite_name": "GrantPulse AI Complete Platform",
        "version": "2.0 Full Production",
        "timestamp": datetime.now().isoformat(),
        "total_modules": len(suite_modules),
        "all_passed": all(d["status"] == "PASSED" for d in diagnostics),
        "module_diagnostics": diagnostics
    }

    summary_file = os.path.join(BASE_DIR, "suite_diagnostic_summary.json")
    with open(summary_file, "w", encoding="utf-8") as f:
        json.dump(suite_summary, f, indent=2)

    print("==========================================================================")
    print("🚀 GrantPulse AI Full 7-Module Suite Execution Complete!")
    print(f"Diagnostic Summary Saved: {summary_file}")
    print("Full Production Client Dashboard Ready: index.html")
    print("==========================================================================")

if __name__ == "__main__":
    run_suite()
