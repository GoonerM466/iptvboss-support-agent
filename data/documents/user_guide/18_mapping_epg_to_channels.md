# Mapping EPG to Channels


EPG (Electronic Program Guide) shows what's playing now and upcoming programs. IPTVBoss matches your channels to EPG sources.


**Visual References**:
- [image18](https://goonerm466.github.io/iptvboss-support-agent/images/image18.png) - Channel list showing highlighted channels with missing EPG mappings ready for auto-mapping
- [image32](https://goonerm466.github.io/iptvboss-support-agent/images/image32.png) - Search Options dialog showing checkboxes for different EPG guides (US, UK, Can) to enable/disable for mapping
- [image7](https://goonerm466.github.io/iptvboss-support-agent/images/image7.png) - Channel Editor showing EPG Assignment section with Auto and Manual buttons and EPG sensitivity settings
**Why mapping is needed**: Your provider's channel names rarely match EPG source channel names exactly. Boss tries auto-matching but sometimes needs manual help.

### Prerequisites

- Boss Pro license (EPG features require Pro)
- EPG sources loaded (Boss Pro includes many built-in)

### Auto-mapping (easiest)

**Load EPG sources**:
- Sources → Sources Manager
- Add EPG sources you need (US, UK, Sports, etc.)
- Boss Pro includes extensive EPG library

**Auto-map channels**:
- Select layout
- Select group or all channels
- Right-click → Auto Map EPG
- Boss attempts intelligent matching
- Review results - may not be 100% accurate

**Verify and fix**:
- Check channels with "Open EPG"
- If EPG is wrong or missing, manually map

### Manual mapping (for accuracy)

**Select channel**:
- In layout view, click channel needing EPG

**Open EPG mapping**:
- Channel options → EPG Mapping
- or right-click → Map EPG

**Search for EPG channel**:
- Type channel name (e.g., "ESPN")
- Browse results
- Match your channel to correct EPG entry

**Assign**:
- Select correct EPG channel
- Click Assign/OK
- Save changes

**Verify**:
- Right-click channel → Open EPG
- Check guide data appears
- Verify it's correct program info

### Best practices

- Map major channels manually for accuracy
- Use auto-map for bulk of channels, then manually fix important ones
- Check EPG after mapping before outputting
- Sport channels need sports EPG sources
- Movie channels need movie EPG sources

### Common issues

- EPG shows briefly then disappears: Check "Days to Keep" settings (see Troubleshooting)
- Wrong program info: Mapped to wrong EPG channel, remap
- No EPG at all: Source not enabled, or channel has no EPG in sources

---

### Related Topics

- [Previous: Import Channels From Layouts Dialog](17_import_from_layouts_dialog.md)
- [Next: Using Universal EPG](19_universal_epg.md)
