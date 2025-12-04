# TinyURL API Authentication Failures

TinyURL integration not working, authentication errors.

### Problem

TinyURL integration fails with authentication or service errors.

### Symptoms

- "Unauthenticated" error when outputting
- "503 Service Unavailable" from TinyURL
- TinyURL links not generating
- EPG URLs show in cloud view but M3U URL missing
- Cloud files upload successfully but no TinyURL links created

### Why This Happens

TinyURL API key not configured or incorrect. Users haven't migrated from old TinyURL system to new API-based system (announced in Discord). TinyURL service experiencing temporary outage.

### Solution

**1. Create TinyURL account** (if not already done)
- Go to tinyurl.com
- Create free account
- This is required for new TinyURL API system

**2. Generate API key**
- Log into TinyURL account
- Navigate to API settings
- Generate API key
- Enable all permissions

**3. Configure in IPTVBoss**
- Settings → IPTVBoss Settings → TinyURL
- Enter API key (copy-paste carefully - no spaces)
- Save settings

**4. Force fresh generation**
- Delete cloud files from Dropbox/Google Drive website
    - This will force new links to be created
- Re-output layout from IPTVBoss
- New TinyURL links should generate
    - add new links to player

### For Specific Errors

**"Unauthenticated":**
- API key not entered or incorrect
- Copy API key again, ensure no spaces or truncation
- Verify in TinyURL account that API key is active

**"503 Service Unavailable":**
- TinyURL service is down (temporary)
- Check if tinyurl.com loads in browser
- Wait 10-15 minutes and retry
- Workaround: Use direct Dropbox/Google Drive URLs temporarily

**EPG links work but M3U missing:**
- M3U upload might have failed (larger file)
- Check IPTVBoss logs for upload errors
- Verify both files exist in cloud storage
- May need to reauthorize cloud storage

### Workaround

Use direct Dropbox/Google Drive URLs without TinyURL if TinyURL has ongoing issues. Players accept full URLs, TinyURL is just for convenience.
You can also manually convert your links to TinyURL (or another shortener) via their website. Note that if done this way, Boss cannnot generate them or manager the link directy. Your cloud files will still update.

### Migration Note

IPTVBoss switched from anonymous TinyURL to TinyURL API system. Old anonymous TinyURL no longer works. All users must create TinyURL accounts.

### Known Limitations

- Migration announcement in Discord - not all users aware of change
- API key setup not intuitive for non-technical users
- Error messages don't clearly indicate "need to create TinyURL account"

### Related Topics

- [TinyURL Links Not Generating](../faq/01_tinyurl_not_generating.md)
- [TinyURL Authentication Errors](../faq/02_tinyurl_authentication_errors.md)
- [TinyURL EPG But No M3U](../faq/03_tinyurl_epg_but_no_m3u.md)
