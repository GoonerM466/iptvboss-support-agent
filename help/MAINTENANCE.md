# Maintenance Guide - IPTVBoss Support Agent

How to maintain and update the support agent.

---

## Updating Knowledge Base

### When to Update

Update when:
- New IPTVBoss features released
- Documentation improved
- Common issues discovered
- User feedback indicates gaps

### Update Process

**1. Update Source Documents**

Edit files in `data/documents/`:
- FAQ.md
- Quick_Start.md
- User_Guide.md
- Troubleshooting_Guide.md
- Known_Issues.md

**2. Rebuild Vector Database**

```bash
python src/embeddings/build_vector_db.py
```

Output should show:
```
✅ Vector database built successfully!
📊 Total chunks: XXX
📊 Total documents: 9
```

**3. Test Locally**

```bash
streamlit run app.py
```

Test queries related to your changes.

**4. Deploy**

```bash
git add data/
git commit -m "Update knowledge base: [description]"
git push
```

Streamlit Cloud will auto-deploy within 1-2 minutes.

---

## Adding New Images

### Process

**1. Add Image Files**

Copy images to `data/images/`:
```bash
cp new_image.png data/images/image44.png
```

**2. Update Image Map**

Edit `config/image_map.json`:

```json
{
  "mappings": [
    {
      "keywords": ["new feature", "new screen"],
      "images": ["image44.png"],
      "description": "New feature screen"
    }
  ],
  "image_details": {
    "image44.png": "Description of what image shows"
  }
}
```

**3. Test and Deploy**

```bash
streamlit run app.py  # Test locally
git add data/images/ config/image_map.json
git commit -m "Add new images for [feature]"
git push
```

---

## Tuning the Agent

### Adjusting Search Sensitivity

Edit minimum score threshold in `app.py`:

```python
# More strict (fewer but more relevant results)
min_score = 0.5

# More lenient (more results, potentially less relevant)
min_score = 0.2

# Current default
min_score = 0.3
```

### Adjusting Number of Results

In `app.py`, change `top_k`:

```python
context, retrieved_chunks = vector_search.search_with_context(
    user_question,
    top_k=3,  # Default: 3 chunks
    min_score=min_score
)
```

Higher `top_k`:
- More context for LLM
- Better answers for complex questions
- Slower response times
- Higher API costs (more tokens)

Lower `top_k`:
- Faster responses
- Lower API costs
- May miss relevant context

### Adjusting LLM Temperature

Edit `src/llm/gemini_client.py`:

```python
def _generation_config(self) -> Dict:
    return {
        "temperature": 0.3,  # Lower = more focused
        "top_p": 0.8,
        "top_k": 40,
    }
```

Temperature scale:
- `0.0-0.3`: Very focused, deterministic
- `0.3-0.7`: Balanced (recommended)
- `0.7-1.0`: More creative, less predictable

---

## Modifying Prompts

### System Prompt

Edit `config/prompts.yaml`:

```yaml
system_prompt: |
  You are the IPTVBoss Support Assistant...

  # Add new rules here
  # Modify existing behavior
```

Changes take effect after restart.

### Testing Prompt Changes

1. Edit prompts.yaml
2. Restart app: `streamlit run app.py`
3. Test with sample queries
4. Iterate until satisfied
5. Commit and push

---

## Monitoring

### Check Usage Stats

**Streamlit Cloud:**
1. Go to https://share.streamlit.io/
2. Click your app
3. View Analytics tab

Shows:
- Daily visitors
- Total page views
- Peak usage times

**Gemini API:**
1. Go to https://aistudio.google.com/app/apikey
2. View quota usage

Shows:
- Requests per day
- Remaining quota
- Rate limit status

### Set Up Alerts (Optional)

**For high usage:**

Create a simple monitoring script:

```python
# monitor_usage.py
import requests
import os

def check_gemini_usage():
    # Check API usage via dashboard
    # Send email if approaching limits
    pass

if __name__ == "__main__":
    check_gemini_usage()
```

Run daily via cron/Task Scheduler.

---

## Common Maintenance Tasks

### Task: User Reports Incorrect Answer

**Steps:**

1. **Reproduce**:
   - Ask same question in app
   - Check "Show debug info" in sidebar
   - See which chunks were retrieved

2. **Identify Issue**:
   - Is information missing from docs?
   - Is information present but not retrieved?
   - Is LLM misinterpreting context?

3. **Fix**:
   - **Missing info**: Add to docs, rebuild vector DB
   - **Retrieval issue**: Adjust min_score or add keywords
   - **Interpretation issue**: Improve system prompt

4. **Test and Deploy**

### Task: Add New FAQ Entry

