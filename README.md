# IPTVBoss Support Agent - RAG System

## Overview
AI-powered customer support agent for IPTVBoss/EPGBoss using Retrieval Augmented Generation (RAG).

**Features:**
- Answers questions based ONLY on provided documentation
- Displays relevant troubleshooting images
- Zero-cost deployment (Streamlit Cloud + Gemini API free tier)
- ~5 users/day capacity

## Architecture

```
User Question
    ↓
Streamlit UI
    ↓
Embedding Model (sentence-transformers)
    ↓
FAISS Vector Search
    ↓
Context Retrieval
    ↓
Gemini 2.0 Flash API (with strict prompts)
    ↓
Response + Conditional Image Display
```

## Tech Stack

- **Frontend**: Streamlit
- **Vector DB**: FAISS (local, in-memory)
- **Embeddings**: sentence-transformers (all-MiniLM-L6-v2)
- **LLM**: Google Gemini 2.0 Flash (free tier: 1500 requests/day)
- **Hosting**: Streamlit Community Cloud (free, unlimited)
- **Images**: Static files in repository

## Project Structure

```
rag_system/
├── src/
│   ├── embeddings/          # Document processing & embedding generation
│   ├── retrieval/           # FAISS vector search
│   ├── llm/                 # Gemini API integration & prompts
│   └── ui/                  # Streamlit interface
├── data/
│   ├── documents/           # Source markdown docs (copied from RAG Docs)
│   ├── images/              # 43 image files (copied from RAG Docs)
│   └── vector_db/           # FAISS index files
├── config/
│   ├── prompts.yaml         # System prompts and templates
│   ├── image_map.json       # Image-to-topic mapping
│   └── settings.yaml        # App configuration
├── deployment/
│   ├── streamlit_config.toml
│   ├── .streamlit/
│   └── requirements.txt
├── docs/
│   ├── DEPLOYMENT.md        # How to deploy to Streamlit Cloud
│   ├── DEVELOPMENT.md       # Local development setup
│   └── MAINTENANCE.md       # How to update knowledge base
├── app.py                   # Main Streamlit application
└── README.md               # This file
```

## Quick Start (Local Development)

1. **Install dependencies:**
   ```bash
   pip install -r deployment/requirements.txt
   ```

2. **Set up Gemini API key:**
   ```bash
   # Get free API key from https://aistudio.google.com/app/apikey
   # Create .streamlit/secrets.toml:
   echo 'GEMINI_API_KEY = "your-key-here"' > .streamlit/secrets.toml
   ```

3. **Build vector database:**
   ```bash
   python src/embeddings/build_vector_db.py
   ```

4. **Run app:**
   ```bash
   streamlit run app.py
   ```

## Deployment to Streamlit Cloud

See [docs/DEPLOYMENT.md](docs/DEPLOYMENT.md) for complete instructions.

**Summary:**
1. Push to GitHub repository
2. Go to https://share.streamlit.io/
3. Connect repository
4. Add `GEMINI_API_KEY` to secrets
5. Deploy (automatic)

## Knowledge Base

**Documentation Files (9 total):**
- `documentation/` folder (6 files):
  - FAQ.md
  - Known_Issues.md
  - Quick_Start.md
  - README.md
  - Troubleshooting_Guide.md
  - User_Guide.md
- `references/` folder (3 files):
  - folder_locations.md
  - image_reference_catalog.md
  - menu_structure.md

**Images:**
- 43 PNG images (image1.png through image43.png)
- Screenshots for troubleshooting and setup guides

**Total size:** ~15MB (well within free tier limits)

## Anti-Hallucination Strategy

1. **Strict RAG pipeline**: Only retrieved context sent to LLM
2. **System prompts**: "Answer ONLY from context, never from general knowledge"
3. **Confidence threshold**: Minimum similarity score of 0.65
4. **Fallback responses**: "I don't have that information" when uncertain
5. **Grounded generation**: Gemini's built-in grounding features
6. **Response validation**: Check if answer references retrieved context

## Cost Analysis

**Permanently Free:**
- Gemini API: 1500 requests/day free tier (5 users/day = ~30-50 requests/day)
- Streamlit Cloud: Unlimited free hosting for public apps
- FAISS: Local, no hosting costs
- Sentence-transformers: Local, no API costs

**Total cost: $0/month forever** ✅

## Limitations

- Public access only (no authentication in v1)
- 1500 Gemini requests/day limit (more than sufficient)
- Streamlit Cloud apps sleep after inactivity (wake on first request)
- Knowledge base updates require redeployment

## Maintenance

**To update knowledge base:**
1. Replace files in `data/documents/` and `data/references/`
2. Run `python src/embeddings/build_vector_db.py`
3. Commit and push to GitHub
4. Streamlit Cloud auto-redeploys

See [docs/MAINTENANCE.md](docs/MAINTENANCE.md) for details.

## Support

- **Developer**: Built for IPTVBoss/EPGBoss support
- **Issues**: Contact project maintainer
- **Updates**: See git commit history

---

**Status**: In Development
**Last Updated**: December 2, 2024
