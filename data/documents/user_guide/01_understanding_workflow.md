# Understanding the IPTVBoss Workflow

### Understanding the IPTVBoss Workflow

IPTVBoss is a **management and organization layer** between your IPTV provider and your player apps. It doesn't stream content - it organizes and enhances playlist files.

**Basic workflow**:
```
Provider → IPTVBoss → Cloud Storage → Player Apps
           ↓
       Organize
       Filter
       Add EPG
```

**Key concept**: IPTVBoss generates static files (M3U playlists and EPG XML files). Your player apps consume these files. When you make changes in Boss, you must output new files and update your player.

**This is NOT real-time**: Think of it like publishing a document. You edit (in Boss), publish (output to cloud), and readers (players) must refresh to see changes.


---

## Related Topics

- [Next: Setting Up Your First Source](02_adding_first_source.md)
