# 🌐 How to Run the Website in Your Browser

## Step-by-Step Instructions

### Prerequisites Check
Before starting, make sure you have:
- ✅ Python installed (check with: `python --version`)
- ✅ Node.js installed (check with: `node --version`)
- ✅ All dependencies installed (see Step 1 below)

---

## Step 1: Install Dependencies (One-Time Setup)

### Install Python Dependencies
Open Command Prompt or PowerShell in the project folder and run:

```bash
pip install -r requirements.txt
```

**Wait for installation to complete** (may take 2-5 minutes)

### Install React Dependencies
In the same terminal, run:

```bash
cd frontend
npm install
cd ..
```

**Wait for installation to complete** (may take 3-5 minutes)

---

## Step 2: Start the Backend Server

### Option A: Using Batch File (Windows)
1. Double-click `start_backend.bat` in the project folder
2. A terminal window will open showing the server starting
3. **Keep this window open!**

### Option B: Using Command Line
1. Open Command Prompt or PowerShell
2. Navigate to the project folder:
   ```bash
   cd "C:\movies recommendations project"
   ```
3. Run:
   ```bash
   python api_server.py
   ```
4. You should see:
   ```
   🎬 Movie Recommendation API Server
   Server starting on http://localhost:5000
   ```
5. **Keep this terminal open!**

---

## Step 3: Start the Frontend (React App)

### Option A: Using Batch File (Windows)
1. Open a **NEW** Command Prompt or PowerShell window
2. Navigate to the project folder:
   ```bash
   cd "C:\movies recommendations project"
   ```
3. Double-click `start_frontend.bat`
4. Or run manually:
   ```bash
   cd frontend
   npm start
   ```

### Option B: Using Command Line
1. Open a **NEW** terminal window (keep the backend terminal open!)
2. Navigate to the project folder:
   ```bash
   cd "C:\movies recommendations project"
   ```
3. Navigate to frontend folder:
   ```bash
   cd frontend
   ```
4. Start React:
   ```bash
   npm start
   ```

---

## Step 4: Open in Browser

After running `npm start`, one of these will happen:

### Automatic (Most Common)
- Your default browser will **automatically open**
- The website will load at: `http://localhost:3000`

### Manual (If browser doesn't open)
1. Open any web browser (Chrome, Firefox, Edge, etc.)
2. Type in the address bar:
   ```
   http://localhost:3000
   ```
3. Press Enter

---

## ✅ What You Should See

### In the Browser:
- Beautiful purple gradient header
- "Movie Recommendation System" title
- Four tabs: Search Movies, Recommendations, Browse All, User Recommendations
- The website is ready to use!

### In the Terminals:
- **Backend terminal:** Shows Flask server running on port 5000
- **Frontend terminal:** Shows React app running on port 3000

---

## 🎯 Using the Website

1. **Search Movies Tab:**
   - Enter a movie title, select platform/genre
   - Click "Search"
   - See results below

2. **Recommendations Tab:**
   - Choose "Content-Based" or "Hybrid"
   - Select a movie you like (or rate multiple movies)
   - Click "Get Recommendations"
   - See personalized recommendations

3. **Browse All Tab:**
   - Use filters to find movies
   - Sort by rating, year, or title
   - Browse all available movies

4. **User Recommendations Tab:**
   - Select a user ID
   - Click "Get User Recommendations"
   - See collaborative filtering results

---

## ⚠️ Important Notes

### Keep Both Terminals Open!
- The backend terminal must stay open (Flask server)
- The frontend terminal must stay open (React app)
- Closing either will stop that part of the website

### To Stop the Website:
1. Go to each terminal window
2. Press `Ctrl + C`
3. Confirm if asked

### To Restart:
Just run the commands again in the same order!

---

## 🐛 Troubleshooting

### Problem: Browser shows "Cannot connect" or blank page
**Solution:**
- Make sure backend is running (Step 2)
- Make sure frontend is running (Step 3)
- Check both terminals for errors
- Try refreshing the browser (F5)

### Problem: "npm is not recognized"
**Solution:**
- Install Node.js from https://nodejs.org/
- Restart your terminal after installation
- Try again

### Problem: "python is not recognized"
**Solution:**
- Make sure Python is installed
- Try: `python3 api_server.py` instead
- Or: `py api_server.py`

### Problem: Port 3000 already in use
**Solution:**
- React will ask: "Would you like to run the app on another port instead?"
- Type `Y` and press Enter
- Use the new port shown (e.g., http://localhost:3001)

### Problem: Port 5000 already in use
**Solution:**
1. Close the program using port 5000
2. Or change the port in `api_server.py`:
   - Change `port=5000` to `port=5001`
   - Update `frontend/src/services/api.js`:
     - Change `http://localhost:5000` to `http://localhost:5001`

### Problem: "ModuleNotFoundError"
**Solution:**
- Run: `pip install -r requirements.txt`
- Make sure you're in the project root folder

### Problem: Website loads but shows errors
**Solution:**
1. Open browser Developer Tools (F12)
2. Check the Console tab for errors
3. Make sure backend is running on port 5000
4. Check Network tab to see if API calls are failing

---

## 📋 Quick Checklist

Before running, make sure:
- [ ] Python dependencies installed (`pip install -r requirements.txt`)
- [ ] React dependencies installed (`cd frontend && npm install`)
- [ ] Two terminal windows ready
- [ ] Backend server started (`python api_server.py`)
- [ ] Frontend started (`cd frontend && npm start`)
- [ ] Browser opened to http://localhost:3000

---

## 🎉 Success!

If you see the website with the purple gradient header and tabs, you're all set!

**Enjoy exploring movie recommendations! 🎬🍿**




