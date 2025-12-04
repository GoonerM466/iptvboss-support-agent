# Mac Cron Permissions for Sync Schedule

Cron entries created successfully but don't run on macOS.

### Status

macOS security limitation - documented workaround.

### Problem

Cron jobs for IPTVBoss sync don't execute on macOS despite being configured correctly.

### Symptoms

- Cron entries created successfully
- Cron should run but doesn't
- Manual nogui works fine
- Times don't save in Boss GUI

### Root Cause

macOS requires explicit permissions for cron to access files.

### Solution

**Documented but often missed:**

1. Grant Full Disk Access to IPTVBoss:
   - System Preferences → Security & Privacy → Privacy
   - Full Disk Access → Add IPTVBoss
2. Or switch from cron to launchd (more Mac-native)

### Recommendation

Boss should use launchd on Mac by default, not cron.

### Escalation

If you cannot resolve the issue contact support on [Discord](https://discord.gg/QCxpA9yvWP)

### Related Topics

- [Mac Cron Sync Schedule Not Working](../faq/34_mac_cron_sync_schedule_not_working.md)
- [EPG Auto-Sync Stopped Working](../troubleshooting/05_epg_auto_sync_stopped_nogui.md)
