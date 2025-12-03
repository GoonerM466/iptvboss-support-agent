# Database Corruption and Failed Startup

IPTVBoss won't start, crashes immediately, or reports database corruption.

### Problem

IPTVBoss fails to start properly, showing database-related errors or crashing.

### Symptoms

- IPTVBoss won't open or immediately closes
- Error message: "Database failed to load or is corrupt"
- GUI running in Task Manager but no window appears on screen
- All playlists and layouts disappeared
- Lost Pro license activation
- Application freezes during startup

### Why This Happens

Database corruption from improper shutdown, disk full, file system errors, or lock file conflicts. Lock files from previous crashed sessions prevent new database access and create illusion of corruption.

### Solution

**1. Force close all IPTVBoss processes**
- Windows: Open Task Manager (Ctrl+Shift+Esc) ’ Find IPTVBoss ’ End Task
- Mac: Activity Monitor ’ Find IPTVBoss ’ Force Quit

**2. Delete lock files**
- Navigate to `IPTVBoss/db` folder
- Delete ALL files with "lock" in the filename (e.g., `database.lock`, `lockfile`)
- These files prevent database access to avoid corruption from multiple instances

**3. Restart IPTVBoss**
- IPTVBoss will attempt auto-recovery
- If successful, you'll see your data restored

**4. If still fails: Manual restore**
- Open IPTVBoss (may show empty)
- Menu ’ Restore ’ Local
- Select most recent backup that predates the problem
- Look in `IPTVBoss/backup` folder for dated backups

**5. If recent backups fail**
- Try progressively older backup files
- Newest backup might also be corrupted
- Go back several days if needed

**6. Re-enter Pro license if needed**
- Menu ’ Activate Pro
- Enter license key

### Prevention

- Always close IPTVBoss properly (don't force quit)
- Ensure adequate disk space
- Don't run multiple instances simultaneously
- Keep antivirus from quarantining database files
- Don't store database on network drives

### Known Limitations

- Multiple instances or cloud sync conflicts can cause recurring corruption
- Antivirus may interfere with database file access
- Database on slow network storage increases corruption risk

### Related Topics

- [No Layouts and Local Restore Crashes](../faq/17_no_layouts_local_restore_crashes.md)
- [Database Failed to Load](../faq/18_database_failed_to_load_corrupt.md)
- [Recurring Database Wipes](../known_issues/01_recurring_database_wipes.md)
