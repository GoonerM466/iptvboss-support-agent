# Deployment Guide - IPTVBoss Support Agent

Complete guide to deploying the support agent to Streamlit Community Cloud.

---

## Prerequisites

1. **GitHub Account** (free)
2. **Google Gemini API Key** (free)
   - Get from: https://aistudio.google.com/app/apikey
3. **Streamlit Account** (free, sign in with GitHub)
   - https://share.streamlit.io/

---

## Step 1: Prepare the Repository

### 1.1 Copy Project to New Location

If you want to keep the RAG system separate:

```bash
# Copy rag_system folder to a new repository location
cp -r rag_system/ ~/my-iptv-support-agent/
cd ~/my-iptv-support-agent/
```

Or deploy from current location (in DiscordSupportBot).

### 1.2 Build Vector Database

```bash
# Install dependencies
pip install -r deployment/requirements.txt

# Copy data files
python setup_data.py

# Build vector database (this will take 1-2 minutes)
python src/embeddings/build_vector_db.py
```

You should see output like:
```
✅ Vector database built successfully!
📁 Output location: data/vector_db
📊 Total chunks: 150
📊 Total documents: 9
```

### 1.3 Test Locally (Recommended)

```bash
# Set API key
export GEMINI_API_KEY="your-key-here"

# Run app
streamlit run app.py
```

Visit http://localhost:8501 and test:
- Ask a question: "How do I set up Dropbox?"
- Verify images display correctly
- Check that responses stay on-topic

---

## Step 2: Create GitHub Repository

### 2.1 Initialize Git

```bash
# Initialize repository
git init

# Create .gitignore
cat > .gitignore << 'EOF'
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
venv/
.venv

# Streamlit
.streamlit/secrets.toml

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# Logs
*.log
EOF

# Add files
git add .
git commit -m "Initial commit: IPTVBoss Support Agent"
```

### 2.2 Push to GitHub

```bash
# Create repository on GitHub (via web interface)
# Then push:

git remote add origin https://github.com/YOUR_USERNAME/iptv-support-agent.git
git branch -M main
git push -u origin main
```

**Important**: Make sure all these files are committed:
- `data/vector_db/` (FAISS index files)
- `data/images/` (all 43 PNG files)
- `data/documents/` (all markdown files)

---

## Step 3: Deploy to Streamlit Cloud

### 3.1 Sign In to Streamlit

1. Go to https://share.streamlit.io/
2. Click "Sign in" (use GitHub account)
3. Authorize Streamlit to access your GitHub

### 3.2 Create New App

1. Click "New app"
2. Select your repository: `YOUR_USERNAME/iptv-support-agent`
3. Branch: `main`
4. Main file path: `app.py`
5. App URL: Choose a name (e.g., `iptv-support.streamlit.app`)

### 3.3 Configure Secrets

Before deploying, add your Gemini API key:

1. Click "Advanced settings"
2. In "Secrets" section, add:

```toml
GEMINI_API_KEY = "your-actual-gemini-api-key-here"
```

3. Click "Save"

### 3.4 Deploy

1. Click "Deploy!"
2. Wait 2-5 minutes for deployment
3. App will be available at your chosen URL

---

## Step 4: Test Deployment

### 4.1 Smoke Tests

Visit your app URL and test:

1. **Greeting shows**: Should see welcome message
2. **Ask question**: "How do I set up Dropbox?"
   - Should get step-by-step answer
   - Should show relevant images (image3-6)
3. **Test edge case**: "What's my password?"
   - Should show privacy warning
4. **Test unknown**: "How do I build a spaceship?"
   - Should say "I don't have that information"

### 4.2 Verify Images

- Images should load and display correctly
- Image captions should be accurate
- Multiple images should display in columns

### 4.3 Check Performance

- First load: ~10-15 seconds (cold start)
- Subsequent loads: ~2-3 seconds
- Answer generation: ~3-5 seconds

---

## Step 5: Share with Users

### 5.1 Get App URL

Your app URL will be: `https://YOUR-APP-NAME.streamlit.app`

### 5.2 Create Landing Page (Optional)

Add a README.md to your repository:

```markdown
# IPTVBoss Support Agent

AI-powered support assistant for IPTVBoss & EPGBoss.

## Use the Agent

Visit: [https://your-app-name.streamlit.app](https://your-app-name.streamlit.app)

## Features

- Answers questions from official documentation
- Shows relevant screenshots and guides
- Available 24/7, no login required

## Support

For complex issues, visit:
- [Discord Support](https://discord.gg/QCxpA9yvWP)
- [Official Website](https://members.bosstees.net)
```

---

## Troubleshooting

### App Won't Start

**Error**: "File not found: data/vector_db"

**Solution**: Make sure you committed the vector database files:
```bash
git add data/vector_db/
git commit -m "Add vector database"
git push
```

### Images Not Loading

**Error**: Images show as broken

**Solution**: Check that images are committed:
```bash
git add data/images/*.png
git commit -m "Add images"
git push
```

### "No module named X"

**Solution**: Check `deployment/requirements.txt` includes all dependencies

### Gemini API Error

**Error**: "API key not configured"

**Solution**:
1. Go to Streamlit Cloud dashboard
2. Click your app → Settings → Secrets
3. Add `GEMINI_API_KEY = "your-key"`
4. Click "Save" and restart app

### App is Slow

**Normal behavior**:
- First load after inactivity: 10-15 seconds (cold start)
- This is expected on free tier

**If consistently slow**:
- Check Streamlit Cloud status
- Try restarting app from dashboard

---

## Updating the App

### Update Documentation

1. Edit files in `data/documents/`
2. Rebuild vector DB: `python src/embeddings/build_vector_db.py`
3. Commit and push:
   ```bash
   git add data/
   git commit -m "Update documentation"
   git push
   ```
4. Streamlit auto-deploys within 1-2 minutes

### Update Prompts

1. Edit `config/prompts.yaml`
2. Commit and push:
   ```bash
   git add config/prompts.yaml
   git commit -m "Update prompts"
   git push
   ```

### Update Code

1. Edit Python files
2. Test locally: `streamlit run app.py`
3. Commit and push
4. Wait for auto-deployment

---

## Monitoring

### Usage Stats

Streamlit Cloud provides:
- Total visitors
- Active users
- Page views

Access from: Dashboard → Your App → Analytics

### Gemini API Usage

Check usage at: https://aistudio.google.com/app/apikey

Free tier limits:
- 15 requests/minute
- 1500 requests/day
- 1 million requests/month

For 5 users/day, you'll use ~30-50 requests/day (well within limits).

---

## Cost Summary

✅ **Total Cost: $0/month forever**

- Streamlit Cloud: Free tier (unlimited for public apps)
- Gemini API: Free tier (1500 requests/day)
- GitHub: Free tier
- FAISS: Local, no hosting cost

---

## Support

- **App issues**: Check Streamlit Cloud dashboard logs
- **API issues**: Check Gemini API dashboard
- **Code issues**: See [DEVELOPMENT.md](DEVELOPMENT.md)

---

**Deployment complete! 🚀**

Your support agent is now live and available to users 24/7.
