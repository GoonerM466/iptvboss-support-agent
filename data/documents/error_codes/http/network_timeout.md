# Network Timeout

**Category**: Connection Error (Non-HTTP)

**What it means**: Connection attempt or data transfer took too long without response.

### Common Causes in IPTVBoss

**Slow Internet Connection**:
- Upload/download speeds too slow
- Bandwidth saturated by other devices
- Poor Wi-Fi signal

**Provider Server Slow to Respond**:
- Server overloaded
- Large datasets processing slowly
- High latency to provider

**Large File Transfers Timing Out**:
- Huge M3U files
- Large EPG files
- Multiple simultaneous uploads

**Network Path Issues**:
- High latency to provider
- Packet loss
- Routing problems
- ISP issues

### How to Fix

**For Slow Connections**:

1. Check internet speed:
   - Run speed test at speedtest.net
   - Verify both upload and download speeds
   - Minimum: 5 Mbps download, 1 Mbps upload recommended

2. Close bandwidth-heavy apps:
   - Stop streaming (Netflix, YouTube)
   - Pause downloads/torrents
   - Close online games
   - Check all devices on network

3. Use wired connection:
   - Ethernet more reliable than Wi-Fi
   - Especially for Boss server
   - Reduces timeouts significantly

4. Check Wi-Fi signal:
   - Move closer to router if using Wi-Fi
   - Check for interference
   - Consider Wi-Fi extender

**For Provider Slowness**:

1. Try during off-peak hours:
   - Early morning often better
   - Fewer users = faster response
   - Late night also good

2. Enable "Ignore Series":
   - Sources → Source Settings
   - Skips VOD series data
   - Dramatically reduces processing time

3. Sync fewer sources at once:
   - Don't sync all simultaneously
   - Prioritize critical sources
   - Let each complete before next

4. Contact provider:
   - If persistent timeout issues
   - May be server capacity problem
   - Provider can check server performance

**For File Transfer Timeouts**:

1. Reduce file sizes:

   **Use Universal EPG**:
   - Sources → Universal EPG Options
   - One optimized file instead of many
   - 80% smaller total size

   **Disable VOD output**:
   - Layout settings
   - VOD makes M3U files huge
   - Only include if needed

   **Use compressed format**:
   - EPG.GZ instead of XML
   - 70-80% smaller
   - Most players support

2. Upload one layout at a time:
   - Don't output all simultaneously
   - Let each complete
   - Reduces network load

3. Increase timeout if available:
   - Check Boss settings
   - May be under advanced options

**For Network Path Issues**:

1. Test latency:
   - `ping provider-server`
   - Check average response time
   - <100ms good, >300ms problematic

2. Check packet loss:
   - Continuous ping test
   - `ping -t provider-server` (Windows)
   - Any packet loss is bad

3. Try VPN:
   - If routing problems
   - VPN may route differently
   - Better path may exist

4. Contact ISP:
   - If persistent issues
   - ISP can check routing
   - May have regional issues

### Prevention

- Optimize file sizes:
  - Universal EPG (80% size reduction)
  - No VOD if not needed
  - Compressed format (.gz)
  - "Days to Keep" at 7 (not ALL)

- Use wired connection - more reliable than Wi-Fi

- Schedule syncs during off-peak - faster provider response

- Monitor network quality:
  - Periodic speed tests
  - Check for packet loss
  - ISP performance

- Keep bandwidth available:
  - Close heavy apps during syncs
  - Quality of Service (QoS) settings on router

### File Size Optimization

**Before Optimization**:
- Multiple EPG files: 5-10 MB each
- M3U with VOD: 5-15 MB
- Total: 10-25 MB per layout
- **Slow upload, frequent timeouts**

**After Optimization**:
- Universal EPG.GZ: 2-3 MB total
- M3U without VOD: 1-2 MB
- Total: 3-5 MB per layout
- **80% faster, rare timeouts**

### Network Quality Testing

**Speed Test**:
- speedtest.net
- Check upload and download
- Minimum: 5 Mbps down, 1 Mbps up

**Latency Test**:
```
ping provider-server
```
- <100ms: Good
- 100-300ms: Acceptable
- >300ms: Problematic

**Packet Loss Test**:
```
ping -t provider-server
```
- 0% loss: Perfect
- <1% loss: Acceptable
- >1% loss: Problem

### Related Errors

- [408 Request Timeout](408_request_timeout.md) - HTTP-level timeout
- [504 Gateway Timeout](504_gateway_timeout.md) - Server-side timeout
- [Connection Reset](connection_reset.md) - Connection drops during transfer

### See Also

- [Troubleshooting: Cloud Storage Upload Failures](../Troubleshooting_Guide.md#cloud-storage-uploadsync-failures)
- [FAQ: EPG Sync Issues](../FAQ.md#epg-electronic-program-guide)
- [HTTP Error Overview](http_error_overview.md)
