# EPG Stopped Auto-Syncing with NoGUI

Check sync schedule in Task Scheduler or cron.

### Problem

EPGs stopped auto-syncing with NoGUI - automatic EPG updates not working.

### Solution

**Check sync schedule:**

1. Verify sync schedule is still set: Check Task Scheduler (Windows) or cron (Linux/Mac)
2. Check cron job/task scheduler entry still exists

**For Linux/Mac:**
```bash
crontab -l
```
or
```bash
sudo crontab -l
```
Verify IPTVBoss nogui entries exist

**For Windows:**
- Check Task Scheduler for IPTVBoss tasks
- Verify task is enabled and not failing

**Manual test:**
```bash
iptvboss -nogui
```
Check if EPGs sync manually. If manual works but automatic doesn't, it's a scheduling issue.

### If issue persist
Remove the current sync schedule and recreate

**Check logs**: IPTVBoss logs should show sync attempts. If no log entries, the scheduler isn't running IPTVBoss, should be set up again & monitored for future issues.

### Related Topics

- [EPG Auto-Sync Stopped Working](../troubleshooting/05_epg_auto_sync_stopped_nogui.md)
- [NoGUI Only Syncs DUMMY EPG](33_nogui_only_syncs_dummy_epg.md)
