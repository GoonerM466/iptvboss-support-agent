# DNS Resolution Failed

**Category**: Connection Error (Non-HTTP)

**What it means**: Couldn't translate hostname to IP address - DNS lookup failed.

### Common Causes in IPTVBoss

**Provider Domain Doesn't Exist**:
- Typo in server address
- Provider domain expired
- DNS not propagated yet (new provider)

**Local DNS Issues**:
- DNS server unreachable
- ISP DNS problems
- Local network misconfiguration

**Network Connectivity Loss**:
- Internet connection down
- Router issues
- Firewall blocking DNS queries

### How to Fix

**For Provider Domain Issues**:

1. Verify server address spelling:
   - Check for typos carefully
   - Common mistakes: .com vs .net, hyphen vs underscore

2. Copy-paste from provider panel:
   - Don't type manually
   - Copy exactly as shown
   - Avoids typo errors

3. Test domain in browser:
   - Try opening `http://server` in browser
   - Should at least connect (may show error page)
   - If doesn't resolve in browser either, domain issue

4. Try IP address instead:
   - If provider gives IP address
   - Use IP directly instead of hostname
   - Format: `http://192.168.1.1:port`

5. Contact provider:
   - If domain doesn't resolve anywhere
   - Domain may have expired
   - Or provider changed domain

**For DNS Issues**:

1. Check internet connectivity:
   - Try browsing other websites
   - Test: `ping 8.8.8.8` (Google DNS)
   - If that fails, internet down

2. Flush DNS cache:

   **Windows**:
   ```
   ipconfig /flushdns
   ```

   **Mac**:
   ```
   sudo killall -HUP mDNSResponder
   ```

   **Linux**:
   ```
   sudo systemd-resolve --flush-caches
   ```

3. Change DNS servers:
   - Use more reliable DNS servers

   **Google DNS**:
   - Primary: 8.8.8.8
   - Secondary: 8.8.4.4

   **Cloudflare DNS**:
   - Primary: 1.1.1.1
   - Secondary: 1.0.0.1

   **Windows**: Network Settings → Change Adapter Options → Properties → IPv4 → DNS
   **Mac**: System Preferences → Network → Advanced → DNS
   **Linux**: Edit `/etc/resolv.conf`

4. Restart router:
   - Power cycle router/modem
   - Wait 30 seconds before powering on
   - Resets DNS cache and connections

### Prevention

- Use reliable DNS servers (Google, Cloudflare) - more stable than ISP DNS
- Keep provider contact info updated - easy to verify changes
- Document working IP addresses as backup - use if DNS fails
- Copy-paste URLs - avoid typos

### Testing DNS Resolution

**Check DNS Resolution**:

**Windows**:
```
nslookup server.example.com
```

**Mac/Linux**:
```
dig server.example.com
```

**Success**: Returns IP address
**Failure**: No IP address or NXDOMAIN error

**Test Different DNS Server**:

**Windows**:
```
nslookup server.example.com 8.8.8.8
```

**Mac/Linux**:
```
dig @8.8.8.8 server.example.com
```

If works with Google DNS (8.8.8.8) but not your DNS:
- Your DNS server has issues
- Change DNS servers permanently

### Related Errors

- [Connection Refused](connection_refused.md) - May follow if DNS resolves but connection fails
- [404 Not Found](404_not_found.md) - May follow if DNS works but URL wrong
- [Network Timeout](network_timeout.md) - May occur during DNS resolution

### See Also

- [FAQ: Source Management](../FAQ.md#source-management)
- [Troubleshooting: Source Sync Failures](../Troubleshooting_Guide.md#source-sync-failures-and-updates-breaking-layouts)
- [HTTP Error Overview](http_error_overview.md)
