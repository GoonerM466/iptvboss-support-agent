# Managing Multiple Users

### Managing Multiple Users

User System allows managing multiple users with identical or customized layouts.

**Use cases**:
- Family members with same channels
- Friends on same provider
- Multiple devices with same setup

**Basic approach**:
- Create separate layouts for each user
- Output each layout separately
- Each user gets unique M3U/EPG URLs
- Hard to manage - linked groups can help

**User System approach**:
- Define one "master" layout
- User System replicates to multiple users
- Changes to master propagate to all users
- Or allow per-user customization

**Setup** (basic):

1. **Create layouts for each user**
   - "User1_Channels"
   - "User2_Channels"
   - etc.

2. **Customize per user**
   - Different channel selections
   - Different organizations

3. **Output separately**
   - Output each layout
   - Each generates unique URLs

4. **Distribute URLs**
   - Give each user their specific M3U/EPG URLs
   - Users can't see other users' customizations

**User System**:
1. **Create master layout**
   - "Master Playlist"

2. **Manager Uers / Add user**
   - Input user/pass for each user for source
   - Enable User, Source & Layout
   - Repeat as needed

3. **Output**
   - Unique outputs for all users (with thier user/pass), same content

4. **Distribute URLs**
   - Give each user their specific M3U/EPG URLs
   - Users can't see other users' credentials
- See dedicated User System documentation


---

## Related Topics

- [Previous: Handling Provider Changes](31_handling_provider_changes.md)
- [Next: IPTVBoss XC Server - Overview and Setup](33_xc_server_overview.md)
