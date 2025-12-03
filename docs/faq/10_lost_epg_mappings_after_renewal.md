# Lost EPG Mappings After Service Expired or Renewed

New credentials create a new source identity, which loses all mappings.

### Problem

You lost all your EPG mappings after your service expired or renewed.

### Explanation

If you added the source as an M3U URL with credentials, **new** credentials create a new source identity, which loses all mappings.

### Recovery

1. Restore from a recent database backup: **Menu ’ Restore ’ Local or Cloud**
2. Check `IPTVBoss/backup` folder for dated backup files

### Prevention

- Use **XC API connection** instead of M3U when available (preserves mappings better)
- Keep regular database backups
- Create a manual backup before renewing expired services

### Related Topics

- [Source Sync Failures Breaking Layouts](../troubleshooting/02_source_sync_breaking_layouts.md)
- [Database Corruption](../troubleshooting/01_database_corruption_startup_failure.md)
