from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import ConsoleSpanExporter, SimpleSpanProcessor
from prometheus_client import Counter, Histogram

# --- OpenTelemetry Tracing Setup ---
trace.set_tracer_provider(TracerProvider())
tracer = trace.get_tracer(__name__)

# Export spans to console for debugging/demo
span_exporter = ConsoleSpanExporter()
span_processor = SimpleSpanProcessor(span_exporter)
trace.get_tracer_provider().add_span_processor(span_processor)

# --- Prometheus Metrics Setup (Custom Metrics) ---
# Counter to count total requests
request_counter = Counter(
    "request_count", "Total number of processed requests"
)

# Counter to count failed requests
error_counter = Counter(
    "error_count", "Total number of failed requests"
)

# Histogram to measure response times
response_time_histogram = Histogram(
    "response_time_seconds", "Response time in seconds"
)

# --- Function to Simulate or Track a Request ---
def process_request(success=True, response_time=0.0):
    request_counter.inc()
    if not success:
        error_counter.inc()
    response_time_histogram.observe(response_time)
