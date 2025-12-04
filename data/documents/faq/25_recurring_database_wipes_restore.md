# Recurring Database Wipes Every 1-2 Weeks

Recurring database loss indicates a deeper issue requiring investigation.

### Problem

Every time you open IPTVBoss (every 1-2 weeks) it shows no data and you have to restore.

### Solution

**Check logs** (`IPTVBoss/logs` folder) for patterns:
- Database write errors
- Disk full errors
- Permission errors
- Backup/sync conflicts

**Common causes:**

- Cloud sync conflict (multiple instances running)
- Insufficient disk space
- Antivirus interfering with database files
- Database on network drive or slow storage
- Memory issues during shutdown

**Temporary workaround**: Restore from Dropbox backup file (change last digit to 0). Keep external backups until root cause is found (NOT Recommended for long term solution)

**This issue should be escalated to the support team on 
[Discord](https://discord.gg/QCxpA9yvWP) - Provide clean logs on request

### Related Topics

- [Recurring Database Wipes](../known_issues/01_recurring_database_wipes.md)
- [Database Corruption](../troubleshooting/01_database_corruption_startup_failure.md)
