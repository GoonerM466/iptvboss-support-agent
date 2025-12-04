# No Layouts or Sources and Local Restore Crashes

Try multiple backups - recent backup might also be corrupted.

### Problem

IPTVBoss shows no layouts or sources, and local restore crashes the app.

### Solution

Restore is required.

**Try multiple backups** (recent backup might also be corrupted):

1. First - try a computer reboot - you never know!
2. Start IPTVBoss and an auto restore will be attempted. If the issue remains continue with a manual restore
3. **Settings → Restore Database → Local, Cloud, or URL**
4. If the restore doesnt return your data you should try earlier backup files
5. Your cloud folders will often have more backup file available in either the "Deleted Items" or "Trash" folders
6. If all backups fail, check logs (`IPTVBoss/logs`) for specific errors.

**Recommended**

- Cloud or URL restore (providing you have cloud sync enabled)
    - URL restore must point to a direct download file
    - With Dropbox make sure the end of the URL is `&dl=1` for direct download

### If you cannot restore your data
- Contact support on [Discord](https://discord.gg/QCxpA9yvWP) with clean logs

### Related Topics

- [Database Corruption and Failed Startup](../troubleshooting/01_database_corruption_startup_failure.md)
- [Where Are IPTVBoss Files Located](16_where_are_iptvboss_files_located.md)
