# No Data in Boss or Player

**Common user descriptions of this issue:**
- "I have no data"
- "I got no data"
- "Nothing is working"
- "No data showing"
- "Nothing is showing up"
- "Everything is blank"
- "Everything is empty"
- "Boss is empty"
- "Player is empty"
- "No channels showing"
- "No EPG data"
- "No guide information"
- "Missing all data"
- "All my data is gone"
- "Data disappeared"
- "Channels disappeared"
- "EPG disappeared"

No M3U playlist data or EPG program information showing in either IPTVBoss or the user's player app.

### Problem

No data in either Boss or the Player indicating a failure in the workflow.

### Symptoms

- No EPG data in Boss
- No EPG data in Player
- No or outdated channels in M3U in Boss
- No or outdated channels in M3U in Player
- Boss setup has been wiped / is corrupt

### Why This Happens

Indicates a failure in the workflow. This could have multiple causes and it's important to determine where the failure is so you can fix it ASAP.

### Solution

**First determine where the failure is**

**1. Where is the user seeing no information / data?**
- In IPTVBoss → goto Step 1a
- In the user's Player → goto Step 1b

    **1a. If in IPTVBoss:**
    - *If there are no playlists, sources or anything showing, and its like you are starting Boss for the first time, you will need to [Restore Database](01_database_corruption_startup_failure.md)*
    - Sources > Sync all sources
    - Sources > Sync all EPGs
    - Check EPG Browser & Channel lists;
        - If fixed, move to step 4.
        - If not fixed, move to step 2

    **1b. If in Player**
    - Sync playlist & EPG
        - If this solves it, ensure player sync schedule is set up
        - If not fixed, move to step 1a

**2. Check connectivity, sources & subscription**
- Is the internet connected; if not, connect internet & try again
- If channel/group or M3U related, check provider is online. If it is and issues persist you should ask for support on Discord
- If EPG related, check subscription is valid
- Still not fixed > continue to Step 3

**3. Clear EPG Cache**
- Shut down IPTVBoss
- Delete the problematic EPG file from `IPTVBoss/cache` - if multiple regions are affected, delete all EPG cache files
- Open IPTVBoss and move to Step 1a

**4. Output**
- In IPTVBoss, output your layout(s) and EPG file(s)
- Sync playlist & EPG in player
    - If you see data the issue is fixed, but you might want to ensure you have a sync schedule set up in Boss
    - If you dont see data this means the issue is between Boss & the cloud, or the cloud and your player. Goto step 5

**5. Check cloud files**
- Go to your cloud provider website and download the affected files
- Open them in a text editor such as Notepad++ or Sublime
- Ensure data is current
    - If data is out of date, there is an issue with Boss outputting to the cloud.

    Reauthorize cloud, and repeat the troubleshooting steps.

    If the issue persists then you should seek help on Discord and provide clean logs.
    - If the data is current then the issue is between the cloud & your player.

    - Ensure you have the correct URLs in your player.

    If the issue persists then you should seek help on Discord and provide clean logs.

### Related Topics

- [Database Corruption and Failed Startup](01_database_corruption_startup_failure.md)
- [Changes Not Reflecting in Player Apps](08_changes_not_reflecting_players.md)
- [Cloud Storage Upload Failures](07_cloud_storage_upload_failures.md)
- [Source Sync Breaking Layouts](02_source_sync_breaking_layouts.md)
- [EPG Sources Show Limited Information](09_epg_sources_limited_information.md)
- [Understanding IPTVBoss Workflow](../user_guide/01_understanding_workflow.md)
- [Manual Output](../user_guide/23_manual_output.md)
- [Cloud Storage Overview](../user_guide/24_cloud_storage_overview.md)
- [Automatic Syncing](../user_guide/26_automatic_syncing.md)
- [Changes Not Showing in Player](../faq/06_changes_not_showing_in_player.md)
- [No Streams Found After Output](../faq/09_no_streams_found_after_output.md)
