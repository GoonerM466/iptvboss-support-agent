# No Layouts or Sources and Local Restore Crashes

Try multiple backups - recent backup might also be corrupted.

### Problem

IPTVBoss shows no layouts or sources, and local restore crashes the app.

### Solution

**Try multiple backups** (recent backup might also be corrupted):

1. Close IPTVBoss completely
2. Navigate to `IPTVBoss/backup` folder
3. Note there are multiple dated backup files
4. Start IPTVBoss and try **Menu ’ Restore ’ Local**
5. If it crashes, try restoring from an older backup file
6. If all backups fail, check logs (`IPTVBoss/logs`) for specific errors

**Alternative:**

- Try cloud (recommended) or URL restore if you have cloud sync enabled
- Contact support with logs

### Related Topics

- [Database Corruption and Failed Startup](../troubleshooting/01_database_corruption_startup_failure.md)
- [Where Are IPTVBoss Files Located](16_where_are_iptvboss_files_located.md)
