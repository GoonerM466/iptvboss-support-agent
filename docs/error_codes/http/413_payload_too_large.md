# 413 Payload Too Large

**Category**: Client Error (4xx)

**What it means**: Request body larger than server's configured limit.

### Common Causes in IPTVBoss

**Huge M3U File Upload to Cloud**:
- M3U with thousands of VOD entries
- Provider with massive channel lists
- Multiple layouts combined

**Large EPG Upload Exceeding Limits**:
- EPG with many days of data
- Multiple EPG sources combined
- Uncompressed XML format

**Cloud Storage API Limits**:
- Single file too large for API call
- Dropbox/Google Drive upload size limits
- Exceeds provider's transfer limit

### How to Fix

**Reduce M3U File Size**:

1. Disable VOD output:
   - Layout settings
   - Exclude VOD categories
   - VOD can be 70-90% of M3U file size
   - Still keep Live TV channels

2. Filter out unused channel groups:
   - Remove groups you don't use
   - Layout Manager → Edit groups
   - Smaller channel list = smaller file

3. Create multiple smaller layouts:
   - Instead of one huge layout
   - Split by category (Sports, Movies, etc.)
   - Each outputs separate, smaller M3U

**Reduce EPG File Size**:

1. Use Universal EPG:
   - Sources → Universal EPG Options
   - One optimized file for all layouts
   - Much more efficient than individual EPGs

2. Reduce "Days to Keep":
   - Set to 7 days instead of ALL
   - Sources → EPG Settings
   - 7 days sufficient for most use cases
   - Dramatically reduces EPG size

3. Use compressed format:
   - EPG.GZ instead of XML
   - 70-80% smaller
   - Most players support compressed format

**For Cloud Upload Limits**:

1. Verify cloud service limits:
   - Dropbox: Check single file upload limit
   - Google Drive: Check upload limits
   - Free vs paid tiers have different limits

2. Split into multiple files:
   - If possible, split layout
   - Create separate outputs
   - Upload smaller chunks

3. Upgrade cloud storage tier:
   - Paid tiers often have higher limits
   - Consider if free tier insufficient

### Prevention

- Use Universal EPG by default - optimized and compressed
- Don't output VOD unless actively used
- Keep "Days to Keep" at 7 days (not ALL)
- Filter channel lists to only what you need
- Monitor file sizes before uploading
- Use compressed formats (.gz instead of .xml)

### File Size Comparison

**Without Optimization**:
- M3U with VOD: 10-15 MB
- EPG XML (ALL days): 8-12 MB each layout
- Total: 18-27 MB per layout
- **May exceed upload limits**

**With Optimization**:
- M3U without VOD: 1-2 MB
- Universal EPG.GZ (7 days): 2-3 MB total
- Total: 3-5 MB per layout
- **80%+ reduction!**

### Workaround

If you must have large files:

1. Host files locally instead of cloud:
   - Use local network file sharing
   - Serve from home server
   - No cloud upload limits

2. Use different cloud provider:
   - Google Drive often more generous than Dropbox
   - Compare upload limits
   - May need paid tier

3. Split users across multiple accounts:
   - Multiple cloud accounts
   - Different layout groups per account
   - Distribute load

### Related Errors

- [408 Request Timeout](408_request_timeout.md) - Large files also cause timeouts
- [403 Forbidden](403_forbidden.md) - Quota exceeded is similar issue
- [429 Too Many Requests](429_too_many_requests.md) - Large frequent uploads trigger rate limits

### See Also

- [Troubleshooting: Cloud Storage Upload Failures](../Troubleshooting_Guide.md#cloud-storage-uploadsync-failures)
- [FAQ: Universal EPG](../FAQ.md#epg-electronic-program-guide)
