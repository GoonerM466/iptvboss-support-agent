# Cloud Storage Issues Diagnostic - Entry Point

**Flow ID**: cloud_storage
**Type**: diagnostic_entry
**Confidence**: low (requires questions)

### Common User Phrases

- "Cloud upload failed"
- "Dropbox not working"
- "Google Drive error"
- "Failed to upload"
- "Authentication failed"
- "Cloud storage error"
- "Output failed"

### Diagnostic Questions

**Question 1**: "Which cloud storage are you using (Dropbox, Google Drive, or Local)?"
- Different cloud providers have different auth methods
- Helps identify cloud-specific issues

**Question 2**: "What error message do you see when outputting?"
- "Authentication failed" → Reauth needed → [Reauthorize Cloud](01_solution_reauth.md)
- "Upload failed" → Network or permissions → [Upload Issues](02_solution_upload_failures.md)
- "No error, but files not updated" → Silent failure → [Verify Upload](02_solution_upload_failures.md)

**Question 3**: "Did this work before, or is this a new setup?"
- **Worked before** → Auth expired or permissions changed
- **New setup** → Configuration or permissions issue

### Related Guide

[Cloud Storage Upload Failures](../../07_cloud_storage_upload_failures.md)
