# Quick Start Guide - IPTVBoss Support Agent

Get your support agent running in 10 minutes.

---

## What You're Building

A free, AI-powered support chatbot that:
- ✅ Answers IPTVBoss questions from your documentation
- ✅ Shows relevant screenshots automatically
- ✅ Runs 24/7 on free cloud hosting
- ✅ Costs $0/month forever

---

## Prerequisites (2 minutes)

1. **Python 3.9+** installed
2. **Git** installed
3. **Accounts** (all free):
   - GitHub account
   - Google account (for Gemini API)

---

## Step 1: Get Gemini API Key (2 minutes)

1. Go to https://aistudio.google.com/app/apikey
2. Click **"Create API key"**
3. Copy the key (starts with `AIza...`)

---

## Step 2: Setup Locally (3 minutes)

```bash
# Navigate to the project
cd rag_system/

# Install dependencies
pip install -r deployment/requirements.txt

# Copy data files
python setup_data.py

# Build vector database
python src/embeddings/build_vector_db.py
```

Expected output:
```
✅ Vector database built successfully!
📊 Total chunks: ~150
📊 Total documents: 9
```

---

## Step 3: Configure API Key (1 minute)

**Option A: Environment Variable**

```bash
# Windows
set GEMINI_API_KEY=your-key-here

# macOS/Linux
export GEMINI_API_KEY=your-key-here
```

**Option B: Secrets File** (Recommended)

Create `.streamlit/secrets.toml`:

```toml
GEMINI_API_KEY = "your-key-here"
```

---

## Step 4: Test Locally (2 minutes)

```bash
streamlit run app.py
```

Visit http://localhost:8501

**Test queries:**
- "How do I set up Dropbox?"
- "My EPG isn't showing"
- "What's the difference between M3U and XC?"

✅ Verify images display correctly

---

## Step 5: Deploy to Cloud (3 minutes)

### 5.1 Push to GitHub

```bash
# Initialize git (if not already)
git init
git add .
git commit -m "Initial commit: IPTVBoss Support Agent"

# Create repository on GitHub
# Then push:
git remote add origin https://github.com/GoonerM466/iptvboss-support-agent.git
git branch -M main
git push -u origin main
```

### 5.2 Deploy to Streamlit Cloud

1. Go to https://share.streamlit.io/
2. Click **"New app"**
3. Select your repository
4. Main file: `app.py`
5. **Advanced settings** → **Secrets**:
   ```toml
   GEMINI_API_KEY = "your-key-here"
   ```
6. Click **"Deploy!"**

Wait 2-5 minutes... Done! 🎉

---

## You're Live!

Your agent is now available at:
```
https://your-app-name.streamlit.app
```

Share this URL with your users!

---

## Next Steps

- Read [docs/DEPLOYMENT.md](docs/DEPLOYMENT.md) for detailed deployment info
- Read [docs/MAINTENANCE.md](docs/MAINTENANCE.md) to learn how to update docs
- Monitor usage at https://share.streamlit.io/

---

## Troubleshooting

**"No module named X"**
```bash
pip install -r deployment/requirements.txt
```

**"Vector DB not found"**
```bash
python src/embeddings/build_vector_db.py
```

**"API key error"**
- Check your GEMINI_API_KEY is set correctly
- Verify it's valid at https://aistudio.google.com/app/apikey

**App won't start on Streamlit Cloud**
- Make sure you committed all files (including `data/` directory)
- Check logs in Streamlit Cloud dashboard

---

## Support

Need help? Check:
- [docs/DEPLOYMENT.md](docs/DEPLOYMENT.md) - Full deployment guide
- [docs/DEVELOPMENT.md](docs/DEVELOPMENT.md) - Development guide
- [docs/MAINTENANCE.md](docs/MAINTENANCE.md) - Maintenance guide

---

**Total time: ~10 minutes**
**Total cost: $0 forever**

Enjoy your AI support agent! 🚀
