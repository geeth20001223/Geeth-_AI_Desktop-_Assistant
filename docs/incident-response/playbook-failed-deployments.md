# Incident Response Playbook: Failed Deployments

## Detection
- GitHub Actions fails with non-zero exit code

## Immediate Action
1. Check workflow logs
2. Re-run with `--debug`
3. Validate SSH key and permissions

## Resolution
- Fix code/test failure
- Retry pipeline
