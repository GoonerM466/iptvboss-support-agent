# 415 Unsupported Media Type

**Category**: Client Error (4xx)

**What it means**: Server refuses request because payload format is unsupported.

### Common Causes in IPTVBoss

**Wrong Content-Type Header in API Request**:
- TinyURL API expecting JSON but received form data
- Cloud API expecting specific format

**File Format Not Supported**:
- Trying to upload unsupported file type
- API expects different encoding

### How to Fix

**This error is very rare in IPTVBoss** - indicates:

1. Boss version outdated:
   - API compatibility issue
   - Provider changed API format
   - **Fix**: Update IPTVBoss to latest version

2. Corrupted configuration:
   - Settings file corrupted
   - API format settings wrong
   - **Fix**: Reset cloud storage configuration

**Steps to Diagnose**:

1. Update IPTVBoss:
   - Restart IPTVBoss or download the latest install file
   - Install latest version
   - Restart Boss

2. Check Boss logs:
   - Navigate to IPTVBoss/logs folder
   - Look for specific API endpoint having issues
   - Note which service (TinyURL, cloud, provider)

3. Reset cloud storage configuration:
   - Settings → Cloud Storage
   - Revoke access in cloud service
   - Reauthorize in Boss
   - Tests with fresh configuration

4. Try different service temporarily:
   - If TinyURL error, use direct cloud URLs
   - If Dropbox error, try Google Drive
   - Helps isolate issue

5. Contact support with logs:
   - Post in Discord support channel
   - Include Boss version and OS
   - Attach relevant log files (cleaned of sensitive info)

### Prevention

- Keep IPTVBoss updated - API compatibility fixes
- Don't manually edit configuration files - use Boss settings GUI
- Monitor provider announcements - API changes often announced

### Related Errors

- [400 Bad Request](400_bad_request.md) - Similar API format issue
- [405 Method Not Allowed](405_method_not_allowed.md) - Related to API compatibility

### See Also

- [HTTP Error Overview](http_error_overview.md)
- [Troubleshooting: NoGUI Update Errors](../Troubleshooting_Guide.md#nogui-update-errors-after-version-updates)
