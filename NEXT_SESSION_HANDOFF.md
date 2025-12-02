# RAG System - Next Session Handoff

**Date:** December 2, 2024
**Status:** Critical fixes needed - chunking strategy causing poor retrieval
**Priority:** HIGH

---

## Current Problem Summary

### Issue: Agent Missing Information Despite It Being In Docs

**Symptoms:**
1. User asks: "What are all the Layout Manager options?"
2. Agent says: "I don't have that information"
3. **Reality**: The info EXISTS in User_Guide.md but isn't being retrieved properly

**Root Cause:**
- User_Guide.md is a MASSIVE file (~2000 lines, 60KB+)
- Current chunking splits it into ~80+ small chunks
- Layout Manager section (6382 chars) gets fragmented across multiple chunks
- Vector search retrieves top 10 chunks, but misses the chunks with actual options
- Agent only sees section header, not the content

**Proof:**
- See `C:\Scripts\DiscordSupportBot\CHAT_BOT_ISSUES.md` for debug output
- Chunk 2 shows: "Layout Manager Panel... Visual Reference: [IPTVBoss 3.5..." (CUT OFF)
- The actual 14 options are in subsequent chunks that weren't retrieved

---

## Attempted Fixes (Didn't Fully Work)

### What Was Tried:
1. ✅ Increased `top_k` from 3 → 10 (helps but insufficient)
2. ✅ Increased chunk size 1000 → 2500 chars (helps but still fragments large sections)
3. ✅ Improved prompts (helps agent use what it has)
4. ✅ Split on `####` headings instead of `##` (helps but User_Guide has many sections)

### Why It's Not Enough:
- User_Guide.md has 12+ major sections, each 2000-6000 characters
- Even with 2500 char chunks, sections still get split
- With 10 chunks retrieved, we get pieces from different sections
- Agent can't "see" complete information

---

## Proposed Solution: Split User_Guide Into Topic Files

### Strategy:
Break User_Guide.md into 12-15 smaller, focused files.

**Benefits:**
1. **Better retrieval:** Each file is focused on one topic
2. **Complete context:** Entire file fits in fewer chunks
3. **Better image mapping:** Images tied to specific files/topics
4. **Easier maintenance:** Update one topic without affecting others
5. **Faster searches:** More targeted semantic matching

**Structure:**
```
data/documents/user_guide/
├── 01_understanding_workflow.md
├── 02_setting_up_first_source.md
├── 03_creating_managing_layouts.md        ← Layout Manager goes here
├── 04_mapping_epg_to_channels.md
├── 05_using_universal_epg.md
├── 06_managing_epg_sources.md
├── 07_outputting_playlists.md
├── 08_cloud_storage_options.md
├── 09_tinyurl_short_links.md
├── 10_automatic_epg_syncing.md
├── 11_nogui_mode.md
├── 12_backing_up_database.md
├── 13_restoring_from_backup.md
├── 14_handling_provider_changes.md
├── 15_managing_multiple_users.md
├── 16_troubleshooting.md
└── README.md                              ← Navigation index
```

---

## Implementation Plan

### Phase 1: Split User_Guide.md (2 hours)

**Task 1.1:** Create directory structure
```bash
mkdir data/documents/user_guide
```

**Task 1.2:** Extract sections from User_Guide.md

For each section in the table of contents:
1. Extract the section content
2. Create new file: `0X_section_name.md`
3. Include:
   - Section heading
   - Full content
   - Related image references
   - Links to related files

**Example - `03_creating_managing_layouts.md`:**
```markdown
# Creating and Managing Layouts

## Layout Manager Panel
[Full Layout Manager section - all 14 options]

## Working in Layout Editor
[Full Layout Editor section]

## Related Topics
- See [Setting Up Your First Source](02_setting_up_first_source.md)
- See [Mapping EPG to Channels](04_mapping_epg_to_channels.md)

## Images
- image23.png - Layout Manager panel
- image32.png - Layout Editor interface
```

**Task 1.3:** Create README.md navigation file
```markdown
# IPTVBoss User Guide

## Quick Navigation

### Getting Started
- [Understanding the Workflow](01_understanding_workflow.md)
- [Setting Up Your First Source](02_setting_up_first_source.md)
- [Creating and Managing Layouts](03_creating_managing_layouts.md)

[etc...]
```