1. Edit `data/documents/FAQ.md`
2. Rebuild: `python src/embeddings/build_vector_db.py`
3. Test query locally
4. Commit and push

### Task: Update for New IPTVBoss Version

1. **Get release notes**
2. **Update docs**:
   - Add new features to User_Guide.md
   - Update Quick_Start.md if setup changed
   - Add new issues to Known_Issues.md
3. **Add images** (if any new screens)
4. **Rebuild vector DB**
5. **Test new features** with queries
6. **Deploy**

---

## Troubleshooting

### App is Down

**Check Streamlit Cloud:**
1. Go to dashboard
2. Check app status
3. View logs for errors

**Common fixes:**
- Restart app from dashboard
- Check if deployment failed
- Verify all files committed to Git

### Slow Responses

**Causes:**
- Cold start (first load after inactivity)
- High API load (Gemini)
- Large context size

**Fixes:**
- Reduce `top_k` in search
- Reduce chunk size
- Upgrade to paid Gemini tier (if needed)

### Images Not Displaying

**Causes:**
- Image files not committed to Git
- Wrong file paths
- Image map not updated

**Fixes:**
```bash
# Check images exist
ls data/images/

# Recommit if needed
git add data/images/*.png
git commit -m "Add missing images"
git push
```

### Hallucinations (Wrong Answers)

**Causes:**
- LLM using general knowledge instead of context
- Retrieved context is weak/irrelevant
- System prompt not strict enough

**Fixes:**
1. Increase `min_score` (more strict retrieval)
2. Strengthen system prompt (emphasize "only from context")
3. Lower temperature (more deterministic)
4. Add validation logic

---

## Backup and Recovery

### Backup Important Files

Regularly backup:
- `data/documents/` (your edited docs)
- `config/prompts.yaml` (custom prompts)
- `config/image_map.json` (image mappings)

```bash
# Create backup
tar -czf backup-$(date +%Y%m%d).tar.gz \
    data/documents/ \
    config/
```

### Restore from Backup

```bash
# Extract backup
tar -xzf backup-20241202.tar.gz

# Rebuild vector DB
python src/embeddings/build_vector_db.py

# Commit and push
git add .
git commit -m "Restore from backup"
git push
```

---

## Version Control Best Practices

### Branching Strategy

**Main branch**: Production (deployed to Streamlit Cloud)

**Feature branches**: For major changes

```bash
# Create feature branch
git checkout -b feature/add-new-docs

# Make changes, test locally
# ...

# Commit
git add .
git commit -m "feat: Add documentation for new feature"

# Merge to main
git checkout main
git merge feature/add-new-docs
git push
```

### Commit Frequency

- Commit after each logical change
- Don't commit broken code to main
- Write clear commit messages

---

## Performance Monitoring

### Track Response Times

Add timing logs to `app.py`:

```python
import time

start = time.time()
answer = gemini_client.generate_answer(...)
elapsed = time.time() - start

logger.info(f"Response time: {elapsed:.2f}s")
```

### Optimize if Needed

If response times > 10 seconds consistently:
1. Reduce context size
2. Use faster embedding model
3. Optimize vector search
4. Consider caching common queries

---

## Updating Dependencies

### Check for Updates

```bash
pip list --outdated
```

### Update Safely

1. **Test in local environment first**:
   ```bash
   pip install --upgrade streamlit
   streamlit run app.py  # Test thoroughly
   ```

2. **Update requirements.txt**:
   ```bash
   pip freeze > deployment/requirements.txt
   ```

3. **Commit and push**:
   ```bash
   git add deployment/requirements.txt
   git commit -m "chore: Update dependencies"
   git push
   ```

4. **Monitor deployment** for errors

---

## Scaling Considerations

### Current Capacity

- **Users**: 5/day comfortably
- **Requests**: ~1500/day (Gemini free tier)
- **Hosting**: Unlimited (Streamlit free tier)

### If Usage Increases

**10-20 users/day:**
- Current setup fine
- Monitor Gemini quota

**50+ users/day:**
- May need paid Gemini tier ($$$)
- Consider caching common queries
- Add rate limiting

**100+ users/day:**
- Switch to paid infrastructure
- Use Redis for caching
- Add proper database for analytics
- Consider Claude API (more expensive but better quality)

---

## Getting Help

### Resources

- [Streamlit Docs](https://docs.streamlit.io/)
- [Gemini API Docs](https://ai.google.dev/docs)
- [FAISS Documentation](https://faiss.ai/)

### Support Channels

- Streamlit Community Forum
- Google AI Studio support
- Project GitHub issues (if public repo)

---

**Keep your agent running smoothly! 🛠️**
