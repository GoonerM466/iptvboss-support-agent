# IPTVBoss Menu Structure Quick Reference

**Purpose**: Accurate reference for all menu locations and navigation paths in IPTVBoss
**For AI Assistant**: Use this to provide accurate menu paths when users ask "where is...?"

**CRITICAL**: This is the ACTUAL menu structure from IPTVBoss. Use ONLY these paths.

---

## Main Menu Structure

### Layout Menu

**Layout → Layout Manager**
- Create new layouts
- Edit existing layouts
- Delete layouts
- Duplicate layouts
- Set active layout

**Layout → Layout Editor**
- Open layout for editing channels
- Edit channel properties
- Manage groups
- Assign EPG and logos

**Layout → EPG Browser**
- Browse available EPG data
- Search EPG listings

**Layout → New Channel Manager**
- Configure automatic channel imports
- Set up source-to-layout mappings
- Manage import rules

**Layout → New Category Manager**
- Manage categories and groups
- Category organization

---

### Sources Menu

**Sources → Sources Manager**
- Add/edit/delete M3U and XC sources
- Configure source settings
- View source status

**Sources → Add M3U Source**
- Add new M3U playlist source

**Sources → Add API Source**
- Add new XC/API source

**Sources → Sync All Sources**
- Manually trigger sync for all sources
- Refresh all M3U/XC playlists

**Sources → Prefix Auto-Removal**
- Configure automatic prefix removal from channel names

**Sources → Add EPG**
- Add EPG (guide) source

**Sources → Sync All EPGs**
- Manually trigger EPG sync for all sources
- Refresh guide data

**Sources → Universal EPG Options**
- Enable/disable Universal EPG
- Configure EPG matching settings

**Sources → EPG Search Options**
- Configure EPG search behavior

**Sources → Manage New Tags**
- Tag management

**Sources → Manage Users**
- Add/edit/delete users
- User-specific layouts
- Per-user configuration

---

### Settings Menu

**Settings → IPTVBoss Settings**
- User Agent
- Timeout
- Logging level
- TinyURL API
- Cloud Provider configuration (Dropbox/Google Drive)
- Cloud sync enable/disable
- Cloud Authorization and credentials

**Settings → IPTVBoss Pro Settings**
- IPTVBoss Pro token entry
- Subscription status
- Days to Keep setting
- License information

**Settings → Theme Settings**
- Application theme configuration
- Color schemes

**Settings → XC Server Settings**
- Enable/disable XC Server
- Port configuration
- Server settings

**Settings → Email Settings**
- Email notification configuration

**Settings → Database Settings**
- Database configuration options

**Settings → Restore Database**
- Restore from backup
- Database recovery

**Settings → Sync Schedule**
- Configure automated sync schedule
- Set update intervals

---

### Output Menu

**Output → Current M3U**
- Generate M3U for current layout only

**Output → Current EPG**
- Generate EPG (XML) for current layout only

**Output → Current M3U & EPG**
- Generate both M3U and EPG for current layout

**Output → All Layouts & EPG**
- Generate M3U and EPG for all layouts

**Output → View Cloud Links**
- View/copy cloud URLs for playlists
- Access TinyURL links if configured

---

### Preferences Menu

**Preferences → Highlight EPGs**
- Highlight channels with EPG data

**Preferences → Highlight Missing Logos**
- Highlight channels without logos

**Preferences → Auto Load Logo**
- Automatically load logos

**Preferences → Use EPG Logos Automatically**
- Use logos from EPG data

**Preferences → Use 24h Time Format**
- Toggle 24-hour time display

**Preferences → Open Editor on Start**
- Automatically open Layout Editor on startup

**Preferences → Preserve Window Size on Exit**
- Remember window size between sessions

**Preferences → Disable Dummy EPG Source**
- Disable dummy EPG placeholders

**Preferences → Use Channel Numbers**
- Display channel numbers

**Preferences → Ignore Prefixes When Sorting**
- Sort channels ignoring prefixes

**Preferences → EPG Emby Support**
- Enable Emby EPG compatibility

**Preferences → Add Provider Name to EPG**
- Include provider name in EPG data

**Preferences → Use CUID in M3U Output**
- Use channel unique IDs in output

**Preferences → AED: Use Portrait Logos**
- Advanced EPG Dummies: Use portrait-oriented logos

**Preferences → AED: Use Portrait Icons**
- Advanced EPG Dummies: Use portrait-oriented icons

---

### Logs Menu

**Logs → View Logs**
- View application logs
- Check for errors

---

## Context Menu Actions (Right-Click)

### In Layout Editor - Channel List

**Right-click on channel(s)**:
- Delete selected channel(s)
- Move to group
- Copy channel properties
- Paste channel properties
- Set logo
- Clear EPG assignment

### In Layout Manager

**Right-click on layout**:
- Edit layout
- Duplicate layout
- Delete layout
- Set as active layout

### In Sources Manager

**Right-click on source**:
- Edit source
- Update source now
- Delete source
- View source details

---

## Common Workflows by Menu Path

### Initial Setup
1. **Settings → IPTVBoss Settings** (configure cloud)
2. **Settings → IPTVBoss Pro Settings** (enter token)
3. **Sources → Add M3U Source** or **Sources → Add API Source** (add first source)
4. **Sources → Sync All Sources** (download playlist)
5. **Layout → Layout Manager** (create first layout)

### Daily Operations
1. **Sources → Sync All Sources** (refresh playlists)
2. **Sources → Sync All EPGs** (refresh guide)
3. **Layout → Layout Editor** (edit channels)
4. **Output → Current M3U & EPG** (publish changes)

### Troubleshooting
1. **Settings → Database Settings** (check database)
2. **Settings → Restore Database** (if issues occur)
3. **Logs → View Logs** (check for errors)
4. **Sources → Sources Manager** (check source status)

---

## Important Corrections from Previous Version

**⚠️ THERE IS NO "Tools" MENU IN IPTVBOSS ⚠️**

**INCORRECT Menu Paths** (NEVER use):
- ❌ Tools → Update Sources
- ❌ Tools → Update EPG
- ❌ Tools → Output Layouts
- ❌ Tools → Database Backup
- ❌ Tools → Restore Database

**CORRECT Menu Paths** (ALWAYS use):
- ✅ Sources → Sync All Sources
- ✅ Sources → Sync All EPGs
- ✅ Output → Current M3U & EPG (or other Output options)
- ✅ Settings → Database Settings
- ✅ Settings → Restore Database

---

## Menu Format Convention

In documentation and responses, use this format:
```
Menu → Submenu → Item
```

**Examples**:
- Settings → IPTVBoss Settings
- Sources → Sync All EPGs
- Output → Current M3U & EPG

Use the → character (not >, not >>, not arrows)

---

## Platform-Specific Notes

### Windows
- Menu bar always visible at top of window
- Standard Windows menu behavior
- Alt key activates menu

### macOS
- Menu bar follows macOS conventions
- Cmd+, for Settings (standard)

### Linux
- Menu bar in application window
- Follows GTK conventions

---

**Last Updated**: December 1, 2024 (Corrected based on actual software menus)
