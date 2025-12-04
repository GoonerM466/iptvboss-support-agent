# EPG Mapping for Specific Group Keeps Reverting

Auto Assign feature may be fighting your manual mapping.

### Problem

EPG mapping for a specific group (like US|Movies) keeps reverting after you save.

### Solution

**Check these settings:**

1. Are you clicking Save after mapping?
2. Do you have "Auto Assign" enabled in group options? (This can auto-remap channels)
3. Are you syncing sources immediately after mapping? (Can overwrite changes)

**Steps to fix:**

1. Disable "Auto Assign" for the problematic group (Group Options)
    - Uncheck "Assign AED..."
    - Uncheck "Assign Dummy..."
2. Map your EPG for the channels
3. Click Save
4. Don't sync sources immediately
5. Output and verify mapping persists

If Auto Assign is enabled, it can fight your manual mapping during sync operations.

### Related Topics

- [EPG Mappings Lost After Renewal](10_lost_epg_mappings_after_renewal.md)
- [Source Sync Breaking Layouts](../troubleshooting/02_source_sync_breaking_layouts.md)
