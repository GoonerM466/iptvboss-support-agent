# Managing Playlist Sources - Adding

There are 3 ways to add playlist sources:


**Visual Reference**: [image15](https://goonerm466.github.io/iptvboss-support-agent/images/image15.png) - Sources Manager panel showing playlist sources and EPG sources management interface
### M3U URL (Basic)

- Name the playlist (don't use symbols in name)
- Paste M3U URL or browse for local file
- **Important**: If playlist uses username/password in video links:
  - Enable "Source Uses Username/Password"
  - Enter username and password
  - Required if planning multiple users or XC conversion later

### XC API (Recommended)

- Name the playlist
- Add IPTV service username/password
- Add IPTV URL up to port (some providers don't have port)
- Example: `http://myiptvservice.net:1234`

### Custom (Advanced)

- For non-standard sources
- Custom configuration required

### After Adding - Load Categories

- Click "Load Categories"
- Wait for provider categories to load
- Multi-select categories you want to edit if needed (Ctrl+Click)
- Right-click to change the sync status for selected group(s)

---

### Related Topics

- [Previous: Source Manager - Advanced Options Overview](03_source_manager_overview.md)
- [Next: Playlist Source Options](05_playlist_source_options.md)
