from prometheus_client import generate_latest, start_http_server, Counter
from http.server import HTTPServer, BaseHTTPRequestHandler
import random

SUCCESS_COUNT = Counter('another_endpoint_success_total', 'Successful /another_endpoint hits')
FAILURE_COUNT = Counter('another_endpoint_failure_total', 'Failed /another_endpoint hits')

def start_metrics_server(port=8000):
    print(f"📊 Prometheus metrics server started on http://localhost:{port}/")
    start_http_server(port)

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/api/status':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'OK')
        elif self.path == '/another_endpoint':
            if random.random() < 0.2:
                FAILURE_COUNT.inc()
                self.send_response(500)
                self.end_headers()
                self.wfile.write(b'Internal Server Error')
            else:
                SUCCESS_COUNT.inc()
                self.send_response(200)
                self.end_headers()
                self.wfile.write(b'Another Endpoint is OK')
        else:
            self.send_response(404)
            self.end_headers()

def start_test_api_server(port=8001):
    server_address = ('', port)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    print(f"🧪 Test API server started on http://localhost:{port}")
    httpd.serve_forever()

# At the bottom of metrics_server.py
if __name__ == "__main__":
    start_metrics_server()
    start_test_api_server()
