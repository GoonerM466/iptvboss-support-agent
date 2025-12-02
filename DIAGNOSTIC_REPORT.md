# RAG System Diagnostic Report

**Date:** December 2, 2024
**Issue:** Poor retrieval quality compared to Claude Projects

---

## Problems Identified

### 1. **Insufficient Context Retrieval** (CRITICAL)
**Current Setting:** `top_k: 3` (only 3 chunks retrieved)

**Problem:**
- The "Layout Manager Panel" section in User_Guide.md has ~14 detailed options
- With 1000-character chunks, this gets split into multiple chunks
- Retrieving only 3 chunks means you get maybe 1-2 options out of 14
- User asks "what are all the options?" but the context only contains partial info

**Example from chat log:**
- User asks about Layout Manager options
- Agent only finds info about "Enabled" toggle
- Says "I don't have information on other options" - **FALSE**
- The info exists but wasn't retrieved

**Root Cause:** `top_k=3` is too low for comprehensive sections

**Claude Projects Comparison:**
- Claude Projects likely uses the ENTIRE document as context
- Or uses much higher top_k (10-20 chunks)
- Gets the complete picture, can "connect the dots"

---

### 2. **Keyword-Only Image Matching** (MAJOR)
**Current Logic:** Simple keyword matching in `image_handler.py`

**Problem:**
```python
# Current logic (line 62):
if keyword.lower() in combined_text:
    score += 1
```

This doesn't consider:
- **Context/section** where keyword appears
- **Semantic similarity** between question and image description
- **Order/proximity** of keywords

**Example Issues:**
- User asks about "XC API source" (adding a source)
  - Keyword "xc" matches
  - Shows images for "XC Server" (completely different feature)
  - Should only show Sources Manager images

- User asks about "Dropbox setup"
  - Shows 2 Dropbox images + 1 Google Drive image
  - Should show ALL 4 Dropbox images (3-6) and NO Drive images

**Root Cause:** No context awareness in image detection

---

### 3. **Chunk Size vs. Content Structure Mismatch** (MODERATE)
**Current Setting:** `chunk_size: 1000` characters

**Problem:**
- User_Guide.md has long sections (e.g., Layout Manager: 2000+ chars)
- Gets split mid-section, losing context
- Related information scattered across multiple chunks
- LLM can't "connect the dots" between chunks

**Example:**
```
Chunk 1: "Layout options: 1. Enabled 2. Cloud Sync..."
Chunk 2: "...3. Upload Raw XML 4. Upload Zipped XML..."
Chunk 3: "...5. M3U Output 6. M3U Filename..."
```

If only Chunk 1 is retrieved → only sees 2 options
User asks "what are ALL the options?" → Agent says "don't have info"

**Claude Projects:**
- Likely uses larger chunks or entire sections
- Or uses a different chunking strategy (semantic, not character-based)

---

### 4. **Min Score Too High** (MINOR)
**Current Setting:** `min_score: 0.3`

**Problem:**
- If user question uses different wording than docs
- Similarity score might be 0.25-0.29
- Gets filtered out, no context retrieved
- Agent says "I don't have that information"

---

### 5. **Temperature Too Low** (MINOR)
**Current Setting:** `temperature: 0.3`

**Problem:**
- Very deterministic responses
- Less ability to "infer" or "reason" from context
- More likely to say "I don't know" vs. synthesizing info

**Claude Projects:**
- Likely uses higher temperature (0.5-0.7)
- Better at connecting ideas and elaborating

---

## Root Cause Summary

The RAG system is suffering from **"tunnel vision"**:

1. **Too little context** retrieved (top_k=3)
2. **Context fragmented** by fixed-size chunking
3. **Image detection** uses naive keyword matching
4. **Settings optimized** for speed/cost, not quality

**Result:** Agent sees only 3 small "keyhole" views of the knowledge base, can't see the full picture.

**Claude Projects:** Sees much more context, can synthesize and elaborate naturally.

---

## Recommended Fixes

### Fix 1: Increase Context Retrieval (HIGHEST PRIORITY)
```yaml
# settings.yaml
vector_search:
  top_k: 10  # Was: 3 → Now: 10
  min_score: 0.2  # Was: 0.3 → Now: 0.2 (more lenient)
```

**Impact:** 3x more context → much better coverage of long sections

**Trade-off:**
- Slower responses (~1-2 seconds longer)
- Higher Gemini API token usage (~3x)
- Still well within free tier limits

---

### Fix 2: Smarter Chunking Strategy
**Current:** Fixed 1000 chars, split anywhere
**Better:** Section-aware chunking

```python
# Split by ## headings first, THEN chunk if needed
# Keep related info together
# Example:
Chunk: "## Layout Manager Panel
       Creating a New Layout:
       1. Click + symbol
       2. Name your layout
       ...
       Layout Options:
       1. Enabled - controls...
       2. Cloud Sync - uploads..."
```

