# Solution: Boss Has No Data (Source Sync Issues)

**Flow ID**: no_data
**Type**: diagnostic_solution
**Confidence**: high
**Solution Steps**: 6

### Context

Boss itself doesn't have data - EPG Browser is empty or shows no program listings. This means Boss isn't getting data from sources.

### Root Cause

Boss hasn't successfully synced data from playlist or EPG sources. Could be connectivity, source issues, subscription problems, or cache corruption.

### Confidence

**HIGH (90%+)** - If Boss has no data, the issue is definitely with source syncing

### Step 1: Sync Sources in Boss

Let's sync your sources to pull fresh data:

**Sync Playlist Sources**:
1. In Boss: **Sources** menu (or View → Sources)
2. Click **Sync All Playlist Sources** (or sync them individually)
3. Wait for completion (may take 1-2 minutes)
4. Check if channels appear in channel list

**Sync EPG Sources**:
1. In Boss: **Sources** menu
2. Click **Sync All EPG Sources** (or sync individually)
3. Wait for completion (may take 2-3 minutes depending on EPG size)
4. Go to **EPG Browser** and check if program data appears

**Did data appear now?**
- ✅ **YES**: Great! Move to Step 6 (Output)
- ❌ **NO**: Continue to Step 2

### Step 2: Check Internet Connectivity

Basic connectivity check:

1. Open a web browser on the same device running Boss
2. Go to any website (google.com)
3. Verify internet is working
4. Try accessing your cloud provider (dropbox.com or drive.google.com)

**If internet is down**:
- Fix internet connection
- Try Step 1 again (sync sources)

**If internet works**:
- Continue to Step 3

### Step 3: Verify Source URLs and Subscription

**Check Provider Subscription**:
- Verify your IPTV subscription is active
- Log into provider's website/panel if available
- Check expiration date
- Some providers show "no data" when subscription expires

**Check Source URLs**:
1. In Boss: **Sources** → View your sources
2. Check that URLs are correct and complete
3. Look for any error messages in source list
4. If using Xtream Codes: verify username, password, server URL all correct

**If subscription expired or URLs wrong**:
- Update subscription with provider
- Correct URLs in Boss sources
- Try Step 1 again (sync sources)

### Step 4: Clear EPG Cache

Corrupted cache can prevent Boss from processing EPG data properly:

1. **Close IPTVBoss completely** (important!)
2. Navigate to Boss folder:
   - **Windows**: `C:\Users\[YourName]\AppData\Roaming\IPTVBoss`
   - **Mac**: `~/Library/Application Support/IPTVBoss`
   - **Linux**: `~/.config/IPTVBoss`
3. Find the **cache** subfolder
4. **Delete problematic EPG files**:
   - If one region/EPG affected: delete that EPG's cache file
   - If multiple regions: delete all EPG cache files (they'll rebuild)
   - **Don't delete the cache folder itself**, just the files inside
5. Restart Boss
6. Try Step 1 again (sync sources)

### Step 5: Check Boss Logs for Errors

Logs can reveal specific sync failures:

1. In Boss folder, find **logs** directory
2. Open the most recent log file
3. Search (Ctrl+F) for these keywords:
   - "ERROR"
   - "Failed to sync"
   - "Failed to download"
   - "Connection"
   - "Timeout"
   - "Authentication"
   - "404" or "401"

**Common errors and solutions**:

- **"Connection timeout" / "Failed to connect"**:
  - Provider server may be down
  - Check with provider or their status page
  - Try again in 15-30 minutes

- **"Authentication failed" / "401 Unauthorized"**:
  - Wrong username/password in source
  - Subscription expired
  - Update credentials

- **"404 Not Found"**:
  - URL is incorrect
  - Provider changed URLs
  - Check with provider for current URL

- **"Failed to parse"**:
  - Corrupted data from provider
  - Clear cache (Step 4)
  - Try syncing again

- **"SSL certificate"**:
  - Provider has certificate issues
  - May need to wait for provider to fix
  - Some providers allow HTTP fallback (not recommended)

### Step 6: Output After Successful Sync

Once Boss shows data in EPG Browser:

1. Click **Output** button
2. Select your layout
3. Wait for "Output successful" message
4. Sync your player (Update Playlist)
5. Check if data appears in player

### ✅ If That Fixed It

Great! Set up automatic syncing to prevent this:

**1. Enable Automatic Syncing**:
1. Boss: **Settings** → **Automatic Syncing**
2. Enable automatic sync schedule
3. Set sync times (recommend: twice daily)
4. Enable **"Output after sync"**
5. This keeps your data fresh automatically

**2. Check for Lock Files** (Optional but Recommended):

If sync failed once, lock files might be present:

1. Close Boss completely
2. Navigate to Boss folder (paths in Step 4)
3. Look for `.lock` files
4. Delete any `.lock` files found
5. Restart Boss

This prevents future sync failures due to stuck locks.

### Alternative: Database Is Corrupt or Empty

If Boss shows **no sources, playlists, layouts** - like a fresh install:

**Database corruption or loss**. You'll need to restore:

1. If you have a backup: Restore from backup
2. If no backup: You'll need to reconfigure from scratch
3. See [Database Corruption and Recovery](../../01_database_corruption_startup_failure.md)

### Still Not Working?

If after all steps Boss still has no data:

**Information needed for support**:
1. Which sources are you using (provider type: M3U URL / Xtream Codes)?
2. What errors show in logs? (copy error lines)
3. Is your subscription active? (check with provider)
4. Can you access provider's panel/website?
5. Did clearing cache help at all?

Ask in [Discord Support](https://discord.gg/QCxpA9yvWP) with the above details and relevant log errors.

### Related Topics

- [Source Sync Breaking Layouts](../../02_source_sync_breaking_layouts.md)
- [EPG Sources Show Limited Information](../../09_epg_sources_limited_information.md)
- [Adding Sources Guide](../../../user_guide/03_adding_sources.md)
- [EPG Source Configuration](../../../user_guide/05_epg_source_configuration.md)
- [Automatic Syncing Setup](../../../user_guide/21_automatic_syncing.md)
- [Database Corruption](../../01_database_corruption_startup_failure.md)
- [Comprehensive No Data Guide](../../13_no_data.md)
