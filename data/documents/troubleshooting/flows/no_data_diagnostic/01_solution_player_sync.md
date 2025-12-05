# Solution: No Data - Player Sync Required

**Flow ID**: no_data
**Type**: diagnostic_solution
**Confidence**: medium
**Solution Steps**: 4

### Context

User's setup either never worked or they haven't tried basic player sync. This is often the simplest fix.

### Root Cause

Most likely: Player needs to pull data from cloud storage. Could also be initial setup incomplete.

### Confidence

**MEDIUM (60-80%)** - Player sync fixes most "no data in player" issues

### Step 1: Sync Your Player

First, let's update your player to pull the latest data from cloud storage:

**TiviMate**:
1. Open TiviMate
2. Go to **Settings** (gear icon)
3. Select **Playlists**
4. Tap your playlist
5. Tap **Update Playlist**
6. Wait 30-60 seconds

**ImPlayer**:
1. Open ImPlayer
2. Go to **Settings**
3. Select **Refresh Playlist**
4. Wait for completion

**Other Players**:
- Look for "Refresh", "Update", or "Sync" option in playlist settings
- May be called "Reload" or "Update EPG"

### Step 2: Check If Data Appears

After syncing:
1. Go back to live TV or EPG view
2. Check if channels appear
3. Check if EPG (program guide) shows

**Did data appear?**

### ✅ If That Fixed It

Great! Here's how to prevent this in the future:

**Set Up Auto-Sync in Player**:
- Most players can auto-refresh playlists every few hours
- TiviMate: Settings → Playlists → [Your playlist] → Auto-update → Set to 6-12 hours
- This keeps your player up to date automatically

**Check Your Boss Sync Schedule**:
1. In IPTVBoss: Settings → Automatic Syncing
2. Verify schedule is active
3. Make sure "Output after sync" is enabled
4. This ensures Boss updates your cloud files regularly

### ❌ If Still No Data in Player

The issue is likely that Boss hasn't output data to cloud yet. Let's check Boss:

**Check Boss Has Data**:
1. Open IPTVBoss
2. Go to **EPG Browser** (or View → EPG)
3. Look for any channel in your layout
4. Do you see program listings (show names, times)?

**Boss has data?**
- **YES**: Issue is between Boss and cloud → [Boss Output Issue Solution](02_solution_boss_output.md)
- **NO**: Issue is with Boss not getting data from sources → [Boss Has No Data Solution](03_solution_boss_no_data.md)

### If This Is a New Setup

If you're setting up for the first time and Boss also has no data:

**1. Add Sources First**:
- Boss needs playlist and EPG sources before it has data
- See [Adding Sources Guide](../../../user_guide/03_adding_sources.md)

**2. Sync Sources**:
- Sources → Sync All Playlists
- Sources → Sync All EPGs
- Wait for completion

**3. Create Layout**:
- Layout Manager → Create new layout
- Add channels to layout
- See [Layout Manager Guide](../../../user_guide/08_layout_manager.md)

**4. Setup Cloud Storage**:
- You need Dropbox, Google Drive, or local network
- See [Cloud Storage Setup](../../../user_guide/04_cloud_storage_setup.md)

**5. Output**:
- Output → Output Current Layout
- Wait for success message

**6. Add URL to Player**:
- Get cloud link from Boss (View Cloud Links)
- Add that URL to your player as a new playlist
- See [Quick Start Guide](../../../Quick_Start.md) for complete setup

### Still Stuck?

If none of these steps helped:

**Provide this info for better help**:
1. Which player app are you using?
2. Does Boss show data in EPG Browser?
3. Which cloud storage (Dropbox / Google Drive / Local)?
4. Any error messages?

Ask in [Discord Support](https://discord.gg/QCxpA9yvWP) with the above details.

### Related Topics

- [Understanding IPTVBoss Workflow](../../../user_guide/01_understanding_workflow.md)
- [Quick Start Guide](../../../Quick_Start.md)
- [Changes Not Reflecting in Players](../../08_changes_not_reflecting_players.md)
- [Comprehensive No Data Guide](../../13_no_data.md)
