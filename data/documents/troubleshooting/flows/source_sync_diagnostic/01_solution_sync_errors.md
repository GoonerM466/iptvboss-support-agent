# Solution: Source Sync Errors

**Flow ID**: source_sync
**Type**: diagnostic_solution
**Confidence**: high
**Solution Steps**: 5

### Context

Source sync fails with error messages. Playlists or EPGs won't sync from provider.

### Solution Steps

### 1. Check Error Message

Common errors and solutions:

**"Failed to connect" / "Timeout"**:
- Provider server down or slow
- Check provider status
- Try again in 15-30 minutes

**"401 Unauthorized" / "Authentication failed"**:
- Wrong credentials
- Subscription expired
- Update username/password
- Verify subscription with provider

**"404 Not Found"**:
- URL incorrect or changed
- Provider moved files
- Get updated URL from provider

**"403 Forbidden"**:
- IP blocked by provider
- Too many sync requests
- Wait before retrying
- Contact provider

### 2. Verify Source Configuration

1. Boss → Sources → View sources
2. Check URLs are complete
3. Verify credentials (Xtream Codes)
4. Test URLs in browser

### 3. Check Provider Status

- Provider's servers may be down
- Maintenance windows
- Check provider's website/status page
- Ask in provider's support channels

### 4. Check Rate Limiting

Some providers:
- Limit sync frequency (max once per hour)
- Block rapid requests
- Require specific user agent

Wait 30-60 minutes between sync attempts

### 5. Check Logs for Details

1. Boss folder → logs
2. Search for: "sync", "failed", "error"
3. Note specific error codes
4. Include in Discord support request if needed

### Related Topics

- [Adding Sources](../../../user_guide/03_adding_sources.md)
- [M3U Playlist Issues](../m3u_playlist_diagnostic/01_solution_playlist_sync.md)
- [EPG Sync Issues](../epg_sync_diagnostic/01_solution_source_sync.md)
- [No Data in Boss](../no_data_diagnostic/03_solution_boss_no_data.md)
