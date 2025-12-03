# Using Universal EPG

Universal EPG generates ONE EPG file for all your layouts. Much more efficient than individual EPGs per layout.

### Benefits

- Saves cloud storage bandwidth (massive)
- One EPG to update instead of many
- Simpler management
- Recommended for multiple layouts

### Setup

**Enable Universal EPG**:
- Sources → Universal EPG Options
- Enable it
- Configure retention (7-14 days recommended)

**Map channels** (same as normal EPG mapping):
- Mappings automatically go into Universal EPG
- All layouts share the same EPG mappings

**Output**:
- When outputting layouts, Boss uses Universal EPG automatically
- One EPG file serves all layouts

### vs Individual EPG

- Individual: Each layout has separate EPG file, separate mappings
- Universal: One EPG file, shared mappings across layouts

### When to use Individual EPG

- Different EPG sources for different layouts (rare need)
- Each layout needs completely different EPG retention settings

### When to use Universal (recommended)

- Multiple layouts
- Want to minimize bandwidth
- Easier management

---

### Related Topics

- [Previous: Mapping EPG to Channels](18_mapping_epg_to_channels.md)
- [Next: Managing EPG Sources](20_managing_epg_sources_full.md)
