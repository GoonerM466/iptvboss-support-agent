# Database Backup Portability After Reinstall or New Computer

Database backups are portable and can be moved to new installations.

### Question

Will my database backup work if I reinstall Windows/IPTVBoss or move to a new computer?

### Answer

Yes, database backups are portable.

**Steps:**

1. **Before reinstall**: Copy the entire IPTVBoss folder (especially `IPTVBoss/db` & `IPTVBoss/backup` directories) to USB or external drive
2. **After reinstalling IPTVBoss**:
   - Start the program once and shut down
   - Copy your saved IPTVBoss folders to the IPTVBoss folder on the new install/computer
   - Start IPTVBoss & make sure transfer is successful. If it isn't continue below
3. Your setup should be reinstated, however if you have issues try **Settings → Restore Database → Local**
4. Re-Authorize cloud

**Alternative**: If using cloud sync (Dropbox/Google Drive), you can restore from cloud after reinstalling however you must enter your cloud settings first.

### Related Topics

- [Where Are IPTVBoss Files Located](16_where_are_iptvboss_files_located.md)
- [Subscription Expired Cannot Restore](21_subscription_expired_cannot_restore.md)
