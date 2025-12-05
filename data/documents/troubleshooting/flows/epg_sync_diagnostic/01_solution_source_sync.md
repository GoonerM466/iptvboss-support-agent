# Solution: EPG Source Sync Problems

**Flow ID**: epg_sync
**Type**: diagnostic_solution
**Confidence**: high
**Solution Steps**: 5

### Context

EPG data isn't syncing from sources into Boss. EPG Browser in Boss shows no or outdated data.

### Solution Steps

### 1. Manual Sync EPG Sources

1. Boss → **Sources**
2. Click **Sync All EPG Sources**
3. Wait 2-3 minutes (EPG files are large)
4. Check EPG Browser for data

### 2. Check EPG Source URLs

1. Sources → View EPG sources
2. Verify URLs are correct
3. Check subscription isn't expired
4. Test URL in browser (should download XML/GZ file)

### 3. Clear EPG Cache

1. Close Boss
2. Navigate to Boss folder → **cache** subfolder
3. Delete EPG cache files (keep the cache folder)
4. Restart Boss
5. Sync EPG sources again

### 4. Check Logs for Errors

1. Boss folder → **logs**
2. Open recent log
3. Search for: "EPG", "Failed", "ERROR"
4. Common errors:
   - "Failed to download" → Provider issue
   - "Failed to parse" → Corrupted file, clear cache
   - "Timeout" → Server slow, try again later

### 5. Verify EPG Format

Some sources have compatibility issues:
- XML.GZ (compressed) - most common, best support
- XML (uncompressed) - works but larger
- Xtream Codes API - built-in support
- Other formats may not work

### If Still Not Working

Try alternative EPG source:
- Many providers offer multiple EPG URLs
- Community EPG sources available
- See [EPG Source Configuration](../../../user_guide/05_epg_source_configuration.md)

### Related Topics

- [EPG Sources Limited Information](../../09_epg_sources_limited_information.md)
- [No Data in Boss](../no_data_diagnostic/03_solution_boss_no_data.md)
- [EPG Source Configuration Guide](../../../user_guide/05_epg_source_configuration.md)
