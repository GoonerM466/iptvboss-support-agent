# Source Sync Issues Diagnostic - Entry Point

**Flow ID**: source_sync
**Type**: diagnostic_entry
**Confidence**: low (requires questions)

### Common User Phrases

- "Sources won't sync"
- "Sync failed"
- "Can't sync sources"
- "Sources not updating"
- "Layouts broken after sync"
- "Lost channels after sync"

### Diagnostic Questions

**Question 1**: "What type of sources (playlists, EPGs, or both)?"
- **Playlists** → [M3U Sync Issues](../m3u_playlist_diagnostic/01_solution_playlist_sync.md)
- **EPGs** → [EPG Sync Issues](../epg_sync_diagnostic/01_solution_source_sync.md)
- **Both** → Multiple issues

**Question 2**: "Do you get an error message, or does sync complete but data is wrong?"
- **Error message** → Auth or connectivity → [Sync Errors](01_solution_sync_errors.md)
- **No error but wrong data** → Layouts broken → [Layout Breakage](02_solution_layout_broken.md)

**Question 3**: "Did layouts/channels break after syncing?"
- **Yes** → Common issue → [Source Sync Breaking Layouts](02_solution_layout_broken.md)
- **No** → Just sync failure

### Related Guide

[Source Sync Breaking Layouts](../../02_source_sync_breaking_layouts.md)
