# Player Sync Issues Diagnostic - Entry Point

**Flow ID**: player_sync
**Type**: diagnostic_entry
**Confidence**: low (requires questions)

### Common User Phrases

- "Changes not showing"
- "Changes don't show in player"
- "Deleted channels still appear"
- "Edits not showing up"
- "Player shows old data"
- "Nothing is updating"
- "Still seeing old channels"
- "My changes disappeared"
- "Player not reflecting changes"
- "Updates not working"

### Diagnostic Strategy

When a user reports changes not appearing in their player, ask strategic questions to identify where in the workflow they're stuck.

### Diagnostic Question 1: What Changed

**Ask**: "What changes did you make in Boss that aren't showing?"

**Why**: Different changes require different verification steps

**Types of Changes**:
- **Deleted channels** → Most common issue, easy to verify
- **Renamed channels** → Check in player channel list
- **Group/category changes** → Check Boss layout vs player groups
- **EPG mappings** → Check EPG Browser first, then player
- **Channel order** → May require player cache clear

### Diagnostic Question 2: Did You Output

**Ask**: "After making changes, did you click Output in Boss and wait for the success message?"

**Why**: #1 reason changes don't show - forgot to output

**Decision Paths**:
- **Yes, I output** → Go to Question 3
- **No, forgot to output** → HIGH CONFIDENCE → [Workflow Completion Solution](01_solution_complete_workflow.md)
- **What's output?** → MEDIUM CONFIDENCE → [Workflow Education Solution](01_solution_complete_workflow.md)

### Diagnostic Question 3: Did You Sync Player

**Ask**: "After outputting, did you update/refresh your playlist in your player app?"

**Why**: #2 reason changes don't show - forgot to sync player

**Decision Paths**:
- **Yes, I synced** → HIGH CONFIDENCE → [Advanced Sync Issues](02_solution_player_cache.md)
- **No, didn't sync** → HIGH CONFIDENCE → [Workflow Completion Solution](01_solution_complete_workflow.md)
- **How do I sync?** → MEDIUM CONFIDENCE → [Workflow Completion Solution](01_solution_complete_workflow.md)

### HIGH CONFIDENCE SOLUTION PATHS

**If user DID output AND sync**:
→ **Confidence: HIGH** - Likely player cache or URL confusion
→ **Solution**: [Player Cache and URL Issues](02_solution_player_cache.md)

**If user forgot output OR sync**:
→ **Confidence: HIGH** - Workflow incomplete
→ **Solution**: [Complete Workflow Guide](01_solution_complete_workflow.md)

### MEDIUM CONFIDENCE PATH

**If user unsure what output/sync means**:
→ **Confidence: MEDIUM** - Needs workflow education
→ **Solution**: [Complete Workflow Guide](01_solution_complete_workflow.md) with explanation

### Additional Diagnostic Questions (If Needed)

**If user did everything correctly**:

**Ask**: "Which player app are you using?"
- TiviMate has aggressive caching
- ImPlayer has different sync behavior
- Each player may need different approach

**Ask**: "Did you check that Boss actually made the change?"
- Sometimes users think they saved but didn't
- Verify change is actually in Boss first

**Ask**: "Are you using the Boss cloud URL or your provider's direct URL?"
- Common mistake: player still using provider URL
- Boss changes won't appear if using provider URL directly

### Related Comprehensive Guide

[Changes Not Reflecting in Player Apps - Full Reference](../../08_changes_not_reflecting_players.md)
