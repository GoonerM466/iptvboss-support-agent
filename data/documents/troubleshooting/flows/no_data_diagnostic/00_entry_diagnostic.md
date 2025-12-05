# No Data Diagnostic - Entry Point

**Flow ID**: no_data
**Type**: diagnostic_entry
**Confidence**: low (requires questions)

### Common User Phrases

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

### Diagnostic Strategy

When a user reports "no data" without specific context, ask strategic questions to narrow down the issue before providing solutions.

### Diagnostic Question 1: Context

**Ask**: "Let me help narrow this down. Has this setup worked before, or is this a new setup that never worked?"

**Why**: Determines if this is a configuration issue vs. something that broke

**Decision Paths**:
- **Was working** → Go to Question 2 (something changed/broke)
- **Never worked** → Likely initial setup issue → Check configuration (sources, cloud, URLs)

### Diagnostic Question 2: Location

**Ask**: "Where are you seeing no data - in IPTVBoss or in your player app?"

**Why**: Identifies where in the workflow the issue occurs

**Decision Paths**:
- **In Boss** → Issue with source sync or database → [Boss Has No Data Solution](03_solution_boss_no_data.md)
- **In Player only** → Issue between Boss and Player → Go to Question 3

### Diagnostic Question 3: Basic Troubleshooting

**If issue is in Player, ask**: "Have you tried syncing your player (Update Playlist / Refresh in your player app)?"

**Why**: Eliminates simplest solution first (70% of "no data in player" issues)

**Decision Paths**:
- **Yes, tried syncing** → Go to HIGH CONFIDENCE solution (output issue)
- **No, haven't tried** → Provide sync instructions with medium confidence
- **Don't know how** → Provide sync instructions with screenshots

### HIGH CONFIDENCE SOLUTION PATH

If user answered:
- "Was working" + "No data in player" + "Tried syncing, didn't help"

→ **Confidence: HIGH (90%+)** - This is an output or Boss sync issue
→ **Solution**: [No Data After Player Sync Failed](02_solution_boss_output.md)

### MEDIUM CONFIDENCE SOLUTION PATH

If user answered:
- "Never worked" OR "Haven't tried syncing"

→ **Confidence: MEDIUM (60-80%)** - Could be setup or simple sync issue
→ **Solution**: [Initial Setup or Player Sync](01_solution_player_sync.md)

### LOW CONFIDENCE PATH

If user answers are still vague or contradictory:
- Ask more specific follow-up questions
- Guide them through basic checks step by step
- See [Comprehensive No Data Reference](../../13_no_data.md) for all scenarios

### Related Comprehensive Guide

[No Data in Boss or Player - Full Reference](../../13_no_data.md)
