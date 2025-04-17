from multiprocessing import Process
import time
import sys
from engine.auth.recoganize import AuthenticateFace
from main import run_assistant
from engine.features import hotword
from my_tracing import process_request
from metrics_server import start_metrics_server, start_test_api_server

def start_metrics():
    start_metrics_server()
    start_test_api_server()

if __name__ == '__main__':
    print("🚀 Starting Geeth AI Assistant...")

    # Start metrics and test API server in a background process
    Process(target=start_metrics).start()

    # Synthetic monitoring and tracing
    process_request("startup")

    # Authenticate the user via face recognition
    result = AuthenticateFace()
    if result == 1:
        print("✅ Face authentication passed")

        # Run assistant and hotword detection in parallel
        p1 = Process(target=run_assistant)
        p2 = Process(target=hotword)

        p1.start()

        p2.start()

        p1.join()
        p2.join()
    else:
        print("❌ Face authentication failed")
        sys.exit(1)
