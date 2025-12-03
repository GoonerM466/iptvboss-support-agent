# IPTVBoss Folder Locations Reference

**Purpose**: Quick reference for file and folder locations across different platforms
**For Claude Project**: Use this when users ask "where are my files?" or "where does IPTVBoss store...?"

---

## Platform-Specific Installation Locations

### Windows

**Application Location**:
- Default: `C:\Program Files\IPTVBoss\` (installed version)
- Portable: Wherever user extracted the ZIP file

**Database Location**:
- `%APPDATA%\IPTVBoss\iptvboss.db`
- Full path typically: `C:\Users\[Username]\AppData\Roaming\IPTVBoss\iptvboss.db`

**Backup Location**:
- `%APPDATA%\IPTVBoss\Backups\`
- Full path: `C:\Users\[Username]\AppData\Roaming\IPTVBoss\Backups\`
- Backup files: `iptvboss_backup_YYYY-MM-DD_HH-MM-SS.db`

**Output Files** (local, before cloud upload):
- `%APPDATA%\IPTVBoss\Output\`
- Full path: `C:\Users\[Username]\AppData\Roaming\IPTVBoss\Output\`

**NoGUI Script Location** (if used):
- User-defined location
- Commonly: Desktop or Documents folder

---

### macOS

**Application Location**:
- `/Applications/IPTVBoss.app`

**Database Location**:
- `~/Library/Application Support/IPTVBoss/iptvboss.db`
- Full path: `/Users/[Username]/Library/Application Support/IPTVBoss/iptvboss.db`

**Backup Location**:
- `~/Library/Application Support/IPTVBoss/Backups/`

**Output Files** (local, before cloud upload):
- `~/Library/Application Support/IPTVBoss/Output/`

---

### Linux

**Application Location**:
- User-defined (extracted from tar.gz)
- Commonly: `/opt/IPTVBoss/` or `~/IPTVBoss/`

**Database Location**:
- `~/.config/IPTVBoss/iptvboss.db`
- Full path: `/home/[username]/.config/IPTVBoss/iptvboss.db`

**Backup Location**:
- `~/.config/IPTVBoss/Backups/`

**Output Files** (local, before cloud upload):
- `~/.config/IPTVBoss/Output/`

---

## Cloud Storage Locations

### Dropbox

**App Folder** (recommended):
- Path in Dropbox: `Dropbox/Apps/[YourAppName]/`
- Files stored here: `playlist.m3u`, `guide.xml`

**Full Dropbox** (if configured):
- User-defined folder within Dropbox
- Example: `Dropbox/IPTVBoss/`

**Access**:
- Web: https://www.dropbox.com/home/Apps/[YourAppName]
- Desktop: `[Dropbox folder]/Apps/[YourAppName]/`

---

### Google Drive

**App Data Folder**:
- Hidden folder in Google Drive
- Not visible in normal Drive view
- Accessible only via IPTVBoss or Drive API

**Shared Folder** (if configured):
- User-defined folder in Google Drive
- Example: `My Drive/IPTVBoss/`

**Access**:
- Web: https://drive.google.com/
- Navigate to configured folder
- Files: `playlist.m3u`, `guide.xml`

---

## Output File Naming

### Default Naming
- M3U file: `playlist.m3u`
- EPG file: `guide.xml`

### Multi-User Setup
- User-specific files: `[username]_playlist.m3u`, `[username]_guide.xml`
- Location: Same cloud folder, different filenames

### Multi-Layout Setup
- Layout-specific files: `[layoutname].m3u`, `[layoutname].xml`
- Requires manual configuration

---

## Database Backup Files

### Automatic Backups
- Filename format: `iptvboss_backup_YYYY-MM-DD_HH-MM-SS.db`
- Example: `iptvboss_backup_2024-12-01_14-30-00.db`
- Location: Platform-specific Backups folder (see above)

### Manual Backups
- Same format as automatic
- User can specify custom location via Tools → Database Backup

### Retention
- IPTVBoss keeps last 30 days of backups by default
- Older backups automatically deleted
- User can manually save important backups elsewhere

---

## NoGUI Script Locations

### Windows
- Script file: `iptvboss-nogui.bat` or `iptvboss-nogui.ps1`
- User-created, typically on Desktop or Documents

### macOS/Linux
- Script file: `iptvboss-nogui.sh`
- User-created, typically in home directory or `/usr/local/bin/`

### Task Scheduler (Windows)
- Tasks stored in: Task Scheduler Library
- View via: Task Scheduler application

### Cron (Linux/macOS)
- Cron jobs stored in: User's crontab
- View via: `crontab -l` command

---

## Log Files (if applicable)

### Windows
- Logs: `%APPDATA%\IPTVBoss\Logs\`
- Error logs: `iptvboss_error.log`
- General logs: `iptvboss.log`

### macOS
- Logs: `~/Library/Application Support/IPTVBoss/Logs/`

### Linux
- Logs: `~/.config/IPTVBoss/Logs/`

---

## XC Server Files

### Server Configuration
- Stored in database (iptvboss.db)
- No separate config file

### Server Runtime (Windows Service)
- Service executable: Part of IPTVBoss installation
- Service logs: Windows Event Viewer

### Server Runtime (Linux systemd)
- Service file: `/etc/systemd/system/iptvboss-xc.service` (user-created)
- Service logs: `journalctl -u iptvboss-xc`

---

## Docker Container Paths

### Container Internal Paths
- Database: `/config/iptvboss.db`
- Backups: `/config/Backups/`
- Output: `/config/Output/`

### Volume Mounts (user-configured)
- Host path: User-defined
- Common: `/home/user/iptvboss/config/`

---

## Environment Variables

### Custom Installation Paths
Some users may have custom paths via environment variables:
- `IPTVBOSS_DATA`: Custom data directory
- `IPTVBOSS_CONFIG`: Custom config directory

*Note: This is advanced usage and not common*

---

## Important Paths Summary Table

| File Type | Windows | macOS | Linux |
|-----------|---------|-------|-------|
| Database | `%APPDATA%\IPTVBoss\` | `~/Library/Application Support/IPTVBoss/` | `~/.config/IPTVBoss/` |
| Backups | `%APPDATA%\IPTVBoss\Backups\` | `~/Library/Application Support/IPTVBoss/Backups/` | `~/.config/IPTVBoss/Backups/` |
| Output | `%APPDATA%\IPTVBoss\Output\` | `~/Library/Application Support/IPTVBoss/Output/` | `~/.config/IPTVBoss/Output/` |
| Cloud (Dropbox) | `Dropbox/Apps/[AppName]/` | `Dropbox/Apps/[AppName]/` | `Dropbox/Apps/[AppName]/` |
| Cloud (GDrive) | Google Drive app folder | Google Drive app folder | Google Drive app folder |

---

## User Guidance

### Finding Files
When users can't find files, ask:
1. **What platform?** (Windows/Mac/Linux)
2. **What are you looking for?** (Database/Backup/Output/Cloud files)
3. **Is IPTVBoss installed or portable?**

### Common Issues
- **Can't find database**: Look in `%APPDATA%` (Windows) or `~/Library/Application Support` (Mac)
- **Can't find cloud files**: Check Dropbox Apps folder or Google Drive
- **Backups disappeared**: Check retention period (30 days default)

---

**Last Updated**: December 1, 2024
