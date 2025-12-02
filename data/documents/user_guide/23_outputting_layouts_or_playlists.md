# Outputting Layouts / Playlists for Players

### Outputting Layouts or Playlists for Players

Outputting generates M3U and EPG files for your player apps.

**When to output**:
- After creating/editing layouts
- After mapping EPG
- After any changes you want players to see
- After source syncs (if channel names changed)

**Output process**:

1. **Select what to output**
   - Output Current Layout (just one layout)
   - Output All Layouts (all at once)
   - Output all alyouts & EPGs (Everything!)

2. **Wait for completion**
   - Progress indicator shows status
   - Files generate locally
   - Files upload to cloud storage
   - May take 1-5 minutes for large playlists

3. **Verify completion**
   - Check for success message
   - View Cloud Links to see URLs

4. **Get URLs**
   - Click "View Cloud Links"
   - Copy M3U URL
   - Copy EPG URL
   - Or copy TinyURL short versions

**What gets generated**:
- `.m3u` file: Playlist with channel URLs
- `.xml` or `.gz` file: EPG data
- Both uploaded to your cloud storage
- TinyURL short links created (if configured)

**Using in players**:

**First time setup**:
1. Player app → Add Playlist
2. Enter M3U URL
3. Enter EPG URL
4. Save/Add
5. Wait for import

**Updating after changes**:
1. Output from Boss (generates new files)
2. Player app → Update Playlist
3. Wait for refresh

**Don't** delete and re-add playlist for updates - just update/refresh.


---

## Related Topics

- [Previous: EPG Browser](22_epg_browser.md)
- [Next: Understanding Cloud Storage Options](24_cloud_storage_overview.md)
