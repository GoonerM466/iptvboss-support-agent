# 502 Bad Gateway

**Category**: Server Error (5xx)

**What it means**: Server acting as gateway/proxy received invalid response from upstream server.

### Common Causes in IPTVBoss

**Provider's Load Balancer Issues**:
- Provider's reverse proxy can't reach backend servers
- Backend servers offline or crashed

**Cloud Storage CDN Issues**:
- Content delivery network routing problems
- Regional CDN node down

**Provider Server Overload**:
- Backend servers overwhelmed
- Database servers unreachable
- Infrastructure failure

### How to Fix

**This is provider/service infrastructure issue** - limited control:

**Wait and Retry**:

1. Usually temporary:
   - Infrastructure problems often resolve quickly
   - Wait 15-30 minutes
   - Don't repeatedly retry immediately

2. Try during off-peak hours:
   - Early morning often better
   - Fewer users = less infrastructure load
   - Provider may be working on fix during day

**Check for Outages**:

1. Provider announcements:
   - Check provider Discord/forums
   - Look for maintenance notices
   - See if other users reporting same issue

2. Status pages:
   - Dropbox: status.dropbox.com
   - Google Drive: google.com/appsstatus
   - Some providers have status pages

3. Multiple users affected = infrastructure:
   - Not your configuration
   - Provider needs to fix
   - Just wait

**Try Different Endpoint**:

**If provider has multiple servers**:
- Some providers offer backup servers
- Try alternative server URL if provided
- Check provider panel for options

**For cloud storage**:
- Try different cloud provider temporarily
- Dropbox error → try Google Drive
- Redundancy helps during outages

### Prevention

- Have backup provider configured and ready
- Configure multiple cloud storage options (both Dropbox and Google Drive)
- Monitor provider announcements - maintenance windows
- Don't panic - infrastructure issues usually resolve quickly

### Related Errors

- [500 Internal Server Error](500_internal_server_error.md) - Similar server problem
- [503 Service Unavailable](503_service_unavailable.md) - Often related to overload
- [504 Gateway Timeout](504_gateway_timeout.md) - Gateway slow rather than failing

### See Also

- [HTTP Error Overview](http_error_overview.md)
- [Troubleshooting: Source Sync Failures](../Troubleshooting_Guide.md#source-sync-failures-and-updates-breaking-layouts)
