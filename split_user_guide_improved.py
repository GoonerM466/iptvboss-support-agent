"""
Split User_Guide.md into fine-grained topic files
Preserves ALL content and ensures proper section boundaries
"""

import re
from pathlib import Path

# Define precise section boundaries and target files
SECTIONS = [
    # Getting Started
    {
        "file": "01_understanding_workflow.md",
        "title": "Understanding the IPTVBoss Workflow",
        "start_marker": "### Understanding the IPTVBoss Workflow",
        "end_marker": "### Setting Up Your First Source"
    },
    {
        "file": "02_adding_first_source.md",
        "title": "Setting Up Your First Source",
        "start_marker": "### Setting Up Your First Source",
        "end_marker": "### Source Manager - Advanced Options"
    },
    {
        "file": "03_source_manager_advanced.md",
        "title": "Source Manager - Advanced Options",
        "start_marker": "### Source Manager - Advanced Options",
        "end_marker": "#### Managing Playlist Sources"
    },
    {
        "file": "04_managing_playlist_sources.md",
        "title": "Managing Playlist Sources",
        "start_marker": "#### Managing Playlist Sources",
        "end_marker": "#### Playlist Source Options"
    },
    {
        "file": "05_playlist_source_options.md",
        "title": "Playlist Source Options",
        "start_marker": "#### Playlist Source Options",
        "end_marker": "#### Managing EPG Sources"
    },
    {
        "file": "06_managing_epg_sources.md",
        "title": "Managing EPG Sources (Adding)",
        "start_marker": "#### Managing EPG Sources",
        "end_marker": "### Creating and Managing Layouts"
    },

    # Layouts
    {
        "file": "07_layouts_overview.md",
        "title": "Creating and Managing Layouts - Overview",
        "start_marker": "### Creating and Managing Layouts",
        "end_marker": "#### Layout Manager Panel"
    },
    {
        "file": "08_layout_manager_panel.md",
        "title": "Layout Manager Panel",
        "start_marker": "#### Layout Manager Panel",
        "end_marker": "**Creating a layout**:"
    },
    {
        "file": "09_creating_a_layout.md",
        "title": "Creating a Layout - Workflow",
        "start_marker": "**Creating a layout**:",
        "end_marker": "### Working in Layout Editor"
    },
    {
        "file": "10_layout_editor_interface.md",
        "title": "Working in Layout Editor",
        "start_marker": "### Working in Layout Editor",
        "end_marker": "### Importing Channels into Layouts"
    },
    {
        "file": "11_importing_channels_overview.md",
        "title": "Importing Channels into Layouts - Overview",
        "start_marker": "### Importing Channels into Layouts",
        "end_marker": "#### Import Channels From Sources Dialog"
    },
    {
        "file": "12_import_from_sources.md",
        "title": "Import Channels From Sources Dialog",
        "start_marker": "#### Import Channels From Sources Dialog",
        "end_marker": "#### Import Channels From Layouts Dialog"
    },
    {
        "file": "13_import_from_layouts.md",
        "title": "Import Channels From Layouts Dialog",
        "start_marker": "#### Import Channels From Layouts Dialog",
        "end_marker": "## EPG Management"
    },

    # EPG Management
    {
        "file": "14_mapping_epg_to_channels.md",
        "title": "Mapping EPG to Channels",
        "start_marker": "### Mapping EPG to Channels",
        "end_marker": "### Using Universal EPG"
    },
    {
        "file": "15_universal_epg.md",
        "title": "Using Universal EPG",
        "start_marker": "### Using Universal EPG",
        "end_marker": "### Managing EPG Sources"
    },
    {
        "file": "16_managing_epg_sources_full.md",
        "title": "Managing EPG Sources (Full Guide)",
        "start_marker": "### Managing EPG Sources",
        "end_marker": "### Customizing EPG Layout (Advanced)"
    },
    {
        "file": "17_customizing_epg_layout.md",
        "title": "Customizing EPG Layout (Advanced)",
        "start_marker": "### Customizing EPG Layout (Advanced)",
        "end_marker": "### EPG Browser"
    },
    {
        "file": "18_epg_browser.md",
        "title": "EPG Browser",
        "start_marker": "### EPG Browser",
        "end_marker": "## Output and Distribution"
    },

    # Output and Distribution
    {
        "file": "19_outputting_playlists.md",
        "title": "Outputting Playlists for Players",
        "start_marker": "### Outputting Playlists for Players",
        "end_marker": "### Understanding Cloud Storage Options"
    },
    {
        "file": "20_cloud_storage_options.md",
        "title": "Understanding Cloud Storage Options",
        "start_marker": "### Understanding Cloud Storage Options",
        "end_marker": "### Using TinyURL for Short Links"
    },
    {
        "file": "21_tinyurl_short_links.md",
        "title": "Using TinyURL for Short Links",
        "start_marker": "### Using TinyURL for Short Links",
        "end_marker": "## Automation"
    },

    # Automation
    {
        "file": "22_automatic_epg_syncing.md",
        "title": "Setting Up Automatic EPG Syncing",
        "start_marker": "### Setting Up Automatic EPG Syncing",
        "end_marker": "### Understanding NoGUI Mode"
    },
    {
        "file": "23_nogui_mode.md",
        "title": "Understanding NoGUI Mode",
        "start_marker": "### Understanding NoGUI Mode",
        "end_marker": "## Managing Automatic Channel Imports"
    },
    {
        "file": "24_new_channel_manager.md",
        "title": "New Channel Manager (Automatic Channel Imports)",
        "start_marker": "## Managing Automatic Channel Imports",
        "end_marker": "## Maintenance"
    },

    # Maintenance
    {
        "file": "25_backing_up_database.md",
        "title": "Backing Up Your Database",
        "start_marker": "### Backing Up Your Database",
        "end_marker": "### Restoring from Backup"
    },
    {
        "file": "26_restoring_from_backup.md",
        "title": "Restoring from Backup",
        "start_marker": "### Restoring from Backup",
        "end_marker": "### Handling Provider Changes"
    },
    {
        "file": "27_handling_provider_changes.md",
        "title": "Handling Provider Changes",
        "start_marker": "### Handling Provider Changes",
        "end_marker": "## Advanced Topics"
    },

    # Advanced Topics
    {
        "file": "28_managing_multiple_users.md",
        "title": "Managing Multiple Users",
        "start_marker": "### Managing Multiple Users",
        "end_marker": "### IPTVBoss XC Server (Advanced)"
    },
    {
        "file": "29_xc_server_overview.md",
        "title": "IPTVBoss XC Server - Overview and Setup",
        "start_marker": "### IPTVBoss XC Server (Advanced)",
        "end_marker": "### Setting Up as Windows Service"
    },
    {
        "file": "30_xc_server_windows_service.md",
        "title": "Setting Up XC Server as Windows Service",
        "start_marker": "### Setting Up as Windows Service",
        "end_marker": "### Setting Up as Ubuntu Service"
    },
    {
        "file": "31_xc_server_linux_service.md",
        "title": "Setting Up XC Server as Ubuntu/Linux Service",
        "start_marker": "### Setting Up as Ubuntu Service",
        "end_marker": "### Troubleshooting Common Issues"
    },
    {
        "file": "32_troubleshooting_overview.md",
        "title": "Troubleshooting Common Issues",
        "start_marker": "### Troubleshooting Common Issues",
        "end_marker": "## Best Practices Summary"
    },
]

