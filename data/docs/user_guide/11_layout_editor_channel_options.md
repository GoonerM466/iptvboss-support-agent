# Layout Editor - Channel Options

When you select one or more channels, the Channel Options panel lets you edit channel properties.

**Channel Name**:
- Editable text box
- Your custom name for the channel
- Provider's original name shown above the box (greyed out)
- Can be different from provider name

**Channel Number**:
- Default: -1 (automatic numbering)
- **Recommended**: Leave at -1
- If you manually assign numbers, **read the tooltip** (hover over field)
- Manual numbering can cause gaps/conflicts

**EPG Source**:
- Dropdown: Which EPG source to use for this channel
- Choose from your enabled EPG sources (US, UK, Sports, etc.)

**EPG-ID**:
- Dropdown: Specific EPG channel ID from the selected source
- Must match a channel in the EPG source
- This is what links your channel to guide data

### EPG Assignment Buttons

**Search Options**:
- Opens dialog to select which EPG sources to search
- **Best Practice**: Only select the region you need
- Example: Mapping USA channel? Only enable USA EPG source
- Improves accuracy by avoiding conflicts from similar international channels

**Auto Assign** (Pro only):
- Automatically matches channel to EPG based on channel name
- Uses enabled sources from Search Options
- Uses Sensitivity setting (see below)
- Quick but may need manual verification

**Manual Assign**:
- Opens dialog showing best EPG matches
- Cycles through highlighted channels one by one
- You select correct EPG from list
- More accurate than Auto

**Sensitivity** dropdown:
- Controls how strict Auto matching is
- Default: 0.9
- Higher = more strict (fewer errors, fewer matches)
- Lower = less strict (more matches, more errors)
- **Recommendation**: Leave at 0.9 unless you understand the implications

**Channel Logo**:
- URL text box showing current logo link
- Image preview (if auto-load logos enabled)
- Click image to view logo

### Logo Buttons

**EPG Logo**: Import logo from selected EPG source (if available)

**M3U Logo**: Import logo from provider's M3U/API source

**Logo Options** (if available):
- Auto-assign logo when source changes
- Can set to use EPG or M3U as default

### Channel Toggle Options

**Channel Enabled** checkbox:
- Enabled: Channel appears in output
- Disabled: Channel hidden from output (but kept in layout)

**Ignore Name Changes** checkbox:
- When enabled: Channel keeps your custom name even if provider renames
- When disabled: Provider name changes will update your channel name

### Action Buttons

**Revert to Provider Name**:
- Resets channel name to provider's original name
- Undoes your custom naming

**Channel Info**:
- Opens dialog showing:
  - Stream URL
  - Channel ID
  - Source information
  - Other technical details

**Open EPG**:
- Opens EPG Browser focused on this channel
- Shows guide data for verification

**Open Stream** (requires VLC):
- Opens channel stream in VLC player for testing
- **Requirements**:
  - VLC64 must be installed
  - VLC architecture (x86/x64) must match Java architecture
- Use to test if stream works before outputting

**Save Channel(s)**:
- Saves changes made to channel properties
- **Important**: Required after changing name, number, logo URL, EPG
- Checkboxes (enabled, ignore name changes) auto-save

### Bulk Editing Channels

**Select multiple channels**:
- Use Shift+Click (range) or Ctrl+Click (individual)
- Or use "Select All" checkbox

**Channel Options become greyed out**

**To edit bulk-selected channels**:
- **Click on the label itself** (e.g., click the text "Channel Logo")
- Field unlocks for bulk editing
- Make changes
- Click Save Channel(s)

**Bulk edit use cases**:
- Assign same EPG source to many channels
- Bulk enable/disable channels
- Apply logo from EPG to multiple channels at once

---

### Related Topics

- [Previous: Working in Layout Editor - Overview](10_layout_editor_overview.md)
- [Next: Layout Editor - Group Options](12_layout_editor_group_options.md)
