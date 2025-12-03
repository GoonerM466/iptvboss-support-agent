# Dropbox Setup - Detailed Guide

Complete step-by-step instructions for setting up Dropbox as your cloud storage provider.


**Visual References**:
- [image11](https://goonerm466.github.io/iptvboss-support-agent/images/image11.png) - Dropbox developer page showing 'Create an App' button
- [image33](https://goonerm466.github.io/iptvboss-support-agent/images/image33.png) - Dropbox app creation dialog with options for Scoped Access, App Folder, and naming the app
- [image14](https://goonerm466.github.io/iptvboss-support-agent/images/image14.png) - Dropbox app permissions tab showing required permissions for IPTVBoss
- [image12](https://goonerm466.github.io/iptvboss-support-agent/images/image12.png) - IPTVBoss settings dialog showing Dropbox cloud provider configuration with App Key and App Secret fields
**Video Tutorial**: https://youtu.be/2cfEEqFYHrc

---

### Prerequisites

- Dropbox account (free tier works for personal use)
- IPTVBoss installed

---

### Setup Steps

### 1. Create Dropbox Account

If you don't already have one:
- Visit [https://www.dropbox.com/basic](https://www.dropbox.com/basic)
- Sign up for free account

### 2. Create Dropbox App

1. Go to [https://www.dropbox.com/developers](https://www.dropbox.com/developers)
2. Click **"Create an App"**
3. Choose settings:
   - Select **"Scoped Access"**
   - Select **"App Folder"**
   - **Name your App** (this will be the folder name inside your Dropbox/Apps folder)
     - Example: "IPTVBoss_Storage"
     - This folder will contain all your outputted M3U/EPG files
4. Click **"Create"**


### 3. Set App Permissions

1. In your app settings page, click the **"Permissions"** tab
2. Enable the following permissions:
   - `files.metadata.write`
   - `files.metadata.read`
   - `files.content.write`
   - `files.content.read`
3. Click **"Submit"** button at bottom


**Important**: You must click Submit after enabling permissions, or they won't be saved.

### 4. Get App Credentials

1. Stay on your Dropbox app settings page
2. Click the **"Settings"** tab (if not already there)
3. Scroll down to find:
   - **App Key**
   - **App Secret**
4. Keep this page open - you'll need these in the next step

---

### Related Topics

- [Understanding Cloud Storage Options](24_cloud_storage_overview.md)
- [Google Drive Setup](24b_google_drive_setup_detailed.md)
- [Outputting Playlists for Players](23_outputting_layouts_or_playlists.md)
- [Using TinyURL for Short Links](25_tinyurl_short_links.md)


- image11.png - Dropbox developer page - Create an App button
- image33.png - Dropbox app creation - Scoped Access, App Folder options
- image14.png - Dropbox app permissions tab

---

## Configure in IPTVBoss

1. **Open IPTVBoss**

2. **Go to Settings**:
   - Menu → **Settings → IPTVBoss Settings**

3. **Select Dropbox**:
   - In the **"Cloud Provider"** dropdown, select **"Dropbox"**

4. **Enter Credentials**:
   - Paste your **App Key** into the App Key field
   - Paste your **App Secret** into the App Secret field

5. **Authorize**:
   - Click the **"Authorize"** button
   - A dialog appears with instructions:
     - Boss opens your web browser
     - Dropbox authorization page loads
     - Click **"Allow"** to authorize the app
     - Dropbox provides an authorization code
     - Copy the authorization code
     - Return to IPTVBoss
     - Paste the code into the dialog
     - Click **"OK"**

6. **Enable Cloud Sync**:
   - At the top of IPTVBoss Settings, check **"Cloud Sync Enabled"**
   - This must be enabled for files to upload

7. **Save Settings**:
   - Click **"OK"** to save


### 6. Verify Setup

1. Output a test layout:
   - Go to **Output → Output Current Layout** (or create a test layout first)
   - Wait for output to complete

2. Check Dropbox:
   - Log into Dropbox website
   - Navigate to **Apps → [Your App Name]**
   - You should see your M3U and EPG files uploaded

3. Get URLs:
   - In IPTVBoss, click **"View Cloud Links"**
   - Your Dropbox URLs should appear
   - These are the URLs you'll use in player apps

### Bandwidth Considerations

**Free Dropbox Account**:
- ~20GB/month bandwidth
- Sufficient for personal use (1-5 devices)
- 40-50 users may exceed bandwidth limits
- Files still accessible, but downloads may be rate-limited

**If you exceed bandwidth**:
- Consider Google Drive (often more generous)
- Upgrade to Dropbox paid tier
- Use Universal EPG to reduce bandwidth
- Use .gz format instead of raw XML
- Exclude VOD if not needed

---

### Related Topics

- [Understanding Cloud Storage Options](24_cloud_storage_overview.md)
- [Google Drive Setup](24b_google_drive_setup_detailed.md)
- [Outputting Playlists for Players](23_outputting_layouts_or_playlists.md)
- [Using TinyURL for Short Links](25_tinyurl_short_links.md)


- image12.png - IPTVBoss settings - Dropbox configuration

---

## Troubleshooting

### Authorization Fails

**Symptoms**: "Authorization failed" or "Invalid code"

**Solutions**:
- Verify App Key and App Secret are correct (no extra spaces)
- Make sure you clicked "Submit" after enabling permissions
- Check that you're authorizing with the same Dropbox account that created the app
- Try regenerating App Secret in Dropbox developer settings

### Files Not Uploading

**Symptoms**: Output completes but no files in Dropbox

**Solutions**:
- Check **"Cloud Sync Enabled"** is checked in IPTVBoss Settings
- Verify authorization is still valid (try re-authorizing)
- Check internet connection
- Check Dropbox status page for service issues
- Look in **Logs → View Logs** for upload errors

### "Token Expired" Error

**Solution**:
- OAuth tokens can expire after OS upgrades or IPTVBoss updates
- Simply re-authorize using the same steps as initial setup
- Your files and settings remain intact

### Files Upload But URLs Don't Work

**Solution**:
- Make sure you're using the links from **"View Cloud Links"** in IPTVBoss
- Don't try to create Dropbox links manually - IPTVBoss generates special API links
- Try re-outputting to regenerate URLs

### Reauthorization

You may need to reauthorize Dropbox periodically:

**When**:
- After major OS updates
- After reinstalling IPTVBoss
- If uploads suddenly fail
- Every 6-12 months (tokens expire)

**How**:
1. Settings → IPTVBoss Settings
2. Click **"Authorize"** button again
3. Follow the same authorization steps
4. Your files and history remain intact

---

### Related Topics

- [Understanding Cloud Storage Options](24_cloud_storage_overview.md)
- [Google Drive Setup](24b_google_drive_setup_detailed.md)
- [Outputting Playlists for Players](23_outputting_layouts_or_playlists.md)
- [Using TinyURL for Short Links](25_tinyurl_short_links.md)
