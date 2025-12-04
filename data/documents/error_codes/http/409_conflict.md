# 409 Conflict

**Category**: Client Error (4xx)

**What it means**: Request conflicts with current state of the server - often occurs with simultaneous updates.

### Common Causes in IPTVBoss

**Cloud Storage Sync Conflict**:
- Multiple Boss instances uploading simultaneously
- File being modified while another update in progress
- Lock file conflict

**Simultaneous Updates to Same File**:
- Two Boss instances outputting same layout
- Manual file edit while Boss uploading

### How to Fix

**For Cloud Storage Conflicts**:

1. Close all Boss instances except one:
   - Check Task Manager (Windows) or Activity Monitor (Mac)
   - Find all IPTVBoss processes
   - Close all but one

2. Delete lock files from cloud storage:
   - Log into Dropbox/Google Drive website
   - Navigate to IPTVBoss sync folder
   - Delete these files:
     - `lockfile.json`
     - Any files with "lock" in name
   - These prevent conflicts but can get stuck

3. Re-output from single Boss instance:
   - Layout Manager → Output Current Layout
   - Let complete without interference
   - Verify upload successful

4. For multi-instance setups:
   - Disable cloud sync on all but one "primary" instance
   - Let primary handle all cloud uploads
   - Secondary instances use local files only

**For Persistent Conflicts**:

1. Delete all cloud files:
   - In cloud storage, delete entire Boss folder
   - Or just delete M3U and EPG files
   - Forces clean state

2. Reauthorize cloud storage:
   - Settings → IPTVBoss Settings
   - Revoke access in cloud service
   - Reauthorize in Boss
   - Fresh OAuth token

3. Re-output fresh:
   - With clean slate, output layout
   - Should upload without conflict
   - Monitor for errors

### Prevention

- Don't run multiple Boss instances simultaneously - primary cause
- If multi-instance required:
  - Disable cloud sync on secondary instances
  - Use one "primary" instance for cloud uploads only
- Let cloud uploads complete - don't start new output while upload in progress
- Monitor upload status - wait for completion before closing Boss

### Multi-Instance Best Practices

If you need multiple Boss instances (multiple users/locations):

1. Designate one primary instance:
   - Only this instance has cloud sync enabled
   - Handles all cloud uploads

2. Secondary instances:
   - Disable cloud sync in settings
   - Use local files only
   - Or sync from primary's cloud uploads (read-only)

3. Coordinate timing:
   - Don't output from multiple instances at once
   - Schedule outputs to avoid overlap

4. Use separate cloud folders:
   - If must have multiple instances uploading
   - Configure each to use different folder
   - Prevents conflicts entirely

### Related Errors

- [403 Forbidden](403_forbidden.md) - May follow 409 if permissions also affected
- [429 Too Many Requests](429_too_many_requests.md) - Multiple instances also cause rate limiting

### See Also

- [Troubleshooting: Cloud Storage Upload Failures](../Troubleshooting_Guide.md#cloud-storage-uploadsync-failures)
- [FAQ: Database Corruption](../FAQ.md#database-and-backups)
