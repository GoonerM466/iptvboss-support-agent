# 401 Unauthorized

**Category**: Client Error (4xx)

**What it means**: Authentication required or authentication failed - credentials are missing, incorrect, or expired.

### Common Causes in IPTVBoss

**Provider Credentials Expired or Incorrect**:
- Service subscription expired
- Password changed by provider
- Username/password typo
- M3U URL credentials embedded incorrectly

**TinyURL API Authentication Failure**:
- API key not entered
- API key incorrect or expired
- API key has insufficient permissions
- Still using old anonymous TinyURL (no longer supported)

**Cloud Storage Authorization Expired**:
- OAuth token expired (common after 30-90 days)
- Authorization revoked in cloud service settings
- Account password changed

**XC API Authentication Issues**:
- Username or password incorrect
- Account suspended by provider
- Server requires different auth method

### How to Fix

**For Provider Sources**:

1. Verify subscription is active:
   - Check provider website/panel
   - Confirm payment processed
   - Look for expiration date

2. Test credentials in provider panel:
   - Log into provider's website
   - Try credentials in provider's own player
   - If they work there Boss configuration issue

3. For M3U URLs with embedded credentials:
   - Format: `http://server:port/get.php?username=USER&password=PASS&type=m3u_plus`
   - Verify username and password correctly placed
   - Check for typos/extra spaces

4. For XC API:
   - Sources → Sources Manager
   - Select source
   - Re-enter username and password exactly from provider panel
   - Save and sync

5. Try syncing source:
   - If 401 persists after correct credentials contact provider support

**For TinyURL**:

1. Verify TinyURL account created:
   - New TinyURL API system requires account
   - Old anonymous TinyURL no longer works
   - Create account at tinyurl.com

2. Generate new API key:
   - Log into tinyurl.com
   - Navigate to API settings
   - Generate new API key
   - Enable all permissions

3. Enter in IPTVBoss:
   - Settings → TinyURL
   - Enter API key (copy-paste no spaces)
   - Save

4. Test by re-outputting:
   - Delete old cloud files
   - Output layout again
   - Check if TinyURL generates

**For Cloud Storage**:

1. Reauthorize OAuth:
   - Settings → IPTVBoss Settings
   - Select Dropbox or Google Drive
   - Click Authorize
   - Complete OAuth flow in browser

2. Verify authorization status:
   - Should show "Authorized" in IPTVBoss
   - If not retry authorization

3. Test with manual output:
   - Layout Manager → Output
   - Check if files upload to cloud
   - View Cloud Links to verify

4. If authorization keeps failing:
   - Check cloud account password didn't change
   - Revoke Boss access in cloud settings
   - Reauthorize fresh

**For XC API**:

1. Check provider panel:
   - Verify account shows active
   - Look for suspension notices

2. Test credentials in browser:
   - `http://server:port/player_api.php?username=USER&password=PASS`
   - Should return JSON with account info
   - If 401 in browser credentials definitely wrong

3. Re-enter in IPTVBoss:
   - Type exactly as shown in provider panel
   - Username and password are case-sensitive

4. Remove and re-add source if persists:
   - Create backup first (mappings will be lost)
   - Delete source
   - Add fresh with correct credentials

### Prevention

- Keep subscriptions current - renew before expiration
- Document credential changes immediately
- Backup database before credential changes - prevents mapping loss
- Reauthorize cloud storage monthly - prevents OAuth expiration
- Use XC API instead of M3U with embedded credentials (more stable)
- Test credentials in provider panel before entering in Boss

### Related Errors

- [403 Forbidden](403_forbidden.md) - Similar but permission/quota issue rather than authentication
- [400 Bad Request](400_bad_request.md) - May occur with malformed credentials
- [404 Not Found](404_not_found.md) - May follow 401 if server URL also wrong

### See Also

- [FAQ: TinyURL Authentication](../FAQ.md#im-getting-unauthenticated-or-503-errors-with-tinyurl-whats-wrong)
- [Troubleshooting: TinyURL API Failures](../Troubleshooting_Guide.md#tinyurl-api-authentication-failures)
- [Troubleshooting: License Validation Failures](../Troubleshooting_Guide.md#license-validation-failures-and-loops)
