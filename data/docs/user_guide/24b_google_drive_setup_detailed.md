# Google Drive Setup - Detailed Guide

Complete step-by-step instructions for setting up Google Drive as your cloud storage provider.

**Video Tutorial**: https://youtu.be/A45N6Vgk-OU

**⚠️ CRITICAL**: You **MUST use the .gz EPG link** with Google Drive, NOT .xml. This is a Google Drive API limitation.

---

### Prerequisites

- Google Account
- IPTVBoss installed

---

### Setup Steps

This process involves creating a Google Cloud Project and configuring OAuth authentication.

### 1. Access Google Cloud Console

1. Log in to your Google Account
2. Go to [https://console.developers.google.com/](https://console.developers.google.com/)
3. You may need to accept terms of service on first visit

**Visual Reference**: [IPTVBoss 3.5 User Manual\images\image36.png](../../IPTVBoss 3.5 User Manual/images/image36.png)

### 2. Create New Project

1. Click the **project dropdown** next to "Google APIs" (top left)
2. Click **"New Project"**
3. Give your project a name (e.g., "IPTVBoss Storage")
4. Organization: Leave as "No organization" (unless you have a business account)
5. Click **"Create"**
6. Wait for project creation (takes ~30 seconds)

**Visual Reference**: [IPTVBoss 3.5 User Manual\images\image22.png](../../IPTVBoss 3.5 User Manual/images/image22.png)

### 3. Enable Google Drive API

1. Make sure your new project is selected (check project dropdown)
2. Click **"+ ENABLE APIS AND SERVICES"** button (big button near top)
3. In the search box, type **"drive"**
4. Select **"Google Drive API"** from results
5. Click **"Enable"** button
6. Wait for API to enable

**Visual References**: [IPTVBoss 3.5 User Manual\images\image42.png](../../IPTVBoss 3.5 User Manual/images/image42.png), [image5.png](../../IPTVBoss 3.5 User Manual/images/image5.png), [image28.png](../../IPTVBoss 3.5 User Manual/images/image28.png)

### 4. Configure OAuth Consent Screen

This step tells Google what your app does and who can use it.

1. **Access OAuth Consent Screen**:
   - Click **"OAuth Consent Screen"** in left sidebar
   - If prompted, select **"External"**
   - Click **"Create"**

**Visual References**: [IPTVBoss 3.5 User Manual\images\image43.png](../../IPTVBoss 3.5 User Manual/images/image43.png), [image23.png](../../IPTVBoss 3.5 User Manual/images/image23.png)

2. **Fill in App Information**:
   - **App Name**: "IPTVBoss" (or your choice)
   - **User support email**: Your email address
   - **Developer contact information**: Your email address again
   - **All other fields**: Optional, can skip
   - Click **"Save and Continue"**

### 5. Add Scopes

Scopes define what permissions your app needs.

1. On the **Scopes** page, click **"Add or Remove Scopes"** button
2. In the list that appears, enable these two scopes:
   - `https://www.googleapis.com/auth/drive.appdata`
   - `https://www.googleapis.com/auth/drive.file`
3. Click **"Update"** button (bottom of scope selector)
4. Click **"Save and Continue"**

**Visual References**: [IPTVBoss 3.5 User Manual\images\image31.png](../../IPTVBoss 3.5 User Manual/images/image31.png), [image38.png](../../IPTVBoss 3.5 User Manual/images/image38.png)

**Important**: These exact scopes are required. Don't add additional scopes.

### 6. Add Test Users

1. On the **Test Users** page, click **"Add Users"** button
2. Enter your own Google email address
3. Click **"Add"**
4. Click **"Save and Continue"**
5. Click **"Back to Dashboard"**

### 7. Publish App (Critical Step!)

**This is extremely important**:

1. On the OAuth consent screen dashboard, click **"Publish App"** button
2. Click **"Confirm"**

**Why this matters**:
- If left in "Testing" mode, your OAuth tokens expire after 7 days
- You'll have to re-authorize every week
- Publishing the app prevents token expiration

**Note**: Publishing for "External" use does NOT require Google verification for personal use. Your app is only accessible to users you explicitly authorize.

**Visual Reference**: [IPTVBoss 3.5 User Manual\images\image19.png](../../IPTVBoss 3.5 User Manual/images/image19.png)

### 8. Create OAuth Credentials

Now create the actual credentials IPTVBoss will use.

1. **Access Credentials**:
   - Click **"Credentials"** in left sidebar
   - Click **"Create Credentials"** button at top
   - Select **"OAuth client ID"**

**Visual References**: [IPTVBoss 3.5 User Manual\images\image35.png](../../IPTVBoss 3.5 User Manual/images/image35.png), [image34.png](../../IPTVBoss 3.5 User Manual/images/image34.png)

2. **Configure Client**:
   - In **"Application type"** dropdown, select **"TVs and Limited Input devices"**
   - **Name**: "IPTVBoss Client" (or your choice)
   - Click **"Create"**

3. **Save Credentials**:
   - A popup appears with your **Client ID** and **Client Secret**
   - Copy both or leave this window open
   - You'll need these in the next step

**Visual Reference**: [IPTVBoss 3.5 User Manual\images\image27.png](../../IPTVBoss 3.5 User Manual/images/image27.png)

---

### Related Topics

- [Understanding Cloud Storage Options](24_cloud_storage_overview.md)
- [Dropbox Setup](24a_dropbox_setup_detailed.md)
- [Outputting Playlists for Players](23_outputting_layouts_or_playlists.md)
- [Using TinyURL for Short Links](25_tinyurl_short_links.md)

### Images

- image36.png - Google Cloud Console - New Project dropdown
- image22.png - Google Cloud Console - New project creation
- image42.png, image5.png, image28.png - Enable Drive API screens
- image43.png, image23.png - OAuth Consent Screen
- image31.png, image38.png - Scopes selection
- image19.png - Publish App button
- image35.png, image34.png - Credentials screens
- image27.png - OAuth client - TVs and Limited Input devices

---

## Configure in IPTVBoss

1. **Open IPTVBoss**

2. **Go to Settings**:
   - Menu → **Settings → IPTVBoss Settings**

3. **Enable Cloud Sync**:
   - At the top, check **"Cloud Sync Enabled"**

4. **Select Google Drive**:
   - In **"Cloud Provider"** dropdown, select **"Google Drive"**

5. **Enter Credentials**:
   - Paste your **Client ID**
   - Paste your **Client Secret**

6. **Authorize**:
   - Click **"Authorize"** button
   - A dialog appears with instructions
   - Boss opens your web browser
   - Google authorization page loads
   - **Log in** to Google (the account you added as test user)
   - **Grant permissions** to the app
   - Google provides an authorization code
   - **Copy** the authorization code
   - Return to IPTVBoss dialog
   - **Paste** the code
   - Click **"OK"**

7. **Save**:
   - Click **"OK"** to save IPTVBoss settings

**Visual Reference**: [IPTVBoss 3.5 User Manual\images\image25.png](../../IPTVBoss 3.5 User Manual/images/image25.png)

### 10. Verify Setup

1. **Output a test layout**:
   - Go to **Output → Output Current Layout**
   - Wait for output to complete

2. **Check Google Drive**:
   - Go to [https://drive.google.com](https://drive.google.com)
   - Files may appear in a hidden "Application Data" folder (not directly visible)
   - This is normal - IPTVBoss can access them via API

3. **Get URLs**:
   - In IPTVBoss, click **"View Cloud Links"**
   - Your Google Drive URLs should appear
   - **IMPORTANT**: Use the **.gz** EPG link, NOT the .xml link

### Google Drive .gz Requirement

**Why .gz is required**:
- Google Drive API has limitations on serving XML files directly
- Compressed .gz format works reliably
- Most modern IPTV players support .gz EPG files

**How to enable**:
1. Layout → Layout Manager
2. Select your layout
3. Enable **"Upload Zipped XML (GZ)"** checkbox
4. Save layout
5. Output layout
6. Use the .gz URL in your player apps

**Players that support .gz**:
- TiviMate ✓
- Implayer ✓
- IPTV Smarters ✓
- Perfect Player ✓
- Most modern players ✓

### Bandwidth Considerations

**Free Google Drive**:
- Typically more generous bandwidth than free Dropbox
- 15GB storage (shared with Gmail and Photos)
- Bandwidth limits exist but are generally higher
- Good for personal to medium use (5-20 users)

**If you exceed limits**:
- Use Universal EPG (reduces bandwidth significantly)
- Use .gz format (already required, but also saves bandwidth)
- Exclude VOD if not needed
- Consider paid Google One plan for more bandwidth

---

### Related Topics

- [Understanding Cloud Storage Options](24_cloud_storage_overview.md)
- [Dropbox Setup](24a_dropbox_setup_detailed.md)
- [Outputting Playlists for Players](23_outputting_layouts_or_playlists.md)
- [Using TinyURL for Short Links](25_tinyurl_short_links.md)

### Images

- image25.png - IPTVBoss settings - Google Drive configuration

---

## Troubleshooting

### "App isn't verified" Warning

**When you see this**:
- During authorization, Google may show "This app isn't verified"

**Solution**:
- Click **"Advanced"**
- Click **"Go to [Your App Name] (unsafe)"**
- This is safe - it's YOUR app, Google just hasn't verified it
- This warning is normal for personal-use apps

### Authorization Fails

**Solutions**:
- Verify Client ID and Client Secret are correct (no extra spaces)
- Make sure app is Published (not in Testing mode)
- Check that you're authorizing with the Google account added as Test User
- Verify Google Drive API is enabled for your project

### Files Not Uploading

**Solutions**:
- Check **"Cloud Sync Enabled"** is checked in IPTVBoss Settings
- Verify authorization is still valid (try re-authorizing)
- Check internet connection
- Ensure you enabled the correct scopes (`drive.appdata` and `drive.file`)
- Check **Logs → View Logs** for upload errors

### EPG Not Working in Player

**Most common cause**: Using .xml URL instead of .gz URL

**Solution**:
1. Check Layout Manager → Your layout → "Upload Zipped XML (GZ)" is enabled
2. Re-output layout
3. View Cloud Links
4. Copy the **.gz** URL (not .xml)
5. Update your player with the .gz URL

### Token Expired After 7 Days

**Cause**: App is still in "Testing" mode, not Published

**Solution**:
1. Go back to Google Cloud Console
2. OAuth Consent Screen
3. Click **"Publish App"**
4. Re-authorize in IPTVBoss

### Reauthorization

You may need to reauthorize periodically:

**When**:
- After major OS updates
- After reinstalling IPTVBoss
- If uploads suddenly fail

**How**:
1. Settings → IPTVBoss Settings
2. Click **"Authorize"** button again
3. Follow the same authorization steps
4. Your files and settings remain intact

---

### Related Topics

- [Understanding Cloud Storage Options](24_cloud_storage_overview.md)
- [Dropbox Setup](24a_dropbox_setup_detailed.md)
- [Outputting Playlists for Players](23_outputting_layouts_or_playlists.md)
- [Using TinyURL for Short Links](25_tinyurl_short_links.md)
