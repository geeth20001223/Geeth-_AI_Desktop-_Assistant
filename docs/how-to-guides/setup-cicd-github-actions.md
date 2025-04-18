# Setup CI/CD with GitHub Actions

This guide explains the multi-environment CI/CD using GitHub Actions.

## Branch Strategy
- `dev` → Dev environment
- `staging` → Staging
- `main` → Production

## CI/CD Flow
- Run unit, integration, and e2e tests
- Scan code (CodeQL, Snyk, OWASP ZAP)
- SSH deploy to Azure VM (20.195.40.50)
