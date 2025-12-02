# Troubleshooting Common Issues

### Troubleshooting Common Issues

Quick reference for common problems.

**See detailed solutions in** [Troubleshooting Guide](Troubleshooting_Guide.md).

**Database won't load**:
- Delete lock files from IPTVBoss/db
- Restore from backup

**Changes don't show in player**:
- Did you output from Boss?
- Did you update playlist in player?
- Using correct URL (Boss URL, not provider URL)?

**EPG not showing**:
- Mapped channels to EPG?
- Enabled EPG sources?
- Days to Keep: Check **Sources → Sources Manager** → Highlight EPG → **EPG Settings** (default 3 days, set to 7 or ALL)
- Synced EPG recently? (**Sources → Sync All EPGs**)

**TinyURL not working**:
- API key entered in Settings?
- Delete cloud files and re-output

**Cloud upload fails**:
- Reauthorize cloud storage
- Check internet connection
- Verify cloud storage website accessible

**Source sync breaks layouts**:
- Restore from backup before sync
- Provider changed channel structure

**Pro license won't validate**:
- Using new website credentials?
- Internet connection working?
- Migrated to new IPTVBoss system?


---

## Related Topics

- [Previous: XC Server Troubleshooting and Comparison](36_xc_server_troubleshooting.md)
