# 404 Not Found

**Category**: Client Error (4xx)

**What it means**: The server can't find the requested resource - URL is wrong, file deleted, or path incorrect.

---

### Common Causes in IPTVBoss

**Provider M3U URL Changed**:
- Provider changed server URLs
- M3U endpoint moved or renamed
- Server no longer exists

**Cloud Storage File Not Found**:
- File deleted from cloud storage
- Wrong file path or folder
- File upload failed but Boss thinks it succeeded

**TinyURL Link Broken**:
- Shortened URL expired or deleted
- Original file removed from cloud storage
- TinyURL account deleted

**XC API Endpoint Incorrect**:
- Wrong server address
- Port number incorrect
- API path changed by provider

**EPG Source URL Invalid**:
- EPG moved to new URL
- EPG no longer provided by source
- URL typo

---

### How to Fix

**For Provider M3U URLs**:

1. Test URL in browser:
- Paste URL into browser address bar
- Should download M3U file
- If 404 in browser too, URL definitely wrong

2. Check provider announcements:
- Look for URL change notices
- Check provider Discord/forums
- Review email from provider

3. Contact provider:
- Ask for current M3U URL
- Verify server hasn't moved

4. Update source in IPTVBoss:
- Sources → Sources Manager
- Select source
- Update URL with correct one from provider
- Save and sync

**For XC API Connections**:

1. Verify server address:
   - Must match provider panel exactly
   - Include correct port number
   - Common ports: 80, 8080, 2086, 25461

2. Test in browser:
   - `http://server:port/player_api.php?username=USER&password=PASS`
   - Should return JSON data
   - If 404, server URL or port wrong

3. Check provider panel:
   - Copy server URL exactly as shown
   - Verify port number
   - Don't assume standard port

4. Get correct URL from provider:
   - If panel info doesn't work, contact support
   - Provider may have changed infrastructure

**For Cloud Storage Files**:

1. Check cloud storage website:
   - Log into Dropbox/Google Drive
   - Navigate to IPTVBoss folder
   - Verify files actually exist

2. Check file paths:
   - Ensure Boss is looking in correct folder
   - Path may have changed

3. Re-output layouts:
   - If files missing, regenerate them
   - Layout Manager → Output Current Layout
   - Files will be recreated and uploaded

4. Verify upload completed:
   - Check Boss logs for upload errors
   - View Cloud Links to confirm files present
   - Check file sizes (shouldn't be 0 bytes)

**For TinyURL Links**:

1. TinyURL 404 means underlying file gone:
   - TinyURL is just a shortcut
   - Real file must exist in cloud storage

2. Check original cloud file:
   - Log into cloud storage
   - Verify M3U/EPG files exist
   - If missing, need to re-output

3. Regenerate TinyURL:
   - Delete cloud files
   - Re-output layout
   - New TinyURL links generate automatically

4. Use direct cloud URLs:
   - Workaround for TinyURL issues
   - View Cloud Links in Boss
   - Players accept full Dropbox/Google Drive URLs

**For EPG Sources**:

1. Test EPG URL in browser:
   - Should download XML or GZ file
   - If 404, EPG provider changed or discontinued

2. Find alternative EPG source:
   - EPG provider may have moved
   - Look for updated URL
   - Or switch to different EPG source

3. Update EPG source in Boss
   - Sources → Sources Manager
   - Select EPG source
   - Update URL
   - Sync EPGs

---

### Prevention

- **Use XC API instead of M3U URLs** - providers update less frequently
- **Monitor provider announcements** - watch for URL changes
- **Keep backup of working URLs** - document what works
- **Test URLs after provider updates** - verify still accessible
- **Don't manually delete cloud files** - let Boss manage them
- **Bookmark provider panels** - easy access to current URLs

---

### Workaround for Broken TinyURL

- Use direct Dropbox/Google Drive URLs instead
- Players accept full URLs
- TinyURL just for convenience, not required
- View Cloud Links in Boss shows direct URLs

---

### Related Errors

- **[401 Unauthorized](401_unauthorized.md)** - May occur first if credentials also wrong
- **[410 Gone](410_gone.md)** - Stronger than 404, indicates permanent deletion
- **[400 Bad Request](400_bad_request.md)** - URL may be malformed rather than just wrong

---

### See Also

- [Troubleshooting: Source Sync Failures](../Troubleshooting_Guide.md#source-sync-failures-and-updates-breaking-layouts)
- [FAQ: TinyURL Links Not Generating](../FAQ.md#why-isnt-my-tinyurl-link-generating-when-i-output-my-playlist)
- [Troubleshooting: Cloud Storage Upload Failures](../Troubleshooting_Guide.md#cloud-storage-uploadsync-failures)

---

**Back to**: [HTTP Error Overview](http_error_overview.md)
