# Application Crashes on Startup or After Updates

IPTVBoss crashes when launching or immediately after opening.

### Problem

IPTVBoss crashes during or immediately after startup.

### Symptoms

- Boss loads splash screen then crashes
- Crashes immediately after opening full window
- Reinstalling doesn't fix crashes
- Crashes after database restore
- Works once after reinstall, crashes on subsequent opens

### Why This Happens

Corrupted database loaded on startup, corrupted settings/preferences, lock files preventing startup, incompatible database from different version, disk space exhausted, or log files consuming excessive space.

### Solution

**1. Force close all IPTVBoss instances** (Task Manager/Activity Monitor)

**2. Delete lock files**
- Navigate to `IPTVBoss/db` folder
- Delete files with "lock" in name

**3. Check disk space**
- Ensure adequate free space on drive with IPTVBoss
- Low disk space causes startup failures

**4. Check log file sizes**
- Navigate to `IPTVBoss/logs` folder
- If logs are excessively large (>50MB), archive or delete old ones
- Keep most recent log for diagnostics

**5. If crashes persist: Clean reinstall**
- Move entire IPTVBoss folder to Documents (preserves backups)
- Reinstall IPTVBoss fresh
- After installation, restore from backup in Documents folder
- This provides clean environment while preserving your data

**6. If crash after restore**
- Try older backup file
- Recent backup might also be corrupted
- Go back to last known good state

**7. Get diagnostic information**
- Before moving IPTVBoss folder, copy most recent log from `IPTVBoss/logs`
- Post in support Discord with log (clean sensitive provider info first)
- Logs show crash reason

### Prevention

- Keep IPTVBoss updated
- Close properly (don't force quit)
- Monitor disk space
- Archive old logs periodically

### Known Limitations

- Some database corruptions prevent clean restore
- Version compatibility issues during major upgrades
- Logs location and cleanup not well documented

### Related Topics

- [Database Corruption and Failed Startup](01_database_corruption_startup_failure.md)
- [No Layouts and Local Restore Crashes](../faq/17_no_layouts_local_restore_crashes.md)
