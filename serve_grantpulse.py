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

PORT = int(os.environ.get("PORT", 8000))
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

class GrantPulseHTTPHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=BASE_DIR, **kwargs)

    def do_GET(self):
        if self.path == "/health":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            health_status = {
                "status": "HEALTHY",
                "app": "GrantPulse AI Platform",
                "version": "2.0 Full Production",
                "timestamp": datetime.now().isoformat(),
                "modules_active": 7
            }
            self.wfile.write(json.dumps(health_status).encode('utf-8'))
        else:
            super().do_GET()

def start_server():
    print("==========================================================================")
    print("⚡ GrantPulse AI — Commercial SaaS Platform Server")
    print(f"Server Running At: http://localhost:{PORT}")
    print(f"Health Endpoint: http://localhost:{PORT}/health")
    print(f"Client Dashboard: http://localhost:{PORT}/index.html")
    print("==========================================================================\n")

    with socketserver.TCPServer(("", PORT), GrantPulseHTTPHandler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n[*] GrantPulse Server stopped cleanly.")

if __name__ == "__main__":
    start_server()
