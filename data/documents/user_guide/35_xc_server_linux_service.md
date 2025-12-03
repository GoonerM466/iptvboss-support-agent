# Setting Up XC Server as Ubuntu/Linux Service

**Setting Up as Ubuntu Service**:

This guide uses Ubuntu 23.04 (similar for other Linux):

1. **Setup IPTVBoss normally first**
   - Run nogui sync after installation to build EPG files

2. **Create service file**:
   ```bash
   sudo nano /etc/systemd/system/iptvboss.service
   ```

3. **Add service configuration**:
   ```
   [Unit]
   Description=IPTVBoss
   After=network.target
   StartLimitIntervalSec=0

   [Service]
   Type=simple
   Restart=always
   RestartSec=10
   User=ubuntu
   ExecStart=/usr/bin/iptvboss -xcserver

   [Install]
   WantedBy=multi-user.target
   ```

   - Change `User=ubuntu` to your username
   - Memory settings can be adjusted based on your needs

4. **Save and exit**:
   - Press `Ctrl+X`
   - Press `Y` to save
   - Press `Enter`

5. **Reload systemctl**:
   ```bash
   sudo systemctl daemon-reload
   ```

6. **Enable and start service**:
   ```bash
   sudo systemctl enable iptvboss
   sudo systemctl start iptvboss
   ```

7. **Check status**:
   ```bash
   sudo systemctl status iptvboss
   ```

---

### Related Topics

- [Previous: Setting Up XC Server as Windows Service](34_xc_server_windows_service.md)
- [Next: XC Server Troubleshooting and Comparison](36_xc_server_troubleshooting.md)
