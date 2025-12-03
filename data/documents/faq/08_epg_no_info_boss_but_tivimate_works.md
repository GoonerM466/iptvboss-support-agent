# EPG Shows No Info in Boss But TiviMate Shows Guide

TiviMate is likely using cached EPG data or a different EPG source.

### Problem

EPG shows no information in IPTVBoss but TiviMate shows the guide correctly.

### Explanation

If TiviMate shows info but Boss doesn't, TiviMate is likely using cached EPG data from before, or it's using a different EPG source.

### Solution

**Test:** Add the playlist fresh in TiviMate (completely remove old one first). If TiviMate truly gets EPG from your Boss output, fresh playlist shouldn't have data if Boss doesn't.

**Check:**

1. Open EPG in Boss for that channel - is it truly empty?
2. Check the EPG mapping for that channel in Boss
3. TiviMate heavily caches EPG data - it may be showing old cached data

### Related Topics

- [EPG Mapping Keeps Reverting](11_epg_mapping_keeps_reverting.md)
- [Specific EPG Sources Show Limited Information](../troubleshooting/09_epg_sources_limited_information.md)
