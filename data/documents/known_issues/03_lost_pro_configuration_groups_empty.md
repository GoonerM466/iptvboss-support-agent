# Lost Pro Configuration - Groups Empty, Authorization Loop

Groups exist but contain no channels, stuck in Pro authorization loop.

### Status

Partial database corruption - needs investigation.

### Problem

Groups exist in layout but contain no channels, accompanied by Pro license validation problems.

### Symptoms

- Groups exist but have no channels
- Stuck in Pro authorization loop
- Database restore doesn't help or partially restores
- Pro license won't validate

### Possible Causes

- Partial database corruption
- Incomplete database restore
- Old website vs new website credential conflicts
- Database and license system desync

### Workaround

- Must restore from older backup (before corruption)
- No recovery from empty-but-existing groups
- If backups don't work, must rebuild from scratch

### Escalation

If you cannot resolve the issue contact support on [Discord](https://discord.gg/QCxpA9yvWP)

### Related Topics

- [Playlists Disappeared and Lost Pro](../faq/19_playlists_disappeared_lost_pro.md)
- [Keeps Asking to Reauthorize Pro](../faq/20_keeps_asking_reauthorize_pro.md)
- [License Validation Failures](../troubleshooting/10_license_validation_failures.md)
