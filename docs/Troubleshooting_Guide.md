# Troubleshooting Guide

Problem-solution guide for common IPTVBoss/EPGBoss issues. Issues are organized by severity and category.

**Quick Start**: If you know your problem, use Ctrl+F to search for keywords like "crash", "sync", "EPG", etc.

---

## Table of Contents

### Critical Issues (Blocks Major Functionality)
- [Database Corruption and Failed Startup](#database-corruption-and-failed-startup)
- [Source Sync Failures and Updates Breaking Layouts](#source-sync-failures-and-updates-breaking-layouts)
- [Application Crashes on Startup or After Updates](#application-crashes-on-startup-or-after-updates)

### High Priority (Causes Significant Issues)
- [EPG Mapping Loss or Auto-Revert](#epg-mapping-loss-or-auto-revert)
- [EPG Auto-Sync Stopped Working (NoGUI/Cron/Task Scheduler)](#epg-auto-sync-stopped-working-noguicrontask-scheduler)

### Medium Priority (Annoying But Workable)
- [TinyURL API Authentication Failures](#tinyurl-api-authentication-failures)
- [Cloud Storage Upload/Sync Failures](#cloud-storage-uploadsync-failures)
- [Changes Not Reflecting in Player Apps](#changes-not-reflecting-in-player-apps)
- [Specific EPG Sources Show Limited or No Information](#specific-epg-sources-show-limited-or-no-information)
- [License Validation Failures and Loops](#license-validation-failures-and-loops)
- [Port-Migration Database and Setup Recovery Issues](#port-migration-database-and-setup-recovery-issues)
- [NoGUI Update Errors After Version Updates](#nogui-update-errors-after-version-updates)

---

## Critical Issues

### Database Corruption and Failed Startup

**Problem**: IPTVBoss won't start, crashes immediately, or reports database corruption

**Symptoms**:
- IPTVBoss won't open or immediately closes
- Error message: "Database failed to load or is corrupt"
- GUI running in Task Manager but no window appears on screen
- All playlists and layouts disappeared
- Lost Pro license activation
- Application freezes during startup

**Why this happens**: Database corruption from improper shutdown, disk full, file system errors, or lock file conflicts. Lock files from previous crashed sessions prevent new database access and create illusion of corruption.

**Solution**:

1. **Force close all IPTVBoss processes**
   - Windows: Open Task Manager (Ctrl+Shift+Esc) → Find IPTVBoss → End Task
   - Mac: Activity Monitor → Find IPTVBoss → Force Quit

2. **Delete lock files**
   - Navigate to `IPTVBoss/db` folder
   - Delete ALL files with "lock" in the filename (e.g., `database.lock`, `lockfile`)
   - These files prevent database access to avoid corruption from multiple instances

3. **Restart IPTVBoss**
   - IPTVBoss will attempt auto-recovery
   - If successful, you'll see your data restored

4. **If still fails: Manual restore**
   - Open IPTVBoss (may show empty)
   - Settings → Restore Database → Local
   - Select most recent backup that predates the problem
   - Look in `IPTVBoss/backup` folder for dated backups

5. **If recent backups fail**
   - Try progressively older backup files
   - Newest backup might also be corrupted
   - Go back several days if needed

6. **Re-enter Pro license if needed**
   - Settings → IPTVBoss Pro Settings
   - Enter license key


**Prevention**:
- Always close IPTVBoss properly (don't force quit)
- Ensure adequate disk space
- Don't run multiple instances simultaneously
- Keep antivirus from quarantining database files
- Don't store database on network drives

**Known limitations**:
- Multiple instances or cloud sync conflicts can cause recurring corruption
- Antivirus may interfere with database file access
- Database on slow network storage increases corruption risk

**See also**: [FAQ: Database and Backups](FAQ.md#database-and-backups)

---

### Source Sync Failures and Updates Breaking Layouts

**Problem**: Syncing source causes channels to disappear or sync errors

**Symptoms**:
- All channels disappear after syncing source
- Groups remain but channels are gone
- Error messages during source update
- Error: "File does not exist"
- Provider channels not updating despite successful sync
- Layouts completely empty after sync

**Why this happens**: Provider changed channel names, IDs, or entire structure. IPTVBoss treats renamed channels as "removed channels" and new channels as additions, completely losing your layout associations. M3U sources are particularly susceptible - XC API sources handle changes better.

**Solution**:

1. **BEFORE syncing**:
   - Check provider announcements for structure changes
   - Switch your source to XC before the next scheduled sync

2. **After problematic sync (Recovery)**:
   - Settings → Restore Database
   - Select backup from immediately before the sync
   - Your channel mapping will return to pre-sync state

3. **For recurring issues**:
   - Switch to XC API source if provider offers it (more stable than M3U)
   - XC sources handle credential and minor structure changes better
   - Check logs for "... Was removed" messages to understand what changed

4. **For series sync errors specifically**:
   - Go to Source settings
   - Enable "Ignore Series" option
   - Retry sync
   - This bypasses series/VOD sync which often causes errors

**Workaround**: If provider frequently changes structure:
- XC is highly recommended
- Consider not syncing automatically
- Do manual syncs only when you have time to remap if needed
- Keep recent backup immediately before each sync attempt
- Some users sync weekly instead of daily to reduce exposure

**Why recovery works**: Backups preserve your channel-to-layout associations. Since providers rarely delete actual streams (just rename them), your backed-up associations often still work even with "old" IDs.

**Known limitations**:
- No way to prevent provider changes from breaking mappings
- M3U sources more fragile than XC sources
- Credential changes with M3U sources create entirely new source identity (complete mapping loss)
- Provider structural changes can't be worked around - only recovered from

**See also**: [FAQ: Lost EPG Mappings](FAQ.md#i-lost-all-my-epg-mappings-after-my-service-expiredrenewed-can-i-recover-them)

---

### Application Crashes on Startup or After Updates

**Problem**: IPTVBoss crashes when launching or immediately after opening

**Symptoms**:
- Boss loads splash screen then crashes
- Crashes immediately after opening full window
- Reinstalling doesn't fix crashes
- Crashes after database restore
- Works once after reinstall, crashes on subsequent opens

**Why this happens**: Corrupted database loaded on startup, corrupted settings/preferences, lock files preventing startup, incompatible database from different version, disk space exhausted, or log files consuming excessive space.

**Solution**:

1. **Force close all IPTVBoss instances** (Task Manager/Activity Monitor)

2. **Delete lock files**
   - Navigate to `IPTVBoss/db` folder
   - Delete files with "lock" in name

3. **Check disk space**
   - Ensure adequate free space on drive with IPTVBoss
   - Low disk space causes startup failures

4. **Check log file sizes**
   - Navigate to `IPTVBoss/logs` folder
   - If logs are excessively large (>50MB), archive or delete old ones
   - Keep most recent log for diagnostics

5. **If crashes persist: Clean reinstall**
   - Move entire IPTVBoss folder to Documents (preserves backups)
   - Reinstall IPTVBoss fresh
   - After installation, restore from backup in Documents folder
   - This provides clean environment while preserving your data

6. **If crash after restore**
   - Try older backup file
   - Recent backup might also be corrupted
   - Go back to last known good state

7. **Get diagnostic information**
   - Before moving IPTVBoss folder, copy most recent log from `IPTVBoss/logs`
   - Post in support Discord with log (clean sensitive provider info first)
   - Logs show crash reason

**Prevention**:
- Keep IPTVBoss updated
- Close properly (don't force quit)
- Monitor disk space
- Archive old logs periodically

**Known limitations**:
- Some database corruptions prevent clean restore
- Version compatibility issues during major upgrades
- Logs location and cleanup not well documented

**See also**: [FAQ: IPTVBoss won't open](FAQ.md#iptvboss-shows-no-layouts-or-sources-and-local-restore-crashes-the-app-how-do-i-recover)

---

## High Priority Issues

### EPG Mapping Loss or Auto-Revert

**Problem**: EPG mappings disappear or revert to unmapped shortly after saving

**Symptoms**:
- EPG mappings disappear after service expiration/renewal
- Mapped EPG reverts to unmapped minutes after saving
- Specific groups (US|Movies, VOD categories) won't stay mapped
- EPG shows "no information" despite being mapped
- Mapping works temporarily then undoes itself

**Why this happens**: Auto-assign feature conflicts with manual mapping. Service credential changes (M3U sources especially) lose mapping. Group-level auto-mapping overrides your channel-level manual mapping during sync operations.

**Solution**:

1. **Disable conflicting Auto-Assign**
   - Navigate to the problematic group
   - Group Options → Disable "Auto Assign"
   - This prevents automatic remapping during syncs

2. **Map EPG manually**
   - Select channels needing EPG
   - Assign EPG sources
   - Click Save (important!)

3. **Test persistence**
   - Don't sync sources immediately after mapping
   - Verify mapping persists before syncing
   - Output and test in player

4. **For lost mappings after renewal**:
   - Settings → Restore Database
   - Select database backup from before credential change
   - This recovers all previous mappings

5. **Output and verify**
   - Layout Manager → Output Current Layout M3U and EPG
   - Check that EPG data appears in output

**For service renewal specifically**:
- Create backup BEFORE renewing
- If possible, try using XC API instead of M3U
- XC sources better handle credential changes

**Workaround**:
- Keep frequent backups (daily) during active mapping work
- Use XC API sources instead of M3U when possible
- XC sources more resistant to credential changes
- Avoid syncing sources immediately after EPG mapping work

**Prevention**:
- Default Auto-Assign to OFF for VOD and movie categories
- Backup before service renewals
- When provider gives new credentials, don't immediately remove old source - set up new source as test first

**Known limitations**:
- Auto-assign logic can be aggressive
- M3U source identity is tied to credentials - no way to preserve mappings through credential changes without XC
- Group vs channel-level mapping hierarchy not always intuitive

**See also**: [FAQ: EPG Mapping Reverts](FAQ.md#epg-mapping-for-a-specific-group-like-usmovies-keeps-reverting-after-i-save-why)

---

### EPG Auto-Sync Stopped Working (NoGUI/Cron/Task Scheduler)

**Problem**: Automatic EPG syncing stops working, only manual sync works

**Symptoms**:
- EPG data becomes stale/outdated
- Manual EPG sync works but automatic doesn't
- NoGUI completes in 5 seconds (only syncs DUMMY EPG)
- Cron job doesn't appear to run
- Windows Task Scheduler task shows as running but EPG not updating
- EPG dates get progressively more out of date

**Why this happens**: Cron job deleted or disabled after update. Task Scheduler permissions changed. NoGUI can't find database (path/permission issues). Environment variables missing in cron context. Minimal cron environment lacks GUI user's context.

**Solution**:

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

**Platform-specific fixes**:

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

**Workaround**:
- Run manual syncs until automated scheduling fixed
- Reduce sync frequency expectations
- EPG typically updates 1-2x daily from providers
- Syncing hourly is excessive and unnecessary

**Best practices**:
- Sync 2x daily is usually sufficient (morning and evening)
- Match sync frequency to EPG provider update frequency
- Over-syncing doesn't improve data, just wastes resources

**Known limitations**:
- Mac cron particularly problematic - launchd strongly recommended
- Windows updates sometimes disable Task Scheduler tasks
- Version updates can break existing schedules
- Cron environment is minimal - lacks many env variables of interactive shell

**See also**: [FAQ: EPGs stopped auto-syncing](FAQ.md#epgs-stopped-auto-syncing-with-nogui-how-do-i-fix-automatic-epg-updates)

---

## Medium Priority Issues

### TinyURL API Authentication Failures

**Problem**: TinyURL integration not working, authentication errors

**Symptoms**:
- "Unauthenticated" error when outputting
- "503 Service Unavailable" from TinyURL
- TinyURL links not generating
- EPG URLs show in cloud view but M3U URL missing
- Cloud files upload successfully but no TinyURL links created

**Why this happens**: TinyURL API key not configured or incorrect. Users haven't migrated from old TinyURL system to new API-based system (announced in Discord). TinyURL service experiencing temporary outage.

**Solution**:

1. **Create TinyURL account** (if not already done)
   - Go to tinyurl.com
   - Create free account
   - This is required for new TinyURL API system

2. **Generate API key**
   - Log into TinyURL account
   - Navigate to API settings
   - Generate API key
   - Enable all permissions

3. **Configure in IPTVBoss**
   - Settings → TinyURL
   - Enter API key (copy-paste carefully - no spaces)
   - Save settings

4. **Force fresh generation**
   - Delete cloud files from Dropbox/Google Drive website
   - Re-output layout from IPTVBoss
   - New TinyURL links should generate

**For specific errors**:

**"Unauthenticated"**:
- API key not entered or incorrect
- Copy API key again, ensure no spaces or truncation
- Verify in TinyURL account that API key is active

**"503 Service Unavailable"**:
- TinyURL service is down (temporary)
- Check if tinyurl.com loads in browser
- Wait 10-15 minutes and retry
- Workaround: Use direct Dropbox/Google Drive URLs temporarily

**EPG links work but M3U missing**:
- M3U upload might have failed (larger file)
- Check IPTVBoss logs for upload errors
- Verify both files exist in cloud storage
- May need to reauthorize cloud storage

**Workaround**: Use direct Dropbox/Google Drive URLs without TinyURL if TinyURL has ongoing issues. Players accept full URLs, TinyURL is just for convenience.

**Migration note**: IPTVBoss switched from anonymous TinyURL to TinyURL API system. Old anonymous TinyURL no longer works. All users must create TinyURL accounts.

**Known limitations**:
- Migration announcement in Discord - not all users aware of change
- API key setup not intuitive for non-technical users
- Error messages don't clearly indicate "need to create TinyURL account"

**See also**: [FAQ: TinyURL and Cloud Setup](FAQ.md#tinyurl-and-cloud-setup)

---

### Cloud Storage Upload/Sync Failures

**Problem**: Files not uploading to Dropbox or Google Drive despite valid credentials

**Symptoms**:
- Dropbox upload fails despite valid credentials
- Google Drive authorization loops repeatedly
- Files not syncing between IPTVBoss instances
- "Bandwidth limit reached" on free Dropbox tier
- Cloud authorization succeeds but uploads fail
- One Boss instance doesn't see other instance's changes

**Why this happens**: OAuth tokens expired periodically. Free Dropbox bandwidth limit (20GB/month) exceeded with many users. Multiple Boss instances causing sync conflicts. File permissions changed after OS update. Firewall blocking cloud services.

**Solution**:

**Step 1: Reauthorize cloud storage**
- Settings → IPTVBoss Settings (Dropbox or Google Drive)
- Click Authorize
- Complete OAuth flow in browser
- Verify authorization success in IPTVBoss

**Step 2: Clean stale cloud files**
- Go to Dropbox/Google Drive website
- Navigate to IPTVBoss sync folder
- Delete these files:
  - IPTVBossSync.backup
  - lockfile.json
  - Any files with "lock" in name
- These can cause conflicts, better to regenerate fresh

**Step 3: Test upload**
- In IPTVBoss: Layout Manager → Output
- Check View Cloud Links to verify upload
- Verify files appear in cloud storage

**For bandwidth limit issues**:

1. **Use Universal EPG**
   - Sources → Universal EPG Options
   - Generates one EPG for all layouts
   - Massive bandwidth savings over individual EPGs

2. **Exclude VOD from M3U**
   - VOD lists are enormous
   - If you don't use VOD, disable it in output
   - Reduces M3U file size by 70-90%

3. **Use .gz format**
   - EPG.GZ is compressed format
   - Much smaller than XML
   - Most players support it

4. **Reduce sync frequency**
   - Don't sync more than 2x daily
   - EPG providers update 1-2x daily anyway

5. **Consider Google Drive**
   - Often more generous bandwidth limits
   - Or upgrade to Dropbox paid tier

**After OS upgrade**:
- Reauthorize cloud storage (OS changes break OAuth)
- Check firewall rules (might have reset)
- Reinstall cloud storage desktop app if needed
- Verify IPTVBoss folder permissions

**For multiple instances**:
- Don't run multiple instances simultaneously
- Cloud sync gets confused
- If you must run multiple: Disable cloud sync on all but one "primary" instance

**Prevention**:
- Use Universal EPG by default
- Monitor bandwidth usage
- Keep cloud storage apps updated
- Backup authorization before OS updates

**Known limitations**:
- Free Dropbox insufficient for 40-50+ users
- Multiple instances without coordination cause issues
- OS upgrades reliably break cloud auth

**See also**: [FAQ: Dropbox bandwidth limit](FAQ.md#im-getting-dropbox-bandwidth-limit-reached-with-40-50-users-do-i-need-to-upgrade)

---

### Changes Not Reflecting in Player Apps

**Problem**: Changes made in IPTVBoss don't appear in player (TiviMate, etc.)

**Symptoms**:
- Deleted channels still appear in TiviMate
- Player shows provider's original categories despite Boss filtering
- Playlist edits don't show up in player
- EPG changes not visible in player
- Old channel list remains after updates
- Player seems "stuck" on old version

**Why this happens**: User didn't output updated files from IPTVBoss. Player wasn't updated/refreshed after output. Player using wrong URL (provider direct URL instead of Boss URL). Player aggressively caching old playlist data.

**Solution**:

**Complete workflow (all steps required)**:

1. **Make changes in IPTVBoss**
   - Edit channels, layouts, EPG mappings, etc.
   - Save your changes

2. **Output the layout**
   - Layout Manager → Output Current Layout M3U and EPG
   - Wait for progress indicator to complete

3. **Verify cloud upload**
   - View Cloud Links
   - Confirm files uploaded (check timestamps)
   - If using TinyURL, verify links updated

4. **Update playlist in player**
   - TiviMate: Settings → Playlists → [Select your playlist] → Update
   - Other players: Find playlist refresh/update option
   - This pulls new files from cloud

5. **Wait for player to process**
   - Give player 30-60 seconds to download and process
   - Large playlists take longer

**If still not working**:

1. **Verify correct URL in player**
   - Check playlist settings in player
   - Confirm using IPTVBoss URL (Dropbox/Google Drive/TinyURL)
   - NOT using provider's direct URL
   - Easy mistake: Having both URLs and forgetting which is active

2. **Clear player cache (nuclear option)**
   - Completely remove playlist from player
   - Re-add playlist using IPTVBoss URL
   - This forces fresh data, no cache

3. **Verify files actually changed**
   - Download M3U from cloud link in browser
   - Open with text editor
   - Search for channel that should be deleted/changed
   - Confirms output actually reflected your changes

**Common mistakes**:
- Editing in Boss but forgetting to output
- Outputting but forgetting to update in player
- Updating wrong playlist in player (if you have multiple)
- Provider URL still configured in player alongside Boss URL

**Workaround**: None - this is the correct workflow. IPTVBoss generates static files; players must pull those files. This is by design, not a bug.

**User expectation mismatch**: Many users expect real-time sync like streaming apps. IPTVBoss works like publishing a document - you must publish (output), host (cloud), and readers (players) must refresh.

**Known limitations**:
- No push mechanism to players
- Multiple URLs (provider, Boss, TinyURL) cause confusion
- Player cache more aggressive than users realize
- Workflow requires 3 separate steps - easy to forget one

**See also**: [FAQ: Changes not showing in player](FAQ.md#changes-i-make-in-iptvboss-arent-showing-up-in-my-player-what-am-i-missing)

---

### Specific EPG Sources Show Limited or No Information

**Problem**: Some EPG sources (especially USA, USA Local) show limited guide data

**Symptoms**:
- USA and USA Local EPG show only couple hours then "no information"
- EPG works for first program then goes blank
- Some channels have EPG, others don't despite mapping
- EPG in Boss shows data but player shows none (or vice versa)
- Guide data progressively disappears

**Why this happens**: "Days to Keep" set too low or to 0 at source, layout, or override level. EPG cache corruption. Conflicting EPG source configurations. TiviMate using cached data from different source than you expect.

**Solution**:

**Step 1: Check Days to Keep settings** (multiple places!)

1. **Source level**:
   - Go to **Sources → Sources Manager**
   - Highlight your EPG source
   - Click **EPG Settings**
   - Check **"Days to Keep"** for EPG
   - Default is **3 days**
   - Should be **7 days** or **ALL** for best results
   - Setting to **0** or very low (1-2) causes this issue

2. **Channel-specific overrides** (if EPG Override enabled):
   - Some channels may have specific EPG overrides set
   - Check individual channel EPG override settings
   - Remove overrides causing issues

**Step 2: EPG cache fix**

1. Shut down IPTVBoss completely
2. Navigate to `IPTVBoss/cache` folder
3. Find and delete files for problematic EPG sources:
   - USA.xml or USA.gz
   - USA_Local.xml or USA_Local.gz
   - Any other problematic source files
4. Start IPTVBoss
5. Sync all EPGs (Sources → Sync All EPGs)
6. Output and test

**Step 3: Player cache check**

If EPG shows in Boss but not in player:
- Player may be using cached data
- Add playlist completely fresh in player
- Remove old playlist first
- This tests if player cache is the issue

If EPG doesn't show in Boss but shows in player:
- Player is using cached EPG from before
- Or player is using different EPG source
- Player will eventually lose data when cache expires

**Prevention**:
- Set "Days to Keep" to **7 days** or **ALL** at source level
- Default is only 3 days - increase for better EPG coverage
- Check channel-specific overrides if EPG Override is enabled
- Periodically clear EPG cache if issues recur

**For Universal EPG users**:
- These settings apply to Universal EPG too
- Check Universal EPG days to keep settings
- Same cache clearing process works

**Known limitations**:
- USA EPG sources particularly affected (provider issue?)
- Override hierarchy not always clear to users
- Cache location not well documented in official docs

**See also**: [FAQ: Specific EPG sources show no info](FAQ.md#specific-epg-sources-usa-usa-local-show-no-info-after-a-couple-of-hours-how-do-i-fix-this)

---

### License Validation Failures and Loops

**Problem**: Pro license won't validate despite being valid

**Symptoms**:
- Prompted to upgrade to Pro despite valid license
- Pro license "doesn't exist" when checking website
- Authorization loop - keeps asking for license repeatedly
- Database restore requires Pro but Pro won't activate
- "License unknown" after update

**Why this happens**: User hasn't migrated account to new IPTVBoss website. Using old website credentials. Database corruption preventing Pro activation. License actually expired. Network blocking license validation. Chicken-and-egg: need DB to activate Pro, need Pro to restore DB.

**Solution**:

**Step 1: Verify license still active**
- Check purchase date/subscription status
- Verify license hasn't expired
- Confirm you have valid license key

**Step 2: Migrate to new website** (if applicable)
- IPTVBoss migrated to new website system
- Old website credentials don't work on new system
- Visit new IPTVBoss website
- Migrate account or create new with license key
- Use license key from NEW website

**Step 3: Enter license correctly**
- Settings → IPTVBoss Pro Settings
- Copy & Paste license key (don't type manually)
- Click Activate

**Step 4: Wait and verify**
- License validation happens online
- May take several minutes
- Ensure stable internet connection
- Some users report 2-5 minute delay before activation

**Step 5: Check network**
- Ensure IPTVBoss can reach validation servers
- Check firewall isn't blocking
- Try disabling VPN temporarily
- Verify IPTVBoss website is accessible

**For "Table SETTINGS not found" error**:
- This means database is completely empty
- Pro license can't activate without database
- Must restore database from backup first
- After restore, re-enter Pro license

**For authorization loops**:
- Clear any old license entries
- Restart IPTVBoss
- Enter fresh license key from new website
- Verify internet connectivity throughout process

**Database + License interaction**:
- Pro activation requires working database
- Database restore sometimes requires Pro
- Usually auto-resolves: database auto-restore allows Pro entry
- If stuck: Try manual restore with free version, then activate Pro

**Prevention**:
- Keep license key accessible
- Don't let license expire without renewal ready
- Update license in Boss before expiration date
- Keep backup of license key email

**Known limitations**:
- Website migration not communicated to all users
- Chicken-and-egg problem with DB vs Pro (usually self-resolves)
- Expired licenses during system migration caused widespread confusion
- Error messages don't clearly indicate "need new website account"

**See also**: [FAQ: Pro license issues](FAQ.md#iptvboss-keeps-asking-me-to-reauthorize-boss-pro-and-wont-restore-my-database-whats-wrong)

---

### Port-Migration Database and Setup Recovery Issues

**Problem**: Setting up IPTVBoss on new computer/OS - restore fails

**Symptoms**:
- Setting up on new computer - restore fails
- After OS reinstall, restore removes Boss token
- Moving to new laptop - authorization loops
- Database restore works but layouts empty
- New machine setup stuck in loops

**Why this happens**: Incorrect setup sequence - restore attempted before Pro activation. Old website credentials used on new installation. Cloud sync trying to overwrite local during restore. Database file incompatibility between significantly different versions.

**Solution**:

**CORRECT setup sequence** (order matters!):

1. **Install IPTVBoss on new machine**
   - Download and install clean

2. **Enter Pro license key FIRST**
   - Before anything else
   - Settings → IPTVBoss Pro Settings
   - Enter license key from new website
   - Wait for validation

3. **Set up cloud credentials**
   - After Pro activation succeeds
   - Configure Dropbox or Google Drive
   - Complete authorization

4. **THEN restore from backup**
   - Now that Pro and cloud are set up
   - Settings → Restore Database
   - Choose Local or Cloud
   - Select backup file

**For manual backup restore**:

Before reinstalling:
1. Copy entire `IPTVBoss/backup` folder to USB or external drive
2. Copy folder to known location on new machine
3. After Pro activation, browse to saved backup location for restore

**Version compatibility**:
- Backups generally compatible across versions
- Major version jumps (2.x to 3.x) may have issues
- Try latest backup first
- If issues, try backup from same version as new installation

**Cloud restore vs Local restore**:
- Cloud restore: Pulls from Dropbox/Google Drive
- Local restore: Uses files from IPTVBoss/backup folder
- If cloud restore fails, try local (and vice versa)

**Common mistakes**:
- Trying to restore before activating Pro
- Using old website credentials
- Not waiting for Pro validation to complete
- Trying to restore from cloud before authorizing cloud storage

**Why sequence matters**:
- Database requires Pro context to restore properly
- Cloud credentials needed before cloud restore can work
- Attempting out-of-order causes various failures and loops

**Prevention**:
- Document correct sequence before starting
- Keep manual backup copies on external storage
- Take screenshots of settings before migration
- Test restore on old machine before wiping

**Known limitations**:
- Setup wizard doesn't enforce sequence
- Error messages don't clearly indicate sequence problem
- Intuitive to try restore first (but wrong order)

**See also**: [FAQ: Setting up on new machine](FAQ.md#setting-up-iptvboss-on-new-machine---restore-keeps-removing-boss-token-and-failing-whats-wrong)

---

### NoGUI Update Errors After Version Updates

**Problem**: NoGUI stops working after updating IPTVBoss version

**Symptoms**:
- After update: NoGUI shows Dropbox errors
- Missing mappings.txt error
- License status "unknown" after update
- Scheduled syncs stop working after update
- Config files not found

**Why this happens**: Update changed file structure or locations. Cloud storage authorization reset during update. Permissions changed on files/folders. Configuration files not migrated properly by update process.

**Solution**:

**After ANY update, always do this checklist**:

1. **Open GUI and refresh license**
   - Settings → IPTVBoss Pro Settings
   - Re-enter license if needed
   - Don't proceed until Pro shows active

2. **Reauthorize cloud storage**
   - Settings → IPTVBoss Settings
   - Reauthorize Dropbox/Google Drive
   - Complete OAuth flow
   - Verify authorization success

3. **Test NoGUI manually**
   - Before trusting automation
   - Command line: `iptvboss -nogui`
   - Watch output - does it work?
   - Check for errors

4. **Check for missing files**
   - Updates may relocate or delete auto-generated files
   - Check logs for "file not found" errors
   - Identify what's missing

5. **Regenerate auto-generated files**
   - Output layouts again
   - This regenerates mappings.txt and other auto files
   - Layout Manager → Output All Layouts

6. **Verify sync schedule**
   - Task Scheduler (Windows) or cron (Linux/Mac)
   - Check if times still set
   - Reconfigure if cleared

7. **Check file permissions**
   - Updates can change folder permissions
   - Verify IPTVBoss folder is readable/writable
   - Especially important on Linux/Mac

**For "missing mappings.txt" specifically**:
- This file is auto-generated during output
- Output layouts to regenerate
- Check IPTVBoss folder permissions

**For scheduled tasks**:
- Verify Task Scheduler/cron entries still exist
- Updates sometimes remove scheduled tasks
- May need to recreate sync schedule in GUI

**Prevention**:
- Read update notes in Discord before updating
- Backup database before updating
- Test manually after updating before relying on automation
- Delay updates until you have time to test and reconfigure

**Best practice**:
- Update during low-usage time
- Plan 30 minutes for post-update verification
- Keep previous version installer as backup

**Known limitations**:
- Update process doesn't always preserve all configurations
- Breaking changes not always clearly communicated
- Automated tasks particularly vulnerable to updates
- Some updates require full reconfiguration

**See also**: [FAQ: After update, things stopped working](FAQ.md#nogui-after-update-to-3992-shows-dropbox-errors-and-missing-mappingstxt-what-happened)

---

## Additional Help

- **Check** [Known Issues](Known_Issues.md) for unresolved problems and workarounds
- **Review** [FAQ](FAQ.md) for quick answers to common questions
- **Post logs** in Discord support channel (clean sensitive info first)
- **Search Discord** - many issues already solved by community
