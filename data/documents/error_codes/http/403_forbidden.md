# 403 Forbidden

**Category**: Client Error (4xx)

**What it means**: Server understood request and authenticated you, but refuses to fulfill it - you lack permissions.

### Common Causes in IPTVBoss

**Provider Account Restrictions**:
- Concurrent connection limit exceeded
- IP address not whitelisted by provider
- Account suspended for TOS violation
- Geo-restriction on content or API

**Cloud Storage Permission Issues**:
- App authorization revoked in cloud account settings
- Folder permissions changed
- Storage quota exceeded
- Security policy blocking access

**TinyURL Rate Limits or Restrictions**:
- Too many URLs created too quickly
- Account flagged for abuse
- Free tier limits exceeded

**Provider Firewall or Security Rules**:
- VPN/proxy blocked by provider
- User-agent blocked
- API access disabled by provider

### How to Fix

**For Provider Sources**:

1. Check concurrent connections:
   - Are you running multiple Boss instances?
   - Close other players/apps using same provider account
   - Each connection counts against limit

2. Verify IP whitelist:
   - Check provider panel for IP restrictions
   - Add your current IP if whitelisting required
   - Dynamic IPs need frequent updates

3. Test with VPN disabled:
   - Disable VPN temporarily
   - If error clears, provider blocks VPNs
   - Try different VPN server/location if VPN required

4. Check account status:
   - Log into provider panel
   - Look for suspension notices
   - Verify no TOS violations

5. Contact provider:
   - If all checks pass, account may be restricted
   - Provider can check server-side logs
   - May need to appeal suspension

**For Cloud Storage**:

1. Check app authorization:
   - Dropbox: Settings → Connected Apps
   - Google Drive: Security → Third-party apps
   - Verify IPTVBoss still authorized
   - Reauthorize if removed

2. Verify storage quota:
   - Dropbox free: 2GB storage, 20GB bandwidth/month
   - Google Drive free: 15GB storage
   - Check usage at cloud website
   - Delete old files or upgrade plan

3. Check bandwidth usage (Dropbox):
   - Free tier: 20GB bandwidth per month
   - Resets monthly
   - If exceeded, wait for reset or upgrade
   - Use Universal EPG to reduce bandwidth 80%+

4. Revoke and reauthorize:
   - In cloud service: Revoke Boss access
   - In Boss: Reauthorize cloud storage
   - Grants fresh permissions

5. Check folder permissions:
   - Verify Boss folder has read/write access
   - Check security policies didn't change

**For TinyURL**:

1. Check account status:
   - Log into tinyurl.com
   - Look for notices or restrictions

2. Review API usage:
   - Check usage against tier limits
   - Free tier has rate limits

3. Wait for rate limit reset:
   - If rate limited, wait 15-30 minutes
   - Then retry

4. Generate new API key:
   - If account flagged, create new key
   - Enable all permissions

5. Use direct cloud URLs:
   - Workaround while TinyURL restricted
   - View Cloud Links in Boss
   - Players accept full URLs

**For VPN/Proxy Blocks**:

1. Disable VPN temporarily:
   - Test if error clears
   - Confirms provider blocking VPNs

2. Try different VPN server:
   - Some locations may not be blocked
   - Residential IP VPNs often work better

3. Contact provider about VPN policy:
   - Some providers explicitly block VPNs
   - Others allow specific VPN services

### Prevention

- Monitor concurrent connections - don't share accounts excessively
- Keep IP whitelisted if provider requires it (dynamic IPs problematic)
- Stay within cloud storage quotas:
  - Use Universal EPG (massive bandwidth savings)
  - Disable VOD output if not needed
  - Use compressed EPG format (.gz)
- Respect API rate limits - don't sync too frequently
- Document provider restrictions - know the rules

### Known Limitations

- No way to bypass provider restrictions - they control access
- Cloud storage quotas hard limit on free tiers - must upgrade or reduce usage
- Provider IP whitelists problematic with dynamic IPs - need frequent updates
- 40-50+ users may exceed Dropbox free tier - consider Google Drive or paid plan

### Related Errors

- [401 Unauthorized](401_unauthorized.md) - Similar but specifically authentication, not permission
- [429 Too Many Requests](429_too_many_requests.md) - Rate limiting, closely related
- [413 Payload Too Large](413_payload_too_large.md) - File size quota issue

### See Also

- [Troubleshooting: Cloud Storage Upload Failures](../Troubleshooting_Guide.md#cloud-storage-uploadsync-failures)
- [FAQ: Dropbox Bandwidth Limit](../FAQ.md#tinyurl-and-cloud-setup)
