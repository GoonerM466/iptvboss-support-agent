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

- Lock files in `IPTVBoss\db`or cloud sync folder
- Corrupt noGUI database in `IPTVBoss\db`
- Task Scheduler disabled the task (Windows update)
- Path in task incorrect after Boss update
- Permissions changed
- Task running but Boss can't access database (partial corruption or lock file)
- Task running under wrong user account
- Power or Internet issues
- Authoriztion or HTTP issues

### Workaround

- Remove lock files locally or in cloud
- Remove partial or corrupt noGUI database from `IPTVBoss\db`
- Delete existing Task Scheduler task
- Recreate sync schedule from Boss GUI, ensuring you start Boss with admin rights
    - Verify new task created and enabled
- Test task runs manually from Task Scheduler

### Escalation

If you cannot resolve the issue contact support on [Discord](https://discord.gg/QCxpA9yvWP)

### Related Topics

- [EPG Auto-Sync Stopped Working](../troubleshooting/05_epg_auto_sync_stopped_nogui.md)
- [EPG Stopped Auto-Syncing](../faq/32_epg_stopped_auto_syncing_nogui.md)
