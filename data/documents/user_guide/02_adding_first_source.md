# Setting Up Your First Source

Sources are your IPTV provider connections.

**Prerequisites**:
- IPTV service subscription
- Either M3U URL or XC API credentials from your provider

### Steps

**Get credentials from your provider**:
- M3U URL method: You'll have a URL, possibly with username/password
- XC API method: You'll have server URL, username, password

**Add source in IPTVBoss**:
- Sources → Sources Manager
- Choose connection type (M3U URL or XC API)

**For M3U URL**:
- Paste URL
- Enter username/password if required
- Click Load
- Wait for import (may take 1-5 minutes for large playlists)

**For XC API** (recommended):
- Enter server URL (e.g., `http://example.com:8080`)
- Enter username
- Enter password
- Click Load
- Wait for import

**Verify import**:
- Check channels list
- Verify categories loaded
- Note channel count

### XC vs M3U

XC API is more stable. It handles credential changes better and preserves mappings. Use XC if your provider offers it.

### Troubleshooting

- "Could not load categories": Verify credentials, check service is active
- Very slow import: Large playlist (5000+ channels), be patient
- Import fails midway: Check internet connection, try again

---

### Related Topics

- [Previous: Understanding the IPTVBoss Workflow](01_understanding_workflow.md)
- [Next: Source Manager - Advanced Options Overview](03_source_manager_overview.md)
