# Solution: Limited EPG Information

**Flow ID**: epg_sync
**Type**: diagnostic_solution
**Confidence**: medium
**Solution Steps**: 3

### Context

EPG shows some data but is incomplete - only shows current program, or only few hours of data, or missing details.

### Root Cause

EPG source has limited data. This is often a source limitation, not a Boss problem.

### Solution Steps

### 1. Understand Source Limitations

**Most EPG sources provide**:
- 3-7 days of program data
- Basic info: show name, start/end time
- Sometimes: descriptions, ratings, categories

**What they DON'T usually provide**:
- Episode numbers
- Detailed descriptions for all shows
- Images/posters
- Full 14-day data

**This is provider-dependent**, not Boss issue.

### 2. Check EPG Mapping

If only some channels have limited EPG:

1. Boss → Match Tab (EPG mapping)
2. Check if channels are mapped to EPG
3. Unmapped channels show no EPG
4. Some automated matches may be wrong
5. Manually map channels to correct EPG IDs

### 3. Try Alternative EPG Sources

If current source is very limited:

**Options**:
1. Check if provider has better EPG URL
2. Use community EPG sources (xTeVe, xtream-editor, etc.)
3. Combine multiple EPG sources in Boss
4. See [EPG Source Configuration](../../../user_guide/05_epg_source_configuration.md)

### Accept Limitations

**Important**: If your provider's EPG is limited, Boss can't create data that doesn't exist. Boss only processes and displays what sources provide.

### Related Topics

- [EPG Sources Show Limited Information](../../09_epg_sources_limited_information.md)
- [EPG Mapping Guide](../../../user_guide/06_matching_epg_to_channels.md)
- [EPG Source Configuration](../../../user_guide/05_epg_source_configuration.md)
