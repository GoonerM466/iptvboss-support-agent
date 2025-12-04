# 405 Method Not Allowed

**Category**: Client Error (4xx)

**What it means**: HTTP method used (GET, POST, PUT, DELETE) is not supported for this endpoint.

### Common Causes in IPTVBoss

**API Endpoint Expects Different HTTP Method**:
- TinyURL API expects POST but GET sent
- Cloud storage API expects PUT for upload but POST sent

**Provider API Version Mismatch**:
- Old API endpoint deprecated
- New API uses different methods

**Server Configuration Error**:
- Provider server misconfigured
- Reverse proxy blocking certain methods

### How to Fix

**This error is rare in IPTVBoss** - usually indicates:

1. Boss version outdated:
   - Provider changed API
   - Boss not yet updated for new API
   - **Fix**: Update IPTVBoss to latest version

2. Provider server misconfiguration:
   - Temporary server issue
   - Provider needs to fix on their end
   - **Fix**: Contact provider support

3. Proxy/firewall modifying requests:
   - Corporate proxy interfering
   - Network security appliance changing requests
   - **Fix**: Check network settings, contact IT

**Steps to Diagnose**:

1. Check for IPTVBoss updates:
   - Restart IPTVBoss or download the latest install file
   - Install latest version
   - May fix API compatibility

2. Check Boss logs:
   - Navigate to IPTVBoss/logs folder
   - Look for specific API endpoint having issues
   - Note which service (provider, TinyURL, cloud)

3. Test with different service:
   - If TinyURL error, try direct cloud URLs
   - If provider error, try different provider temporarily
   - Helps isolate which service has problem

4. Contact provider support:
   - Report 405 error
   - May be server misconfiguration
   - Provider can check server logs

5. Post logs in Discord support:
   - If problem persists after update
   - Include Boss version and OS
   - Community may recognize pattern

### Prevention

- Keep IPTVBoss updated - API compatibility fixes
- Monitor provider announcements - API changes often announced
- Test after provider updates - catch issues early

### Related Errors

- [400 Bad Request](400_bad_request.md) - Similar API compatibility issue
- [415 Unsupported Media Type](415_unsupported_media_type.md) - Related to request format

### See Also

- [HTTP Error Overview](http_error_overview.md)
- [Troubleshooting: NoGUI Update Errors](../Troubleshooting_Guide.md#nogui-update-errors-after-version-updates)
