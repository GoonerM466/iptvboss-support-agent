# All Playlists Disappeared and Lost Pro License

Your backups should still exist - restore database and re-enter license.

### Problem

All your playlists disappeared and you lost your Pro license.

### Solution

**Don't panic - your backups should still exist.**

**Recovery steps:**

1. Re-enter your Pro license key: **Settings → IPTVBoss Pro Settings**
2. Restore database: **Settings → Restore Database → Local, Cloud or URL**
    - Cloud restore requires cloud setup to be completed first
    - URL restore must point to a direct download file
    - With Dropbox make sure the end of the URL is `&dl=1` for direct download
3. Select the most recent backup that predates the problem
4. If you've migrated to the new IPTVBoss website, make sure you're using new credentials

**If restore doesn't work:**

- Try multiple backup files (the newest might be corrupted too)
- Check that `IPTVBoss/backup` folder exists and contains .backup files
- Verify disk isn't full
- Check logs for specific error messages
- Contact support on [Discord](https://discord.gg/QCxpA9yvWP) with clean logs

### Related Topics

- [Database Failed to Load](18_database_failed_to_load_corrupt.md)
- [Keeps Asking to Reauthorize Boss Pro](20_keeps_asking_reauthorize_pro.md)
