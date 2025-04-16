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

# Export spans to console
span_exporter = ConsoleSpanExporter()
span_processor = SimpleSpanProcessor(span_exporter)
trace.get_tracer_provider().add_span_processor(span_processor)

# --- Prometheus Metrics Setup ---
request_counter = Counter("request_count", "Total number of processed requests")
error_counter = Counter("error_count", "Total number of failed requests")
response_time_histogram = Histogram("response_time_seconds", "Response time in seconds")

# --- Email Alert Function ---
def send_email(subject, body):
    sender_email = "shamal.geethanjanpathirana@gmail.com"
    sender_password = "zozg rvmx zuio tpof"  # App Password
    receiver_email = "shamal.geethanjanpathirana@gmail.com"

    message = MIMEText(body)
    message['Subject'] = subject
    message['From'] = sender_email
    message['To'] = receiver_email

    try:
        print("Connecting to SMTP server...")
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, receiver_email, message.as_string())
        print("✅ Email sent successfully")
    except Exception as e:
        print(f"❌ Email failed to send: {e}")
        with tracer.start_as_current_span("email_error") as span:
            span.record_exception(e)

# --- Synthetic Test Function ---
def synthetic_test(url, test_name):
    with tracer.start_as_current_span(test_name) as span:
        response_time = 0
        try:
            print(f"Sending request to: {url}")
            start_time = time.time()
            response = requests.get(url)
            end_time = time.time()
            response_time = end_time - start_time

            status_code = response.status_code
            is_successful = status_code == 200

            span.set_attribute("http.status_code", status_code)
            span.set_attribute("response_time", response_time)

            print(f"Status code: {status_code}, Response time: {response_time:.3f}s")

            return {
                'response_time': response_time,
                'status_code': status_code,
                'is_successful': is_successful
            }
        except Exception as e:
            print(f"❌ Request failed: {e}")
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

# --- Process Result and Send Email if Failed ---
def process_request(url, test_name):
    print("Running synthetic test...")
    result = synthetic_test(url, test_name)
    if not result['is_successful']:
        print("🔔 Test failed, sending email alert...")
        send_email(
            subject=f"Failure - {test_name}",
            body=f"Request to {url} failed at {time.ctime()} with result:\n{result}"
        )
    else:
        print("✅ Test passed, no alert needed.")
    return result

# --- MAIN ---
if __name__ == "__main__":
    # Simulate a failure by calling an invalid port or wrong URL
    test_url = "http://localhost:9999"  # Force failure here
    process_request(test_url, "Test - Localhost Down")
