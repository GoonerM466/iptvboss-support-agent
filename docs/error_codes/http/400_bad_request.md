# 400 Bad Request

**Category**: Client Error (4xx)

**What it means**: The server couldn't understand your request because it was malformed or invalid.

### Common Causes in IPTVBoss

**Malformed M3U URL or XC API Parameters**
- URL contains invalid characters or encoding
- Missing required parameters for XC API
- Incorrect URL format

**Invalid TinyURL API Request**
- Malformed URL being shortened
- Invalid characters in alias or tags
- Missing required fields

**Cloud Storage API Issues**
- Invalid file path or filename
- Forbidden characters in filename (*, ?, <, >, |, etc.)
- Metadata or parameters incorrectly formatted

### How to Fix

**For Provider Sources**:

1. Verify M3U URL is correctly formatted - Check for extra spaces or line breaks, ensure proper encoding of special characters
2. Test URL directly - Paste URL into browser, should download M3U file, if browser also fails URL is wrong
3. For XC API - Verify server/username/password fields, check for special characters that need encoding, format: `http://server:port/player_api.php?username=USER&password=PASS`
4. Copy-paste URLs - Don't type manually, copy from provider panel exactly
5. Contact provider - If URL looks correct ask for proper format, provider may have specific requirements

**For TinyURL**:

1. Check URL being shortened - Must be valid accessible URL, should start with http:// or https://
2. Verify API key entry - No extra spaces or line breaks, copy-paste carefully
3. Test manually - Create TinyURL manually at tinyurl.com, if manual works Boss configuration issue
4. Remove custom settings - Remove custom alias if set, may contain invalid characters

**For Cloud Storage**:

1. Check output filename - Remove forbidden characters (Windows: \ / : * ? " < > |), keep filenames simple
2. Verify file path exists - Check cloud storage folder structure, ensure Boss has access to path
3. Test manual upload - Upload test file manually to cloud storage, if manual works Boss configuration issue

### Prevention

- Copy-paste URLs instead of typing manually
- Use XC API instead of M3U URLs when possible (more reliable)
- Avoid special characters in layout names (they become filenames)
- Test URLs in browser before adding to Boss
- Keep URLs from provider panel for reference

### Related Errors

- [401 Unauthorized](401_unauthorized.md) - Similar to 400 but specifically credential problems
- [404 Not Found](404_not_found.md) - URL format might be correct but resource doesn't exist
- [415 Unsupported Media Type](415_unsupported_media_type.md) - Request format issue

### See Also

- [HTTP Error Overview](http_error_overview.md)
- [FAQ: Source Management](../FAQ.md#source-management)
- [Troubleshooting: Source Sync Failures](../Troubleshooting_Guide.md#source-sync-failures-and-updates-breaking-layouts)
