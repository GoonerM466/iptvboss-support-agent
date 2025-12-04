# Connection Refused

**Category**: Connection Error (Non-HTTP)

**What it means**: Target server actively refused connection - server not listening on that port, or firewall blocking.

### Common Causes in IPTVBoss

**Wrong Server Port Number**:
- XC API port incorrect
- Common ports: 80, 8080, 2086, 25461
- Provider changed port

**Provider Server Firewall**:
- IP not whitelisted
- Port blocked by firewall
- Security rules blocking connection

**Provider Server Offline**:
- Server not running
- Maintenance
- Server crashed

**Local Firewall Blocking Outbound**:
- Windows Firewall blocking IPTVBoss
- Antivirus blocking connection
- Router firewall rules

### How to Fix

**For Provider Connections**:

1. Verify server address and port:
   - Check provider panel for exact URL
   - Format: `http://server:port`
   - Copy exactly as shown

2. Test in browser:
   - Try: `http://server:port/player_api.php?username=USER&password=PASS`
   - Should return JSON data
   - If browser also refuses: provider server issue

3. Try common ports:
   - 80 (HTTP default)
   - 8080 (alternate HTTP)
   - 2086 (common for XC)
   - 25461 (common for XC)
   - One may work if provider panel shows wrong port

4. Check provider status:
   - Look for maintenance announcements
   - Check Discord/forums for outages
   - Contact provider support

5. Verify IP whitelist:
   - Some providers require IP whitelisting
   - Add your IP in provider panel
   - Dynamic IPs need frequent updates

**For Firewall Issues**:

1. Test with firewall disabled:
   - Temporarily disable Windows Firewall
   - If works: Firewall blocking Boss
   - Re-enable after test

2. Add Boss to firewall exceptions:
   - Windows: Settings → Firewall → Allow app
   - Add IPTVBoss executable
   - Allow both private and public networks

3. Check antivirus:
   - Antivirus may block connections
   - Add Boss to antivirus whitelist
   - Check firewall module in antivirus

4. Router firewall:
   - Check router firewall rules
   - Ensure outbound connections allowed
   - Usually not an issue (routers allow outbound)

### Prevention

- Keep provider server info updated - document changes
- Document working server:port combinations - reference for future
- Add Boss to firewall exceptions preemptively - before problems occur
- Monitor provider announcements - maintenance and server changes

### Testing Connection

**Quick Test in Browser**:

```
http://server:port/player_api.php?username=USER&password=PASS
```

**Success**: Returns JSON with account info
**Failure**: Connection refused or timeout

**Command Line Test (Advanced)**:

**Windows**:
```
telnet server port
```

**Mac/Linux**:
```
nc -zv server port
```

**Success**: Connection established
**Failure**: Connection refused or timeout

### Related Errors

- [Connection Reset](connection_reset.md) - Connection established then dropped
- [Network Timeout](network_timeout.md) - Similar but times out rather than refuses
- [404 Not Found](404_not_found.md) - May follow if port correct but path wrong

### See Also

- [FAQ: Source Management](../FAQ.md#source-management)
- [Troubleshooting: Source Sync Failures](../Troubleshooting_Guide.md#source-sync-failures-and-updates-breaking-layouts)
- [HTTP Error Overview](http_error_overview.md)
