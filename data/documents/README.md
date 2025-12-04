# IPTVBoss/EPGBoss Documentation

User documentation generated from Discord support channel analysis.

---

## What's Here

This documentation was created by analyzing real user support conversations from the IPTVBoss/EPGBoss Discord server. It reflects actual problems users face and solutions that actually work.

### Documentation Files

**[Quick Start Guide](Quick_Start.md)** - 10-15 minute setup guide
- Get IPTVBoss working quickly
- Essential setup only
- Perfect for new users

**[User Guide](User_Guide.md)** - Complete task-oriented guide
- Detailed workflows
- EPG management
- Layout creation
- Automation setup
- Best practices

**[FAQ](FAQ.md)** - Frequently asked questions
- Organized by topic
- Quick answers
- Cross-referenced
- Searchable

**[Troubleshooting Guide](Troubleshooting_Guide.md)** - Problem-solution format
- Organized by severity
- Symptoms → Solution
- Workarounds included
- Most common issues covered

**[Known Issues](Known_Issues.md)** - Unresolved problems
- Current limitations
- Temporary workarounds
- Issues under investigation
- Feature requests

---

## How to Use This Documentation

### If You're New
1. Start with [Quick Start Guide](Quick_Start.md)
2. Get basic setup working
3. Then explore [User Guide](User_Guide.md) for advanced features

### If You Have a Problem
1. Check [FAQ](FAQ.md) first (might have quick answer)
2. Then [Troubleshooting Guide](Troubleshooting_Guide.md) for detailed solutions
3. Check [Known Issues](Known_Issues.md) if no solution found
4. Post in Discord support channel with logs

### If You Want to Learn
1. [User Guide](User_Guide.md) for comprehensive task-oriented instructions
2. [FAQ](FAQ.md) to understand common concepts
3. Discord community for specific questions

---

## Finding Information

### By Problem Type

**Setup/Installation Issues**
- [Quick Start](Quick_Start.md)
- [FAQ: Setting up on new machine](FAQ.md#setting-up-iptvboss-on-new-machine---restore-keeps-removing-boss-token-and-failing-whats-wrong)

**Database/Backup Issues**
- [Troubleshooting: Database Corruption](Troubleshooting_Guide.md#database-corruption-and-failed-startup)
- [FAQ: Database and Backups](FAQ.md#database-and-backups)
- [User Guide: Backing Up](User_Guide.md#backing-up-your-database)

**EPG (Guide) Issues**
- [Troubleshooting: EPG Mapping Loss](Troubleshooting_Guide.md#epg-mapping-loss-or-auto-revert)
- [FAQ: EPG](FAQ.md#epg-electronic-program-guide)
- [User Guide: EPG Management](User_Guide.md#epg-management)

**Sync/Update Issues**
- [Troubleshooting: Source Sync Failures](Troubleshooting_Guide.md#source-sync-failures-and-updates-breaking-layouts)
- [Troubleshooting: EPG Auto-Sync Stopped](Troubleshooting_Guide.md#epg-auto-sync-stopped-working-noguicrontask-scheduler)

**Player Integration Issues**
- [Troubleshooting: Changes Not Reflecting](Troubleshooting_Guide.md#changes-not-reflecting-in-player-apps)
- [FAQ: Output and Player Integration](FAQ.md#output-and-player-integration)

**Cloud/TinyURL Issues**
- [Troubleshooting: TinyURL Failures](Troubleshooting_Guide.md#tinyurl-api-authentication-failures)
- [Troubleshooting: Cloud Storage Failures](Troubleshooting_Guide.md#cloud-storage-uploadsync-failures)
- [FAQ: TinyURL and Cloud Setup](FAQ.md#tinyurl-and-cloud-setup)

### By Task

**Initial Setup**
- [Quick Start Guide](Quick_Start.md)

**Creating Layouts**
- [User Guide: Creating and Managing Layouts](User_Guide.md#creating-and-managing-layouts)

**Mapping EPG**
- [User Guide: Mapping EPG to Channels](User_Guide.md#mapping-epg-to-channels)

**Outputting Playlists**
- [User Guide: Outputting Playlists](User_Guide.md#outputting-playlists-for-players)

**Setting Up Automation**
- [User Guide: Automatic EPG Syncing](User_Guide.md#setting-up-automatic-epg-syncing)

**Recovering from Problems**
- [User Guide: Restoring from Backup](User_Guide.md#restoring-from-backup)
- [User Guide: Handling Provider Changes](User_Guide.md#handling-provider-changes)

---

## Contributing

### Found an Issue?
- Errors in documentation
- Missing information
- Unclear explanations

**Report in Discord** or submit corrections.

### Have a Solution?
If you solved a problem not covered here:
1. Post detailed solution in Discord
2. Include steps that worked for you
3. Tag moderators to add to documentation

### Documentation Updates
This documentation was generated from Discord exports through December 4, 2025. For latest information, always check Discord announcements.

---

## Key Concepts

Understanding these concepts helps with troubleshooting:

**Workflow**: IPTVBoss → Output → Cloud → Player → Update
- Changes don't auto-sync
- Must output, then update player

**Database**: Contains all your work
- Backup regularly
- Restore when things go wrong
- Lock files can block access

**Sources vs Layouts**:
- Sources: Provider connections
- Layouts: Your custom channel organizations

**M3U vs XC**:
- M3U: URL-based, less stable
- XC API: More stable, handles changes better

**Universal EPG**:
- One EPG for all layouts
- More efficient than individual EPGs
- Recommended approach

**NoGUI**:
- Command-line mode for automation
- Used for scheduled syncs

---

## Platform-Specific Notes

### Windows
- Task Scheduler for automation
- Check Task Manager for running instances
- Lock files in `IPTVBoss/db` folder

### Mac
- Launchd or cron for automation
- Full Disk Access permission required
- Activity Monitor for running instances

### Linux
- Cron for automation
- File permissions critical for nogui
- Absolute paths in cron entries

---

## Getting Support

### Before Asking for Help

1. **Search this documentation** (Ctrl+F in each file)
2. **Check Discord history** (problem likely discussed before)
3. **Try obvious fixes** (restart, reauthorize, restore from backup)
4. **Gather information**:
   - What you were trying to do
   - What you expected to happen
   - What actually happened
   - Error messages (exact text)
   - Logs from IPTVBoss/logs folder

### When Posting for Help

**Include**:
- Boss version
- Operating system
- Clear problem description
- Steps to reproduce
- What you've already tried
- Logs (cleaned of sensitive info!)

**Don't include in logs**:
- Provider names or URLs
- Usernames or passwords
- Personal information
- License keys
- API keys

**Clean logs before posting** - search for and remove sensitive information.

---

## Version Information

**Documentation Generated**: December 4, 2025
**Based On**: Discord support threads through December 4, 2025
**IPTVBoss Versions Covered**: 3.9.x series
**Last Updated**: 2025-12-04

---

## License & Disclaimer

This documentation is community-maintained and not officially endorsed by IPTVBoss developers. Information is provided as-is based on community experience.

**Always backup your data before following troubleshooting steps.**

---

## Quick Links

- [**Discord Support Channel**](https://discord.gg/QCxpA9yvWP): Primary support venue
- [**IPTVBoss Website**](https://members.bosstees.net): Official site, downloads, license management
- [**YouTube Tutorials**](https://www.youtube.com/@IPTVBoss-wt9fe): Visual guides for setup and features

---

**Need help right now?** Start with [Troubleshooting Guide](Troubleshooting_Guide.md) or post in Discord support channel.
