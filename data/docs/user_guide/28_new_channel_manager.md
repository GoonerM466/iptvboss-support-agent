# New Channel Manager (Automatic Channel Imports)

The New Channel Manager controls how new channels added by your provider are automatically imported into your layouts.

**What it does**:
- When providers add new channels to enabled categories
- IPTVBoss can automatically add them to your Layout Groups
- Saves manual work of constantly checking for new channels
- Ensures you don't miss new content from your provider

**Access New Channel Manager**:
- **Layout → New Channel Manager**
- Or from Layout Editor toolbar (may appear as button)

**How it works**:

When you import channels directly from a source, IPTVBoss automatically creates links between:
- **Provider Categories** (source groups)
- **Layout Groups** (your custom groups)

When the provider adds channels to those categories, they automatically appear in your linked Layout Groups.

**Managing Category Links**:

1. **Select Layout Group** (left side)
   - Choose which Layout Group you want to configure

2. **View Included Categories** (right side)
   - Shows which provider categories feed into this group
   - These are the "Included Categories"

3. **Add Category Links**:
   - Drag provider categories from Categories list into "Included Categories"
   - New channels from those categories will auto-import to this Layout Group

4. **Remove Category Links**:
   - Drag category out of "Included Categories"
   - Or right-click and remove
   - Stops automatic imports from that category

**Use Cases**:

**Scenario 1: Keep Sports Group Updated**
- You have a "Sports" Layout Group
- Link it to provider categories: "Sports", "ESPN Channels", "NFL Network"
- When provider adds new sports channels, they automatically appear in your Sports group

**Scenario 2: Kids Safe Playlist**
- Create "Kids" Layout Group
- Link only to "Kids", "Cartoons", "Family" provider categories
- New family-friendly channels auto-import
- Adult categories are NOT linked, so stay out

**Scenario 3: International Channels**
- "Spanish Channels" Layout Group
- Link to "Spanish", "Latin America", "Spain" provider categories
- New Spanish channels auto-add

**Best Practices**:

1. **Review New Channels Periodically**:
   - Auto-import adds channels, but doesn't map EPG
   - Check new channels and map EPG as needed

2. **Use Selective Linking**:
   - Don't link every category to every group
   - Be intentional about which categories feed which groups

3. **Combine with Source Settings**:
   - In Source Manager, you can enable "Automatically Enable New Groups Added by Provider"
   - This works with New Channel Manager for complete automation

4. **Test Before Outputting**:
   - After provider adds channels, open Layout Editor
   - Verify new channels appear where expected
   - Map EPG, adjust channel order, etc.
   - Then output to players

**Troubleshooting**:

**New channels not appearing**:
- Check category is in "Included Categories" for the Layout Group
- Verify category is enabled in Source Manager
- Check source sync completed successfully

**Wrong channels appearing**:
- Provider may have reorganized categories
- Review Included Categories links
- Remove unwanted category links

**Too many channels auto-importing**:
- Be more selective with category links
- Use "Don't Import Duplicate Channels" in import settings
- Consider manual channel management for complex setups

**Visual Reference**: [IPTVBoss 3.5 User Manual\images\image36.png](../IPTVBoss 3.5 User Manual/images/image36.png)


---

### Related Topics

- [Previous: Understanding NoGUI Mode](27_nogui_mode.md)
- [Next: Backing Up Your Database](29_backing_up_database.md)
