# Cloud Storage Upload/Sync Failures

Files not uploading to Dropbox or Google Drive despite valid credentials.

### Problem

Files fail to upload to cloud storage services.

### Symptoms

- Dropbox upload fails despite valid credentials
- Google Drive authorization loops repeatedly
- Files not syncing between IPTVBoss instances
- "Bandwidth limit reached" on free Dropbox tier
- Cloud authorization succeeds but uploads fail
- One Boss instance doesn't see other instance's changes

### Why This Happens

OAuth tokens expire periodically. Free Dropbox bandwidth limit (20GB/month) exceeded with many users. Multiple Boss instances causing sync conflicts. File permissions changed after OS update. Firewall blocking cloud services.

### Solution

**Step 1: Reauthorize cloud storage**
- Settings → IPTVBoss Settings (Dropbox or Google Drive)
- Click Authorize
- Complete OAuth flow in browser
- Verify authorization success in IPTVBoss

**Step 2: Clean stale cloud files**
- Go to Dropbox/Google Drive website
- Navigate to IPTVBoss sync folder
- Delete any files with "lock" in name
- These can cause conflicts, better to regenerate fresh

**Step 3: Test upload**
- In IPTVBoss: **Output → Output current M3u & EPG**
- Check View Cloud Links to verify upload
- Verify files appear in cloud storage

### For Bandwidth Limit Issues

**1. Use Universal EPG**
- Sources → Universal EPG Options
- Generates one EPG for all layouts
- Massive bandwidth savings over individual EPGs
- Once enabled, disable layout EPG upload, delete cloud XML & GZ files, update player URLS

**2. Exclude VOD & Series from M3U**
- VOD lists are enormous
- If you don't use VOD, disable it in output
- Also "Igore" both to save time syncing
- Reduces M3U file size by 70-90%

**3. Use .gz format**
- EPG.GZ is compressed format
- Much smaller than XML
- Most players support it

**4. Reduce player sync frequency**
- Don't sync more than 2x daily
- EPG providers update 1-2x daily anyway

**5. Consider Google Drive (requires gz)**
- Often more generous bandwidth limits
- Or upgrade to Dropbox paid tier

### After OS Upgrade

- Reauthorize cloud storage (OS changes break OAuth)
- Check firewall rules (might have reset)
- Reinstall cloud storage desktop app if needed
- Verify IPTVBoss folder permissions

### For Multiple Instances

- Don't run multiple instances simultaneously
- Cloud sync gets confused
- If you must run multiple only 1 machine should have an auto sync shedule

### Prevention

- Use Universal EPG by default
- Monitor bandwidth usage
- Keep cloud storage apps updated
- Backup authorization before OS updates

### Known Limitations

- Free Dropbox insufficient for 40-50+ users
- Multiple instances without coordination cause issues
- OS upgrades reliably break cloud auth

### Escalation

If you cannot resolve the issue contact support on [Discord](https://discord.gg/QCxpA9yvWP)

### Related Topics

- [TinyURL EPG But No M3U](../faq/03_tinyurl_epg_but_no_m3u.md)
- [Windows 11 Files Not Syncing](../faq/35_windows11_files_not_syncing.md)
