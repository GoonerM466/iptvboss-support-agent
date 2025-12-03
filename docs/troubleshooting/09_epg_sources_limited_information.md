# Specific EPG Sources Show Limited or No Information

Some EPG sources (especially USA, USA Local) show limited guide data.

### Problem

Certain EPG sources display minimal or no program guide information.

### Symptoms

- USA and USA Local EPG show only couple hours then "no information"
- EPG works for first program then goes blank
- Some channels have EPG, others don't despite mapping
- EPG in Boss shows data but player shows none (or vice versa)
- Guide data progressively disappears

### Why This Happens

"Days to Keep" set too low or to 0 at source, layout, or override level. EPG cache corruption. Conflicting EPG source configurations. TiviMate using cached data from different source than you expect.

### Solution

**Step 1: Check Days to Keep settings** (multiple places!)

**1. Source level:**
- Go to **Sources ’ Sources Manager**
- Highlight your EPG source
- Click **EPG Settings**
- Check **"Days to Keep"** for EPG
- Default is **3 days**
- Should be **7 days** or **ALL** for best results
- Setting to **0** or very low (1-2) causes this issue

**2. Channel-specific overrides** (if EPG Override enabled):
- Some channels may have specific EPG overrides set
- Check individual channel EPG override settings
- Remove overrides causing issues

**Step 2: EPG cache fix**

1. Shut down IPTVBoss completely
2. Navigate to `IPTVBoss/cache` folder
3. Find and delete files for problematic EPG sources:
   - USA.xml or USA.gz
   - USA_Local.xml or USA_Local.gz
   - Any other problematic source files
4. Start IPTVBoss
5. Sync all EPGs (Sources ’ Sync All EPGs)
6. Output and test

**Step 3: Player cache check**

If EPG shows in Boss but not in player:
- Player may be using cached data
- Add playlist completely fresh in player
- Remove old playlist first
- This tests if player cache is the issue

If EPG doesn't show in Boss but shows in player:
- Player is using cached EPG from before
- Or player is using different EPG source
- Player will eventually lose data when cache expires

### Prevention

- Set "Days to Keep" to **7 days** or **ALL** at source level
- Default is only 3 days - increase for better EPG coverage
- Check channel-specific overrides if EPG Override is enabled
- Periodically clear EPG cache if issues recur

### For Universal EPG Users

- These settings apply to Universal EPG too
- Check Universal EPG days to keep settings
- Same cache clearing process works

### Known Limitations

- USA EPG sources particularly affected (provider issue?)
- Override hierarchy not always clear to users
- Cache location not well documented in official docs

### Related Topics

- [Specific EPG Sources Show No Info](../faq/13_specific_epg_sources_no_info_hours.md)
- [Multiple Layouts Only First Has Guide](../faq/12_multiple_layouts_only_first_has_guide.md)
- [EPG No Info in Boss But TiviMate Works](../faq/08_epg_no_info_boss_but_tivimate_works.md)