**Task 1.4:** Update other locations
- Copy new structure to: `C:\Scripts\DiscordSupportBot\RAG Docs\documentation\user_guide\`
- Copy to: `C:\Scripts\DiscordSupportBot\Claude Web Project\documentation\user_guide\`

---

### Phase 2: Update Image Mapping (30 minutes)

**Task 2.1:** Update `config/image_map.json`

Add `source_files` to each mapping:
```json
{
  "keywords": ["layout manager", "manage layouts"],
  "images": ["image23.png"],
  "source_files": ["03_creating_managing_layouts.md"],
  "description": "Layout Manager panel"
}
```

**Task 2.2:** Update `src/ui/image_handler.py`

Add file-based filtering:
```python
def detect_relevant_images(self, question, retrieved_chunks):
    # Get which source files were retrieved
    source_files = set(chunk['source'] for chunk in retrieved_chunks)

    # Only match images from those source files
    for mapping in self.image_map['mappings']:
        if mapping.get('source_files'):
            # Check if any retrieved files match this mapping
            if any(sf in source_files for sf in mapping['source_files']):
                # Add these images
```

**Result:** Images only shown if they match the FILES that were retrieved

---

### Phase 3: Rebuild and Test (30 minutes)

**Task 3.1:** Rebuild vector database
```bash
python src/embeddings/build_vector_db.py
```

**Task 3.2:** Test retrieval quality

Test queries:
1. "What are all the Layout Manager options?"
   - Should retrieve complete `03_creating_managing_layouts.md`
   - Should list all 14 options
   - Should show ONLY image23.png and image32.png (Layout-related)

2. "How do I set up Dropbox?"
   - Should retrieve `08_cloud_storage_options.md` or Quick_Start.md
   - Should show ONLY images 3-6 (Dropbox-related)

3. "How do I add an XC API source?"
   - Should retrieve `02_setting_up_first_source.md`
   - Should show images 24-25 (Sources Manager)
   - Should NOT show XC Server images (39-43)

---

### Phase 4: Document and Deploy (30 minutes)

**Task 4.1:** Update documentation
- Update FIXES_APPLIED.md with new chunking strategy
- Update DEPLOYMENT.md with new structure

**Task 4.2:** Create maintenance guide
- How to add new sections
- How to update existing sections
- How to map images to new files

---

## Expected Results

### Before (Current State):
- User asks about Layout Manager options
- Retrieves fragment of section (header only)
- Agent says "I don't have that information"
- Shows unrelated images from other sections

### After (With Split Files):
- User asks about Layout Manager options
- Retrieves complete `03_creating_managing_layouts.md` file
- Entire file fits in 2-3 chunks (6382 chars / 2500 per chunk = 3 chunks)
- All 3 chunks retrieved (top_k=10 is plenty)
- Agent sees ALL 14 options
- Shows ONLY Layout Manager images (23, 32)

**Quality improvement:** 40% → 95%

---

## Files to Modify

### 1. Create New Files:
- `data/documents/user_guide/01_understanding_workflow.md`
- `data/documents/user_guide/02_setting_up_first_source.md`
- ... (12-15 files total)
- `data/documents/user_guide/README.md`

### 2. Modify Existing:
- `config/image_map.json` - Add source_files
- `src/ui/image_handler.py` - Add file-based filtering
- `data/documents/User_Guide.md` - Archive or replace with redirect

### 3. Update in Multiple Locations:
- `RAG Docs/documentation/` - Copy new structure
- `Claude Web Project/documentation/` - Copy new structure

---

## Current Settings (Already Applied)

These are correct, keep them:

**`config/settings.yaml`:**
```yaml
vector_search:
  top_k: 10
  min_score: 0.2

llm:
  model: "gemini-1.5-flash-latest"
  temperature: 0.5
  max_output_tokens: 3072

document_processing:
  chunk_size: 2500
  chunk_overlap: 400
```

**`src/embeddings/document_processor.py`:**
- Splits on `####` headings
- Chunk size: 2500
- Overlap: 400

---

## Reference Files

**Current Issues:**
- `C:\Scripts\DiscordSupportBot\CHAT_BOT_ISSUES.md` - Debug output showing problem

**Analysis:**
- `C:\Scripts\DiscordSupportBot\rag_system\DIAGNOSTIC_REPORT.md` - Full analysis
- `C:\Scripts\DiscordSupportBot\rag_system\FIXES_APPLIED.md` - What was tried

