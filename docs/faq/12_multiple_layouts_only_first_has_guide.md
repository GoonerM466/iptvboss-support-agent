# Multiple Layouts Only Show Guide for First Layout

Use Universal EPG instead of individual EPGs per layout.

### Problem

You created additional layouts/EPGs but they only show guide for the first layout, then "No Information" for the others.

### Solution

You must either:
    - Ensure you are outputting an EPG for each layout & it is used with the M3U in the player
    *or*
    - Use Universal EPG instead (Recommended)

1. Set up Universal EPG:
**Sources → Universal EPG Options**
2. All layouts automatically use the same EPG source
3. No need to manage multiple EPG files
4. Saves significant cloud bandwidth

**If you must use individual EPGs:**

- Check "Days to Keep" settings for the layout (not just source)
- Verify EPG source is syncing properly (check last sync time)
- Look for override settings affecting EPG duration
- You may need to delete cached EPG files and re-sync

**Recommendation**: Universal EPG is the recommended approach for multiple layouts.

### Related Topics

- [Specific EPG Sources Show No Info](13_specific_epg_sources_no_info_hours.md)
- [EPG Sources Limited Information](../troubleshooting/09_epg_sources_limited_information.md)
