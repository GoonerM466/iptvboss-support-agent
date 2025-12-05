# Solution: Reauthorize Cloud Storage

**Flow ID**: cloud_storage
**Type**: diagnostic_solution
**Confidence**: high
**Solution Steps**: 3

### Context

Cloud storage authentication failed or expired. Need to reconnect Boss to cloud provider.

### Confidence

**HIGH (90%+)** - Reauthorization fixes most cloud auth issues

### Solution Steps

### 1. Disconnect Current Cloud

1. Boss → **Settings** → **Cloud Storage**
2. Find your cloud provider (Dropbox/Google Drive)
3. Click **Disconnect** or **Remove**
4. Confirm disconnection

### 2. Reconnect with Full Permissions

**For Dropbox**:
1. Boss → Settings → Cloud Storage → **Add Dropbox**
2. Opens browser for Dropbox login
3. Log into Dropbox account
4. **Grant all permissions** when asked
5. Return to Boss
6. Verify connection successful

**For Google Drive**:
1. Boss → Settings → Cloud Storage → **Add Google Drive**
2. Opens browser for Google login
3. Log into Google account
4. **Select correct Google account** if multiple
5. Click **Allow** and grant all permissions
6. Return to Boss
7. Verify connection successful

**Important**: Must grant **full access**, not restricted

### 3. Test Upload

1. Boss → **Output** → Select any layout
2. Click Output
3. Wait for success message
4. Click **View Cloud Links**
5. Verify files show recent timestamps

### ✅ If That Fixed It

Set reminder to reauth annually:
- Dropbox tokens can expire
- Google tokens may need refresh
- Save cloud login credentials securely

### Common Mistakes

**Partial permissions**:
- Some users deny certain permissions
- Boss needs full read/write access
- Must grant all requested permissions

**Wrong account**:
- Multiple Dropbox/Google accounts
- Boss authenticated to wrong account
- Verify correct account when logging in

### Related Topics

- [Cloud Storage Setup](../../../user_guide/04_cloud_storage_setup.md)
- [Cloud Upload Failures](../../07_cloud_storage_upload_failures.md)
- [Upload Issues](02_solution_upload_failures.md)
