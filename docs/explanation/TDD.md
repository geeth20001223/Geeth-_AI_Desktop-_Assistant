# Technical Design Document (TDD)

## 1. Overview
The Geeth_AI_Desktop_Assistant is a locally-run intelligent assistant application for desktop users. It leverages facial recognition for secure login, voice command processing, integration with Android via ADB, and advanced NLP features for user interaction. This document outlines the system's architectural and technical design.

## 2. Goals and Non-Goals
### Goals
- Enable voice-activated desktop assistant functionality.
- Provide secure user authentication using facial recognition.
- Automate communication via WhatsApp and device interaction via ADB.
- Enable AI-powered conversational responses.

### Non-Goals
- Cloud-based deployment
- Mobile-first user interface

## 3. Architecture
- **Frontend**: Eel (Python + HTML/JS frontend rendering)
- **Backend**: Python (speech recognition, facial auth, command handling)
- **Monitoring**: OpenTelemetry + Prometheus + Email alerts
- **CI/CD**: GitHub Actions (build, test, deploy to VM)
- **Infrastructure**: Azure Linux VM with blue-green folders

## 4. Key Modules
- `main.py`: Launches UI and assistant interface.
- `run.py`: Orchestrates startup, authentication, and process control.
- `engine/command.py`: Handles speech commands.
- `engine/features.py`: Implements utilities like YouTube, WhatsApp, chatbot.
- `recoganize.py`: Facial recognition using OpenCV.
- `metrics_server.py`: Serves metrics for Prometheus.
- `synthetic-monitor.py`: Synthetic endpoint monitoring script.

## 5. Data Flow
1. Facial recognition authenticates user.
2. Hotword detection starts assistant.
3. Voice input captured and transcribed.
4. Commands are processed via NLP + hardcoded actions.
5. Responses are spoken and executed.

## 6. Dependencies
- Python 3.10+
- `speech_recognition`, `eel`, `opencv-python`, `pyttsx3`, `pvporcupine`
- HuggingFace `hugchat`, Prometheus client, OpenTelemetry

## 7. Error Handling
- All critical modules have try/except blocks.
- Failures in startup processes will trigger fallback logs.
- Monitoring and alerting will notify errors via email.

## 8. Security Considerations
- Facial recognition for identity validation.
- Device connections restricted to ADB-authenticated devices.

## 9. Future Improvements
- Replace `pyttsx3` with more natural voice models.
- Extend CI/CD for auto-rollbacks.
- Add mobile companion app.

---
Last updated: April 2025

