from flask import Flask
from prometheus_client import generate_latest, start_http_server, Counter
import time
import random
from threading import Thread
from http.server import HTTPServer, BaseHTTPRequestHandler

# Set up the Flask app
app = Flask(__name__)

@app.route("/metrics")
def metrics():
    return generate_latest()  # Prometheus scrapes the metrics from this route

# Start the Prometheus server (on port 8000)
def run_prometheus_server(port=8000):
    start_http_server(port)  # Expose metrics on port 8000

# Prometheus counters
SUCCESS_COUNT = Counter('another_endpoint_success_total', 'Successful /another_endpoint hits')
FAILURE_COUNT = Counter('another_endpoint_failure_total', 'Failed /another_endpoint hits')

# HTTPRequestHandler for other endpoints
class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/api/status':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'OK')

        elif self.path == '/another_endpoint':
            if random.random() < 0.2:  # Simulate a 20% failure rate
                FAILURE_COUNT.inc()
                self.send_response(500)
                self.send_header('Content-type', 'text/plain')
                self.end_headers()
                self.wfile.write(b'Internal Server Error')
            else:
                SUCCESS_COUNT.inc()
                self.send_response(200)
                self.send_header('Content-type', 'text/plain')
                self.end_headers()
                self.wfile.write(b'Another Endpoint is OK')

        else:
            self.send_response(404)
            self.end_headers()

# Function to run the HTTP server
def run_http_server(port=8001):
    server_address = ('', port)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    print(f'Starting HTTP server on port {port}...')
    httpd.serve_forever()

# Run the app
if __name__ == "__main__":
    # Start Prometheus server in a separate thread
    prometheus_thread = Thread(target=run_prometheus_server, args=(8000,))
    prometheus_thread.daemon = True
    prometheus_thread.start()

    # Start HTTP server in a separate thread
    http_thread = Thread(target=run_http_server, args=(8001,))
    http_thread.daemon = True
    http_thread.start()

    # Start Flask app in the main thread
    print('Starting Flask app...')
    app.run(host="0.0.0.0", port=5000, use_reloader=False)
