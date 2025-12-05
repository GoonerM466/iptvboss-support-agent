# EPG Shows No Info in My Player

IPTV Player, such as Tivimate, iMplayer, Sparkle, etc, shows no or limited program information in the guide.

### Problem

EPG shows no information in player

### Explanation

If you have no or liited EPG in your player, it's important to perform the basic steps first and find the most likely are to investigate - the issue might just be player side.

### Solution

**Test:** Sync your EPG in the player to see if this correts the issue. If it does it could just be a temporary issue but might be worth checking why your player didn't update, set up a player EPG sync schedule, etc.
If it doens't you need to find out at what stage the data is failing, by now checking in Boss itself.

**Check:**

1. Open EPG in Boss for that channel - do you see up to date data, or is it also empty?
    - If you see data, look into your sync schedule to make sure its running as planned. Check logs for errors.
    - If you dont see data, then there might be a deeper issue
2. Sync your EPG sources in Boss to see if this corrects the issue
3. Check channel EPG mappings
4. Output and sync your player once you have data showing in Boss
5. Additionally, ensure you have a sync schedule set up and/or check logs for errors to pinpoint why your sync schedule is failing

### Related Topics

- [EPG Mapping Keeps Reverting](11_epg_mapping_keeps_reverting.md)
- [Specific EPG Sources Show Limited Information](../troubleshooting/09_epg_sources_limited_information.md)
