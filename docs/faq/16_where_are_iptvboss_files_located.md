# Where Are IPTVBoss Files and Folders Located

IPTVBoss folder locations vary by operating system.

### Question

Where are IPTVBoss files and folders located on my system?

### Answer

**IPTVBoss Folder Locations:**

**Windows:**
```
C:\Users\{user}\IPTVBoss
```

**Linux:**
```
/home/{user}/IPTVBoss
```

**Mac:**
```
~/Library/Application Support/IPTVBoss/
```

**Headless Linux (installed on Windows):**
```
/home/{user}/IPTVBoss/C:
```
*Or custom drive letter (e.g., D:) if Windows installation uses custom path*

### Important Subfolders

- `/backup` - Automatic database backups (restore from here if needed)
- `/db` - Database files (do not manually edit)
- `/cache` - EPG cache files
- `/logs` - Log files (helpful for troubleshooting)
- `/output` - Local M3U/XML output files

### Tips

- **Backup folder**: Check here when restoring (Settings → Restore Database)
- **Logs folder**: Share logs when asking for support (remove sensitive info first)
- **Output folder**: Find locally generated M3U/EPG files here (if not using cloud)

### Related Topics

- [Database Backup Portability](24_database_backup_portable_reinstall.md)
[Folder Locations](../folder_locations.md)