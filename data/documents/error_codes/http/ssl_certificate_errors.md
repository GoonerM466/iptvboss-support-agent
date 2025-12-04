# SSL/TLS Certificate Errors

**Category**: Connection Error (Non-HTTP)

**What it means**: SSL certificate validation failed - certificate expired, self-signed, or hostname mismatch.

### Common Causes in IPTVBoss

**Provider Using Self-Signed Certificate**:
- Common with smaller providers
- Certificate not from trusted authority
- Browser/Boss won't trust by default

**Provider Certificate Expired**:
- Provider forgot to renew
- Let's Encrypt cert expired (90 day cycle)
- Common oversight

**Certificate Hostname Mismatch**:
- Certificate for different domain
- Provider infrastructure misconfiguration
- Using IP address instead of hostname

**Man-in-the-Middle Interference**:
- Corporate proxy injecting certificates
- Antivirus SSL scanning
- Network security appliance

### How to Fix

**For Provider Certificate Issues**:

1. Try HTTP instead of HTTPS:
   - If provider supports it
   - Change `https://` to `http://`
   - Bypasses certificate issues
   - Less secure but may work

2. Contact provider:
   - Report certificate problem
   - Provider needs to renew/fix certificate
   - Usually fixed quickly once notified

3. Check if certificate just expired:
   - Test URL in browser
   - Browser shows certificate details
   - If just expired, provider likely fixing

4. Verify correct server address:
   - Ensure connecting to correct hostname
   - Certificate must match hostname exactly
   - Using IP may cause mismatch

**For Local Interference**:

1. Disable antivirus SSL scanning:
   - Temporarily disable SSL inspection
   - If works, add Boss to exceptions
   - Re-enable after testing

2. Corporate network:
   - IT may need to whitelist provider
   - Corporate proxy may interfere
   - Contact IT department

3. Check proxy settings:
   - Verify no unwanted proxy configured
   - Windows: Internet Options → Connections → LAN Settings
   - Mac: System Preferences → Network → Advanced → Proxies

### Security Notes

**Do NOT Blindly Ignore Certificate Errors**:

**Why certificates matter**:
- Prevent man-in-the-middle attacks
- Verify you're connecting to legitimate server
- Encrypt connection

**When to ignore** (carefully):
- Known provider with temporary certificate issue
- Provider you trust with self-signed cert
- Testing in isolated environment

**When NOT to ignore**:
- Unknown provider
- Unexpected certificate warning
- Public network (café, airport)

**Best Practice**:

1. Contact provider to fix properly:
   - Provider should maintain valid certificates
   - Free options like Let's Encrypt available

2. Use HTTP if provider allows:
   - Only if HTTPS problematic
   - Only with trusted provider

3. Document exception:
   - Note why ignoring certificate error
   - Set reminder to recheck

### Prevention

- Providers should maintain valid certificates - industry standard
- Use HTTP if HTTPS problematic - and provider allows
- Document certificate exceptions - know why ignoring errors
- Monitor certificate expiration - if provider shares details
- Have backup provider - with proper certificates

### Testing Certificate

**Check Certificate in Browser**:

1. Open provider URL in browser
2. Click lock icon in address bar
3. View certificate details
4. Check:
   - Expiration date
   - Issued to (should match domain)
   - Issued by (trusted authority?)

**Certificate Warnings to Watch For**:

- **Expired**: Past expiration date
- **Self-signed**: Not from trusted authority
- **Hostname mismatch**: Cert for different domain
- **Revoked**: Certificate invalidated

### Related Errors

- [Connection Refused](connection_refused.md) - May follow if also blocking connection
- [400 Bad Request](400_bad_request.md) - May occur with certificate issues

### See Also

- [FAQ: Source Management](../FAQ.md#source-management)
- [Troubleshooting: Source Sync Failures](../Troubleshooting_Guide.md#source-sync-failures-and-updates-breaking-layouts)
- [HTTP Error Overview](http_error_overview.md)
