from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor, ConsoleSpanExporter
from opentelemetry.sdk.resources import Resource

trace.set_tracer_provider(
    TracerProvider(
        resource=Resource.create({"service.name": "geeth-ai"})
    )
)

tracer = trace.get_tracer(__name__)

span_processor = BatchSpanProcessor(ConsoleSpanExporter())
trace.get_tracer_provider().add_span_processor(span_processor)

def process_request(request_name: str):
    with tracer.start_as_current_span(request_name):
        print(f"Processing request: {request_name}")
