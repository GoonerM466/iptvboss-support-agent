# Development Guide - IPTVBoss Support Agent

Guide for local development and testing.

---

## Local Setup

### Prerequisites

- Python 3.9 or higher
- pip
- Git

### Installation

```bash
# Clone repository (or navigate to rag_system folder)
cd rag_system/

# Create virtual environment (recommended)
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r deployment/requirements.txt
```

### Get Gemini API Key

1. Go to https://aistudio.google.com/app/apikey
2. Click "Create API key"
3. Copy the key

### Configure API Key

Create `.streamlit/secrets.toml`:

```toml
GEMINI_API_KEY = "your-api-key-here"
```

Or set environment variable:

```bash
# Windows
set GEMINI_API_KEY=your-key-here

# macOS/Linux
export GEMINI_API_KEY=your-key-here
```

### Prepare Data

```bash
# Copy documents and images
python setup_data.py

# Build vector database
python src/embeddings/build_vector_db.py
```

### Run Application

```bash
streamlit run app.py
```

Visit: http://localhost:8501

---

## Project Structure

```
rag_system/
├── app.py                      # Main Streamlit app
├── setup_data.py               # Data setup script
│
├── src/
│   ├── embeddings/
│   │   ├── document_processor.py    # Load & chunk documents
│   │   └── build_vector_db.py       # Build FAISS index
│   ├── retrieval/
│   │   └── vector_search.py         # FAISS search
│   ├── llm/
│   │   └── gemini_client.py         # Gemini API integration
│   └── ui/
│       └── image_handler.py         # Image detection & display
│
├── data/
│   ├── documents/              # Markdown docs (copied from RAG Docs)
│   ├── images/                 # PNG images (copied from RAG Docs)
│   └── vector_db/              # FAISS index files (generated)
│
├── config/
│   ├── prompts.yaml           # System prompts
│   ├── image_map.json         # Image keyword mappings
│   └── settings.yaml          # App settings (future)
│
├── deployment/
│   └── requirements.txt       # Python dependencies
│
└── docs/
    ├── DEPLOYMENT.md          # Deployment guide
    ├── DEVELOPMENT.md         # This file
    └── MAINTENANCE.md         # Maintenance guide
```

---

## Development Workflow

### Testing Components Individually

**Test Document Processor:**

```bash
python src/embeddings/document_processor.py
```

**Test Vector Search:**

```bash
python src/retrieval/vector_search.py
```

**Test Gemini Client:**

```bash
python src/llm/gemini_client.py
```

**Test Image Handler:**

```bash
python src/ui/image_handler.py
```

### Adding New Documents

1. Add markdown files to `data/documents/`
2. Rebuild vector DB:
   ```bash
   python src/embeddings/build_vector_db.py
   ```
3. Restart Streamlit app

### Modifying Prompts

1. Edit `config/prompts.yaml`
2. Restart Streamlit app (prompts are loaded at startup)

### Adding Image Mappings

1. Edit `config/image_map.json`
2. Add new keywords and image filenames
3. Add new images to `data/images/`
4. Restart Streamlit app

---

## Testing

### Manual Testing Checklist

**Basic Functionality:**
- [ ] App loads without errors
- [ ] Greeting message displays
- [ ] User can type and send messages
- [ ] Responses are generated

**Content Accuracy:**
- [ ] Answers stay within knowledge base
- [ ] No hallucinations (making up information)
- [ ] Responses cite source documents
- [ ] "I don't know" when appropriate

**Image Display:**
- [ ] Images load correctly
- [ ] Relevant images shown for queries
- [ ] Image captions are accurate
- [ ] Multiple images display in columns

**Safety Features:**
- [ ] Privacy warning on sensitive queries
- [ ] No credential requests
- [ ] Appropriate escalation to Discord/support

**Edge Cases:**
- [ ] Empty message handling
- [ ] Very long messages
- [ ] Special characters
- [ ] Multiple consecutive messages

### Test Queries

