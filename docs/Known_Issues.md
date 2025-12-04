# Known Issues

Unresolved problems, limitations, and workarounds. Issues are organized by severity.

**Note**: These are issues without complete solutions yet. For solved problems, see [Troubleshooting Guide](Troubleshooting_Guide.md).

---

## Critical/High Priority

### Recurring Database Wipes Every 1-2 Weeks

**Status**: Needs user-specific investigation

**Symptoms**:
- IPTVBoss shows no data every 1-2 weeks
- Must restore from backup repeatedly
- Pattern is consistent (same interval)

**Possible Causes**:
- Cloud sync conflicts from multiple instances
- Disk space issues
- Antivirus quarantining database files
- Database on network drive or slow storage
- Memory issues during shutdown
- Background process killing IPTVBoss improperly

**Investigation Steps**:
1. Check IPTVBoss/logs folder for patterns around time of data loss
2. Look for:
   - Database write errors
   - Disk full errors
   - Permission errors
   - Sync conflict messages
3. Monitor disk space over time
4. Check if running multiple Boss instances
5. Verify antivirus isn't flagging Boss files
6. Check if database is on local drive (not network)

**Workaround**:
- Keep frequent external backups
- Restore from Dropbox backup: IPTVBossSync.backup (change last digit to 0)
- Document exactly when failures occur (time of day, after what actions)
- Consider dedicated machine for Boss if running on shared system

**Needs**: Detailed logs from user at time of failure, environment specifics

---

### Provider Showing ALL Categories Despite Boss Filtering

**Status**: User configuration issue - needs investigation per case

**Symptoms**:
- Player shows all provider categories
- IPTVBoss layout has filtered/organized channels
- Output seems successful
- Changes in Boss don't affect what player shows

**Possible Causes**:
- Player configured with provider's direct URL (not Boss URL)
- Player has multiple playlists and wrong one is active
- Player cache from before Boss setup
- Boss output URL not actually being used

**Workaround**:
1. Completely remove playlist from player
2. Verify you're using ONLY the Boss M3U URL (from cloud links)
3. Re-add playlist fresh with Boss URL
4. Don't add provider's direct URL to player

**Why investigation needed**: Almost always user configuration, but hard to diagnose remotely without seeing player setup.

---

### Lost Pro Configuration - Groups Empty, Authorization Loop

**Status**: Partial database corruption - needs investigation

**Symptoms**:
- Groups exist but have no channels
- Stuck in Pro authorization loop
- Database restore doesn't help or partially restores
- Pro license won't validate

**Possible Causes**:
- Partial database corruption
- Incomplete database restore
- Old website vs new website credential conflicts
- Database and license system desync

**Workaround**:
- Must restore from older backup (before corruption)
- No recovery from empty-but-existing groups
- If backups don't work, must rebuild from scratch

**Needs**: Better diagnostic tools for partial corruption, clearer error messages

---

## Medium Priority

### Phantom Group Keeps Appearing in Player

**Status**: Unknown - needs investigation

**Symptoms**:
- Group deleted from layout in Boss
- Output and sync successful
- Group still appears in player apps
- Persists across multiple output/update cycles

**Possible Causes**:
- Player not using IPTVBoss M3U file
- Player cache not clearing properly
- M3U file not actually updated despite Boss saying so
- Cloud storage serving stale/cached file
- Hidden group or reference somewhere in Boss

**Workaround**:
- No reliable workaround found yet
- Try: Complete playlist removal and re-add in player
- Try: Delete cloud files completely, re-output, re-add in player

**Needs**: Reproducible case, M3U file inspection at each step

---

### Daily Sync No Longer Working on Windows

**Status**: Task Scheduler configuration - needs per-user debugging

**Symptoms**:
- Scheduled task exists in Task Scheduler
- Task appears to run
- EPG doesn't actually update
- Manual nogui works fine

**Possible Causes**:
- Task Scheduler disabled the task (Windows update)
- Path in task incorrect after Boss update
- Permissions changed
- Task running but Boss can't access database
- Task running under wrong user account

