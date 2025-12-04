# Connection Reset

**Category**: Connection Error (Non-HTTP)

**What it means**: Connection established but then terminated abruptly by remote server.

### Common Causes in IPTVBoss

**Provider Server Killed Connection**:
- Request took too long
- Server overloaded and dropped connection
- Connection limit per IP exceeded

**Network Instability**:
- Router/modem issues
- ISP network problems
- Wi-Fi connection dropped

**Provider Anti-Abuse Mechanisms**:
- Too many concurrent connections
- Detected unusual activity
- IP temporarily blocked

### How to Fix

**For Provider Resets**:

1. Close other apps using same account:
   - Check all devices
   - Multiple connections count against limit
   - Each Boss instance counts as connection

2. Limit concurrent connections:
   - Don't run multiple Boss instances
   - Close duplicate processes
   - Check Task Manager/Activity Monitor

3. Try during off-peak hours:
   - Early morning often better
   - Fewer users = more stable
   - Provider servers less loaded

4. Check IP whitelisting:
   - Some providers require whitelisting
   - Add your IP in provider panel
   - Ensures connection not blocked

5. Contact provider about limits:
   - Ask about connection limits
   - May need to upgrade account
   - Or reduce concurrent usage

**For Network Issues**:

1. Test internet stability:
   - Run continuous ping test
   - `ping -t 8.8.8.8` (Windows)
   - `ping 8.8.8.8` (Mac/Linux)
   - Look for packet loss

2. Use wired connection:
   - Wi-Fi more prone to drops
   - Ethernet more stable
   - Especially for Boss server

3. Restart network equipment:
   - Restart router/modem
   - Power cycle completely
   - Wait 30 seconds before powering on

4. Contact ISP:
   - If persistent network issues
   - ISP can check line quality
   - May have area issues

### Prevention

- Use wired connection for Boss server - more stable than Wi-Fi
- Monitor concurrent connection limits - don't exceed provider limits
- Don't run multiple Boss instances on same account
- Keep network equipment updated - firmware updates
- Avoid peak usage times - if provider resets common

### Testing Network Stability

**Continuous Ping Test**:

**Windows**:
```
ping -t 8.8.8.8
```

**Mac/Linux**:
```
ping 8.8.8.8
```

**Watch for**:
- Packet loss
- High latency spikes
- Request timeouts

**Good**: 0% packet loss, consistent latency
**Bad**: Any packet loss, erratic latency

### Related Errors

- [Connection Refused](connection_refused.md) - Connection never established
- [Network Timeout](network_timeout.md) - Connection too slow
- [403 Forbidden](403_forbidden.md) - May follow if IP blocked after resets

### See Also

- [Troubleshooting: Source Sync Failures](../Troubleshooting_Guide.md#source-sync-failures-and-updates-breaking-layouts)
- [HTTP Error Overview](http_error_overview.md)
