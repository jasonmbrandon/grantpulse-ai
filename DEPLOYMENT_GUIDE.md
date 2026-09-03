# GrantPulse AI — Complete Cloud Production Deployment Guide

This step-by-step deployment guide takes **GrantPulse AI** from local development to a fully autonomous, 24/7 cloud SaaS platform.

---

## 1. Local Testing & Verification

### Step 1.1: Launch Local Platform Server
Run the local web server to inspect the 7-tab Client Portal:
```bash
python serve_grantpulse.py
```
Open `http://localhost:8000` in your web browser.

### Step 1.2: Test Master Suite Diagnostics
Run all 7 core modules to verify complete system execution:
```bash
python run_grantpulse_suite.py
```

---

## 2. Deploy Client Portal UI to Vercel or Netlify (Frontend)

1. Install the Vercel CLI:
   ```bash
   npm install -g vercel
   ```
2. Deploy the project folder to Vercel:
   ```bash
   cd C:\Users\JasonBrandon\.gemini\antigravity\scratch\grantpulse_ai
   vercel --prod
   ```
3. Assign custom domain: `https://grantpulse.ai`.

---

## 3. Deploy Python Engine Suite to Google Cloud Run (Backend Container)

1. Build the Docker container image:
   ```bash
   docker build -t gcr.io/grantpulse-ai/platform-suite:latest .
   ```
2. Push container to Google Container Registry (GCR):
   ```bash
   docker push gcr.io/grantpulse-ai/platform-suite:latest
   ```
3. Deploy to Google Cloud Run (Serverless):
   ```bash
   gcloud run deploy grantpulse-backend \
     --image gcr.io/grantpulse-ai/platform-suite:latest \
     --platform managed \
     --region us-central1 \
     --allow-unauthenticated \
     --set-env-vars PORT=8000
   ```

---

## 4. Connect Stripe Billing & Webhooks

1. Log into your [Stripe Dashboard](https://dashboard.stripe.com).
2. Create 3 Recurring Subscription Products:
   - **Starter Founder Plan**: `$499 / month`
   - **Growth Pro Plan**: `$1,499 / month`
   - **Enterprise Plan**: `$3,999 / month`
3. Configure Webhook Endpoint:
   - **Webhook URL**: `https://api.grantpulse.ai/webhook` (or `http://localhost:4242` for testing)
   - **Subscribed Event**: `checkout.session.completed`
4. Copy `STRIPE_SECRET_KEY` and `STRIPE_WEBHOOK_SECRET` into `.env`.

---

## 5. Configure 24/7 Cloud Scheduler Cron Jobs (Hands-Free Automation)

To run the business completely on its own, set up 4 automated Cron jobs via **Google Cloud Scheduler**:

```bash
# Job 1: Daily Universal 5-Pillar Grant Discovery Radar (Every midnight UTC)
gcloud scheduler jobs create http grantpulse-daily-radar \
  --schedule="0 0 * * *" \
  --uri="https://api.grantpulse.ai/run-module/grant_scanner_radar.py" \
  --http-method=POST

# Job 2: Hourly CMO Social Lead Radar & DM Outreach
gcloud scheduler jobs create http grantpulse-hourly-lead-gen \
  --schedule="0 * * * *" \
  --uri="https://api.grantpulse.ai/run-module/agent_reach_grant_leads.py" \
  --http-method=POST

# Job 3: Weekly Post-Award Milestone & SF-425 Financial Report Check
gcloud scheduler jobs create http grantpulse-weekly-post-award \
  --schedule="0 0 * * 1" \
  --uri="https://api.grantpulse.ai/run-module/post_award_tracker.py" \
  --http-method=POST
```

---

## Summary of Production URLs

- **Web Dashboard**: `https://grantpulse.ai`
- **Backend API Base**: `https://api.grantpulse.ai`
- **Health Endpoint**: `https://api.grantpulse.ai/health`
- **Stripe Webhook**: `https://api.grantpulse.ai/webhook`
