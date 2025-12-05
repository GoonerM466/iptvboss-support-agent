# Solution: Cloud Upload Failures

**Flow ID**: cloud_storage
**Type**: diagnostic_solution
**Confidence**: medium
**Solution Steps**: 4

### Context

Files not uploading to cloud or uploads failing silently. Authentication is valid but uploads don't complete.

### Solution Steps

### 1. Check Internet Connection

1. Open browser
2. Visit cloud provider website (dropbox.com or drive.google.com)
3. Verify you can access files
4. Test upload a file manually in browser

**If internet issues**: Fix connection, try Boss output again

### 2. Check Cloud Storage Space

**Dropbox**:
- Free: 2GB limit
- Plus: 2TB+ (paid)
- Check usage at dropbox.com

**Google Drive**:
- Free: 15GB limit (shared with Gmail/Photos)
- Check usage at drive.google.com/settings/storage

**If storage full**:
- Delete old files
- Upgrade plan
- Switch to different cloud provider

### 3. Verify Folder Permissions

1. Go to cloud provider website
2. Navigate to IPTVBoss folder
3. Check folder isn't read-only
4. Verify Boss has write permissions
5. Check folder isn't shared with restrictions

### 4. Check Firewall/Antivirus

**Windows**:
- Windows Firewall may block Boss
- Antivirus may quarantine files
- Add Boss to whitelist/exceptions

**Mac**:
- System Preferences → Security & Privacy
- Grant Boss "Full Disk Access"

**Network**:
- Corporate firewalls may block cloud access
- VPN may interfere
- Try from different network (mobile hotspot)

### Check Logs

1. Boss folder → logs
2. Search for: "upload", "cloud", "failed"
3. Note error codes:
   - 403 → Permission denied
   - 429 → Rate limited (too many requests)
   - 500s → Provider server issues

### Still Failing?

Try alternative cloud or local output:
- Switch to different cloud provider
- Use local network folder
- See [Cloud Storage Setup](../../../user_guide/04_cloud_storage_setup.md)

### Related Topics

- [Cloud Storage Upload Failures](../../07_cloud_storage_upload_failures.md)
- [Reauthorize Cloud](01_solution_reauth.md)
- [Cloud Storage Setup](../../../user_guide/04_cloud_storage_setup.md)
