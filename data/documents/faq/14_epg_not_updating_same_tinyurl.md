# EPG Not Updating and Shows Same Old TinyURL

TinyURL links are persistent - same short URL for same file.

### Problem

EPG is not updating and keeps showing the same old TinyURL.

### Solution

**Force TinyURL regeneration:**

1. Delete cloud files from your Dropbox/Google Drive (via the website)
2. Save your TinyURL API settings again in IPTVBoss
3. Output layouts again
4. New TinyURL links should generate

### Why This Happens

TinyURL links are persistent (same short URL for same file). If the cloud file hasn't changed, TinyURL stays the same.

**Check**: Are your EPGs actually syncing? If EPG content isn't updating, new TinyURLs won't help - fix EPG sync first.

### Related Topics

- [EPG Auto-Sync Stopped Working](../troubleshooting/05_epg_auto_sync_stopped_nogui.md)
- [TinyURL Links Not Generating](01_tinyurl_not_generating.md)
