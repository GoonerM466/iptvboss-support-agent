# Solution: Source Sync Breaking Layouts

**Flow ID**: source_sync
**Type**: diagnostic_solution
**Confidence**: medium
**Solution Steps**: 4

### Context

After syncing sources, layouts broke - channels disappeared, groups changed, or layouts became empty.

### Root Cause

Provider changed channel IDs, group names, or playlist structure. Boss layouts reference old IDs that no longer match.

### Confidence

**MEDIUM (60-70%)** - Can often fix, but may need manual rebuild

### Solution Steps

### 1. Understand What Happened

**Provider changed**:
- Channel IDs (tvg-id)
- Channel names
- Group names/categories
- Playlist structure

**Boss layouts reference**:
- Old IDs that don't match new playlist
- Result: channels "disappear" from layouts
- Actually: Boss can't find them anymore

### 2. Check Channel Matching

1. Boss → **Match Tab** or similar
2. Check if channels show "unmatched"
3. Some automatic matching may fix itself
4. Manual matching may be needed

### 3. Recreate Layout (If Needed)

If layout severely broken:

**Option A - Rebuild from scratch**:
1. Layout Manager → Create new layout
2. Add channels from updated source
3. Organize into groups
4. Delete old broken layout
5. Output new layout

**Option B - Duplicate and fix**:
1. Duplicate broken layout
2. Remove missing channels
3. Add them back from source
4. Verify and output

### 4. Prevention

**After rebuilding**:
1. **Backup database** immediately
2. Contact provider: "Please don't change IDs frequently"
3. Some providers warn before playlist changes
4. Keep backup before syncing

### ❌ When This Happens

**This is frustrating because**:
- Not Boss's fault - provider changed data
- No way to auto-fix (old IDs don't exist)
- Manual work required

**Boss can't**:
- Predict provider changes
- Auto-map old IDs to new IDs (impossible)
- Prevent providers from changing structure

### Related Topics

- [Source Sync Breaking Layouts](../../02_source_sync_breaking_layouts.md)
- [Layout Manager Guide](../../../user_guide/08_layout_manager.md)
- [EPG Mapping Loss](../../04_epg_mapping_loss_auto_revert.md)
