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

### Workaround

- Keep frequent external backups
- Restore from Dropbox backup: IPTVBossSync.backup (change last digit to 0)
- Document exactly when failures occur (time of day, after what actions)
- Consider dedicated machine for Boss if running on shared system

### What's Needed

Detailed logs from user at time of failure, environment specifics.

### Related Topics

- [Recurring Database Wipes Restore](../faq/25_recurring_database_wipes_restore.md)
- [Database Corruption](../troubleshooting/01_database_corruption_startup_failure.md)
