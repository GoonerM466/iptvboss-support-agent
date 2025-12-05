# Solution: Database Recovery Without Backup

**Flow ID**: database_issues
**Type**: diagnostic_solution
**Confidence**: medium
**Solution Steps**: 5

### Context

Database is corrupted and no backup available. Will attempt recovery methods, but may need to rebuild from scratch.

### Root Cause

Database corruption without backup. May be recoverable depending on corruption severity.

### Confidence

**MEDIUM (40-60%)** - Recovery success varies based on corruption type

### Step 1: Remove Lock Files

1. Close Boss completely
2. Navigate to Boss folder (see paths in [restore guide](01_solution_restore.md))
3. Delete all files ending in `.lock`
4. Try starting Boss

**If Boss starts**: Issue was just lock files, you're good!
**If still fails**: Continue to Step 2

### Step 2: Check Database File

1. Find `database.db` in Boss folder
2. Check file size:
   - **0 bytes**: Completely lost, need to rebuild
   - **Normal size** (KB to MB): May be recoverable

**If 0 bytes**: Skip to Step 5 (rebuild)
**If normal size**: Continue to Step 3

### Step 3: Try SQLite Recovery (Advanced)

If comfortable with command line:

1. Install SQLite tools (sqlite.org)
2. Open command prompt/terminal in Boss folder
3. Run: `sqlite3 database.db ".recover" > recovered.sql`
4. If no errors: `sqlite3 new_database.db < recovered.sql`
5. Rename `database.db` to `database_corrupt.db`
6. Rename `new_database.db` to `database.db`
7. Try starting Boss

### Step 4: Contact Support for Advanced Recovery

Before rebuilding, get help:

1. Join [Discord Support](https://discord.gg/QCxpA9yvWP)
2. Describe the issue
3. Provide:
   - Error message
   - Database file size
   - What happened before corruption
4. Support may have recovery tools

### Step 5: Rebuild From Scratch

If recovery fails, you'll need to rebuild:

**1. Rename corrupted database**:
- Rename `database.db` to `database_old.db`

**2. Start Boss** (will create fresh database):
- Opens like first time
- Everything blank

**3. Reconfigure**:
- Add sources (provider URLs, credentials)
- Add EPG sources
- Sync sources
- Create layouts
- Configure cloud storage
- Map EPGs to channels
- Output layouts

**4. Follow Quick Start Guide**:
- See [Quick Start Guide](../../../Quick_Start.md)
- Complete setup process

**What You'll Lose**:
- All layouts and channel organization
- EPG mappings
- Settings and preferences
- Channel favorites
- Custom groups

**What You Can Recover**:
- Channels (re-sync from provider)
- EPG data (re-sync from sources)
- Cloud storage (just reconnect)

### ✅ Prevention for Future

**SET UP BACKUPS NOW**:
1. After rebuilding, immediately backup database
2. Set weekly backup reminder
3. Keep multiple backup copies
4. Store backups off-system

See [restore guide](01_solution_restore.md) for backup instructions.

### Related Topics

- [Database Restore](01_solution_restore.md)
- [Database Corruption Full Guide](../../01_database_corruption_startup_failure.md)
- [Quick Start Guide](../../../Quick_Start.md)
