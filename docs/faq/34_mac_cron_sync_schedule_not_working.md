# Mac Cron Job for Sync Schedule Not Working

Cron may need Full Disk Access permission on Mac.

### Problem

Mac cron job for sync schedule isn't working - times don't save.

### Solution

**Check actual cron file:**
```bash
crontab -l
```
or if using sudo:
```bash
sudo crontab -l
```

**Verify:**

- Do cron entries actually exist?
- Are times in the correct format?
- Does cron have permission to run IPTVBoss?

**Mac-specific:**

- Cron may require Full Disk Access permission for IPTVBoss
- Check **System Preferences ’ Security & Privacy ’ Privacy ’ Full Disk Access**
- Alternatively, use **launchd** instead of cron on Mac (more reliable)

**Test**: Run nogui command manually to verify it works outside cron before debugging cron itself.

### Related Topics

- [EPG Stopped Auto-Syncing](32_epg_stopped_auto_syncing_nogui.md)
- [Mac Cron Permissions](../known_issues/08_mac_cron_permissions_sync_schedule.md)
