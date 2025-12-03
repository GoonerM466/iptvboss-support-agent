# Port-Migration Database and Setup Recovery Issues

Setting up IPTVBoss on new computer/OS - restore fails.

### Problem

Database restore fails when setting up IPTVBoss on a new machine.

### Symptoms

- Setting up on new computer - restore fails
- After OS reinstall, restore removes Boss token
- Moving to new laptop - authorization loops
- Database restore works but layouts empty
- New machine setup stuck in loops

### Why This Happens

Incorrect setup sequence - restore attempted before Pro activation. Old website credentials used on new installation. Cloud sync trying to overwrite local during restore. Database file incompatibility between significantly different versions.

### Solution

**CORRECT setup sequence** (order matters!):

**1. Install IPTVBoss on new machine**
- Download and install clean

**2. Enter Pro license key FIRST**
- Before anything else
- Menu ’ Activate Pro
- Enter license key from new website
- Wait for validation

**3. Set up cloud credentials**
- After Pro activation succeeds
- Configure Dropbox or Google Drive
- Complete authorization

**4. THEN restore from backup**
- Now that Pro and cloud are set up
- Menu ’ Restore
- Choose Local or Cloud
- Select backup file

### For Manual Backup Restore

Before reinstalling:
1. Copy entire `IPTVBoss/backup` folder to USB or external drive
2. Copy folder to known location on new machine
3. After Pro activation, browse to saved backup location for restore

### Version Compatibility

- Backups generally compatible across versions
- Major version jumps (2.x to 3.x) may have issues
- Try latest backup first
- If issues, try backup from same version as new installation

### Cloud Restore vs Local Restore

- Cloud restore: Pulls from Dropbox/Google Drive
- Local restore: Uses files from IPTVBoss/backup folder
- If cloud restore fails, try local (and vice versa)

### Common Mistakes

- Trying to restore before activating Pro
- Using old website credentials
- Not waiting for Pro validation to complete
- Trying to restore from cloud before authorizing cloud storage

### Why Sequence Matters

- Database requires Pro context to restore properly
- Cloud credentials needed before cloud restore can work
- Attempting out-of-order causes various failures and loops

### Prevention

- Document correct sequence before starting
- Keep manual backup copies on external storage
- Take screenshots of settings before migration
- Test restore on old machine before wiping

### Known Limitations

- Setup wizard doesn't enforce sequence
- Error messages don't clearly indicate sequence problem
- Intuitive to try restore first (but wrong order)

### Related Topics

- [New Machine Restore Removes Token](../faq/22_new_machine_restore_removes_token.md)
- [Database Backup Portability](../faq/24_database_backup_portable_reinstall.md)
- [License Validation Failures](10_license_validation_failures.md)
