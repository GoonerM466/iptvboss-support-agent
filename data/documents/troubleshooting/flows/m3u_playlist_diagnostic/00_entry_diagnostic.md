# M3U Playlist Issues Diagnostic - Entry Point

**Flow ID**: m3u_playlist
**Type**: diagnostic_entry
**Confidence**: low (requires questions)

### Common User Phrases

- "No channels"
- "Channels missing"
- "Playlist not loading"
- "M3U sync failed"
- "Channels disappeared"
- "Old channels showing"
- "Wrong channels"

### Diagnostic Questions

**Question 1**: "Are channels missing in Boss or in your player?"
- **In Boss** → Source sync issue → [Source Sync Problems](01_solution_playlist_sync.md)
- **In Player only** → Output/player sync → [Player Sync](../player_sync_diagnostic/01_solution_complete_workflow.md)

**Question 2**: "Did you recently add a new playlist source?"
- **Yes** → Did you sync it? → [Add and Sync Source](01_solution_playlist_sync.md)
- **No** → Existing source issue

**Question 3**: "What type of playlist source (M3U URL or Xtream Codes)?"
- **M3U URL** → Direct playlist sync
- **Xtream Codes** → API-based, check credentials

### Related Guides

- [Adding Sources](../../../user_guide/03_adding_sources.md)
- [Source Sync Issues](../source_sync_diagnostic/00_entry_diagnostic.md)
