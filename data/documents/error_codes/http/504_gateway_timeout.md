# 504 Gateway Timeout

**Category**: Server Error (5xx)

**What it means**: Server acting as gateway didn't receive timely response from upstream server.

### Common Causes in IPTVBoss

**Provider Backend Servers Slow/Unresponsive**:
- Database queries timing out
- Server overloaded with requests
- Processing taking too long

**Large File Processing Timeout**:
- Generating huge M3U taking too long
- EPG processing exceeding timeout
- VOD list generation slow

**Cloud Storage Upload Timeout**:
- Large files taking too long to upload
- Network issues between services
- API processing slow

### How to Fix

**For Provider Timeouts**:

1. Try during off-peak hours:
   - Early morning often better
   - Fewer users = faster response
   - Provider servers less loaded

2. Enable "Ignore Series":
   - Sources → Source Settings
   - Skips VOD series data
   - Dramatically reduces processing time

3. Sync fewer items at once:
   - Don't sync all sources simultaneously
   - Sync critical sources first
   - Let each complete before next

4. Contact provider if persistent:
   - Report consistent timeout issues
   - May be server capacity problem
   - Provider can check server performance

**For Cloud Uploads**:

1. Reduce file sizes:
   - **Use Universal EPG**:
     - Sources → Universal EPG Options
     - Faster processing and upload
   - **Disable VOD output** if not needed:
     - Layout settings
     - VOD makes files huge
   - **Use compressed format**:
     - EPG.GZ instead of XML
     - Much smaller and faster

2. Upload during stable connection:
   - Use wired connection instead of Wi-Fi
   - Close bandwidth-heavy apps
   - Check internet speed

3. Upload one layout at a time:
   - Don't output all layouts simultaneously
   - Let each complete
   - Reduces server load

**For EPG Syncs**:

1. Sync fewer EPG sources:
   - Don't sync all at once
   - Prioritize important sources
   - Spread out over time

2. Check EPG source responsiveness:
   - Some EPG providers slower than others
   - Consider switching to faster source
   - Test EPG URL response time in browser

### Prevention

- Use Universal EPG - faster processing, smaller files
- Disable VOD if not using it - huge processing savings
- Sync during off-peak hours - faster provider response
- Use compressed EPG format (.gz) - faster upload
- Don't sync too frequently - reduces exposure to timeout issues
- Use wired connection for Boss server - more stable than Wi-Fi

### File Size Optimization

Reducing file sizes helps prevent timeouts:

**Before**:
- Multiple EPG files: 5-10 MB each
- M3U with VOD: 5-15 MB
- Total: 10-25 MB per layout
- **Slow processing and upload**

**After**:
- Universal EPG.GZ: 2-3 MB total
- M3U without VOD: 1-2 MB
- Total: 3-5 MB per layout
- **80% faster!**

### Related Errors

- [408 Request Timeout](408_request_timeout.md) - Similar but client-side timeout
- [503 Service Unavailable](503_service_unavailable.md) - May transition to 503 if overloaded
- [502 Bad Gateway](502_bad_gateway.md) - Gateway failure rather than timeout

### See Also

- [Troubleshooting: Cloud Storage Upload Failures](../Troubleshooting_Guide.md#cloud-storage-uploadsync-failures)
- [FAQ: EPG Sync Issues](../FAQ.md#epg-electronic-program-guide)
- [HTTP Error Overview](http_error_overview.md)
