# Customizing EPG Layout (Advanced)


IPTVBoss allows you to customize how EPG information appears in your player apps. This powerful feature lets you control what information shows in program titles and descriptions.


**Visual References**:
- [image1](https://goonerm466.github.io/iptvboss-support-agent/images/image1.png) - EPG Layout Settings dialog showing custom title and description configuration with draggable components
- [image8](https://goonerm466.github.io/iptvboss-support-agent/images/image8.png) - Example result of custom EPG layout showing formatted program title and description in player
- [image24](https://goonerm466.github.io/iptvboss-support-agent/images/image24.png) - Another example result of custom EPG layout showing formatted program information
- [image2](https://goonerm466.github.io/iptvboss-support-agent/images/image2.png) - Third example result of custom EPG layout showing formatted program details
**Compatible Players**:
- TiviMate (enable "Two-line program titles")
- Implayer (enable "Two-line program titles")
- Other players may support custom EPG formatting

**What you can customize**:
- EPG Title format
- EPG Description format
- Add/remove components like:
  - NEW tag (for new episodes)
  - LIVE tag (for live events)
  - Episode information
  - Season/Episode numbers
  - Ratings
  - Year
  - Categories
  - And more

### Access EPG Layout Settings

**For specific EPG source**:
- Go to **Sources → Sources Manager**
- Select an EPG source
- Click **"EPG Layout Settings"** button
- EPG Layout Settings dialog opens

**For layout override**:
- Some layouts can override EPG layout settings
- Layout Manager → Select layout → "EPG Layout Override" button
- (If "Override EPG Layout Settings" is enabled for that layout)

### Customizing the Layout

**Title and Description Windows**:
- You'll see two panels: **Title** and **Description**
- These control what appears in your player's EPG

**Available Components** (bottom of dialog):
- Drag components from the bottom into Title or Description windows
- Common components:
  - `{NEW}` - Shows "NEW" tag for new episodes
  - `{LIVE}` - Shows "LIVE" tag for live broadcasts
  - `{EPISODE_TITLE}` - Episode name
  - `{SEASON}` - Season number
  - `{EPISODE}` - Episode number
  - `{RATING}` - Content rating
  - `{YEAR}` - Release year
  - `{CATEGORIES}` - Program categories

**Arrangement**:
- Drag components to arrange order
- Remove components you don't want
- Add text/separators between components

**Important Notes**:
- Your EPG source must include these components for them to appear
- Not all EPG sources have all fields available
- Players are limited in how much they can display (keep it reasonable)
- Premium EPG sources (Schedules Direct, TV Guide, Zap2it) have the most components

### Copy Layout From Another Source

If you created an EPG layout you like and want to use it for other sources:

1. Add the new EPG source
2. Open its EPG Layout Settings
3. Click **"Copy Layout From"** button
4. Select the source whose layout you want to copy
5. Click Copy
6. The layout is duplicated to the new source

### Example Use Case

DVR Recording Setup:
- Some DVR software (Emby, Plex) only records episodes marked "NEW", not "LIVE"
- Solution: Add `{NEW}` tag to sports event titles
- Settings → Manage Live Tags → Change "Live Tag Format" to "New"
- Sports events now appear as "NEW" and DVR will record them

### Troubleshooting

- **Components not appearing**: EPG source doesn't include that data
- **Player not showing custom format**: Enable "Two-line program titles" in player settings
- **Too much information**: Player apps have display limits, simplify your layout


---

### Related Topics

- [Previous: Managing EPG Sources](20_managing_epg_sources_full.md)
- [Next: EPG Browser](22_epg_browser.md)
