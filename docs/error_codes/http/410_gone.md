# 410 Gone

**Category**: Client Error (4xx)

**What it means**: Resource permanently deleted - stronger than 404, indicates intentional removal.

### Common Causes in IPTVBoss

**Provider Permanently Shut Down Service/URL**:
- Provider discontinued service
- Server decommissioned
- API endpoint deprecated and removed

**Cloud Storage File Permanently Deleted**:
- File removed from cloud storage
- Folder structure changed
- Account deleted

### How to Fix

**For Provider Sources**:

1. 410 means resource permanently gone:
   - Not a temporary issue
   - Provider intentionally removed resource
   - Won't come back

2. Contact provider:
   - Ask for new URL/server
   - Provider may have migrated to new infrastructure
   - May need new credentials

3. Check for provider announcements:
   - Look for migration notices
   - Check Discord/forums
   - Email from provider

4. Switch providers if necessary:
   - If provider shut down permanently
   - Find alternative provider
   - Restore backup before remapping channels

5. Update source in Boss:
   - If provider gives new URL
   - Sources → Sources Manager
   - Update with new URL from provider
   - Save and sync

**For Cloud Storage**:

1. Re-output layouts:
   - If files permanently deleted
   - Recreate by outputting again
   - Layout Manager → Output Current Layout

2. Verify cloud storage folder structure:
   - Check Boss folder still exists
   - May need to recreate folder
   - Or reconfigure Boss cloud path

3. Reauthorize if needed:
   - If cloud account had issues
   - Settings → Cloud Storage
   - Reauthorize OAuth

### Prevention

- Monitor provider status - watch for shutdown announcements
- Keep backup of provider info - contact details, alternatives
- Have alternative provider ready - don't rely on single provider
- Don't manually delete cloud files - let Boss manage them
- Keep database backups - easier to switch providers with backups

### Related Errors

- [404 Not Found](404_not_found.md) - Similar but doesn't indicate permanent removal
- [503 Service Unavailable](503_service_unavailable.md) - Temporary vs permanent unavailability

### See Also

- [Troubleshooting: Source Sync Failures](../Troubleshooting_Guide.md#source-sync-failures-and-updates-breaking-layouts)
- [FAQ: Source Management](../FAQ.md#source-management)
