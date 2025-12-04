# HTTP Error Code Overview

Quick reference guide for HTTP errors encountered in IPTVBoss when connecting to providers, XC servers, TinyURL, Dropbox, and Google Drive.

### How to Use This Guide

1. **Find your error code** in the tables below
2. **Click the link** to open the detailed troubleshooting guide for that error
3. **Follow the fix steps** specific to IPTVBoss

Each error code has its own detailed page with:
- What the error means in plain language
- Common causes in IPTVBoss
- Step-by-step fixes
- Prevention tips
- Related errors

### Error Code Quick Reference - Client Errors (4xx)

Problems with your request - credentials, URLs, permissions, rate limits

| Code | Name | Common Cause | Detailed Guide |
|------|------|--------------|----------------|
| 400 | Bad Request | Malformed URL/parameters | [400_bad_request.md](400_bad_request.md) |
| 401 | Unauthorized | Wrong/expired credentials | [401_unauthorized.md](401_unauthorized.md) |
| 403 | Forbidden | Permission denied, quota exceeded | [403_forbidden.md](403_forbidden.md) |
| 404 | Not Found | Wrong URL or file deleted | [404_not_found.md](404_not_found.md) |
| 405 | Method Not Allowed | API method mismatch | [405_method_not_allowed.md](405_method_not_allowed.md) |
| 408 | Request Timeout | Transfer too slow | [408_request_timeout.md](408_request_timeout.md) |
| 409 | Conflict | Simultaneous updates | [409_conflict.md](409_conflict.md) |
| 410 | Gone | Resource permanently deleted | [410_gone.md](410_gone.md) |
| 413 | Payload Too Large | File exceeds size limit | [413_payload_too_large.md](413_payload_too_large.md) |
| 415 | Unsupported Media Type | Wrong content format | [415_unsupported_media_type.md](415_unsupported_media_type.md) |
| 429 | Too Many Requests | Rate limited | [429_too_many_requests.md](429_too_many_requests.md) |

### Error Code Quick Reference - Server Errors (5xx)

Problems on provider/service side - limited control, usually need to wait

| Code | Name | Common Cause | Detailed Guide |
|------|------|--------------|----------------|
| 500 | Internal Server Error | Provider server crash/error | [500_internal_server_error.md](500_internal_server_error.md) |
| 502 | Bad Gateway | Provider infrastructure issue | [502_bad_gateway.md](502_bad_gateway.md) |
| 503 | Service Unavailable | Maintenance or overload | [503_service_unavailable.md](503_service_unavailable.md) |
| 504 | Gateway Timeout | Provider server too slow | [504_gateway_timeout.md](504_gateway_timeout.md) |

### Error Code Quick Reference - Connection Errors

Network-level problems before HTTP communication even starts

| Error | Common Cause | Detailed Guide |
|-------|--------------|----------------|
| Connection Refused | Wrong port or firewall | [connection_refused.md](connection_refused.md) |
| Connection Reset | Server dropped connection | [connection_reset.md](connection_reset.md) |
| DNS Resolution Failed | Can't resolve hostname | [dns_resolution_failed.md](dns_resolution_failed.md) |
| SSL/TLS Certificate Error | Invalid/expired certificate | [ssl_certificate_errors.md](ssl_certificate_errors.md) |
| Network Timeout | Connection too slow | [network_timeout.md](network_timeout.md) |

### Quick Diagnostic Flowchart

**I'm getting a 4xx error** - Problem with your request. Check credentials and API keys. Verify URLs are correct. Check quotas and rate limits. Review permissions.

**I'm getting a 5xx error** - Provider/service problem. Wait 15-30 minutes and retry. Check service status pages. Try during off-peak hours. Contact provider if persistent.

**Connection failed before getting error code** - Network connectivity issue. Check internet connection. Verify server address and port. Test in browser. Check firewall settings.

### Most Common Errors by Service

**Provider/XC Server Errors**:
1. **[401 Unauthorized](401_unauthorized.md)** - Expired subscription or wrong credentials
2. **[404 Not Found](404_not_found.md)** - Provider changed server URL
3. **[403 Forbidden](403_forbidden.md)** - IP not whitelisted or too many connections
4. **[503 Service Unavailable](503_service_unavailable.md)** - Maintenance or overload
5. **[Connection Refused](connection_refused.md)** - Wrong port number

**TinyURL Errors**: 401 Unauthorized (API key not configured), 503 Service Unavailable (temporary outage), 429 Too Many Requests (rate limited), 404 Not Found (original cloud file missing)

**Dropbox Errors**: 401 Unauthorized (OAuth token expired), 403 Forbidden (quota exceeded), 409 Conflict (simultaneous updates), 429 Too Many Requests (rate limited)

**Google Drive Errors**: 401 Unauthorized (OAuth token expired), 403 Forbidden (API quota exceeded), 429 Too Many Requests (rate limited)

### Prevention Best Practices

**Minimize Authentication Errors (401, 403)**: Keep subscriptions current. Reauthorize cloud storage monthly. Monitor API key validity. Use XC API instead of M3U URLs.

**Minimize Rate Limit Errors (429)**: Sync EPGs 2x daily maximum. Use Universal EPG (reduces API calls). Don't run multiple Boss instances. Batch changes before outputting.

**Minimize File Size Errors (413, 408)**: Use Universal EPG. Disable VOD if not needed. Use compressed EPG format (.gz). Limit "Days to Keep" to 7 days.

**Minimize Server Errors (5xx)**: Sync during off-peak hours. Monitor provider announcements. Have backup provider configured. Configure multiple cloud storage options.

### When to Contact Support

**Contact Provider Support**: 401/403 with correct credentials persists. 404 on provider URLs. 500/503 lasting more than few hours. Connection refused with correct server:port.

**Contact IPTVBoss Support**: Error only in Boss, not browser/other apps. Error started after Boss update. Error doesn't match any guide patterns. Need help interpreting logs.

**Post in Discord With**: Exact error code and message. What you were trying to do. Logs from IPTVBoss/logs (cleaned of sensitive info). Boss version and OS. What you've already tried.

### Related Documentation

- [FAQ](../FAQ.md) - Common questions answered
- [Troubleshooting Guide](../Troubleshooting_Guide.md) - Problem-solution workflows
- [User Guide](../User_Guide.md) - Comprehensive usage documentation
- [Known Issues](../Known_Issues.md) - Unresolved problems

### Error Categories Explained

**Client Errors (4xx)**: These indicate a problem with IPTVBoss's request to the server. Usually fixable by correcting credentials, URLs, or reducing request frequency/size. You can typically fix these.

**Server Errors (5xx)**: These indicate a problem on the provider/service side. Usually temporary - wait and retry. Limited control - usually need to wait for provider to fix.

**Connection Errors**: These occur before HTTP communication even starts. Usually network, firewall, or DNS issues. Check your network connectivity and firewall settings.
