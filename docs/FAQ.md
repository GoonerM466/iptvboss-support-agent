# Frequently Asked Questions

Quick answers to common questions about IPTVBoss and EPGBoss.

**Can't find what you need?** Check the [Troubleshooting Guide](Troubleshooting_Guide.md) for problem-specific solutions.

---

## Table of Contents

- [TinyURL and Cloud Setup](#tinyurl-and-cloud-setup)
- [Output and Player Integration](#output-and-player-integration)
- [EPG (Electronic Program Guide)](#epg-electronic-program-guide)
- [Database and Backups](#database-and-backups)
- [Channels and Layouts](#channels-and-layouts)
- [Source Management](#source-management)
- [Automation and Syncing](#automation-and-syncing)
- [License and Pro Features](#license-and-pro-features)

---

## TinyURL and Cloud Setup

### Why isn't my TinyURL link generating when I output my playlist?

**Quick Answer**: Your TinyURL API key is missing or incorrect.

**Solution**:
1. Create a TinyURL account at tinyurl.com (if you haven't already)
2. Generate an API key with all permissions enabled
3. In IPTVBoss: Go to Settings → TinyURL and enter your API key
4. Delete the existing cloud file from your Dropbox/Google Drive website
5. Output your playlist and EPG again

**Note**: IPTVBoss now requires the new TinyURL API system (announced in Discord). Old TinyURL credentials won't work.

**See also**: [Troubleshooting: TinyURL API Authentication Failures](Troubleshooting_Guide.md#tinyurl-api-authentication-failures)

---

### I'm getting 'Unauthenticated' or '503' errors with TinyURL. What's wrong?

**'Unauthenticated' error**: Your TinyURL API key is either not entered or incorrect.
- Go to Settings → TinyURL
- Verify your API key is entered correctly (no extra spaces)

**'503 Service Unavailable' error**: TinyURL's service is temporarily down.
- Check if tinyurl.com loads in your browser
- Try again in a few minutes
- As a workaround, use direct Dropbox/Google Drive URLs

---

### TinyURL EPG links show in cloud view, but the M3U link is missing. Why?

This usually means the M3U file failed to upload while the EPG succeeded.

**Solution**:
1. Verify both Dropbox/Google Drive AND TinyURL API credentials are configured
2. Check IPTVBoss logs for upload errors
3. Delete existing cloud files from your cloud storage website
4. Re-output your layout's playlist (.m3u) and EPG
5. Check your cloud storage to confirm both files uploaded before checking TinyURL links

**See also**: [Cloud Storage Upload Failures](Troubleshooting_Guide.md#cloud-storage-uploadsync-failures)

---

### How do I export or download the M3U file to my laptop?

IPTVBoss generates files on cloud storage, and local files.

**To get the files**:
1. Set up cloud storage (Dropbox or Google Drive) in IPTVBoss settings
2. Output your layout: Layout Manager → Output Current Layout M3U and EPG
3. Files automatically upload to your cloud storage
4. Access via "View Cloud Links" or TinyURL
5. **Use these URLs in your player apps**
6. They are also output locally to 'IPTVBoss/output'

**To download the cloud file**:
- Open the cloud URL in your browser (it will download)
- Or access files directly in your Dropbox/Google Drive folder

**See also**: [Quick Start Guide](Quick_Start.md) for initial setup

---

## Output and Player Integration

### Why aren't my deleted channels/groups showing up as removed in TiviMate?

You need to complete all three steps:

1. **In IPTVBoss**: Delete channels/groups using the (-) button and save
2. **Output**: Go to Layout Manager → Output Current Layout M3U and EPG
3. **In TiviMate**: Update your playlist (Settings → Playlists → Select playlist → Update)

Deleting in IPTVBoss alone won't affect your player until you output the new files and update the playlist in your player app.

**See also**: [Changes Not Reflecting in Player Apps](Troubleshooting_Guide.md#changes-not-reflecting-in-player-apps)

---

### Changes I make in IPTVBoss aren't showing up in my player. What am I missing?

IPTVBoss doesn't automatically push changes to your player.

**Required workflow**:
1. Make your changes in IPTVBoss (layouts, EPG mappings, channel edits, etc.)
2. **Output** your layout: Layout Manager → Output Current Layout's M3U and EPG
3. Wait for files to upload to your cloud storage
4. **Update** the playlist in your player app (TiviMate: Settings → Playlists → Update)

If using TinyURL, verify your TinyURL links have updated before updating the player.

---

### My IPTV provider shows ALL categories in my player despite filtering in IPTVBoss. Why?

Your player is loading your provider's original M3U file instead of IPTVBoss's filtered output.

**Check**:
1. Verify in your player that you're using the IPTVBoss M3U URL (from Dropbox/Google Drive/TinyURL), NOT your provider's direct URL
2. Confirm you've output the layout from IPTVBoss after making changes
3. Update the playlist in your player after outputting

**If still showing all categories**: Remove the playlist completely from your player and re-add it using only the IPTVBoss URL. This ensures no cached provider data remains.

---

### EPG shows no info in IPTVBoss but TiviMate shows the guide correctly. Why?

If TiviMate shows info but Boss doesn't, TiviMate is likely using cached EPG data from before, or it's using a different EPG source.

**Test**: Add the playlist fresh in TiviMate (completely remove old one first). If TiviMate truly gets EPG from your Boss output, fresh playlist shouldn't have data if Boss doesn't.

**Check**:
1. Open EPG in Boss for that channel - is it truly empty?
2. Check the EPG mapping for that channel in Boss
3. TiviMate heavily caches EPG data - it may be showing old cached data

---

### After I output, no streams are found in my player. What happened?

**Troubleshooting steps**:
1. **Test your URLs**: Paste M3U and EPG URLs into your browser
2. Let the files download, then open with a text editor
3. Check if files contain actual stream URLs or are empty/malformed
4. Verify cloud storage successfully uploaded the files (check file sizes)

**If files are empty or wrong**:
- Output didn't complete successfully
- Cloud upload failed
- Wrong layout was selected during output

**If files look good but player says no streams**:
- Player might be caching old version
- Remove and re-add playlist in player completely
- Verify you're using the correct URL format

---

## EPG (Electronic Program Guide)

### I lost all my EPG mappings after my service expired/renewed. Can I recover them?

If you added the source as an M3U URL with credentials, **new** credentials create a new source identity, which loses all mappings.

**Recovery**:
1. Restore from a recent database backup: Menu → Restore → Local or Cloud
2. Check IPTVBoss/backup folder for dated backup files

**Prevention**:
- Use XC API connection instead of M3U when available (preserves mappings better)
- Keep regular database backups
- Create a manual backup before renewing expired services

**See also**: [Source Sync Failures](Troubleshooting_Guide.md#source-sync-failures-and-updates-breaking-layouts)

---

### EPG mapping for a specific group (like US|Movies) keeps reverting after I save. Why?

**Check these settings**:
1. Are you clicking Save after mapping?
2. Do you have "Auto Assign" enabled in group options? (This can auto-remap channels)
3. Are you syncing sources immediately after mapping? (Can overwrite changes)

**Solution**:
1. Disable "Auto Assign" for the problematic group (Group Options)
2. Map your EPG for the channels
3. Click Save
4. Don't sync sources immediately
5. Output and verify mapping persists

If Auto Assign is enabled, it can fight your manual mapping during sync operations.

---

### I created additional layouts/EPGs but they only show guide for the first layout, then "No Information" for the others. Why?

**Use Universal EPG instead**:
1. Set up Universal EPG once: Sources → Universal EPG Options
2. All layouts automatically use the same EPG source
3. No need to manage multiple EPG files
4. Saves significant cloud bandwidth

**If you must use individual EPGs**:
- Check "Days to Keep" settings for the layout (not just source)
- Verify EPG source is syncing properly (check last sync time)
- Look for override settings affecting EPG duration
- You may need to delete cached EPG files and re-sync

**Recommendation**: Universal EPG is the recommended approach for multiple layouts.

---

### Specific EPG sources (USA, USA Local) show no info after a couple of hours. How do I fix this?

**Check Days to Keep settings**:
1. **Sources → Sources Manager**
2. Highlight your EPG source
3. Click **EPG Settings**
4. Check **"Days to Keep"** - default is **3 days**
5. Set to **7 days** or **ALL** for full coverage
6. Also check for EPG overrides on specific channels (if EPG Override enabled)

**Cache corruption fix**:
1. Shut down IPTVBoss completely
2. Navigate to IPTVBoss/cache folder
3. Delete USA and USA Local EPG files
4. Start IPTVBoss
5. **Sources → Sync All EPGs**
6. **Output → Current M3U & EPG**
7. Test in player

Make sure "Days to Keep" is not set to 0 or very low (1-2). Default is 3 days which may not be enough.

**See also**: [Specific EPG Sources Show Limited Information](Troubleshooting_Guide.md#specific-epg-sources-show-limited-or-no-information)

---

### EPG is not updating and keeps showing the same old TinyURL. How do I force new links?

**Force TinyURL regeneration**:
1. Delete cloud files from your Dropbox/Google Drive (via the website)
2. Save your TinyURL API settings again in IPTVBoss
3. Output layouts again
4. New TinyURL links should generate

**Why this happens**: TinyURL links are persistent (same short URL for same file). If the cloud file hasn't changed, TinyURL stays the same.

**Check**: Are your EPGs actually syncing? If EPG content isn't updating, new TinyURLs won't help - fix EPG sync first.

**See also**: [EPG Auto-Sync Stopped Working](Troubleshooting_Guide.md#epg-auto-sync-stopped-working-noguicrontask-scheduler)

---

### How do I show live sports with "NEW" tag instead of "LIVE" for DVR recording?

Some DVR software (Emby, Plex, etc.) only records episodes marked "NEW", not "LIVE".

**Solution**:
1. Go to Settings → Manage Live Tags
2. Change "Live Tag Format" to "New"
3. Output your playlist and EPG
4. Update in your player/DVR

This tags live sports events as "NEW" so your DVR will record them.

---

## Database and Backups

### Where are IPTVBoss files and folders located on my system?

**IPTVBoss Folder Locations**:

**Windows**:
```
C:\Users\{user}\IPTVBoss
```

**Linux**:
```
/home/{user}/IPTVBoss
```

**Mac**:
```
~/Library/Application Support/IPTVBoss/
```

**Headless Linux (installed on Windows)**:
```
/home/{user}/IPTVBoss/C:
```
*Or custom drive letter (e.g., D:) if Windows installation uses custom path*

**Important Subfolders**:

- `/backup` - Automatic database backups (restore from here if needed)
- `/db` - Database files (do not manually edit)
- `/cache` - EPG cache files
- `/logs` - Log files (helpful for troubleshooting)
- `/output` - Local M3U/XML output files

**Tips**:
- **Backup folder**: Check here when restoring (Menu → Restore → Local)
- **Logs folder**: Share logs when asking for support (remove sensitive info first)
- **Output folder**: Find locally generated M3U/EPG files here (if not using cloud)

---

### IPTVBoss shows no layouts or sources, and local restore crashes the app. How do I recover?

**Try multiple backups** (recent backup might also be corrupted):
1. Close IPTVBoss completely
2. Navigate to IPTVBoss/backup folder
3. Note there are multiple dated backup files
4. Start IPTVBoss and try Menu → Restore → Local
5. If it crashes, try restoring from an older backup file
6. If all backups fail, check logs (IPTVBoss/logs) for specific errors

**Alternative**:
- Try cloud (reccomended) or URL restore if you have cloud sync enabled
- Contact support with logs

**See also**: [Database Corruption and Failed Startup](Troubleshooting_Guide.md#database-corruption-and-failed-startup)

---

### IPTVBoss says "Database failed to load or is corrupt" and freezes. What now?

**Immediate fixes**:
1. Force close IPTVBoss (Task Manager on Windows)
2. Go to IPTVBoss/db folder and delete any files with "lock" in the name
3. Restart IPTVBoss - it should attempt auto-restore
4. If still frozen, manually restore: Menu → Restore → Local, Cloud or URL

**If restore fails**:
- Try older backup files from IPTVBoss/backup
- Verify you're still on Pro license (may need to re-enter license key)
- Check if you've migrated your account to the new IPTVBoss website
- Post logs in support Discord for help

**See also**: [Troubleshooting: Database Corruption](Troubleshooting_Guide.md#database-corruption-and-failed-startup)

---

### All my playlists disappeared and I lost my Pro license. How do I get everything back?

**Don't panic - your backups should still exist.**

**Recovery steps**:
1. Re-enter your Pro license key (Menu → Activate Pro)
2. Restore database: Menu → Restore → Local or Cloud
3. Select the most recent backup that predates the problem
4. If you've migrated to the new IPTVBoss website, make sure you're using new credentials

**If restore doesn't work**:
- Try multiple backup files (the newest might be corrupted too)
- Check that IPTVBoss/backup folder exists and contains .backup files
- Verify disk isn't full
- Check logs for specific error messages

---

### IPTVBoss keeps asking me to reauthorize Boss Pro and won't restore my database. What's wrong?

**License authorization loop fix**:
1. Verify your Pro license is still active (check purchase date)
2. If using old website credentials, migrate to the new IPTVBoss website
3. Enter the license key from the new website
4. Try restore again after successful Pro activation

**If activation fails**:
- Check internet connection (Pro license validates online)
- Verify license key is copied correctly (no extra spaces)
- Check if Boss Pro website is accessible
- Wait several minutes after entering the key (some users report delays)

**Error "Table SETTINGS not found"**: Database is completely empty/corrupt. You MUST restore from a backup before Boss Pro can activate.

---

### Will my database backup work if I reinstall Windows/IPTVBoss or move to a new computer?

Yes, database backups are portable.

**Steps**:
1. **Before reinstall**: Copy the entire IPTVBoss folder (especially IPTVBoss/db & IPTVBoss/backup directories) to USB or external drive
2. **After reinstalling IPTVBoss**: 
  - Start the program once and shut down
  - Copy your saved IPTVBoss folders to the IPTVBoss folder on the new install/computer
  - Start IPTVBoss & make sure transfer is sucessfull. If it isn't continue below
3. Use Menu → Restore → Local
4. Re-Authorize cloud

**Alternative**: If using cloud sync (Dropbox/Google Drive), you can restore from cloud after reinstalling however you must enter your cloud settings first.

---

### Every time I open IPTVBoss (every 1-2 weeks) it shows no data and I have to restore. Why does this keep happening?

Recurring database loss indicates a deeper issue.

**Check logs** (IPTVBoss/logs folder) for patterns:
- Database write errors
- Disk full errors
- Permission errors
- Backup/sync conflicts

**Common causes**:
- Cloud sync conflict (multiple instances running)
- Insufficient disk space
- Antivirus interfering with database files
- Database on network drive or slow storage
- Memory issues during shutdown

**Temporary workaround**: Restore from Dropbox backup file (change last digit to 0). Keep external backups until root cause is found.

**See also**: [Known Issues: Recurring Database Wipes](Known_Issues.md#recurring-database-wipes-every-1-2-weeks)

---
..........THIS PROBABLY NEEDS TO BE REMOVED........
### I'm getting database corruption errors during NoGUI backup runs. How do I fix this?

This is an advanced issue requiring database investigation.

**Investigation**:
1. Check IPTVBoss logs for specific corruption errors

**Solution from user experience**:
- One user found an old channels table from a deleted source causing corruption
- Dropping old tables referencing non-existent categories fixed the issue

**Workaround (not recommended long-term)**:
- Set database backup days to 0
- Disable cloud DB backup
- This prevents corruption during backup but loses protection

Issue likely stems from improper source deletion or failed database migrations during updates.

---
.............................................
## Channels and Layouts

### Channels are sorted incorrectly (A-Z not working). How do I fix sorting?

Channel sorting uses the first character/number in the channel name. If channels start with prefixes like "CA", "US", numbers, or symbols, these determine sort order.

**Solution**: Remove prefixes that interfere with sorting:
1. Edit channel names to remove country codes or numbering prefixes
2. Or use a consistent prefix format for all channels
3. Re-output your playlist after making changes

**Example**: "CA: ESPN" and "ESPN" will sort under "C" and "E" respectively, not together.

---

### Can I copy/duplicate a layout to use for another source or user?

**For identical layouts across sources**: Use the User System
- This is designed for creating the same layout for multiple users/sources
- See documentation for User System setup

**For similar but customizable layouts**:
- Use the user system & import groups from th primary layout
- You'll need to manually manage these groups and channel
- You can also import groups from other layouts as "linked" groups, which will be synced with the layout they were imported from

**If both sources are from the same server**: User System is definitely what you want.

---

### Can I copy groups from one layout to another?

**If you want an exact copy**: Import from the other layout, enabling "import as linked"

**If you want a customizable copy**:
- Import from the other layout without linking

**Question**: Do you want the groups to always stay identical? If yes, use linking.

---

### After syncing my source, all my custom layout channels disappeared. Can I recover them?

**Your provider likely changed channel names/IDs**, causing IPTVBoss to see them as removed.

**Recovery**:
1. Restore database backup from before the sync
2. All your channel mapping should return

**Prevention**:
- Use XC sources instead of M3U when possible (less susceptible to changes)
- Check logs for "... Was removed" messages after syncs
- Consider preventing source sync temporarily if your provider is unstable

**If you must remap everything**: Provider changed their channel structure fundamentally. Keep frequent backups before syncing.

**See also**: [Source Sync Failures](Troubleshooting_Guide.md#source-sync-failures-and-updates-breaking-layouts)

---

### All my channels disappeared from layout after syncing, but groups remain. Can I recover?

**Restore immediately**:
1. Menu → Restore → Local, Cloud or URL
2. Select backup from before the sync
3. This recovers your channel mappings

**Why it happened**:
- Provider changed channel structure/IDs
- Boss saw all channels as "removed"
- Your group structure remained but channel assignments were lost

**Prevention**: Keep regular backups before syncing. Use XC sources when possible (more stable).

---

## Source Management

### I'm getting "Could not load categories, check your source link" error. What's wrong?

**Source validation failed**:
1. Verify M3U URL is accessible (paste in browser, should download)
2. Check username/password are correct
3. Ensure provider service is active
4. Try source URL in VLC to verify it's valid M3U format

**Common causes**:
- Expired service/credentials
- Provider URL changed
- M3U format is malformed
- Network/firewall blocking access

**Recommendation**: Try XC API instead of M3U URL if your provider offers it - more reliable.

---

## Automation and Syncing

### EPGs stopped auto-syncing with NoGUI. How do I fix automatic EPG updates?

**Check sync schedule**:
1. Verify sync schedule is still set: Check Task Scheduler (Windows) or cron (Linux/Mac)
2. Check cron job/task scheduler entry still exists

**For Linux/Mac**:
```bash
crontab -l
```
or
```bash
sudo crontab -l
```
Verify IPTVBoss nogui entries exist

**For Windows**:
- Check Task Scheduler for IPTVBoss tasks
- Verify task is enabled and not failing

**Manual test**:
```bash
iptvboss -nogui
```
Check if EPGs sync manually. If manual works but automatic doesn't, it's a scheduling issue.

**Check logs**: IPTVBoss logs should show sync attempts. If no log entries, the scheduler isn't running IPTVBoss.

**See also**: [EPG Auto-Sync Stopped Working](Troubleshooting_Guide.md#epg-auto-sync-stopped-working-noguicrontask-scheduler)

---

### NoGUI cronjob only syncs DUMMY EPG and finishes in 5 seconds. What's wrong?

This indicates NoGUI isn't finding your configuration.

**Check**:
1. Run nogui manually and watch output: `iptvboss-c -nogui`
2. Check nogui log file for errors
3. Verify IPTVBoss database is in expected location
4. Ensure cron user has permissions to access IPTVBoss directory

**Linux-specific**:
- Cron environment is minimal (different PATH, no display)
- Use absolute paths in cron entries
- Check you're editing the correct user's crontab (user vs sudo)

**Note**: Syncing every 2 hours is excessive. EPGs typically update 1-2 times per day.

---

### Mac cron job for sync schedule isn't working - times don't save. How do I fix it?

**Check actual cron file**:
```bash
crontab -l
```
or if using sudo:
```bash
sudo crontab -l
```

**Verify**:
- Do cron entries actually exist?
- Are times in the correct format?
- Does cron have permission to run IPTVBoss?

**Mac-specific**:
- Cron may require Full Disk Access permission for IPTVBoss
- Check System Preferences → Security & Privacy → Privacy → Full Disk Access
- Alternatively, use launchd instead of cron on Mac (more reliable)

**Test**: Run nogui command manually to verify it works outside cron before debugging cron itself.

---

### After OS upgrade to Windows 11, files aren't syncing to devices. What broke?

**Check**:
- IPTVBoss folder permissions after OS upgrade
- Firewall rules might have reset

If you copied the IPTVBoss folder from Windows 10, it should work, but cloud reauthorization is often needed after OS changes.

---

## License and Pro Features

### My subscription expired and now I can't restore my database. How do I recover?

**If you renewed with a new key**:
1. Don't try restoring old database first
2. Install IPTVBoss fresh
3. Enter NEW license key
4. After Pro is activated, then restore from backup
  - Ensure token is NEW one after restoring

**If using old database backup with new key**:
- Some users report database backups tied to old license keys
- Try system restore to before expiration, open Boss, enter new key while old DB is loaded
- Or restore from external drive backup if you have one

**Lesson**: Keep external backups before license expiration, and update your license before it expires to avoid this issue.

---

### Setting up IPTVBoss on new machine - restore keeps removing Boss token and failing. What's wrong?

**Setup order matters**:
1. Install IPTVBoss on new machine
2. Enter Pro license key FIRST
3. Set up cloud credentials (Google Drive/Dropbox)
4. THEN restore from cloud

**Check**:
- Using new IPTVBoss website credentials (not old site)
- License is still active
- Internet connection works
- Logs for specific error messages

Logs help diagnose - post in support Discord with cleaned logs (remove provider names and sensitive info).

---

### I'm prompted to upgrade to Pro despite having a valid license. Why?

**Check**:
1. Verify your license is still active (check purchase date/subscription)
2. Migrate to the new IPTVBoss website if using the old system
3. Use the license key from the NEW website, not old credentials
4. Ensure internet connection is active (validates online)

**If still failing**:
- Check if Boss Pro website is accessible
- Wait several minutes after entering the key
- Contact support if license shows active but won't validate

---

## Still Need Help?

- **Check the** [Troubleshooting Guide](Troubleshooting_Guide.md) for detailed problem-solution guides
- **Review** [Known Issues](Known_Issues.md) for unresolved problems and workarounds
- **Post in** Discord support channel with logs (clean sensitive info first)
- **See** [Quick Start Guide](Quick_Start.md) if you're new to IPTVBoss
