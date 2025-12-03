# NoGUI Cronjob Only Syncs DUMMY EPG

NoGUI isn't finding your configuration.

### Problem

NoGUI cronjob only syncs DUMMY EPG and finishes in 5 seconds.

### Solution

This indicates NoGUI isn't finding your configuration.

**Check:**

1. Run nogui manually and watch output: `iptvboss-c -nogui`
2. Check nogui log file for errors
3. Verify IPTVBoss database is in expected location
4. Ensure cron user has permissions to access IPTVBoss directory

**Linux-specific:**

- Cron environment is minimal (different PATH, no display)
- Use absolute paths in cron entries
- Check you're editing the correct user's crontab (user vs sudo)

**Note**: Syncing every 2 hours is excessive. EPGs typically update 1-2 times per day.

### Related Topics

- [EPG Auto-Sync Stopped Working](../troubleshooting/05_epg_auto_sync_stopped_nogui.md)
- [EPG Stopped Auto-Syncing](32_epg_stopped_auto_syncing_nogui.md)
