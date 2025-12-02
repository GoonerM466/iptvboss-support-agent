# XC Server Troubleshooting and Comparison

**Troubleshooting XC Server**:
- **Server won't start**: Check Universal EPG is enabled
- **No channels in XC output**: Ensure layouts have "XC Enabled" checked
- **EPG not showing**: Build programmes database (output EPG once)
- **Can't access remotely**: Check firewall, server URL/port settings
- **Commands not working**: Verify API key is correct

**XC Server vs Traditional Output**:

**Traditional (M3U/XML)**:
- Files uploaded to cloud storage
- Players download files periodically
- Simpler setup
- Works with all players

**XC Server**:
- Players connect to your server via API
- Dynamic delivery
- More complex setup
- Requires running server
- Only works with XC-compatible players


---

## Related Topics

- [Previous: Setting Up XC Server as Ubuntu/Linux Service](35_xc_server_linux_service.md)
- [Next: Troubleshooting Common Issues](37_troubleshooting_overview.md)
