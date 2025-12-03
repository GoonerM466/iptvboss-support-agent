# Managing EPG Sources

Boss Pro includes many built-in EPG sources. You enable what you need.


**Visual Reference**: [image6](https://goonerm466.github.io/iptvboss-support-agent/images/image6.png) - Add EPG dialog showing EPG source dropdown with built-in guide options
### Available sources

- US: US channels (networks, cable, etc.)
- UK: UK channels (networks, cable, etc.)
- International Sports: Comprehensive sports EPG
- Many others (By region)

### Enabling sources

**Access EPG sources**:
- Sources → Sources Manager
- Click "Add EPG" to add EPG sources

**Enable needed sources**:
- Add only sources you need
- Don't enable everything - only what you actually use
- More sources = slower sync, more bandwidth

**Sync EPG**:
- Sources → Sync All EPGs
- Downloads current EPG data
- Takes 1-15 minutes depending on sources enabled

**Set sync schedule**:
- Configure via automation (Task Scheduler/cron)
- Automatic daily syncs recommended
- 1-2x daily is typical

### External EPG sources

- You can add external EPG XML files if needed
- Sources → Sources Manager → Add EPG
- Provide URL to EPG XML file
- Less common - built-in sources usually sufficient

---

### Related Topics

- [Previous: Using Universal EPG](19_universal_epg.md)
- [Next: Customizing EPG Layout (Advanced)](21_customizing_epg_layout.md)
