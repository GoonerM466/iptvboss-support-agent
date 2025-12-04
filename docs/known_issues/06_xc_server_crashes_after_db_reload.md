# XC Server Crashes After DB Reload Post-Sync

XC server crashes during database reload after source sync.

### Status

XC database corruption - advanced troubleshooting needed.

### Problem

XC server component crashes when reloading database after completing a source sync.

### Symptoms

- Source sync completes successfully
- Database reload begins
- XC server crashes
- Main Boss still works

### Possible Causes

- XC database (separate from main DB) is corrupted
- XC configuration conflict
- Memory issues during reload

### Workaround

1. Identify XC database file in `IPTVBoss/db` folder
2. Delete XC database and run sync / refresh

### Escalation

If you cannot resolve the issue contact support on [Discord](https://discord.gg/QCxpA9yvWP)

### Related Topics

- [Application Crashes on Startup](../troubleshooting/03_application_crashes_startup_updates.md)
- [Database Corruption](../troubleshooting/01_database_corruption_startup_failure.md)