**Implementation:** Modify `document_processor.py` to:
1. Split on `##` headings
2. Only sub-chunk if section > 2000 chars
3. Keep section header with each chunk

---

### Fix 3: Context-Aware Image Detection
**Current:** Keyword matching only
**Better:** Use retrieved chunk sources + semantic matching

```python
def detect_relevant_images(self, question, retrieved_chunks):
    # NEW: Check which sections chunks came from
    chunk_sections = set()
    for chunk in retrieved_chunks:
        # Extract section from chunk metadata
        if 'SETUP DROPBOX' in chunk['source']:
            chunk_sections.add('dropbox')
        elif 'XC Server' in chunk['source']:
            chunk_sections.add('xc_server')
        # etc.

    # NEW: Only match images from those sections
    relevant_mappings = []
    for mapping in self.image_map['mappings']:
        if mapping['section'] in chunk_sections:
            relevant_mappings.append(mapping)

    # Then do keyword matching WITHIN relevant mappings only
```

**Impact:**
- Images always contextual to retrieved content
- No more "XC Server" images when asking about "XC API sources"

---

### Fix 4: Increase Temperature
```yaml
# settings.yaml
llm:
  temperature: 0.5  # Was: 0.3 → Now: 0.5
  max_output_tokens: 3072  # Was: 2048 → Now: 3072 (for longer answers)
```

**Impact:**
- More natural, elaborative responses
- Better at synthesizing info from multiple chunks

---

### Fix 5: Improve System Prompt
**Current prompt issue:** Tells LLM to say "I don't know" too readily

**Better prompt:**
```yaml
system_prompt: |
  You are the IPTVBoss Support Assistant.

  CRITICAL: When answering questions:
  1. Use ALL information from the context provided
  2. If context is partial, give what you know and suggest "I can provide more details if needed"
  3. ONLY say "I don't have that information" if context is truly empty or unrelated
  4. For multi-part questions, answer each part separately
  5. If user asks "what are all the options", list EVERY option found in context

  Context contains chunks from a larger document. Assume related info exists even if not fully in context.
```

---

## Quick Win: Immediate Improvements

**Change These 3 Settings:**
```yaml
# settings.yaml
vector_search:
  top_k: 10  # 3x more context
  min_score: 0.2  # More lenient matching

llm:
  temperature: 0.5  # More natural responses
  max_output_tokens: 3072  # Longer answers
```

**Rebuild vector DB:**
```bash
python src/embeddings/build_vector_db.py
```

**Restart app:**
```bash
streamlit run app.py
```

**Expected improvement:** 60-70% better (not perfect, but much closer to Claude Projects)

---

## Long-Term Fixes (If Quick Win Insufficient)

1. **Implement section-aware chunking** (2-3 hours work)
2. **Add metadata to chunks** (section name, document name)
3. **Context-aware image detection** (1 hour work)
4. **Hybrid search** (keyword + semantic) for better retrieval
5. **Re-ranking** retrieved chunks by relevance

---

## Why Claude Projects Works Better

**Claude Projects likely:**
1. Uses entire documents as context (no chunking)
2. Has 200K context window vs. our 3-10 chunks
3. Uses Claude's superior reasoning (Sonnet > Gemini Flash for RAG)
4. Has better prompt engineering built-in
5. Uses full document structure (headings, lists, etc.)

**Our system limitations:**
- Limited to 10 chunks × 1000 chars = 10K context
- Gemini Flash is faster but less capable than Claude Sonnet
- Manual RAG implementation vs. Anthropic's optimized system

---

## Recommendation

**Immediate:** Apply Quick Win settings (5 minutes)
**Test:** See if quality improves to acceptable level
**If insufficient:** Implement section-aware chunking (2-3 hours)
**If still insufficient:** Consider switching to Claude API (costs ~$1-2/month)

---

## Test Cases

After applying fixes, test these:

1. **"How do I set up Dropbox?"**
   - Should show images 3-6 ONLY (no Google Drive)
   - Should give complete setup steps

2. **"What are all the Layout Manager options?"**
   - Should list ALL 14+ options (not just "Enabled")
   - Should explain each option briefly

3. **"How do I add an XC API source?"**
   - Should show Sources Manager images (24-25)
   - Should NOT show XC Server images (39-43)
   - Should explain XC API vs M3U difference

4. **"How do I set up XC Server?"**
   - Should show XC Server images (39-43)
   - Should NOT show Sources Manager images
   - Should explain server setup, not source adding

---

**Status:** Ready to implement fixes
**Priority:** HIGH - Core functionality impaired
**Estimated fix time:** 5 minutes (quick win) to 3 hours (full fix)
