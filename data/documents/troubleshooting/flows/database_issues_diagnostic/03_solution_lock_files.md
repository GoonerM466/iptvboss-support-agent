# Solution: Remove Lock Files

**Flow ID**: database_issues
**Type**: diagnostic_solution
**Confidence**: high
**Solution Steps**: 3

### Context

Boss freezes on startup or won't start due to lock files from previous crash or improper shutdown.

### Root Cause

Lock files prevent multiple Boss instances from accessing database simultaneously. After crash, lock files remain and block access.

### Confidence

**HIGH (90%+)** - Lock file removal usually resolves freeze-on-startup issues

### Step 1: Close All Boss Instances

1. Close Boss if it's open (or force close if frozen)
2. **Windows**: Task Manager → End "IPTVBoss" process
3. **Mac**: Activity Monitor → Quit "IPTVBoss"
4. **Linux**: `killall iptvboss` or System Monitor

### Step 2: Delete Lock Files

1. Navigate to Boss folder:
   - **Windows**: `C:\Users\[YourName]\AppData\Roaming\IPTVBoss`
   - **Mac**: `~/Library/Application Support/IPTVBoss`
   - **Linux**: `~/.config/IPTVBoss`
2. Look for files ending in `.lock`:
   - `database.db.lock`
   - `iptvboss.lock`
   - Any other `.lock` files
3. **Delete all** `.lock` files
4. If hesitant, rename them to `.lock.old` instead

### Step 3: Restart Boss

1. Open IPTVBoss normally
2. Should start without freezing
3. If still issues, see [Database Recovery](02_solution_recovery.md)

### ✅ Prevention

**Always close Boss properly**:
- Use File → Exit or close button
- Don't force close unless frozen
- Don't shut down PC with Boss running

**After crashes**:
- Wait 30 seconds before restarting
- Check for lock files first
- Delete lock files if present

### Related Topics

- [Database Corruption](../../01_database_corruption_startup_failure.md)
- [Application Crashes](../../03_application_crashes_startup_updates.md)
