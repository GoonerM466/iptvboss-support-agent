# 429 Too Many Requests

**Category**: Client Error (4xx)

**What it means**: You've sent too many requests in a given time period - rate limited.

### Common Causes in IPTVBoss

**TinyURL Rate Limiting**:
- Too many URLs created too quickly
- Free tier rate limits exceeded
- Multiple Boss instances hitting same TinyURL account

**Cloud Storage API Rate Limits**:
- Too many uploads in short period
- Dropbox/Google Drive throttling
- Frequent small updates instead of batching

**Provider API Rate Limiting**:
- Syncing sources too frequently
- Multiple Boss instances syncing same provider account
- Automated syncs running too often

### How to Fix

**For TinyURL Rate Limits**:

1. Wait for rate limit reset:
   - Usually 15-30 minutes
   - Don't retry immediately
   - Timer resets automatically

2. Reduce output frequency:
   - Don't output after every small change
   - Batch multiple edits
   - Then output once

3. Close duplicate Boss instances:
   - Check Task Manager/Activity Monitor
   - Multiple instances count toward same limit
   - Keep only one running

4. Use direct cloud URLs temporarily:
   - Workaround while rate limited
   - View Cloud Links in Boss
   - Players accept full URLs

5. Upgrade TinyURL account if available:
   - Paid tiers have higher rate limits
   - Consider if frequently hitting limits

**For Cloud Storage Rate Limits**:

1. Wait for rate limit reset:
   - Usually 15-60 minutes
   - Check cloud service documentation
   - Timer resets automatically

2. Reduce sync/output frequency:
   - Don't sync multiple times per hour
   - 2x daily is sufficient for EPG
   - Batch changes before outputting

3. Use Universal EPG:
   - Dramatically reduces API calls
   - One EPG file instead of many
   - 80%+ fewer API requests

4. Check for API usage:
   - Dropbox: Check API usage in developer console
   - Google Drive: Check API quotas
   - Identify what's consuming quota

**For Provider Rate Limits**:

1. Reduce sync frequency:
   - Don't sync more than 2x daily
   - Providers update EPG 1-2x daily anyway
   - More frequent sync doesn't help

2. Disable auto-sync temporarily:
   - If NoGUI running too frequently
   - Check Task Scheduler/cron settings
   - Adjust schedule to less frequent

3. Close other Boss instances:
   - Multiple instances count toward limit
   - Each sync attempt counts
   - Keep only one instance running

4. Contact provider:
   - Ask about rate limits
   - May be able to increase for your account
   - Verify you're not violating TOS

### Prevention

**Optimize Sync Frequency**:

**EPG Syncing**:
- **Recommended**: 2x daily (morning and evening)
- **Maximum**: Every 6 hours
- **Never**: Every hour or more
- **Why**: EPG providers update 1-2x daily anyway

**Source Syncing**:
- **Recommended**: Once daily or less
- **Only when needed**: Provider announces changes
- **Never**: Automatic every few hours
- **Why**: Channel lists rarely change

**Optimize API Usage**:

1. Use Universal EPG:
   - Single EPG file for all layouts
   - Reduces API calls by 80%+
   - Settings → Universal EPG Options

2. Batch changes before outputting:
   - Make multiple edits in Boss
   - Output once when done
   - Not after each tiny change

3. Don't run multiple Boss instances:
   - All count toward same rate limits
   - If multi-instance needed:
     - Disable cloud sync on secondary instances
     - Stagger sync times

4. Monitor frequency:
   - Check NoGUI schedule (cron/Task Scheduler)
   - Verify not running too often
   - Adjust if needed

### Rate Limit Best Practices

**Appropriate Sync Schedule**:

```
EPG Sync: 2x daily
- 6:00 AM (morning)
- 6:00 PM (evening)

Source Sync: Once daily or on-demand
- Only when provider announces changes
- Manual sync preferred

Output: As needed after changes
- After completing multiple edits
- Not after each individual change
```

**Why This Works**:
- EPG data updates 1-2x daily from providers
- Over-syncing doesn't improve data
- Just wastes API quota
- Reduces risk of rate limiting

### Related Errors

- [403 Forbidden](403_forbidden.md) - May follow rate limiting
- [409 Conflict](409_conflict.md) - Multiple instances cause both issues
- [408 Request Timeout](408_request_timeout.md) - Server may slow down when rate limiting

### See Also

- [FAQ: EPG Sync Frequency](../FAQ.md#automation-and-syncing)
- [Troubleshooting: EPG Auto-Sync Issues](../Troubleshooting_Guide.md#epg-auto-sync-stopped-working-noguicrontask-scheduler)
- [FAQ: TinyURL Errors](../FAQ.md#tinyurl-and-cloud-setup)
