# IPTVBoss XC Server - Overview and Setup

The IPTVBoss XC Server delivers streams and EPG to players using XC API instead of traditional M3U and XML files.


**Visual References**:
- [image40](https://goonerm466.github.io/iptvboss-support-agent/images/image40.png) - XC Server Settings dialog showing server configuration options including URL, port, sync times, and XC enable options
- [image41](https://goonerm466.github.io/iptvboss-support-agent/images/image41.png) - XC Server web interface showing server log and control buttons (Stop/Reload) for headless operation
- [image4](https://goonerm466.github.io/iptvboss-support-agent/images/image4.png) - XC User Links dialog showing list of users with their XC API login credentials and URLs
**What is XC Server**:
- Built-in server that runs alongside or instead of traditional file-based output
- Uses IPTVBoss databases to feed players with channel lineups and EPG
- Players connect via XC API protocol instead of M3U/XML URLs
- Alternative distribution method for advanced users

**When to use XC Server**:
- You want XC API-style delivery instead of files
- Players support XC API connections
- You need server-based delivery with API endpoints
- Advanced server setups (headless systems, always-on servers)

**Prerequisites**:
- **Universal EPG must be enabled** (required for XC Server)
- Understanding of server operation
- System that can run IPTVBoss continuously (or scheduled)

**Setup XC Server Settings**:

1. **Enable Universal EPG First** (Required!)
   - Go to **Sources → Universal EPG Options**
   - Enable Universal EPG
   - XC Server requires this

2. **Configure XC Server**
   - Go to **Settings → XC Server Settings**
   - Enable XC Server (checkbox at top)

3. **Set Server URL and Port**
   - Enter **Server URL** (this will be in the XC JSONs created)
   - Enter **Server Port**
   - Important: These values must be working/accessible URLs
   - If using reverse proxy for SSL, port may not be needed in URL

4. **Configure M3U Support** (Optional)
   - Enable "Support M3U Downloading" if you want server to deliver M3U files
   - Choose Sync Method for M3U delivery

5. **Set Update Interval**
   - How often XC Server checks for IPTVBoss updates
   - Recommended: 30 minutes minimum
   - Don't set too low (causes excessive resource use)

6. **Manual Sync Options**
   - View XC API Key: Gives API key for web-based log/command access
   - Don't share this key (provides server control)

7. **Sync Times**
   - Set specific times for XC server to run nogui syncs
   - Server will launch nogui instance of IPTVBoss at these times

8. **Enable XC for Layouts**
   - In Layout Manager, each layout has "XC Enabled" option
   - Enable for layouts you want available via XC Server

9. **Build Programmes Database**
   - Complete an EPG Output to build the programmes database
   - This database feeds EPG info to XC API clients (non-XML players)

**Testing XC Server**:

From GUI:
- Click **"Start Testing Server"** button (in XC Server Settings)
- Starts XC server from within IPTVBoss GUI
- For testing only
- Should function from localhost

**Running XC Server** (Production):

**Windows**:
```
IPTVBoss -xcserver
```

With console output:
```
IPTVBoss-c -xcserver
```

**Linux/Mac**:
```
iptvboss -xcserver
```

**Server Commands** (while running):

Once started, two commands are available:
1. **Stop** - Shuts down the server
2. **Reload** - Forces reload of server and update of all files

**Remote Access** (Headless/Service):

If running as service or headless, access log and commands via web endpoint:

```
{serverurl}:{serverport}/boss.php?apikey={api-key}
```

This page shows:
- Server log
- Links for Stopping and Reloading server
- Visual reference: [image40](https://goonerm466.github.io/iptvboss-support-agent/images/image40.png)

**User Links for XC**:

View XC login credentials for users:
- Go to Layout Manager (layouts pane)
- Click **"View XC Login"** button
- Shows XC credentials for all users
- Click user to copy link to clipboard
- Visual reference: [image41](https://goonerm466.github.io/iptvboss-support-agent/images/image41.png)

---

### Related Topics

- [Previous: Managing Multiple Users](32_managing_multiple_users.md)
- [Next: Setting Up XC Server as Windows Service](34_xc_server_windows_service.md)
