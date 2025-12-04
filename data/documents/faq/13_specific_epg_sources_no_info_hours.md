# Specific EPG Sources Show No Info After Hours

Days to Keep settings may be too low, or cache may be corrupted. If an external EPG source is affected you should check with the provider, in addition to performing the steps below.
Boss provides upto 7 days of data for most channels.

### Problem

Specific EPG sources (USA, USA Local) show no info after a couple of hours.

### Solution

**Check Days to Keep settings:**

1. **Sources → Sources Manager**
2. Highlight your EPG source
3. Click **EPG Settings**
4. Check **"Days to Keep"** - default is **3 days**
5. Set to **7 days** or **ALL** for full coverage
6. Also check for EPG overrides on specific channels (if EPG Override enabled)

**Cache corruption fix:**

1. Shut down IPTVBoss completely
2. Navigate to `IPTVBoss/cache` folder
3. Delete affected EPG cache files
4. Start IPTVBoss
5. **Sources → Sync All EPGs**
6. **Output → Current M3U & EPG**
7. Test in player

Make sure "Days to Keep" is not set to 0 or very low (1-2). Default is 3 days which may not be enough.
If your player can handle it, and you have no bandwidth concerns, 7 days or "All" is the recommend value.

### Related Topics

- [Multiple Layouts Only First Has Guide](12_multiple_layouts_only_first_has_guide.md)
- [EPG Sources Limited Information](../troubleshooting/09_epg_sources_limited_information.md)
