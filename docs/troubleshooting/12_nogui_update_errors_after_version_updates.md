# NoGUI Update Errors After Version Updates

NoGUI stops working after updating IPTVBoss version.

### Problem

NoGUI functionality breaks after updating to a new IPTVBoss version.

### Symptoms

- After update: NoGUI shows Dropbox errors
- Missing mappings.txt error
- License status "unknown" after update
- Scheduled syncs stop working after update
- Config files not found

### Why This Happens

Update changed file structure or locations. Cloud storage authorization reset during update. Permissions changed on files/folders. Configuration files not migrated properly by update process.

### Solution

**After ANY update, always do this checklist:**

**1. Open GUI and refresh license**
- Menu ’ Check license status
- Re-enter license if needed
- Don't proceed until Pro shows active

**2. Reauthorize cloud storage**
- Settings ’ IPTVBoss Settings
- Reauthorize Dropbox/Google Drive
- Complete OAuth flow
- Verify authorization success

**3. Test NoGUI manually**
- Before trusting automation
- Command line: `iptvboss -nogui`
- Watch output - does it work?
- Check for errors

**4. Check for missing files**
- Updates may relocate or delete auto-generated files
- Check logs for "file not found" errors
- Identify what's missing

**5. Regenerate auto-generated files**
- Output layouts again
- This regenerates mappings.txt and other auto files
- Layout Manager ’ Output All Layouts

**6. Verify sync schedule**
- Task Scheduler (Windows) or cron (Linux/Mac)
- Check if times still set
- Reconfigure if cleared

**7. Check file permissions**
- Updates can change folder permissions
- Verify IPTVBoss folder is readable/writable
- Especially important on Linux/Mac

### For Specific Issues

**"missing mappings.txt" specifically:**
- This file is auto-generated during output
- Output layouts to regenerate
- Check IPTVBoss folder permissions

**For scheduled tasks:**
- Verify Task Scheduler/cron entries still exist
- Updates sometimes remove scheduled tasks
- May need to recreate sync schedule in GUI

### Prevention

- Read update notes in Discord before updating
- Backup database before updating
- Test manually after updating before relying on automation
- Delay updates until you have time to test and reconfigure

### Best Practice

- Update during low-usage time
- Plan 30 minutes for post-update verification
- Keep previous version installer as backup

### Known Limitations

- Update process doesn't always preserve all configurations
- Breaking changes not always clearly communicated
- Automated tasks particularly vulnerable to updates
- Some updates require full reconfiguration

### Related Topics

- [EPG Auto-Sync Stopped Working](05_epg_auto_sync_stopped_nogui.md)
- [NoGUI Only Syncs DUMMY EPG](../faq/33_nogui_only_syncs_dummy_epg.md)
