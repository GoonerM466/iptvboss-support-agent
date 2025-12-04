# Source Sync Failures and Updates Breaking Layouts

Syncing source causes channels to disappear or sync errors.

### Problem

Source synchronization causes channels to disappear or produces errors.

### Symptoms

- All channels disappear after syncing source
- Groups remain but channels are gone
- Error messages during source update
- Error: "File does not exist"
- Provider channels not updating despite successful sync
- Layouts completely empty after sync

### Why This Happens

Provider changed channel names, IDs, or entire structure. IPTVBoss treats renamed channels as "removed channels" and new channels as additions, completely losing your layout associations. M3U sources are particularly susceptible - XC API sources handle changes better.

### Solution

**1. BEFORE syncing:**
- Check provider announcements for structure changes
- Switch your source to XC before the next scheduled sync

**2. After problematic sync (Recovery):**
- Settings → Restore Database → Local, Cloud or URL
    - URL restore must point to a direct download file
    - With Dropbox make sure the end of the URL is `&dl=1` for direct download
- Select backup from immediately before the sync
- Your channel mapping will return to pre-sync state

**3. For recurring issues:**
- Switch to XC API source if provider offers it (more stable than M3U)
- XC sources handle credential and minor structure changes better
- Check logs for "... Was removed" messages to understand what changed

**4. For series sync errors specifically:**
- Go to Source settings
- Enable "Ignore Series" option
- Retry sync
- This bypasses series/VOD sync which often causes errors

### Workaround

If provider frequently changes structure:
- XC is highly recommended
- Consider not syncing automatically
- Do manual syncs only when you have time to remap if needed
- Keep recent backup immediately before each sync attempt
- Some users sync weekly instead of daily to reduce exposure
- Raise auto remove setting for the source in source settings
- Ignore both VOD & Series

**Why recovery works**: Backups preserve your channel-to-layout associations. Since providers rarely delete actual streams (just rename them), your backed-up associations often still work even with "old" IDs.

### Known Limitations

- No way to prevent provider changes from breaking mappings
- M3U sources more fragile than XC sources
- Credential changes with M3U sources create entirely new source identity (complete mapping loss)
- Provider structural changes can't be worked around - only recovered from

### Related Topics

- [Lost EPG Mappings After Renewal](../faq/10_lost_epg_mappings_after_renewal.md)
- [Custom Channels Disappeared After Sync](../faq/29_custom_channels_disappeared_after_sync.md)
- [All Channels Disappeared But Groups Remain](../faq/30_all_channels_disappeared_groups_remain.md)
