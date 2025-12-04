# Pro Activation Fails Despite Valid License

Boss shows "Unable to Activate Pro" despite valid license key.

### Status

Multiple possible causes - needs case-by-case investigation.

### Problem

Pro license validation fails even though the license key is confirmed valid on the website.

### Symptoms

- License key is valid (checked on website)
- Boss shows "Unable to Activate Pro"
- Repeated attempts fail
- Internet connection works

### Possible Causes

- Network/firewall blocking validation servers
- DNS issue
- Boss validation servers experiencing issues
- Credential migration incomplete (old website → new website)
- Boss can't reach validation endpoint (corporate firewall, VPN, etc.)

### Workaround

1. Verify license on new IPTVBoss website (not old)
2. Try different network (disable VPN, try mobile hotspot)
3. Check firewall rules for Boss
4. Check logs for HTTP, authorization or connection errors
5. Contact support with logs if verified valid license

### Escalation

If you cannot resolve the issue contact support on [Discord](https://discord.gg/QCxpA9yvWP)

### Related Topics

- [Prompted to Upgrade Pro Valid License](../faq/23_prompted_upgrade_pro_valid_license.md)
- [License Validation Failures](../troubleshooting/10_license_validation_failures.md)
