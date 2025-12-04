# EPG Mapping Loss or Auto-Revert

EPG mappings disappear or revert to unmapped shortly after saving.

### Problem

EPG mappings don't persist or automatically revert after being saved.

### Symptoms

- EPG mappings disappear after service expiration/renewal
- Mapped EPG reverts to unmapped minutes after saving
- Specific groups (US|Movies, VOD categories) won't stay mapped
- EPG shows "no information" despite being mapped
- Mapping works temporarily then undoes itself

### Why This Happens

Auto-assign feature conflicts with manual mapping. Service credential changes (M3U sources especially) lose mapping. Group-level auto-mapping overrides your channel-level manual mapping during sync operations.

### Solution

**1. Disable conflicting Auto-Assign**
- Navigate to the problematic group
- Group Options: Disable "Auto Assign"
- This prevents automatic remapping during syncs

**2. Map EPG manually**
- Select channels needing EPG
- Assign EPG sources
- Click Save (important!)

**3. Test persistence**
- Don't sync sources immediately after mapping
- Verify mapping persists before syncing
- Output and test in player

**4. For lost mappings after renewal:**
- Settings → Restore Database → Local, Cloud or URL
    - URL restore must point to a direct download file
    - With Dropbox make sure the end of the URL is `&dl=1` for direct download
- Select backup from immediately before the sync
- Your channel mapping will return to pre-sync state

**5. Output and verify**
- Output → Output Current Layout M3U and EPG
- Check that EPG data appears in output

### For Service Renewal Specifically

- Create backup BEFORE renewing
- If possible, try using XC API instead of M3U
- XC sources better handle credential changes

### Workaround

- Keep frequent backups (daily) during active mapping work
- Use XC API sources instead of M3U when possible
- XC sources more resistant to credential changes
- Avoid syncing sources immediately after EPG mapping work

### Prevention

- Auto-Assign to OFF unless absolutely required
- Backup before service renewals
- When provider gives new credentials, don't immediately remove old source - set up new source as test first (if M3U)

### Known Limitations

- Auto-assign logic can be aggressive
- M3U source identity is tied to credentials - no way to preserve mappings through credential changes without XC
- Group vs channel-level mapping hierarchy not always intuitive

### Related Topics

- [EPG Mapping Keeps Reverting](../faq/11_epg_mapping_keeps_reverting.md)
- [Lost EPG Mappings After Renewal](../faq/10_lost_epg_mappings_after_renewal.md)
- [Source Sync Breaking Layouts](02_source_sync_breaking_layouts.md)