def read_full_guide():
    """Read the complete User_Guide.md"""
    guide_path = Path("C:/Scripts/DiscordSupportBot/rag_system/data/documents/User_Guide.md")
    with open(guide_path, 'r', encoding='utf-8') as f:
        return f.read()

def extract_section(content, start_marker, end_marker):
    """Extract section between start and end markers"""
    start_idx = content.find(start_marker)
    if start_idx == -1:
        print(f"  WARNING: Start marker not found: {start_marker}")
        return None

    if end_marker:
        end_idx = content.find(end_marker, start_idx + len(start_marker))
        if end_idx == -1:
            # Take until end of file
            section = content[start_idx:]
        else:
            section = content[start_idx:end_idx]
    else:
        section = content[start_idx:]

    return section.strip()

def create_file_header(title):
    """Create markdown header for file"""
    return f"# {title}\n\n"

def create_related_topics(current_idx, sections):
    """Generate related topics links"""
    related = []

    # Previous topic
    if current_idx > 0:
        prev = sections[current_idx - 1]
        prev_title = prev['title']
        prev_file = prev['file']
        related.append(f"- [Previous: {prev_title}]({prev_file})")

    # Next topic
    if current_idx < len(sections) - 1:
        next = sections[current_idx + 1]
        next_title = next['title']
        next_file = next['file']
        related.append(f"- [Next: {next_title}]({next_file})")

    if related:
        return "\n---\n\n## Related Topics\n\n" + "\n".join(related) + "\n"
    return ""

def main():
    print("=" * 70)
    print("Splitting User_Guide.md into fine-grained topic files")
    print("=" * 70)

    # Read full guide
    print("\nReading User_Guide.md...")
    content = read_full_guide()
    print(f"  Total length: {len(content)} characters")

    # Create output directory
    output_dir = Path("C:/Scripts/DiscordSupportBot/rag_system/data/documents/user_guide")
    output_dir.mkdir(exist_ok=True)

    # Extract and write each section
    print(f"\nExtracting {len(SECTIONS)} sections...")

    for idx, section_def in enumerate(SECTIONS):
        filename = section_def['file']
        title = section_def['title']
        start = section_def['start_marker']
        end = section_def.get('end_marker')

        print(f"\n[{idx+1}/{len(SECTIONS)}] {filename}")
        print(f"  Title: {title}")

        # Extract section
        section_content = extract_section(content, start, end)

        if section_content is None:
            print(f"  SKIPPED: Could not extract")
            continue

        # Remove the heading if it's already in the content (we'll add it back)
        section_content = section_content.replace(start, "").strip()

        # Build file content
        file_content = create_file_header(title)
        file_content += section_content
        file_content += create_related_topics(idx, SECTIONS)

        # Write file
        output_path = output_dir / filename
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(file_content)

        print(f"  OK Created: {len(file_content)} characters")

    print("\n" + "=" * 70)
    print(f"COMPLETE: Created {len(SECTIONS)} topic files")
    print("=" * 70)

if __name__ == "__main__":
    main()