```python
# Setup questions
"How do I set up Dropbox?"
"How do I configure Google Drive?"
"What is IPTVBoss Pro?"

# Feature questions
"What's the difference between M3U and XC?"
"How do I create a layout?"
"How do I manage multiple users?"

# Troubleshooting
"My EPG isn't showing"
"Database won't load"
"Channels are missing"

# Out of scope
"What's my password?"
"How do I build a spaceship?"
"Tell me a joke"

# Sensitive information
"Here is my provider URL..."
"What's my API key?"
"Read my log file"
```

---

## Debugging

### Enable Debug Mode

In Streamlit sidebar:
- Check "Show debug info"

This displays:
- Retrieved chunks
- Similarity scores
- Source documents

### View Logs

Streamlit shows logs in terminal:

```bash
streamlit run app.py
```

Look for:
- `INFO` messages (normal operations)
- `WARNING` messages (potential issues)
- `ERROR` messages (failures)

### Common Issues

**"No module named X"**
```bash
pip install -r deployment/requirements.txt
```

**"File not found: data/vector_db"**
```bash
python src/embeddings/build_vector_db.py
```

**"FAISS index is empty"**
```bash
# Check documents exist
ls data/documents/

# Rebuild
python src/embeddings/build_vector_db.py
```

**"Gemini API error"**
- Check API key is set correctly
- Check API key is valid
- Check you haven't exceeded free tier limits

---

## Code Style

### Python Style Guide

- Follow PEP 8
- Use type hints
- Write docstrings for functions
- Keep functions focused and small

### Example:

```python
def search(
    self,
    query: str,
    top_k: int = 5,
    min_score: float = 0.3
) -> List[Dict[str, any]]:
    """
    Search for most relevant chunks

    Args:
        query: User query string
        top_k: Number of results to return
        min_score: Minimum similarity score

    Returns:
        List of dicts with text, source, and score
    """
    # Implementation
    pass
```

---

## Performance Optimization

### Vector Search Speed

Current: ~100-200ms for 3 results

To optimize:
- Use IVF (Inverted File) index for larger datasets
- Increase chunk size to reduce total chunks
- Use GPU acceleration (requires `faiss-gpu`)

### LLM Response Time

Current: ~3-5 seconds

To optimize:
- Use streaming responses (Gemini supports this)
- Reduce context size sent to LLM
- Use shorter prompts

### App Load Time

Current: ~2-3 seconds

To optimize:
- Lazy load components
- Cache embeddings in session state
- Use Streamlit caching decorators

---

## Adding New Features

### Example: Add User Feedback

1. **Add UI component** (in `app.py`):

```python
# After response
col1, col2 = st.columns(2)
with col1:
    if st.button("👍 Helpful"):
        log_feedback(True)
with col2:
    if st.button("👎 Not helpful"):
        log_feedback(False)
```

2. **Create feedback logger**:

```python
def log_feedback(helpful: bool):
    with open("feedback.log", "a") as f:
        f.write(f"{timestamp},{helpful}\n")
```

3. **Test locally**
4. **Commit and deploy**

---

## Contributing

### Before Committing

1. Test locally
2. Run all component tests
3. Check for errors in logs
4. Test on sample queries

### Commit Message Format

```
<type>: <description>

Types:
- feat: New feature
- fix: Bug fix
- docs: Documentation
- refactor: Code refactoring
- test: Tests
- chore: Maintenance

Examples:
feat: Add user feedback buttons
fix: Image display on mobile
docs: Update deployment guide
```

---

## Resources

- **Streamlit Docs**: https://docs.streamlit.io/
- **Gemini API Docs**: https://ai.google.dev/docs
- **FAISS Docs**: https://faiss.ai/
- **Sentence Transformers**: https://www.sbert.net/

---

## Getting Help

- Check [DEPLOYMENT.md](DEPLOYMENT.md) for deployment issues
- Check [MAINTENANCE.md](MAINTENANCE.md) for update procedures
- Review logs in Streamlit terminal
- Check Gemini API dashboard for quota/errors

---

**Happy developing! 🚀**
