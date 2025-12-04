# TinyURL EPG Links Show But M3U Link Missing

The M3U file failed to upload while the EPG succeeded.

### Problem

TinyURL EPG links appear in cloud view, but the M3U link is missing.

### Solution

1. Verify both **Dropbox/Google Drive AND TinyURL API credentials** are configured
2. Check IPTVBoss logs for upload errors
3. Delete existing cloud files from your cloud storage website (will force generation of new links)
4. Re-output your layout's playlist (.m3u) and EPG
5. Check your cloud storage to confirm **both files uploaded** before checking TinyURL links

### Related Topics

- [TinyURL Links Not Generating](01_tinyurl_not_generating.md)
- [Cloud Storage Upload Failures](../troubleshooting/07_cloud_storage_upload_failures.md)
