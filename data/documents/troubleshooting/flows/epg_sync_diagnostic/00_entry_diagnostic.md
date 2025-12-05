# EPG Sync Issues Diagnostic - Entry Point

**Flow ID**: epg_sync
**Type**: diagnostic_entry
**Confidence**: low (requires questions)

### Common User Phrases

- "EPG not syncing"
- "No EPG data"
- "EPG won't update"
- "Guide information missing"
- "EPG shows limited info"
- "Only shows current program"
- "EPG sync failed"

### Diagnostic Questions

**Question 1**: "Is the EPG missing completely, or does it show partial/limited information?"
- **Missing completely** → Source sync issue → [Source Sync Problems](01_solution_source_sync.md)
- **Partial/limited** → Source limitation or mapping issue → [Limited EPG Info](02_solution_limited_info.md)

**Question 2**: "Does Boss show EPG data in EPG Browser?"
- **Yes** → Output/player issue → [EPG Not in Player](../no_data_diagnostic/02_solution_boss_output.md)
- **No** → Boss sync problem → [Boss EPG Sync](01_solution_source_sync.md)

**Question 3**: "What type of EPG source are you using (XML URL, GZ file, Xtream Codes)?"
- Helps identify source-specific issues
- Different sources have different limitations

### Related Guide

[EPG Sources Show Limited Information](../../09_epg_sources_limited_information.md)
