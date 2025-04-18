# 🏗️ System Architecture - Geeth_AI Desktop Assistant

## 🔧 System Components Overview

The Geeth_AI project follows a modular architecture. Each component is loosely coupled and focused on a specific functionality, ensuring maintainability and scalability.

---

## 🧠 Core Components

### 1. **Frontend (Eel + HTML/CSS/JS)**
- Provides a desktop GUI for user interaction.
- Renders assistant interface and responses visually.
- Communicates with backend using `eel.expose()` Python-JavaScript bridge.

### 2. **Backend (Python)**
- Handles voice recognition, text-to-speech, NLP, and logic.
- Organized into modules:
  - `main.py`: Entry point, initializes Eel, authentication, and logic.
  - `run.py`: Starts multiprocessing and synthetic monitoring.
  - `engine/command.py`: Processes user commands (open apps, play music, WhatsApp messaging).
  - `features.py`: Supports YouTube, hotword detection, chatbot (Hugging Face), etc.
  - `recoganize.py`: Facial recognition using OpenCV.

### 3. **Monitoring & Observability**
- **OpenTelemetry**: Tracing synthetic events.
- **Prometheus**: Collects system metrics.
- **Custom Metrics Server**: Exposes app-specific metrics.
- **Alerting**: Email-based alerts on anomalies.

### 4. **CI/CD & DevOps**
- **GitHub Actions**: Runs tests, scans, and environment-specific deployments.
- **Blue-Green Deployment**: Uses `Geeth_AI_Blue` and `Geeth_AI_Green` folders.
- **Snyk / CodeQL / OWASP ZAP**: Code quality and security gates.

### 5. **Infrastructure-as-Code (IaC)**
- **Azure Linux VM**: Host for all environments (dev, staging, prod).
- **Shell Scripts**: Used for SSH deployment and environment setup.

---

## 🔄 Deployment Flow
1. Developer pushes to GitHub → Triggers CI/CD pipeline.
2. Pipeline runs tests, scans, and builds artifacts.
3. Pipeline connects to Azure VM via SSH.
4. Code is deployed to either `Geeth_AI_Blue` or `Geeth_AI_Green` based on branch.
5. Monitoring tools verify success or rollback.

---

## 📊 Diagram (Insert Screenshot)
Include a system architecture diagram showing:
- User → Desktop App GUI → Backend (Python)
- Backend → Metrics/Tracing + Azure VM
- Azure VM → CI/CD Deployer + Blue/Green folders

---

## 🔒 Security Design
- Authentication via Face ID
- ADB controls secured via dynamic IP linking
- GitHub Secrets for keys and deployment credentials
- Periodic vulnerability scans (Snyk, CodeQL)

---

## 📌 Summary
This architecture ensures modularity, maintainability, security, and a smooth developer workflow. CI/CD automation, blue-green deployments, and monitoring provide production-grade robustness for the AI assistant.

