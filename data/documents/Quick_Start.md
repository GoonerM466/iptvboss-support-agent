# Quick Start Guide

Get IPTVBoss/EPGBoss working in 10-15 minutes. This guide covers essential setup only.

**Already set up?** See [User Guide](User_Guide.md) for advanced features.

---

## Prerequisites

- Valid IPTV service subscription (with M3U URL or XC API credentials)
- Boss Pro license (for EPG features)
- Cloud storage account (Dropbox or Google Drive)
- TinyURL account (free, for short URLs)

---

## Step 1: Install and Activate (2 minutes)

1. **Download IPTVBoss** from official website
2. **Install** following prompts for your OS
3. **Launch** IPTVBoss
4. **Activate Pro**:
   - Menu → Activate Pro
   - Enter your Pro license key
   - Wait for validation (may take 1-2 minutes)
   - Confirm "Pro Active" status

**Important**: Activate Pro before proceeding. Many features require it.

---

## Step 2: Add Your IPTV Source (3 minutes)

**If you have M3U URL**:
1. Copy your provider's M3U URL
2. IPTVBoss → Sources → Sources Manager
3. Select "M3U URL"
4. Paste URL, enter username/password if required
5. Click "Load" and wait for channels to import

**If you have XC API credentials** (recommended):
1. Get server URL, username, and password from provider
2. IPTVBoss → Sources → Sources Manager
3. Select "XC API"
4. Enter server, username, password
5. Click "Load"

**Troubleshooting**: If you get "Could not load categories" error, verify your credentials are correct and service is active.

---

## Step 3: Set Up Cloud Storage (10-15 minutes)

You need cloud storage to share playlists with your player apps.

**Choose Dropbox OR Google Drive:**

### Option A: Dropbox Setup

**Video Tutorial**: https://youtu.be/2cfEEqFYHrc

**Written Steps**:

1. **Create Dropbox Account** (if you don't have one)
   - Visit [https://www.dropbox.com/basic](https://www.dropbox.com/basic)
   - Sign up for free account

2. **Create Dropbox App**
   - Go to [https://www.dropbox.com/developers](https://www.dropbox.com/developers)
   - Click **"Create an App"**
   - Choose settings:
     1. **Scoped Access**
     2. **App Folder**
     3. **Name your App** (this will be the folder name inside your Dropbox/Apps folder)
   - Click Create

3. **Set App Permissions**
   - In your app settings, click the **Permissions** tab
   - Enable required permissions (see image references in manual - [IPTVBoss 3.5 User Manual\images\image5.png](../IPTVBoss 3.5 User Manual/images/image5.png))
   - Click **Submit**

4. **Get App Credentials**
   - Stay on your Dropbox app settings page
   - Note your **App Key** and **App Secret** (you'll need these next)

5. **Configure in IPTVBoss**
   - Open IPTVBoss
   - Go to **Settings → IPTVBoss Settings**
   - Select **"Dropbox"** as your Cloud Provider
   - Enter your **App Key** and **App Secret**
   - Click **"Authorize"**
   - Follow the instructions in the dialog:
     - Opens web browser
     - Authorize the app in Dropbox
     - Copy the authorization code
     - Return to IPTVBoss and paste code
   - Select **"Cloud Sync Enabled"** at the top
   - Click **OK**

**Note**: Free Dropbox works for personal use (1-5 devices). For more users, consider Google Drive or Dropbox paid tier.

### Option B: Google Drive Setup

**Video Tutorial**: https://youtu.be/A45N6Vgk-OU

**⚠️ Important**: You **must use the .gz EPG link** with Google Drive, NOT .xml

**Written Steps**:

1. **Access Google Cloud Console**
   - Log in to your Google Account
   - Go to [https://console.developers.google.com/](https://console.developers.google.com/)

2. **Create New Project**
   - Click the dropdown next to "Google APIs"
   - Select **"New Project"**
   - Give your project a name
   - Click **"Create"**

3. **Enable Google Drive API**
   - Make sure your new project is selected (check dropdown)
   - Click **"+ ENABLE APIS AND SERVICES"**
   - Search for **"drive"**
   - Select **"Google Drive API"**
   - Click **"Enable"**

4. **Configure OAuth Consent Screen**
   - Select **"OAuth Consent Screen"** on left sidebar
   - Select **"External"**
   - Click **"Create"**
   - Fill in required fields:
     - App Name
     - User support email
   - Skip optional fields
   - Click **"Save and Continue"**

5. **Add Scopes**
   - On the Scopes page, click **"Add or Remove Scopes"**
   - Enable these two scopes:
     - `drive.appdata`
     - `drive.file`
   - Click **"Update"**
   - Click **"Save and Continue"**

6. **Add Test Users**
   - On Test Users page, click **"Add User"**
   - Add your own email address
   - Click **"Save and Continue"**
   - Click **"Back to Dashboard"**

7. **Publish App** (Important!)
   - Click **"Publish App"**
   - Click **"Confirm"**
   - **Why**: If left in "Testing", tokens expire after 7 days

8. **Create OAuth Credentials**
   - Click **"Credentials"** on left sidebar
   - Click **"Create Credentials"** at top
   - Select **"OAuth client ID"**
   - In Application type dropdown, select **"TVs and Limited Input devices"**
   - Click **"Create"**
   - Note your **Client ID** and **Client Secret**

9. **Configure in IPTVBoss**
   - Open IPTVBoss
   - Go to **Settings → IPTVBoss Settings**
   - Select **"Cloud Sync Enabled"**
   - From Cloud Provider dropdown, select **"Google Drive"**
   - Enter your **Client ID** and **Client Secret**
   - Click **"Authorize"**
   - Follow directions in the pop-up:
     - Opens browser to Google authorization
     - Log in and grant permissions
     - Copy authorization code
     - Return to IPTVBoss
   - Click **OK**

---

## Step 4: Set Up TinyURL *Optional* (2 minutes)

TinyURL creates short URLs for easy playlist sharing.

1. **Create TinyURL account**:
   - Go to tinyurl.com
   - Sign up for free account

2. **Generate API key**:
   - Log into TinyURL
   - Go to API settings
   - Create API key with all permissions

3. **Configure in IPTVBoss**:
   - Settings → TinyURL
   - Paste API key
   - Save

**Skip this?**: You can use direct Dropbox/Google Drive URLs instead, but they're very long.

---

## Step 5: Create a Basic Layout (5 minutes)

Layouts organize your channels. Start with a simple one.
You can watch the video "My First Layout" to help guide you: https://youtu.be/gfw0RLfSAnI

1. **Create Layout**:
   - IPTVBoss → Layout → Layout Manager (click "+" to create new)
   - Name it (e.g., "Home", "Main")

2. **Add Channels**:
   - Select your layout
   - Click "Add Channels"
   - Select channels from your source
   - Choose groups/categories to add
   - Click "Add to Layout"

3. **Assing EPG**
   - Select a channel or channels
   - Select only the EPG region for the channel yo uare mapping in Search Options
   - Click Auto
   
4. **Organize** (optional):
   - Drag channels between groups
   - Rename groups for clarity
   - Delete unwanted channels/groups

**Tip**: Start small - add 20-30 favorite channels. You can always add more later.
You can also import everyting by using the "Import Source" button!

---

## Step 6: Output and Use in Player (3 minutes)

Now generate files for your player app.

1. **Output Files**:
   - Layout Manager → Output Current Layout M3U and EPG
   - Wait for completion (progress bar)
   - Files upload to your cloud storage

2. **Get URLs**:
   - Click "View Cloud Links"
   - Copy M3U URL and EPG URL
   - (TinyURL short URLs if configured)

3. **Add to Player** (TiviMate example):
   - Open TiviMate
   - Settings → Playlists → Add Playlist
   - Paste M3U URL
   - Paste EPG URL (in EPG section)
   - Click "Add"
   - Wait for import

4. **Verify**:
   - Check channels appear in TiviMate
   - Select channel and verify EPG (guide) shows

**Done!** You now have IPTVBoss managing your IPTV service.

---

## Common Gotchas

### Changes Don't Show in Player

**Remember the workflow**:
1. Make changes in IPTVBoss
2. Output layout (Layout Manager → Output)
3. Update playlist in player (TiviMate: Settings → Playlists → Update)

Changes don't auto-sync. You must output → update.

### No EPG Data

**Check**:
- Did you add Boss Pro EPG sources? (**Sources → Add EPG**)
- Did you sync EPGs? (**Sources → Sync All EPGs**)
- Did you map channels to EPG? (Channel Options panel in Layout Editor)
- Did you output after mapping? (**Output → Current M3U & EPG**)
- Check "Days to Keep": **Sources → Sources Manager** → Highlight EPG → **EPG Settings**
  - Default is **3 days** - increase to **7 days** or **ALL**

### TinyURL Not Working

**Most common**: API key not entered or incorrect.
- Settings → TinyURL → Verify API key entered
- Try deleting cloud files and re-outputting

---

## Next Steps

**Essential setup complete!** Now learn more:

- **[User Guide](User_Guide.md)** - EPG mapping, advanced layouts, automation, "noGUI" syncs
- **[FAQ](FAQ.md)** - Common questions answered
- **[Troubleshooting](Troubleshooting_Guide.md)** - Fix problems when they occur

**Key concepts to learn**:
- EPG mapping (assigning guide data to channels)
- Multiple layouts (different channel lists for different users)
- Automatic syncing (NoGUI for EPG updates)
- User system (manage multiple users)

---

## Pro Tips

1. **Backup regularly**: Menu → Backup (keeps you safe from disasters)
2. **Use XC API**: More stable than M3U URLs if provider offers it
3. **Universal EPG**: Sources → Universal EPG Options (easier than individual EPGs)
4. **Start simple**: Master basics before exploring advanced features
5. **Join Discord**: Community support is excellent

---

## Need Help?

- **Discord Support Channel** - Fastest help, friendly community
- **[FAQ](FAQ.md)** - Answers to common questions
- **[Troubleshooting Guide](Troubleshooting_Guide.md)** - Fix common problems
- **YouTube Tutorials** - Visual guides for setup

**Before asking for help**:
- Check FAQ and Troubleshooting Guide first
- Include logs if you have errors (IPTVBoss/logs folder)
- Clean sensitive info from logs (provider names, URLs, credentials)
