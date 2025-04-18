# 🛠️ Operations Runbook – Geeth_AI_Desktop_Assistant

This document provides standard operating procedures (SOPs) for running and maintaining the **Geeth_AI_Desktop_Assistant** in production. It includes health checks, monitoring, deployment verification, and incident handling.

---

## 📌 Table of Contents

- [✅ System Health Checks](#-system-health-checks)
- [📊 Monitoring & Observability](#-monitoring--observability)
- [🚀 Deployment Procedures](#-deployment-procedures)
- [⚠️ Incident Response](#️-incident-response)
- [🧪 Testing After Changes](#-testing-after-changes)
- [🔒 Security Considerations](#-security-considerations)
- [📁 Backup and Recovery](#-backup-and-recovery)

---

## ✅ System Health Checks

| Component       | Check Method                         | Expected Outcome              |
|----------------|--------------------------------------|-------------------------------|
| App Process     | `ps aux | grep main.py`              | Assistant running             |
| Face Auth       | Run app → Face cam opens             | Auth module loads correctly   |
| Hotword         | Say "Jarvis"                         | Detected and triggers action  |
| Web Frontend    | `localhost:8000`                     | Loads Eel UI dashboard        |

---

## 📊 Monitoring & Observability

| Tool             | Purpose                            |
|------------------|-------------------------------------|
| Prometheus       | Metrics collection                  |
| Grafana (optional)| Dashboard visualization             |
| OpenTelemetry    | Tracing and performance insights    |
| Email Alerts     | Critical failure notification       |

> 💡 **Metrics**: CPU, memory, face auth errors, command fail rate.

---

## 🚀 Deployment Procedures

1. **Push to GitHub** (`dev`, `staging`, or `main` branch).
2. **GitHub Actions CI/CD** triggers:
   - Linting, tests
   - Snyk/CodeQL scans
   - SSH deployment to Azure Linux VM (`20.195.40.50`)
3. **Verify application health** post-deploy:
   - Monitor `run.py` output
   - Check Prometheus dashboard
   - Test hotword and voice commands

---

## ⚠️ Incident Response

| Scenario                        | Action                                                                 |
|----------------------------------|------------------------------------------------------------------------|
| App crash                        | Check `main.py` logs, restart service                                 |
| Hotword not working              | Restart `features.py`, verify `pvporcupine` package                   |
| Face Auth fails                  | Check webcam access, retrain model using `trainer.py`                |
| Deployment failed                | Inspect GitHub Actions log, retry manually via SSH                    |
| High memory/CPU usage            | Use `htop`, kill unused processes, reboot if necessary                |

---

## 🧪 Testing After Changes

- Run `run.py` and verify:
  - Face recognition
  - Hotword detection
  - Voice commands execute
- Confirm metrics are still collected in Prometheus.
- Conduct secret scanning + CodeQL/Snyk scan manually if needed.

---

## 🔒 Security Considerations

- GitHub Secrets encrypted for deployment credentials.
- Secret scanning enabled in GitHub repository.
- Use Snyk + CodeQL on each pull request for vulnerabilities.

---

## 📁 Backup and Recovery

| Task           | Command/Action                                                          |
|----------------|--------------------------------------------------------------------------|
| Backup         | Zip `Geeth_AI` folder, upload to Azure Blob via scheduled GitHub Action |
| Recovery       | SSH into server, unzip latest backup into deployment directory          |
| Schedule       | Weekly full backup, daily incremental recommended                       |

---

✅ **Always document incidents in the [Incident Response Playbooks](https://github.com/geeth20001223/Geeth-_AI_Desktop-_Assistant/wiki/Incident-Response-Playbooks)** section for team learning.

---

🧑‍💻 Maintained by: `geeth20001223`  
📅 Last Updated: April 2025
