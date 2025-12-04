# Database Failed to Load or Is Corrupt

Delete lock files and attempt restore.

### Problem

IPTVBoss says "Database failed to load or is corrupt" and freezes.

### Solution

**Immediate fixes:**

1. Force close IPTVBoss (Task Manager on Windows)
2. Go to `IPTVBoss/db` folder and delete any files with "lock" in the name
3. Restart IPTVBoss - it should attempt auto-restore
- If IPTVBoss wont start, move the contents of `IPTVBoss/db` somewhere safe so that the folder is empty and continue to the next step to restore your database
4. If still frozen, manually restore: Settings → Database Restore → Local, Cloud or URL
    - URL restore must point to a direct download file
    - With Dropbox make sure the end of the URL is `&dl=1` for direct download

**If restore fails:**

- Try older backup files 
- Verify you're still on Pro license (may need to re-enter license key)
- Check if you've migrated your account to the new IPTVBoss website
- Post logs in support Discord for help

### Related Topics

- [Database Corruption and Failed Startup](../troubleshooting/01_database_corruption_startup_failure.md)
- [No Layouts and Local Restore Crashes](17_no_layouts_local_restore_crashes.md)
