from flask import Flask
from prometheus_client import generate_latest, start_http_server

# Set up the Flask app
app = Flask(__name__)

@app.route("/metrics")
def metrics():
    return generate_latest()  # Prometheus scrapes the metrics from this route

# Start the Prometheus server (on port 8000)
if __name__ == "__main__":
    start_http_server(8000)  # Expose metrics on port 8000
    app.run(host="0.0.0.0", port=5000)  # Your main app running on port 5000
