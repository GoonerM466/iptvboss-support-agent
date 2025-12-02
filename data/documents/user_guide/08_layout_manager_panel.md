# Layout Manager Panel

#### Layout Manager Panel

The Layout Manager Panel is the main control center for creating and configuring layouts.

**Access**: **Layout → Layout Manager**

**Visual Reference**: [IPTVBoss 3.5 User Manual\images\image23.png](../IPTVBoss 3.5 User Manual/images/image23.png)

**Creating a New Layout**:

1. Click the **"+"** symbol
2. Give your layout a name (e.g., "Family", "Sports", "Kids Safe")
3. Press OK

### Layout manager Options ###:

Once you have a layout created, you can configure the following options:

**Basic Toggles**:

1. **Enabled**:
   - Controls whether this layout gets synced during NoGUI output
   - Disabled layouts are ignored by automation
   - Useful for temporarily disabling layouts without deleting them

2. **Cloud Sync Enabled**:
   - When enabled: Outputted M3U and EPG files upload to your configured cloud provider
   - When disabled: Files only save locally
   - Requires cloud provider setup (see Cloud Storage section)


**Layout Upload Options**:

3. **Upload Raw XML**:
   - Uploads uncompressed EPG XML file to cloud
   - Larger file size, faster for player to load
   - Some players require raw XML

4. **Upload Zipped XML (GZ)**:
   - Uploads compressed (.gz) EPG file to cloud
   - Much smaller file size, saves bandwidth
   - **Google Drive requires .gz format** (API limitation)
   - Most modern players support .gz

5. **M3U Output Enabled**:
   - When enabled: Outputs M3U playlist file during NoGUI sync
   - When disabled: No M3U generated (EPG only - Not recommended)

6. **M3U Filename**:
   - Custom name for your M3U file
   - **Must end in ".m3u"**
   - Example: `family_playlist.m3u`

7. **Output Layout EPG**:
   - When enabled: Generates layout-specific EPG file during NoGUI sync
   - When disabled: No EPG generated (M3U only - Not recommended unless you have universal EPG enabled or for advanced users)

8. **EPG Filename**:
   - Custom name for your EPG file
   - **Must end in ".xml"** (or ".xml.gz" if using compression)
   - Example: `family_epg.xml`

**EPG Configuration**:

9. **Layout EPG - Days to Keep**:
   - Controls how many days of EPG data to include
   - Lower value = smaller XML file
   - Default is usually sufficient
   - **Use case**: Reduce file size if player has memory limits

10. **Override EPG Layout Settings** (checkbox):
    - When enabled: Use custom EPG layout settings for this layout only
    - When disabled: Use global EPG layout settings
    - See "EPG Layout Customization" section for details

11. **EPG Layout Override** (button):
    - Opens EPG Layout Settings dialog
    - Only active when "Override EPG Layout Settings" is checked
    - Configure title/description format for this layout's EPG
    - See "EPG Layout Customization" section for details

**Output Location**:

12. **Use Custom Output Folder** (checkbox):
    - When enabled: Save M3U/XML files to custom location instead of default
    - When disabled: Files save to default `IPTVBoss/output` folder (Recommended)

13. **Custom Output Folder**:
    - Path where outputted files are saved locally
    - Only used if "Use Custom Output Folder" is enabled
    - Example: `D:\MyPlaylists\`

14. **Cloud Provider Folder**:
    - Subfolder path within your cloud provider
    - Organizes outputted files in cloud storage
    - Example: `Layouts/Family` creates `/{App_Name}/Layouts/Family/` in cloud
    - Leave empty to save in default `/{App_Name}/` cloud folder (Recomended)

**Action Buttons**:

1. **Save Layout**:
   - Saves all layout settings
   - **Important**: Must click after changing any options above

2. **Edit Layout**:
   - Opens Layout Editor for the selected layout
   - Same as **Layout → Layout Editor** menu

3. **Manage Users**:
   - Opens dialog to enable/disable users for this layout
   - User must already exist (see "Managing Multiple Users" section)
   - Controls which users can access this layout

4. **View Cloud Links**:
   - Displays your cloud URLs for M3U and EPG
   - Copy these links to use in your IPTV player app
   - **Note**: Links only appear after first successful upload to cloud

**Tips**:

- **Enable both Raw and GZ**: Some players prefer raw, others need GZ (Google Drive requires GZ)
- **Cloud Provider Folder**: Useful for organizing multiple layouts in cloud storage
- **Custom Output Folder**: Useful if you want local files in specific location for backup/testing
- **Disabled layouts**: Still editable, just not included in automated outputs

---

---

## Related Topics

- [Previous: Creating and Managing Layouts - Overview](07_layouts_overview.md)
- [Next: Creating a Layout - Workflow and Strategies](09_creating_layout_workflow.md)
