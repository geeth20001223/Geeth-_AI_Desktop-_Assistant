import multiprocessing
import subprocess
from my_tracing import tracer, process_request  # Import tracer and metrics tracking functions
from metrics_server import app  # Import Flask app that exposes metrics

# Main function for application logic with tracing
def main():
    with tracer.start_as_current_span("process-user-input"):
        print("This part of the code is being traced.")
        # Add your application logic here
        # Example:
        # run_engine()
        # handle_voice_input()
        # process_user_command()

        # Simulate processing a request and track metrics
        process_request(success=True, response_time=0.2)  # Simulate a 200ms response time

# Function to start the Jarvis process (another part of your system)
def startJarvis():
    with tracer.start_as_current_span("start-jarvis-process"):
        print("Jarvis process is running.")
        # Simulate some work being done by Jarvis
        from main import start
        start()  # Assuming the start function is in your main.py

# Function to listen for hotword detection
def listenHotword():
    with tracer.start_as_current_span("hotword-detection-process"):
        print("Hotword detection process is running.")
        # Simulate hotword detection
        from engine.features import hotword
        hotword()  # Assuming hotword detection is in engine.features

# Start both processes in parallel
if __name__ == '__main__':
    with tracer.start_as_current_span("run-main-process"):
        # Start the Jarvis and hotword detection processes
        p1 = multiprocessing.Process(target=startJarvis)
        p2 = multiprocessing.Process(target=listenHotword)

        p1.start()
        subprocess.call(['device.bat'])
        p2.start()

        p1.join()

        if p2.is_alive():
            p2.terminate()
            p2.join()

        print("system stop")
