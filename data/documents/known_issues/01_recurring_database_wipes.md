# Recurring Database Wipes Every 1-2 Weeks

IPTVBoss shows no data every 1-2 weeks requiring repeated restores.

### Status

Needs user-specific investigation.

### Problem

IPTVBoss loses all data on a consistent recurring schedule (every 1-2 weeks).

### Symptoms

- IPTVBoss shows no data every 1-2 weeks
- Must restore from backup repeatedly
- Pattern is consistent (same interval)

### Possible Causes

- Cloud sync conflicts from multiple instances
- Disk space issues
- Antivirus quarantining database files
- Database on network drive or slow storage
- Memory issues during shutdown
- Background process killing IPTVBoss improperly

### Investigation Steps

1. Check `IPTVBoss/logs` folder for patterns around time of data loss
2. Look for:
   - Database write errors
   - Disk full errors
   - Permission errors
   - Sync conflict messages
3. Monitor disk space over time
4. Check if running multiple Boss instances
5. Verify antivirus isn't flagging Boss files
6. Check if database is on local drive (not network)

### Escalation
This issue needs investigation if you cannot solve on your own
- Contact support on [Discord](https://discord.gg/QCxpA9yvWP)

Detailed logs from the time of failure, environment specifics, etc will be needed - ensure they are clean before posting to support channels.

### Related Topics

- [Recurring Database Wipes Restore](../faq/25_recurring_database_wipes_restore.md)
- [Database Corruption](../troubleshooting/01_database_corruption_startup_failure.md)
