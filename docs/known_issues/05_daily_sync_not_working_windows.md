# Daily Sync No Longer Working on Windows

Scheduled task exists but EPG doesn't actually update.

### Status

Task Scheduler configuration - needs per-user debugging.

### Problem

Windows Task Scheduler shows task is running but EPG data doesn't update.

### Symptoms

- Scheduled task exists in Task Scheduler
- Task appears to run
- EPG doesn't actually update
- Manual nogui works fine

### Possible Causes

- Task Scheduler disabled the task (Windows update)
- Path in task incorrect after Boss update
- Permissions changed
- Task running but Boss can't access database
- Task running under wrong user account

### Workaround

1. Delete existing Task Scheduler task
2. Recreate sync schedule from Boss GUI, ensuring you start Boss with admin rights
3. Verify new task created and enabled
4. Test task runs manually from Task Scheduler

### What's Needed

Better Task Scheduler integration, automated verification.

### Related Topics

- [EPG Auto-Sync Stopped Working](../troubleshooting/05_epg_auto_sync_stopped_nogui.md)
- [EPG Stopped Auto-Syncing](../faq/32_epg_stopped_auto_syncing_nogui.md)
