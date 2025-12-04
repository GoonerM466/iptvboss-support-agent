# Import Channels From Sources Dialog

**What it does**: Imports channels from your IPTV provider sources into the current layout.

**Visual Reference**: ![image30](https://goonerm466.github.io/iptvboss-support-agent/images/image30.png)

### Import Methods

**By Source**: Import all enabled groups from selected source(s)
- Select one or more sources
- Click "Import by Source"
- All enabled categories from those sources get imported

**By Category**: Import specific categories
- Select one or more categories (multi-select with Shift/Ctrl)
- Click "Import by Category"
- Only selected categories get imported

**By Channel**: Import individual channels
- Select category to see its channels
- Multi-select specific channels
- Click "Import by Channel"

**Multi-Select**:
- **Shift+Click**: Select range
- **Ctrl+Click**: Select individual items

**Search Boxes**:
- Bottom of Groups panel and Channels panel
- Filter lists by typing search term
- Makes finding specific groups/channels faster

**Import Behavior**:
- Channels can be imported multiple times (no duplicate prevention by default)
- If a Layout Group name matches a Provider Category name, channels go into that existing Layout Group
- Otherwise, a new Layout Group is created matching the Category name

### Options

**Keep Dialog Open After Import**:
- When enabled: Dialog stays open after clicking import
- **Use case**: Manually adding multiple individual groups or channels one at a time
- When disabled: Dialog closes after import

**Add to Layout Group included Categories**:
- **Enabled by default**
- Links this Provider Category to this Layout Group
- **Result**: Future channels added by provider to this category automatically import to this Layout Group
- This is how automatic channel updates work (see New Channel Manager)

**Don't Import Duplicate Channels**:
- When enabled: Won't import a channel that already exists in the target Layout Group
- Prevents duplicate entries
- Useful when re-importing or updating from source

---

### Related Topics

- [Previous: Importing Channels into Layouts - Overview](15_importing_channels_overview.md)
- [Next: Import Channels From Layouts Dialog](17_import_from_layouts_dialog.md)
