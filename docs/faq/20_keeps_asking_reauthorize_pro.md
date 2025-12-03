# IPTVBoss Keeps Asking to Reauthorize Boss Pro

License validation loop - verify license is active and migrate to new website if needed.

### Problem

IPTVBoss keeps asking you to reauthorize Boss Pro and won't restore your database.

### Solution

**License authorization loop fix:**

1. Verify your Pro license is still active (check purchase date)
2. If using old website credentials, migrate to the new IPTVBoss website
3. Enter the license key from the new website
4. Try restore again after successful Pro activation

**If activation fails:**

- Check internet connection (Pro license validates online)
- Verify license key is copied correctly (no extra spaces)
- Check if Boss Pro website is accessible
- Wait several minutes after entering the key (some users report delays)

**Error "Table SETTINGS not found"**: Database is completely empty/corrupt. You MUST restore from a backup before Boss Pro can activate.

### Related Topics

- [Playlists Disappeared and Lost Pro](19_playlists_disappeared_lost_pro.md)
- [License Validation Failures](../troubleshooting/10_license_validation_failures.md)
