# Disaster Recovery Plan – Geeth AI

## Scenario 1: Code Loss
- Restore from latest GitHub commit/tag.
- If local, use `backups/` folder.

## Scenario 2: Database Corruption
- Restore latest good version of `geeth.db` from `backups/`.
- Consider implementing SQLite WAL (Write-Ahead Logging) mode.

## Scenario 3: Environment Broken
- Run: `python -m venv .venv`
- Install: `pip install -r requirements.txt`

## Scenario 4: System Crash
- Clone repo from GitHub
- Restore `backups/` contents
- Run `run.py`
