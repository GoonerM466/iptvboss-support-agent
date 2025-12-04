# EPG Auto-Sync Stopped Working (NoGUI/Cron/Task Scheduler)

Automatic EPG syncing stops working, only manual sync works.

### Problem

Automatic EPG synchronization has stopped functioning while manual syncs work fine.

### Symptoms

- EPG data becomes stale/outdated
- Manual EPG sync works but automatic doesn't
- NoGUI completes in 5 seconds (only syncs DUMMY EPG)
- Cron job doesn't appear to run
- Windows Task Scheduler task shows as running but EPG not updating
- EPG dates get progressively more out of date

### Why This Happens

Cron job deleted or disabled after update. Task Scheduler permissions changed. NoGUI can't find database (path/permission issues). Environment variables missing in cron context. Minimal cron environment lacks GUI user's context.

### Solution

**Step 1: Verify sync schedule still configured**
- Configure via Task Scheduler (Windows) or cron (Linux/Mac)
- Check if times are still set
- If empty, schedule was lost - reconfigure

**Step 2: Check automated task exists**

For Linux/Mac:
```bash
crontab -l
```
or if configured with sudo:
```bash
sudo crontab -l
```
Verify IPTVBoss nogui entries exist

For Windows:
- Open Task Scheduler
- Look for IPTVBoss tasks
- Verify tasks are enabled (not disabled)
- Check "Last Run Result" column for errors

**Step 3: Test manual NoGUI**
```bash
iptvboss -nogui
```
Watch output. Does it sync EPGs? If manual works, problem is with automation.

**Step 4: Check NoGUI logs**
- Navigate to `IPTVBoss/logs`
- Look for nogui-specific logs
- Check for errors about database access, permissions, or paths

### Platform-Specific Fixes

**Linux:**
- Ensure cron user has read/write permissions to IPTVBoss folder
- Use absolute paths in cron entries (not relative paths like `./iptvboss`)
- Example good cron entry: `/usr/local/bin/iptvboss -nogui`
- Check you're editing correct user's crontab

**Mac:**
- Grant Full Disk Access to IPTVBoss
  - System Preferences → Security & Privacy → Privacy → Full Disk Access
  - Add IPTVBoss
- Consider using launchd instead of cron (more reliable on Mac)
- Cron on Mac has additional permission restrictions

**Windows:**
- Task must run "whether user is logged in or not"
- Run with highest privileges if permission errors
- Use absolute path to IPTVBoss executable
- Check task history for specific error codes

**Step 5: Verify sync schedule settings**
- Even if cron/task exists, schedule must be configured in GUI
- Verify Task Scheduler (Windows) or cron (Linux/Mac) times are set

### Workaround

- Run manual syncs until automated scheduling fixed
- Reduce sync frequency expectations
- EPG typically updates 1-2x daily from providers
- Syncing hourly is excessive and unnecessary

### Best Practices

- Sync 2x daily is usually sufficient (morning and evening)
- Match sync frequency to EPG provider update frequency
- Over-syncing doesn't improve data, just wastes resources

### Known Limitations

- Mac cron particularly problematic - launchd strongly recommended
- Windows updates sometimes disable Task Scheduler tasks
- Version updates can break existing schedules
- Cron environment is minimal - lacks many env variables of interactive shell

### Related Topics

- [EPG Stopped Auto-Syncing](../faq/32_epg_stopped_auto_syncing_nogui.md)
- [NoGUI Only Syncs DUMMY EPG](../faq/33_nogui_only_syncs_dummy_epg.md)
- [Mac Cron Sync Schedule Not Working](../faq/34_mac_cron_sync_schedule_not_working.md)
