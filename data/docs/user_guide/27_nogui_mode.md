# Understanding NoGUI Mode

NoGUI is IPTVBoss running in command-line mode without the graphical interface. This is triggered and should be setup via the sync menu, but can be actioned or setup manually.

**What NoGUI is**:
- Command-line mode that runs Boss without GUI
- Used by automatic sync schedule (created via Settings → Sync Schedule)
- Boss launches NoGUI automatically when scheduled tasks/cron jobs run

**What NoGUI does when it runs**:
- Syncs all enabled EPG sources (**Sources → Sync All EPGs**)
- Syncs all enabled playlist sources (**Sources → Sync All Sources**)
- Outputs all enabled layouts (**Output → All Layouts & EPG**)
- Exits when done

**You DON'T need to manually set up NoGUI** - it's handled automatically when you use **Settings → Sync Schedule**.

**Manual NoGUI run** (for testing only):
```bash
iptvboss -nogui
```
This runs Boss in command-line mode to test that sync works. Watch output to see what happens.

**Troubleshooting NoGUI**:
- **Completes in 5 seconds**: Not finding configuration/database - check paths
- **No output generated**: Check permissions, paths, or that layouts are enabled
- **Errors**: Check **Logs → View Logs** for error messages

**Platform-Specific Notes**:

**Windows**:
- NoGUI tasks created by Boss run via Windows Task Scheduler
- Tasks automatically run with "highest privileges" (if Boss was opened as admin)
- If sync fails, check Task Scheduler to ensure task exists and runs correctly

**Mac**:
- NoGUI jobs created by Boss use cron or launchd
- **May require**: System Preferences → Security & Privacy → Full Disk Access → Add IPTVBoss
- Launchd is more reliable than cron on macOS
- Check permissions if syncs don't run

**Linux**:
- NoGUI jobs created by Boss use cron
- User must have read/write permissions to IPTVBoss folder
- Boss automatically uses absolute paths in cron entries
- Run `crontab -l` to verify Boss-created entries exist


---

### Related Topics

- [Previous: Setting Up Automatic Syncing (noGUI)](26_automatic_syncing.md)
- [Next: New Channel Manager (Automatic Channel Imports)](28_new_channel_manager.md)