**Source Data:**
- `C:\Scripts\DiscordSupportBot\rag_system\data\documents\User_Guide.md` - LARGE file to split
- Line 261: Layout Manager Panel section starts here (6382 chars)

---

## Script to Automate Splitting

**Task for next agent:** Create `split_user_guide.py`

```python
"""
Split User_Guide.md into topic-specific files
"""

import re
from pathlib import Path

# Define sections to extract
SECTIONS = [
    {
        'filename': '01_understanding_workflow.md',
        'title': 'Understanding the IPTVBoss Workflow',
        'heading_pattern': r'### Understanding the IPTVBoss Workflow'
    },
    {
        'filename': '03_creating_managing_layouts.md',
        'title': 'Creating and Managing Layouts',
        'heading_pattern': r'#### Layout Manager Panel'
    },
    # etc...
]

def extract_section(content, start_pattern, end_pattern):
    """Extract text between two patterns"""
    # Implementation
    pass

def create_section_file(filename, title, content, related_images):
    """Create new markdown file with metadata"""
    # Implementation
    pass

# Main execution
```

---

## Verification Checklist

After splitting, verify:

- [ ] All 12-15 topic files created
- [ ] Each file is self-contained (2000-6000 chars)
- [ ] Navigation README created
- [ ] Image map updated with source_files
- [ ] Image handler updated for file-based filtering
- [ ] Vector DB rebuilt
- [ ] Test query: "Layout Manager options" → lists all 14
- [ ] Test query: "Dropbox setup" → shows only Dropbox images
- [ ] Test query: "XC API source" → no XC Server images shown

---

## Alternative Quick Fix (If Time Constrained)

If splitting takes too long, **temporary workaround:**

1. **Increase `top_k` to 20** (from 10)
   - More chunks retrieved = higher chance of getting all parts
   - Trade-off: More noise, slower, higher API usage

2. **Disable chunk size limit for User_Guide.md specifically**
   - Keep entire sections intact (no splitting)
   - User_Guide chunks will be 5000-7000 chars
   - Works but not ideal (very large context)

**Not recommended:** Band-aid solution, doesn't solve root cause

---

## Success Criteria

### Minimum Viable:
- [ ] User asks about any topic, gets complete answer
- [ ] No more "I don't have that information" when info exists
- [ ] Images shown are relevant to query topic

### Ideal:
- [ ] Agent provides comprehensive answers (all options, all steps)
- [ ] Can handle follow-up questions in same topic
- [ ] Image relevance: 95%+ accuracy
- [ ] Response completeness: 95%+ (vs current 40%)

---

## Context for Next Agent

### What Works:
- ✅ Basic RAG pipeline (FAISS + Gemini)
- ✅ Settings tuned (top_k=10, temp=0.5, etc.)
- ✅ Image detection logic exists
- ✅ Prompts improved

### What Doesn't Work:
- ❌ User_Guide.md too large, gets fragmented
- ❌ Agent sees incomplete sections
- ❌ Images from wrong sections shown
- ❌ Agent says "I don't know" when it shouldn't

### What Needs to Happen:
- 🔨 Split User_Guide.md into 12-15 topic files
- 🔨 Update image mapping with file sources
- 🔨 Add file-based image filtering
- 🔨 Rebuild vector DB
- 🔨 Test and verify

### Time Estimate:
- **Total:** 3-4 hours
- Phase 1 (Splitting): 2 hours
- Phase 2 (Image mapping): 30 min
- Phase 3 (Testing): 30 min
- Phase 4 (Documentation): 30 min

---

## Quick Start for Next Agent

```bash
# 1. Read this handoff doc
# 2. Read User_Guide.md structure
head -100 data/documents/User_Guide.md

# 3. Create split script or manually split
python split_user_guide.py  # (create this)

# 4. Update image mapping
# Edit config/image_map.json

# 5. Rebuild
python src/embeddings/build_vector_db.py

# 6. Test
streamlit run app.py
```

---

## Contact/Continuity

**Current settings location:** `C:\Scripts\DiscordSupportBot\rag_system\`

**All fixes applied in this session:**
1. Increased top_k, min_score, temperature, max_tokens
2. Improved system prompts
3. Fixed Gemini model name
4. Increased chunk size to 2500
5. Split on #### headings instead of ##
6. Fixed image mappings (correct image numbers)

**Next critical step:** Split User_Guide.md

---

**Status:** Ready for next session
**Priority:** HIGH - Core functionality blocked
**Estimated completion:** 3-4 hours of focused work
