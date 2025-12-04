# IPTVBoss Folder Locations Reference

**Purpose**: Quick reference for file and folder locations across different platforms
**For Claude Project**: Use this when users ask "where are my files?" or "where does IPTVBoss store...?"

---

## Platform-Specific Installation Locations

### Windows

**Application Location**:
- Default: `C:\Program Files\WindowsApps\IPTVBoss\` (App version - hidden/restricted access - **users should never need to access this folder**)
- Jar: Wherever user choose (advanced setup)

**Database Location**:
- Full path: `C:\Users\[Username]\IPTVBoss\db`

**Backup Location**:
- Full path: `C:\Users\[Username]\IPTVBoss\backups\`

**Local Output Files**:
- Full path: `C:\Users\[Username]\IPTVBoss\output\`

**Log Files**:
- Logs: `C:\Users\[Username]\IPTVBoss\Logs\`

---

### macOS

**Application Location**:
- `/Applications/IPTVBoss.app`

**Database Location**:
- `~/Library/Application Support/IPTVBoss/iptvboss.db`
- Full path: `/Users/[Username]/Library/Application Support/IPTVBoss/iptvboss.db`

**Backup Location**:
- `~/Library/Application Support/IPTVBoss/backups/`

**Local LOutput Files**:
- `~/Library/Application Support/IPTVBoss/output/`

**Log Files**:
- Logs: `~/Library/Application Support/IPTVBoss/logs/`

---

### Linux

**Application Location**:
- User-defined (extracted from tar.gz)
- Commonly: `/opt/IPTVBoss/` or `~/IPTVBoss/`

**Database Location**:
- `~/.config/IPTVBoss/iptvboss.db`
- Full path: `/home/[username]/.config/IPTVBoss/iptvboss.db`

**Backup Location**:
- `~/.config/IPTVBoss/backups/`

**Local Output Files**:
- `~/.config/IPTVBoss/output/`

**Log Files**:
- Logs: `~/.config/IPTVBoss/logs/`

---

## Cloud Storage Locations

### Dropbox

**App Folder** (recommended):
- Default Path in Dropbox: `Dropbox/Apps/[YourAppName]/`
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

### Retention
- IPTVBoss keeps last 5 days of backups by default
    - This can be changed in IPTVBoss Settings
    - Cloud often stores upto 30 days in "Deleted Items" or "Trash" folders
- Older backups automatically deleted
- User can manually save important backups elsewhere

---

## NoGUI Locations

### Task Scheduler (Windows)
- Tasks stored in: Task Scheduler Library
- View via: Task Scheduler application

### Cron (Linux/macOS)
- Cron jobs stored in: User's crontab
- View via: `crontab -l` command

---

## Log File Types

- General logs: `IPTVBoss-YYYY-MM-DD.log`
- NoGUI Log: `NoGUI-YYYY-MM-DD.log`
- AED Log: `AdvEPGDummy-YYYY-MM-DD.log`

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
- Backups: `/config/backups/`
- Output: `/config/output/`

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
| Database | `C:\Users\[Username]\IPTVBoss\db` | `~/Library/Application Support/IPTVBoss/db` | `~/.config/IPTVBoss/db` |
| Backups | `C:\Users\[Username]\IPTVBoss\backups` | `~/Library/Application Support/IPTVBoss/backups/` | `~/.config/IPTVBoss/backups/` |
| Output | C:\Users\[Username]\IPTVBoss\output` | `~/Library/Application Support/IPTVBoss/output/` | `~/.config/IPTVBoss/output/` |
| Logs | C:\Users\[Username]\IPTVBoss\logs` | `~/Library/Application Support/IPTVBoss/logs/` | `~/.config/IPTVBoss/logs/` |
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
- **Can't find database**: Look in `Users Directory` (Windows) or `~/Library/Application Support` (Mac)
- **Can't find cloud files**: Check Dropbox Apps folder or Google Drive
- **Backups disappeared**: Check retention period (5 days local, 30 days cloud is default)

---

**Last Updated**: December 4, 2025
