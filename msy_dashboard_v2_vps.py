#!/usr/bin/env python3
import os
from http.server import BaseHTTPRequestHandler, HTTPServer
from datetime import datetime

class MSYHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/api/status':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            status = {
                "president": "IBK",
                "msy_int": "OPÉRATIONNEL",
                "vps": "157.173.119.36",
                "timestamp": datetime.utcnow().isoformat() + "Z",
                "modules": 2500,
                "status": "EN LIGNE"
            }
            self.wfile.write(json.dumps(status).encode())
        else:
            self.send_response(404)
            self.end_headers()

import json
if __name__ == '__main__':
    server = HTTPServer(('0.0.0.0', 8000), MSYHandler)
    print("MSY API V2 démarrée sur :8000")
    server.serve_forever()
