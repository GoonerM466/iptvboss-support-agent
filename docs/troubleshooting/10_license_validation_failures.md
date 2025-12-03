# License Validation Failures and Loops

Pro license won't validate despite being valid.

### Problem

Pro license fails to validate or repeatedly requests reauthorization.

### Symptoms

- Prompted to upgrade to Pro despite valid license
- Pro license "doesn't exist" when checking website
- Authorization loop - keeps asking for license repeatedly
- Database restore requires Pro but Pro won't activate
- "License unknown" after update

### Why This Happens

User hasn't migrated account to new IPTVBoss website. Using old website credentials. Database corruption preventing Pro activation. License actually expired. Network blocking license validation. Chicken-and-egg: need DB to activate Pro, need Pro to restore DB.

### Solution

**Step 1: Verify license still active**
- Check purchase date/subscription status
- Verify license hasn't expired
- Confirm you have valid license key

**Step 2: Migrate to new website** (if applicable)
- IPTVBoss migrated to new website system
- Old website credentials don't work on new system
- Visit new IPTVBoss website
- Migrate account or create new with license key
- Use license key from NEW website

**Step 3: Enter license correctly**
- IPTVBoss GUI ’ Menu ’ Activate Pro
- Copy license key (don't type manually)
- Paste carefully - no extra spaces or line breaks
- Click Activate

**Step 4: Wait and verify**
- License validation happens online
- May take several minutes
- Ensure stable internet connection
- Some users report 2-5 minute delay before activation

**Step 5: Check network**
- Ensure IPTVBoss can reach validation servers
- Check firewall isn't blocking
- Try disabling VPN temporarily
- Verify IPTVBoss website is accessible

### For Specific Errors

**"Table SETTINGS not found":**
- This means database is completely empty
- Pro license can't activate without database
- Must restore database from backup first
- After restore, re-enter Pro license

**For authorization loops:**
- Clear any old license entries
- Restart IPTVBoss
- Enter fresh license key from new website
- Verify internet connectivity throughout process

### Database + License Interaction

- Pro activation requires working database
- Database restore sometimes requires Pro
- Usually auto-resolves: database auto-restore allows Pro entry
- If stuck: Try manual restore with free version, then activate Pro

### Prevention

- Keep license key accessible
- Don't let license expire without renewal ready
- Update license in Boss before expiration date
- Keep backup of license key email

### Known Limitations

- Website migration not communicated to all users
- Chicken-and-egg problem with DB vs Pro (usually self-resolves)
- Expired licenses during system migration caused widespread confusion
- Error messages don't clearly indicate "need new website account"

### Related Topics

- [Keeps Asking to Reauthorize Pro](../faq/20_keeps_asking_reauthorize_pro.md)
- [Prompted to Upgrade Pro Valid License](../faq/23_prompted_upgrade_pro_valid_license.md)
- [Subscription Expired Cannot Restore](../faq/21_subscription_expired_cannot_restore.md)
