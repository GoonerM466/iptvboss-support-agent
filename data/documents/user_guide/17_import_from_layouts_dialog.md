# Import Channels From Layouts Dialog

**What it does**: Copies channels from one layout to another layout.

**Visual Reference**: [IPTVBoss 3.5 User Manual\images\image31.png](../IPTVBoss 3.5 User Manual/images/image31.png)

### Use Cases

- Creating a second layout for different users (e.g., Kids layout from Main layout)
- Sharing channels between layouts
- Creating specialized layouts from master layout

### Import Methods

**By Layout**: Import all enabled groups from selected layout(s)
- Select one or more layouts
- Click "Import by Layout"
- All enabled groups from those layouts get imported

**By Group**: Import specific groups
- Select one or more groups (multi-select with Shift/Ctrl)
- Click "Import by Group"
- Only selected groups get imported

**By Channel**: Import individual channels
- Select group to see its channels
- Multi-select specific channels
- Click "Import by Channel"

**Search Boxes**:
- Bottom of Groups panel and Channels panel
- Filter lists by typing
- Helps find specific groups/channels across layouts

**Import Behavior**:
- Channels can be imported multiple times
- If a Layout Group name matches an existing group, channels go into that existing group
- Otherwise, a new Layout Group is created

### Options

**Keep Dialog Open After Import**:
- Same as Sources dialog
- Keeps dialog open for multiple imports

**Import as Linked Layout Group**:
- **Important advanced option**
- Creates a **carbon copy** of the selected group
- **Group is NOT editable** in the new layout
- Any changes made to the group in the **original layout** automatically appear in the new layout
- **Use cases**:
  - Master layout with shared content across multiple user layouts
  - Maintaining consistent groups across layouts
  - Centralized control of specific groups

**Don't Import Duplicate Channels**:
- Prevents importing channels that already exist in target Layout Group

### Tips

- **First-time setup**: Import by Category/Group for bulk setup
- **Fine-tuning**: Import by Channel for specific additions
- **Multi-layout management**: Use "Linked Layout Groups" for content you want synced across layouts
- **Search feature**: Essential when dealing with large channel lists

---

### Related Topics

- [Previous: Import Channels From Sources Dialog](16_import_from_sources_dialog.md)
- [Next: Mapping EPG to Channels](18_mapping_epg_to_channels.md)
