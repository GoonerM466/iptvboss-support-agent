# Solution: Restore Database from Backup

**Flow ID**: database_issues
**Type**: diagnostic_solution
**Confidence**: high
**Solution Steps**: 4

### Context

Database is corrupted or failed to load, but user has a backup available. This is the ideal scenario for quick recovery.

### Root Cause

Database file corrupted due to crash, power loss, or file system issue. Backup provides clean restore point.

### Confidence

**HIGH (95%+)** - Restoring from backup is straightforward and reliable

### Step 1: Close Boss and Locate Database Folder

1. **Close IPTVBoss completely** (important!)
2. Navigate to Boss database folder:
   - **Windows**: `C:\Users\[YourName]\AppData\Roaming\IPTVBoss`
   - **Mac**: `~/Library/Application Support/IPTVBoss`
   - **Linux**: `~/.config/IPTVBoss`

**Tips for finding folder**:
- **Windows**: Press `Win+R`, type `%appdata%\IPTVBoss`, press Enter
- **Mac**: Finder → Go menu → Hold Option → Library → Application Support → IPTVBoss
- **Linux**: Usually hidden, enable "Show Hidden Files" in file manager

### Step 2: Backup Current (Corrupted) Database

Even though it's corrupted, keep it as reference:

1. Find `database.db` file
2. **Rename** it to `database_corrupted_[DATE].db`
   - Example: `database_corrupted_2025_12_05.db`
3. This preserves it in case needed later
4. Also backup or rename any `.lock` files:
   - Rename `.lock` to `.lock.old`

### Step 3: Restore Your Backup

**If backup is in same folder**:
1. Find your backup file (e.g., `database_backup_2025_12_01.db`)
2. **Copy** it (don't move)
3. Rename the copy to `database.db` (exact name)
4. Verify file exists and has normal size (not 0 bytes)

**If backup is elsewhere**:
1. Locate your backup file
2. **Copy** it to the IPTVBoss folder
3. Rename to `database.db`
4. Verify file is in correct location

### Step 4: Restart Boss and Verify

1. Open **IPTVBoss**
2. Should start normally now
3. **Verify**:
   - Sources are present
   - Layouts exist
   - Channels show in lists
   - Settings are correct
4. Check EPG Browser for data

### ✅ If Boss Starts Successfully

Great! Now set up automatic backups to prevent data loss:

**1. Enable Boss Auto-Backup** (if available in your version):
1. Boss → Settings → Backup
2. Enable automatic backups
3. Set frequency (daily or weekly)
4. Set retention (keep last 5-10)

**2. Manual Backup Schedule**:

If Boss doesn't have auto-backup, set a reminder to backup manually:

**Weekly Backup**:
1. Close Boss
2. Navigate to Boss folder
3. Copy `database.db`
4. Save as `database_backup_[DATE].db` somewhere safe
5. Keep last 3-5 backups

**Good backup locations**:
- Different drive (external HD, USB)
- Cloud storage (Dropbox, Google Drive - separate from Boss output folder)
- Network drive
- **Not** the same disk as Boss (if disk fails, backup is gone)

**3. Sync Before Backup**:

Before backing up:
1. Open Boss
2. Sources → Sync All (refresh data from providers)
3. Wait for completion
4. Close Boss normally
5. Then backup database file

This ensures backup has latest data.

**4. Delete Lock Files Periodically**:

Prevent future issues:
1. Close Boss normally (don't force close)
2. Check Boss folder for `.lock` files
3. Delete any `.lock` files when Boss is closed
4. Restart Boss

### How Recent Was Your Backup?

**Backup from today/yesterday**:
- Minimal data loss
- You're good to go

**Backup from last week**:
- Lost recent changes
- May need to re-sync sources
- Recreate recent layout edits

**Backup from months ago**:
- Significant data loss
- Definitely re-sync all sources
- Verify layouts and channels
- Check settings

**After restoring old backup**:
1. Sources → Sync All Playlists
2. Sources → Sync All EPGs
3. Verify layouts have current channels
4. Output layouts
5. Sync players

### ❌ If Boss Still Won't Start

**Backup might also be corrupted**:

**Try older backups**:
- If you have multiple backups, try next oldest
- One of them might work

**If no working backup**:
→ **Solution**: [Recovery Attempts](02_solution_recovery.md)

### Prevent Future Corruption

**1. Always close Boss properly**:
- Use File → Exit or Close button
- **Don't** force-close or end task
- **Don't** shut down PC while Boss is running

**2. Handle crashes carefully**:
- If Boss crashes, wait 30 seconds before restarting
- Check for lock files before restarting
- Consider backing up before restarting

**3. Power protection**:
- Use UPS (battery backup) for desktop
- Ensures clean shutdown during power outages
- Prevents mid-write corruption

**4. Disk health**:
- Run disk checks periodically
- Watch for disk errors in system logs
- Replace aging drives before failure

**5. Keep multiple backups**:
- Don't overwrite same backup file
- Keep dated backups (last 5-10)
- Backup to multiple locations

### Related Topics

- [Database Corruption Full Guide](../../01_database_corruption_startup_failure.md)
- [Port Migration and Recovery](../../11_port_migration_database_recovery.md)
- [Application Crashes](../../03_application_crashes_startup_updates.md)
