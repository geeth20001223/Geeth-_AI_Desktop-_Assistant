import requests
import time
import smtplib
from email.mime.text import MIMEText
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
request_counter = Counter("request_count", "Total number of processed requests")
error_counter = Counter("error_count", "Total number of failed requests")
response_time_histogram = Histogram("response_time_seconds", "Response time in seconds")

def send_email(subject, body):
    sender_email = "your_email@gmail.com"
    sender_password = "your_password"
    receiver_email = "recipient_email@example.com"

    message = MIMEText(body)
    message['Subject'] = subject
    message['From'] = sender_email
    message['To'] = receiver_email

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, receiver_email, message.as_string())
        print("Email sent successfully")
    except Exception as e:
        print(f"Email failed to send: {e}")
        with tracer.start_as_current_span("email_error") as span:
            span.record_exception(e)

def synthetic_test(url, test_name):
    with tracer.start_as_current_span(test_name) as span:
        response_time = 0
        try:
            start_time = time.time()
            response = requests.get(url)
            end_time = time.time()
            response_time = end_time - start_time

            status_code = response.status_code
            span.set_attribute("http.status_code", status_code)
            span.set_attribute("response_time", response_time)
            is_successful = status_code == 200
            return {
                'response_time': response_time,
                'status_code': status_code,
                'is_successful': is_successful
            }
        except Exception as e:
            error_counter.inc()
            span.record_exception(e)
            return {
                'response_time': 0,
                'status_code': 500,
                'is_successful': False
            }
        finally:
            request_counter.inc()
            response_time_histogram.observe(response_time)

if __name__ == "__main__":
    # Correct port should be 8001 (your custom HTTP server)
    result_api_status = synthetic_test("http://localhost:8001/api/status", "synthetic_test_api_status")
    print(f"API Status - Response Time: {result_api_status['response_time']:.2f} seconds")
    print(f"API Status - Status Code: {result_api_status['status_code']}")
    print(f"API Status - Test Passed: {result_api_status['is_successful']}")

    if not result_api_status['is_successful']:
        message_body = f"API Status test failed at {time.ctime()}: {result_api_status}"
        send_email("Synthetic Monitoring Failure - API Status", message_body)

    result_another_endpoint = synthetic_test("http://localhost:8001/another_endpoint", "synthetic_test_another_endpoint")
    print(f"Another Endpoint - Response Time: {result_another_endpoint['response_time']:.2f} seconds")
    print(f"Another Endpoint - Status Code: {result_another_endpoint['status_code']}")
    print(f"Another Endpoint - Test Passed: {result_another_endpoint['is_successful']}")

    if not result_another_endpoint['is_successful']:
        message_body = f"Another Endpoint test failed at {time.ctime()}: {result_another_endpoint}"
        send_email("Synthetic Monitoring Failure - Another Endpoint", message_body)
