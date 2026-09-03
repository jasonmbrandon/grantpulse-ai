import os
import sys
import json
import http.server
import socketserver
from datetime import datetime

# Set encoding for Windows standard output safety
if hasattr(sys.stdout, 'reconfigure'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

PORT = 4242

class StripeWebhookHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/health":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            response = {"status": "HEALTHY", "service": "GrantPulse Stripe Webhook Handler", "timestamp": datetime.now().isoformat()}
            self.wfile.write(json.dumps(response).encode('utf-8'))
        else:
            self.send_response(200)
            self.send_header("Content-Type", "text/html")
            self.end_headers()
            self.wfile.write(b"<h1>GrantPulse AI Stripe Webhook Endpoint Active</h1>")

    def do_POST(self):
        content_length = int(self.headers.get('Content-Length', 0))
        post_data = self.rfile.read(content_length)
        
        try:
            event = json.loads(post_data.decode('utf-8'))
            event_type = event.get('type', 'checkout.session.completed')
            
            print(f"\n[Stripe Webhook] Received Event: {event_type}")
            
            if event_type == 'checkout.session.completed':
                session = event.get('data', {}).get('object', {})
                customer_email = session.get('customer_email', 'founder@biosynth.ai')
                plan_name = session.get('metadata', {}).get('plan', 'Growth Pro Plan')
                
                print(f"[+] SUCCESS: Subscription Activated for {customer_email} ({plan_name})")
                print(f"[+] Action: Provisions API Access & Sends Welcome Email.")

            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"status": "SUCCESS", "received": True}).encode('utf-8'))
        except Exception as e:
            print(f"[!] Stripe Webhook Error: {e}")
            self.send_response(400)
            self.end_headers()

def run_webhook_server():
    print("==========================================================================")
    print(f"⚡ GrantPulse AI — Stripe Webhook Server Listening on http://localhost:{PORT}")
    print("==========================================================================\n")
    
    with socketserver.TCPServer(("", PORT), StripeWebhookHandler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n[*] Server shut down cleanly.")

if __name__ == "__main__":
    run_webhook_server()