**Workaround**:
1. Delete existing Task Scheduler task
2. Recreate sync schedule from Boss GUI, esnuring you start Boss with admin rights
3. Verify new task created and enabled
4. Test task runs manually from Task Scheduler

**Needs**: Better Task Scheduler integration, automated verification

---

### XC Server Crashes After DB Reload Post-Sync

**Status**: XC database corruption - advanced troubleshooting needed

**Symptoms**:
- Source sync completes successfully
- Database reload begins
- XC server crashes
- Main Boss still works

**Possible Causes**:
- XC database (separate from main DB) is corrupted
- XC configuration conflict
- Memory issues during reload

**Workaround**:
1. Identify XC database file in IPTVBoss/db folder
2. Restore from backup (if XC-specific backup exists)
3. Or delete XC database and recreate XC configuration

**Needs**: XC database structure documentation, better error messages

---

### Pro Activation Fails Despite Valid License

**Status**: Multiple possible causes - needs case-by-case investigation

**Symptoms**:
- License key is valid (checked on website)
- Boss shows "Unable to Activate Pro"
- Repeated attempts fail
- Internet connection works

**Possible Causes**:
- Network/firewall blocking validation servers
- Boss validation servers experiencing issues
- Credential migration incomplete (old website → new website)
- Boss can't reach validation endpoint (corporate firewall, VPN, etc.)

**Workaround**:
1. Verify license on new IPTVBoss website (not old)
2. Try different network (disable VPN, try mobile hotspot)
3. Check firewall rules for Boss
4. Contact support with logs if verified valid license

**Needs**: Better validation error messages, local validation option, clearer migration docs

---

### Mac Cron Permissions for Sync Schedule

**Status**: macOS security limitation - documented workaround

**Symptoms**:
- Cron entries created successfully
- Cron should run but doesn't
- Manual nogui works fine
- Times don't save in Boss GUI

**Root Cause**: macOS requires explicit permissions for cron to access files

**Solution** (documented but often missed):
1. Grant Full Disk Access to IPTVBoss:
   - System Preferences → Security & Privacy → Privacy
   - Full Disk Access → Add IPTVBoss
2. Or switch from cron to launchd (more Mac-native)

**Recommendation**: Boss should use launchd on Mac by default, not cron

---

## Low Priority / Cosmetic

### Channel Sorting Ignores Prefixes

**Status**: By design, but confusing to users

**Symptoms**:
- A-Z sort doesn't group channels as expected
- Channels with prefixes (US, CA, numbers) sort by prefix
- "ESPN" and "US ESPN" don't sort together

**Root Cause**: Sort uses first character/number in channel name

**Workaround**: Remove or standardize prefixes in channel names

**Enhancement Request**: Option for "smart sort" ignoring common prefixes

---

### EPG Layout Title Doesn't Show Teams for Sports

**Status**: EPG source data limitation

**Symptoms**:
- College football games show "NCAA Football" in title
- Team matchup only in description, not title
- Affects DVR recording rules

**Root Cause**: EPG source provides data this way

**Workaround**: Use EPG title format settings (may have limited control)

**Needs**: EPG source provider to improve data format, or Boss to parse description into title

---

## Reporting Issues

When reporting new issues:

1. **Check** [FAQ](FAQ.md) and [Troubleshooting Guide](Troubleshooting_Guide.md) first
2. **Search** Discord support channel (likely already discussed)
3. **Include**:
   - Boss version
   - Operating system
   - Logs from IPTVBoss/logs (clean sensitive info!)
   - Clear description of problem
   - Steps to reproduce
   - What you've already tried
4. **Post** in Discord support channel (not DM - community can help)

**Don't include** in logs:
- Provider names or URLs
- Usernames or passwords
- Personal information
- License keys

---

## Contributing Workarounds

Found a workaround for a known issue? Help the community:

1. Post in Discord with clear steps
2. Tag moderators to add to documentation
3. Be specific - others need to reproduce your success

---

## Issue Priorities

**Critical**: Blocks major functionality, data loss risk
**High**: Significant usability impact, affects core features
**Medium**: Annoying but workable, workarounds exist
**Low**: Cosmetic or minor inconvenience

---

**Last Updated**: Based on Discord support threads through December 4, 2025
