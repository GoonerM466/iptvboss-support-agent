# 408 Request Timeout

**Category**: Client Error (4xx)

**What it means**: Server didn't receive complete request within timeout period.

### Common Causes in IPTVBoss

**Slow Internet Connection**:
- Upload to cloud storage timing out
- Large M3U/EPG file downloads timing out

**Server Overloaded**:
- Provider server slow to respond
- Cloud storage API slow

**Large File Transfers**:
- Huge M3U files (with VOD)
- Large EPG XML files
- Multiple layouts uploading simultaneously

### How to Fix

**For Provider Sources**:

1. Check internet speed:
   - Run speed test (speedtest.net)
   - Verify both upload and download speeds
   - Minimum: 5 Mbps download recommended

2. Try during off-peak hours:
   - Sync at night or early morning
   - Fewer users = faster provider response
   - Less network congestion

3. Reduce file size:
   - For M3U: Enable "Ignore Series"
   - Sources → Source Settings
   - This skips VOD series data
   - Much faster sync

4. Contact provider:
   - If timeout persists with good connection
   - May be server issue on their end
   - Provider can check server performance

**For Cloud Uploads**:

1. Reduce file sizes:
   - **Use Universal EPG** (one file instead of many):
     - Sources → Universal EPG Options
     - Dramatically reduces upload time
   - **Disable VOD output** if not needed:
     - Layout settings
     - VOD makes M3U files huge
   - **Use EPG.GZ format** (compressed):
     - Much smaller than XML
     - Most players support it

2. Upload during good connection:
   - Check other devices aren't saturating bandwidth
   - Close streaming apps, downloads
   - Use wired connection instead of Wi-Fi

3. Upload one layout at a time:
   - Don't output all layouts simultaneously
   - Let each complete before starting next

**For EPG Syncs**:

1. Sync fewer EPG sources at once:
   - Sync All EPGs can timeout
   - Sync critical EPGs first
   - Let complete before syncing others

2. Increase timeout if available:
   - Check Boss settings for timeout options
   - May be under advanced settings

3. Use more reliable EPG sources:
   - Some EPG providers faster than others
   - Switch to faster source if available

### Prevention

- Use Universal EPG - dramatically reduces upload size/time
- Disable VOD categories if not using them
- Use compressed EPG format (.gz instead of .xml)
- Sync during off-peak hours - faster provider response
- Use wired connection for Boss server - more reliable than Wi-Fi
- Keep "Days to Keep" at 7 days (not ALL) - smaller EPG files

### File Size Optimization

**Before Optimization**:
- Multiple EPG files per layout: 5-10 MB each
- M3U with VOD: 5-15 MB
- Total: 10-25 MB per layout
- 40 users × 25 MB = 1 GB bandwidth per output

**After Optimization**:
- Universal EPG (compressed): 2-3 MB total
- M3U without VOD: 1-2 MB
- Total: 3-5 MB per layout
- 40 users × 5 MB = 200 MB bandwidth per output
- **80% reduction!**

### Related Errors

- [504 Gateway Timeout](504_gateway_timeout.md) - Similar but server-side timeout
- [413 Payload Too Large](413_payload_too_large.md) - File size exceeds limit
- [Network Timeout](network_timeout.md) - Connection-level timeout

### See Also

- [Troubleshooting: Cloud Storage Upload Failures](../Troubleshooting_Guide.md#cloud-storage-uploadsync-failures)
- [FAQ: Cloud Storage Bandwidth](../FAQ.md#tinyurl-and-cloud-setup)
