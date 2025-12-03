# EPG Browser

The EPG Browser is a viewing tool that lets you see the guide data for your channels, helping you verify that EPG mappings are correct.

**What it is**:
- Visual EPG viewer built into IPTVBoss
- Shows program guide data for channels
- Verifies EPG mapping accuracy
- Previews what will appear in your player apps

### Access Methods

**From main menu**:
- **Layout → EPG Browser**
- Opens browser showing all channels in current layout
- Navigate between channels

**From Layout Editor** (specific channel):
- Select a channel in Layout Editor
- In Channel Options panel, click **"Open EPG"** button
- Opens EPG Browser focused on that specific channel
- Quickest way to verify individual channel mapping

**What it shows**:
- Program schedule for the selected channel
- Program titles
- Dates and times
- Descriptions (if available)
- EPG coverage range (how many days of guide data)

### Why use it

**Verify EPG mapping**: After assigning EPG to a channel, use EPG Browser to confirm:
- Correct channel mapped (shows proper programs)
- EPG data is current
- No gaps in guide data

**Troubleshoot EPG issues**:
- Channel shows "No EPG": Either no EPG assigned, or EPG source doesn't have data for this channel
- Wrong programs showing: Mapped to wrong EPG channel, needs remapping
- Old data: EPG needs syncing (Sources → Sync All EPGs)

**Preview before output**:
- See what guide data will appear in player
- Verify EPG customization (if using custom EPG layouts)

### Workflow Example

1. Map EPG to channel using Auto or Manual assign
2. Click "Open EPG" button in Channel Options
3. EPG Browser opens showing guide data
4. Verify program titles match what should be on this channel
5. If correct: Move to next channel
6. If incorrect: Close browser, remap channel to different EPG

### Tips

- **Color indicators**: In Layout Editor, "Highlight Missing EPGs" preference colorizes channels by EPG status
  - **Important**: Color indicates EPG is assigned, NOT that it's correct
  - Always verify important channels with EPG Browser
- **No data showing**: EPG source might not include this channel, try different EPG source
- **Gaps in schedule**: Normal for some channels, EPG sources vary in completeness

---

### Related Topics

- [Previous: Customizing EPG Layout (Advanced)](21_customizing_epg_layout.md)
- [Next: Manually outputting Layouts / Playlists, m3u and epg files for Players](23_manual_output.md)
