# Playlist Source Options

Once source is added, configure these options:

### Channel Name Modifications

**Prefix** (Optional):
- Enter text to add BEFORE all channel names from this source
- Example: "UK: " → channels become "UK: BBC One", "UK: ITV", etc.
- Useful for identifying source when mixing multiple providers

**Suffix** (Optional):
- Enter text to add AFTER all channel names from this source
- Example: " (HD)" → channels become "ESPN (HD)", "CNN (HD)", etc.

**Source Color** (Optional):
- Select color for channels from this source
- Channels display in this color in Layout Editor
- Helps visually identify which source provides which channels

### Content Filtering

**Ignore VOD** checkbox:
- When enabled: Source will NOT sync VOD (Video on Demand) channels
- Reduces clutter if you don't use VOD
- Speeds up sync

**Ignore Series** checkbox:
- When enabled: Source will NOT sync TV Series channels
- Useful if you only want live channels
- Can fix series sync errors from problematic providers
- Series is not supported when outputing via m3u

### Automatic Sync Behavior

**Automatically Sync Source on GUI Start**:
- When enabled: Source syncs automatically when you open IPTVBoss GUI
- Default: Disabled
- **Caution**: Can slow down startup if you have many sources

**Automatically Enable New Groups Added by Provider**:
- When enabled: New categories from provider automatically enable
- New channels in those categories appear in Layout Editor
- When disabled: Must manually enable new categories
- **Recommended**: Enable for stable providers, disable for frequently-changing providers

**Automatically Clear Channels Removed by Provider after ___ Days**:
- Enter number of days
- Channels provider removes are kept for this many days
- If channel doesn't return within timeframe, Boss removes it from layouts
- **Purpose**: Handles temporary provider outages vs permanent removals
- **Example**: Set to 7 days → if provider removes channel but brings it back within a week, your layouts aren't affected
- **Recommended**: At least 2 days

### Advanced Options

**Provider Uses Tokens** (M3U option only):
- Enable if provider uses token system where stream IDs change regularly
- IPTVBoss uses channel names as "Key" instead of stream ID
- **Only use if provider specifically uses tokens**
- Not needed for most providers

**Use API for Series**:
- Makes IPTVBoss use API for series channels
- **Very slow**
- Only use if provider doesn't allow "M3U" for series
- Most providers don't need this


---

### Related Topics

- [Previous: Managing Playlist Sources - Adding](04_managing_playlist_sources_adding.md)
- [Next: Managing EPG Sources - Adding](06_managing_epg_sources_adding.md)
