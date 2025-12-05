# Database Issues Diagnostic - Entry Point

**Flow ID**: database_issues
**Type**: diagnostic_entry
**Confidence**: low (requires questions)

### Common User Phrases

- "Boss won't start"
- "Database failed to load"
- "Database error"
- "Boss is blank/empty"
- "All my settings are gone"
- "Starting from scratch"
- "Lost all my data"
- "Database corruption"
- "Failed to load database"
- "Can't open Boss"

### Diagnostic Strategy

Database issues can range from minor (lock file) to severe (corruption). Ask questions to assess severity before providing solutions.

### Diagnostic Question 1: What Happens When You Start Boss

**Ask**: "What exactly happens when you try to open Boss? Do you see an error message?"

**Why**: Different symptoms indicate different severities

**Symptom Types**:
- **"Database failed to load" error** → Database corruption → HIGH confidence solution
- **Boss opens but is blank/empty** → Corruption or wrong database path
- **Boss won't open at all** → Might not be database issue
- **Boss freezes on startup** → Lock file or ongoing process

### Diagnostic Question 2: Did This Follow an Event

**Ask**: "When did this start? Was it after an update, crash, or power loss?"

**Why**: Helps identify root cause and prevention

**Common Triggers**:
- **After Boss crash** → Lock file or corrupted during crash
- **After power outage** → Mid-write corruption
- **After Boss update** → Migration issue or compatibility
- **Suddenly, no apparent cause** → File system issue or disk problem

### Diagnostic Question 3: Do You Have a Backup

**Ask**: "Do you have a backup of your Boss database?"

**Why**: Determines if we can restore or need to rebuild

**Decision Paths**:
- **Yes, have backup** → HIGH CONFIDENCE → [Database Restore Solution](01_solution_restore.md)
- **No backup** → MEDIUM CONFIDENCE → [Recovery Attempts Solution](02_solution_recovery.md)
- **What's a backup?** → Need education + recovery attempts

### HIGH CONFIDENCE SOLUTION PATHS

**If "Database failed to load" error + have backup**:
→ **Confidence: HIGH** - Clean restore path
→ **Solution**: [Database Restore from Backup](01_solution_restore.md)

**If lock file suspected (Boss freezes)**:
→ **Confidence: MEDIUM-HIGH** - Simple lock file removal
→ **Solution**: [Lock File Removal](03_solution_lock_files.md)

### MEDIUM CONFIDENCE PATHS

**If no backup + corruption**:
→ **Confidence: MEDIUM** - May recover, may need rebuild
→ **Solution**: [Recovery Attempts](02_solution_recovery.md)

**If Boss blank but no error**:
→ **Confidence: MEDIUM** - Could be wrong data path
→ **Solution**: [Database Location Check](02_solution_recovery.md)

### Additional Diagnostic Questions (If Needed)

**If unclear severity**:

**Ask**: "When you open Boss, do you see your sources, layouts, and channels, or is everything missing?"
- Everything missing → Likely corruption or wrong path
- Some things present → Partial corruption or specific feature issue

**Ask**: "Can you navigate to the Boss database folder and tell me the file size of database.db?"
- 0 bytes → Completely corrupted, need backup
- Normal size (varies, usually KB to MB) → May be recoverable
- File missing → Boss looking in wrong location

### Quick Triage

**Severity Levels**:

**MINOR** (Easy fix):
- Lock file causing freeze
- Boss looking at wrong folder
- Permission issue

**MODERATE** (May recover):
- Recent corruption
- Backup available
- Database file exists with data

**SEVERE** (Rebuild likely needed):
- Database file is 0 bytes or corrupt beyond repair
- No backup available
- Multiple failed recovery attempts

### Related Comprehensive Guide

[Database Corruption and Startup Failures - Full Reference](../../01_database_corruption_startup_failure.md)
