# Solution: M3U Playlist Sync Issues

**Flow ID**: m3u_playlist
**Type**: diagnostic_solution
**Confidence**: high
**Solution Steps**: 5

### Context

Channels missing or outdated in Boss. Playlist source isn't syncing properly.

### Solution Steps

### 1. Manual Sync Playlist Source

1. Boss → **Sources**
2. Click **Sync All Playlist Sources**
3. Wait for completion
4. Check channel list for channels

### 2. Verify Source Configuration

**For M3U URL**:
1. Sources → View playlist sources
2. Check URL is complete and correct
3. Test URL in browser (should download M3U file)
4. Verify no authentication required (or credentials correct)

**For Xtream Codes**:
1. Verify server URL, username, password
2. Check subscription is active
3. Test login on provider's panel/website

### 3. Check Provider Status

- Provider's servers might be down
- Check provider's status page or support
- Try syncing in 15-30 minutes
- Contact provider if persistent

### 4. Check Logs for Errors

1. Boss folder → logs
2. Search for: "playlist", "failed", "error"
3. Common errors:
   - "404 Not Found" → Wrong URL
   - "401 Unauthorized" → Wrong credentials or expired
   - "Timeout" → Provider server slow or down

### 5. Source Limitations

Some providers:
- Limit sync frequency (e.g., max once per hour)
- Block rapid requests
- Require specific user agent
- Have temporary outages

### Related Topics

- [Adding Sources Guide](../../../user_guide/03_adding_sources.md)
- [Source Sync Breaking Layouts](../../02_source_sync_breaking_layouts.md)
- [No Data in Boss](../no_data_diagnostic/03_solution_boss_no_data.md)
