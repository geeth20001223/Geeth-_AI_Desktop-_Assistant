# System Architecture

The assistant is structured into the following layers:
- UI Layer: Eel (HTML/JS)
- Backend Logic: Python (`command.py`, `features.py`)
- Monitoring: Prometheus, OpenTelemetry
- Deployment: GitHub Actions → SSH → Azure VM
