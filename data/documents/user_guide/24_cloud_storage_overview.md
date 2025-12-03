# Understanding Cloud Storage Options

IPTVBoss uploads M3U and EPG files to cloud storage for access from player apps.

**Supported providers**:
- Dropbox (Recommended)
- Google Drive

**Choosing**:
- Dropbox: Simple, widely supported
- Google Drive: Often more generous bandwidth
- Either works fine

**Bandwidth considerations**:

**Free Dropbox**:
- ~20GB/month bandwidth
- Fine for personal use (1-5 devices)
- 40-50 users often exceeds limit

**Free Google Drive**:
- Often more generous
- Check current limits

**Paid tiers**:
- Consider if supporting many users
- Or use bandwidth optimization (Universal EPG, exclude VOD, .gz format)

*Watch cloud setup video of your choice and follow cloud storage setup instructions before continuing*
- Dropbox (recommended): https://youtu.be/2cfEEqFYHrc
- Google Drive: https://youtu.be/A45N6Vgk-OU
   - You must use the gz EPG link with Google Drive - Not XML

**Setup** (quick reminder):
1. Settings → IPTVBoss Settings
2. Choose Dropbox or Google Drive
3. Authorize (OAuth in browser)
4. Verify authorization success

**Reauthorization**:
- OAuth tokens expire periodically
- After OS reinstalls/upgrades
- If uploads fail, try reauthorizing


---

### Related Topics

- [Previous: Manually outputting](23_manual_output.md)
- [Next: Using TinyURL for Short Links](25_tinyurl_short_links.md)
