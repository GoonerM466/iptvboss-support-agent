# Handling Provider Changes

Providers sometimes change channel names, URLs, or structure. This can break your layouts.

**Prevention**:

1. **Check provider announcements**
   - Before syncing, see if provider posted changes

2. **Use XC API instead of M3U**
   - XC handles changes better
   - More stable than M3U URLs
   - Ask provider if they offer XC

**When sync breaks layouts**:

**Symptoms**:
- Channels disappear after sync
- EPG mappings lost
- Groups empty

**Recovery**:
1. Menu → Restore
2. Select backup from immediately before sync
3. Your layouts return to pre-sync state

**Going forward**:
- Don't sync that source again until provider stabilizes
- Or remap everything manually (time-consuming)
- Or switch to XC API if available

**Credential changes**:
- New username/password from provider
- With M3U: Creates new source identity, loses all mappings
- With XC: Often preserves mappings
- Backup before changing credentials


---

### Related Topics

- [Previous: Restoring from Backup](30_restoring_from_backup.md)
- [Next: Managing Multiple Users](32_managing_multiple_users.md)
