# Setting Up XC Server as Windows Service


**Visual References**:
- [image3](https://goonerm466.github.io/iptvboss-support-agent/images/image3.png) - Windows Task Scheduler showing basic settings for creating a task to auto-start IPTVBoss XC Server
- [image39](https://goonerm466.github.io/iptvboss-support-agent/images/image39.png) - Windows Task Scheduler Actions tab showing program/script and arguments configuration for starting XC Server
**Setting Up as Windows Service**:

Using Task Scheduler (recommended for Windows):

1. Open Task Scheduler
2. Create new task
3. **Program/Script**: `C:\Windows\System32\cmd.exe`
4. **Add arguments**: `/C iptvboss-c -xcserver`
5. **Trigger**: At startup (or your preference)
6. **Settings**: Run whether user is logged in or not

Visual references: [image42](https://goonerm466.github.io/iptvboss-support-agent/images/image42.png), [image43](https://goonerm466.github.io/iptvboss-support-agent/images/image43.png)

---

### Related Topics

- [Previous: IPTVBoss XC Server - Overview and Setup](33_xc_server_overview.md)
- [Next: Setting Up XC Server as Ubuntu/Linux Service](35_xc_server_linux_service.md)
