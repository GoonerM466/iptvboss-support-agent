"""
Properly split User_Guide.md into fine-grained topic files
ALL content preserved, proper section boundaries
"""

from pathlib import Path

def read_guide():
    path = Path("C:/Scripts/DiscordSupportBot/rag_system/data/documents/User_Guide.md")
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def write_file(filename, title, content, prev_file=None, next_file=None):
    """Write a markdown file with navigation"""
    out_dir = Path("C:/Scripts/DiscordSupportBot/rag_system/data/documents/user_guide")
    out_dir.mkdir(exist_ok=True)

    # Build file content
    output = f"# {title}\n\n{content}\n"

    # Add navigation
    if prev_file or next_file:
        output += "\n---\n\n## Related Topics\n\n"
        if prev_file:
            output += f"- [Previous: {prev_file[1]}]({prev_file[0]})\n"
        if next_file:
            output += f"- [Next: {next_file[1]}]({next_file[0]})\n"

    with open(out_dir / filename, 'w', encoding='utf-8') as f:
        f.write(output)

    print(f"Created: {filename} ({len(content)} chars)")

def extract(content, start_line, end_line=None):
    """Extract content between line numbers"""
    lines = content.split('\n')
    if end_line:
        return '\n'.join(lines[start_line-1:end_line-1])
    else:
        return '\n'.join(lines[start_line-1:])

