# ⚡ Quick Start - Website Version

## 🎯 Run the Website in 3 Steps

### Step 1: Install Dependencies

**Python (Backend):**
```bash
pip install -r requirements.txt
```

**Node.js (Frontend):**
```bash
cd frontend
npm install
cd ..
```

### Step 2: Start Backend (Terminal 1)

```bash
python api_server.py
```

Wait for: `Server starting on http://localhost:5000`

### Step 3: Start Frontend (Terminal 2)

```bash
cd frontend
npm start
```

Browser opens automatically at: `http://localhost:3000`

## ✅ Done!

Your website is now running! 🎉

## 🎬 What You Can Do

1. **Search Movies** - Find by title, platform, genre
2. **Get Recommendations** - Content-based or hybrid
3. **Browse All** - Explore with filters
4. **User Recommendations** - Collaborative filtering

## 📝 Important Notes

- Keep both terminals open
- Backend must run before frontend
- If port 3000 is busy, React will ask to use another port
- If port 5000 is busy, change it in `api_server.py`

## 🆘 Quick Fixes

**"ModuleNotFoundError"** → Run `pip install -r requirements.txt`

**"npm is not recognized"** → Install Node.js from nodejs.org

**"Cannot connect to API"** → Make sure backend is running on port 5000

---

For detailed instructions, see [WEBSITE_SETUP.md](WEBSITE_SETUP.md)

