# All Channels Disappeared from Layout After Sync But Groups Remain

Provider changed channel structure/IDs - restore immediately.

### Problem

All your channels disappeared from layout after syncing, but groups remain.

### Solution

**Restore immediately:**

1. **Settings → Restore → Local, Cloud or URL**
2. Select backup from before the sync
3. This recovers your channel mappings
4. Consider converting source to XC if you are currently using M3U

### Why This Happened

- Provider changed channel structure/IDs
- Boss saw all channels as "removed"
- Your group structure remained but channel assignments were lost

### Prevention

- Keep regular backups before syncing. Use XC sources when possible (more stable).
- Increase the "auto remove" setting for the source: **Sources → Sources Manager → (Highlight Source) → Settings → set auto remove to a higher number.**

*If channels are totally gone and not available to import then your provider removed them from their line up*.

### Related Topics

- [Custom Channels Disappeared After Sync](29_custom_channels_disappeared_after_sync.md)
- [Source Sync Breaking Layouts](../troubleshooting/02_source_sync_breaking_layouts.md)