def main():
    print("Creating properly split files...")
    content = read_guide()
    lines = content.split('\n')

    # Define ALL splits with precise line numbers from the 1912-line file
    files = [
        # Getting Started
        ("01_understanding_workflow.md", "Understanding the IPTVBoss Workflow", 43, 60),
        ("02_adding_first_source.md", "Setting Up Your First Source", 62, 106),
        ("03_source_manager_overview.md", "Source Manager - Advanced Options Overview", 107, 116),
        ("04_managing_playlist_sources_adding.md", "Managing Playlist Sources - Adding", 117, 148),
        ("05_playlist_source_options.md", "Playlist Source Options", 149, 217),
        ("06_managing_epg_sources_adding.md", "Managing EPG Sources - Adding", 219, 249),

        # Layouts
        ("07_layouts_overview.md", "Creating and Managing Layouts - Overview", 251, 260),
        ("08_layout_manager_panel.md", "Layout Manager Panel", 261, 386),
        ("09_creating_layout_workflow.md", "Creating a Layout - Workflow and Strategies", 387, 431),
        ("10_layout_editor_overview.md", "Working in Layout Editor - Overview", 433, 449),
        ("11_layout_editor_channel_options.md", "Layout Editor - Channel Options", 450, 574),
        ("12_layout_editor_group_options.md", "Layout Editor - Group Options", 575, 596),
        ("13_layout_editor_controls.md", "Layout Editor - Groups and Channels List Controls", 597, 634),
        ("14_layout_editor_features.md", "Layout Editor - Additional Features", 635, 664),
        ("15_importing_channels_overview.md", "Importing Channels into Layouts - Overview", 666, 672),
        ("16_import_from_sources_dialog.md", "Import Channels From Sources Dialog", 673, 729),
        ("17_import_from_layouts_dialog.md", "Import Channels From Layouts Dialog", 730, 795),

        # EPG Management
        ("18_mapping_epg_to_channels.md", "Mapping EPG to Channels", 799, 863),
        ("19_universal_epg.md", "Using Universal EPG", 865, 903),
        ("20_managing_epg_sources_full.md", "Managing EPG Sources", 905, 942),
        ("21_customizing_epg_layout.md", "Customizing EPG Layout (Advanced)", 944, 1036),
        ("22_epg_browser.md", "EPG Browser", 1038, 1101),

        # Output and Distribution
        ("23_outputting_playlists.md", "Outputting Playlists for Players", 1105, 1160),
        ("24_cloud_storage_overview.md", "Understanding Cloud Storage Options", 1162, 1206),
        ("25_tinyurl_short_links.md", "Using TinyURL for Short Links", 1208, 1236),

        # Automation
        ("26_automatic_epg_syncing.md", "Setting Up Automatic EPG Syncing", 1240, 1321),
        ("27_nogui_mode.md", "Understanding NoGUI Mode", 1323, 1370),
        ("28_new_channel_manager.md", "New Channel Manager (Automatic Channel Imports)", 1372, 1471),

        # Maintenance
        ("29_backing_up_database.md", "Backing Up Your Database", 1475, 1490),
        ("30_restoring_from_backup.md", "Restoring from Backup", 1492, 1537),
        ("31_handling_provider_changes.md", "Handling Provider Changes", 1539, 1576),

        # Advanced Topics
        ("32_managing_multiple_users.md", "Managing Multiple Users", 1580, 1637),
        ("33_xc_server_overview.md", "IPTVBoss XC Server - Overview and Setup", 1639, 1754),
        ("34_xc_server_windows_service.md", "Setting Up XC Server as Windows Service", 1755, 1767),
        ("35_xc_server_linux_service.md", "Setting Up XC Server as Ubuntu/Linux Service", 1768, 1821),
        ("36_xc_server_troubleshooting.md", "XC Server Troubleshooting and Comparison", 1822, 1844),
        ("37_troubleshooting_overview.md", "Troubleshooting Common Issues", 1846, 1885),
    ]

    # Create all files
    for i, (filename, title, start, end) in enumerate(files):
        section_content = extract(content, start, end)

        # Determine prev/next
        prev_file = (files[i-1][0], files[i-1][1]) if i > 0 else None
        next_file = (files[i+1][0], files[i+1][1]) if i < len(files)-1 else None

        write_file(filename, title, section_content, prev_file, next_file)

    print(f"\nDone! Created {len(files)} files.")
    print("\nNow creating README...")

    # Create README
    readme_content = """# IPTVBoss User Guide

Task-oriented guides for managing your IPTV channels with IPTVBoss/EPGBoss.

**New to IPTVBoss?** Start with the main [Quick Start Guide](../Quick_Start.md).

---

## Quick Navigation

### Getting Started (Files 01-06)

- [01 - Understanding the IPTVBoss Workflow](01_understanding_workflow.md)
- [02 - Setting Up Your First Source](02_adding_first_source.md)
- [03 - Source Manager - Overview](03_source_manager_overview.md)
- [04 - Managing Playlist Sources - Adding](04_managing_playlist_sources_adding.md)
- [05 - Playlist Source Options](05_playlist_source_options.md)
- [06 - Managing EPG Sources - Adding](06_managing_epg_sources_adding.md)

### Layouts (Files 07-17)

- [07 - Layouts Overview](07_layouts_overview.md)
- [08 - Layout Manager Panel](08_layout_manager_panel.md)
- [09 - Creating a Layout Workflow](09_creating_layout_workflow.md)
- [10 - Layout Editor Overview](10_layout_editor_overview.md)
- [11 - Layout Editor - Channel Options](11_layout_editor_channel_options.md)
- [12 - Layout Editor - Group Options](12_layout_editor_group_options.md)
- [13 - Layout Editor - List Controls](13_layout_editor_controls.md)
- [14 - Layout Editor - Additional Features](14_layout_editor_features.md)
- [15 - Importing Channels Overview](15_importing_channels_overview.md)
- [16 - Import From Sources Dialog](16_import_from_sources_dialog.md)
- [17 - Import From Layouts Dialog](17_import_from_layouts_dialog.md)

### EPG Management (Files 18-22)

- [18 - Mapping EPG to Channels](18_mapping_epg_to_channels.md)
- [19 - Using Universal EPG](19_universal_epg.md)
- [20 - Managing EPG Sources](20_managing_epg_sources_full.md)
- [21 - Customizing EPG Layout](21_customizing_epg_layout.md)
- [22 - EPG Browser](22_epg_browser.md)

### Output and Distribution (Files 23-25)

- [23 - Outputting Playlists for Players](23_outputting_playlists.md)
- [24 - Cloud Storage Options](24_cloud_storage_overview.md)
- [25 - Using TinyURL for Short Links](25_tinyurl_short_links.md)

### Automation (Files 26-28)

- [26 - Setting Up Automatic EPG Syncing](26_automatic_epg_syncing.md)
- [27 - Understanding NoGUI Mode](27_nogui_mode.md)
- [28 - New Channel Manager](28_new_channel_manager.md)

### Maintenance (Files 29-31)

- [29 - Backing Up Your Database](29_backing_up_database.md)
- [30 - Restoring from Backup](30_restoring_from_backup.md)
- [31 - Handling Provider Changes](31_handling_provider_changes.md)

### Advanced Topics (Files 32-37)

- [32 - Managing Multiple Users](32_managing_multiple_users.md)
- [33 - XC Server Overview and Setup](33_xc_server_overview.md)
- [34 - XC Server Windows Service](34_xc_server_windows_service.md)
- [35 - XC Server Linux Service](35_xc_server_linux_service.md)
- [36 - XC Server Troubleshooting](36_xc_server_troubleshooting.md)
- [37 - Troubleshooting Overview](37_troubleshooting_overview.md)

---

## Other Documentation

- [FAQ](../FAQ.md) - Common questions answered
- [Troubleshooting Guide](../Troubleshooting_Guide.md) - Problem-solution format
- [Known Issues](../Known_Issues.md) - Unresolved problems and workarounds
- [Quick Start](../Quick_Start.md) - 10-15 minute setup guide

---

## Getting Help

- **Discord Support** - Community help, very active
- **Logs are crucial** - IPTVBoss/logs folder, clean sensitive info first
- **Be specific** - describe exact steps, what you expected, what happened

---

**This guide is community-maintained.** Found an error or have a suggestion? Post in Discord!
"""

    readme_path = Path("C:/Scripts/DiscordSupportBot/rag_system/data/documents/user_guide/README.md")
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(readme_content)

    print("README created!")
    print("\nAll done! 37 topic files + 1 README = 38 files total")

if __name__ == "__main__":
    main()
