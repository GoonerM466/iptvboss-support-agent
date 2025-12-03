# Custom Layout Channels Disappeared After Source Sync

Provider likely changed channel names/IDs.

### Problem

After syncing your source, all your custom layout channels disappeared.

### Explanation

Your provider likely changed channel names/IDs, causing IPTVBoss to see them as removed.

### Recovery

1. Restore database backup from before the sync
2. All your channel mapping should return

### Prevention

- Use **XC sources** instead of M3U when possible (less susceptible to changes)
- Check logs for "... Was removed" messages after syncs
- Consider preventing source sync temporarily if your provider is unstable

**If you must remap everything**: Provider changed their channel structure fundamentally. Keep frequent backups before syncing.

### Related Topics

- [Source Sync Breaking Layouts](../troubleshooting/02_source_sync_breaking_layouts.md)
- [All Channels Disappeared but Groups Remain](30_all_channels_disappeared_groups_remain.md)
