# Setting Up Automatic EPG Syncing

### Setting Up Automatic EPG Syncing

EPG data updates periodically. Automate syncing so guide stays current.

**Why automate**:
- Manual syncing is tedious
- EPG goes stale without updates
- Set it once, forget it

**Video Tutorial**: https://youtu.be/2nIsgC3wv_E

---

**Setup Steps**:

1. **Open IPTVBoss with proper permissions**:
   - **Windows**: Right-click IPTVBoss → "Run as administrator" (REQUIRED)
   - **Mac/Linux**: Open normally (permissions handled during setup)

2. **Configure sync schedule in Boss**:
   - Go to **Settings → Sync Schedule**
   - Select sync times (e.g., 6 AM and 6 PM)
   - Choose which days (typically all days)
   - Enable the schedule
   - Click OK

3. **What Boss does automatically**:
   - **Windows**: Boss creates Windows Task Scheduler tasks for you
   - **Mac**: Boss creates cron jobs for you
   - **Linux**: Boss creates cron jobs for you
   - ✅ You do NOT manually create tasks/cron entries - Boss handles it

4. **Verify automation created**:
   - **Windows**: Open Task Scheduler → Look for IPTVBoss sync tasks
   - **Mac/Linux**: Run `crontab -l` in terminal to see Boss-created cron jobs

5. **Test it**:
   - Wait for scheduled time, OR
   - Manually test: **Sources → Sync All EPGs** (doesn't affect schedule)
   - Check **Logs → View Logs** for sync activity
   - Verify EPG updated

---

**Important Platform-Specific Notes**:

**Windows**:
- ⚠️ **MUST run Boss as administrator** to access Sync Schedule menu
- Boss creates Task Scheduler tasks with correct permissions automatically
- Tasks run even when Boss isn't open
- If sync fails, check task runs with "highest privileges" in Task Scheduler

**Mac**:
- Boss creates cron jobs automatically
- **May require**: System Preferences → Security & Privacy → Full Disk Access → Add IPTVBoss
- Alternative: Use launchd instead of cron (more reliable on Mac)
- Check permissions if syncs don't run

**Linux**:
- Boss creates cron jobs automatically
- User must have permissions to IPTVBoss folder
- Cron uses absolute paths (Boss handles this automatically)
- Check `crontab -l` if syncs don't run

---

**Recommended Sync Frequency**:
- **1-2 times daily** is typical
- EPG providers update 1-2x daily usually
- More frequent syncing doesn't improve data, just wastes resources
- **Don't sync more than 4 times daily**

**Best Sync Times**:
- **Early morning (6-8 AM)**: Fresh data for the day
- **Evening (6-8 PM)**: Updated evening/night data
- Avoid peak usage times

**Manual Sync Anytime**:
- You can always manually sync: **Sources → Sync All EPGs**
- Manual syncs don't affect automatic schedule


---

## Related Topics

- [Previous: Using TinyURL for Short Links](25_tinyurl_short_links.md)
- [Next: Understanding NoGUI Mode](27_nogui_mode.md)
