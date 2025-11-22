# 🌐 Website Setup Guide - React + Flask

This guide will help you set up and run the Movie Recommendation System website with React frontend and Flask backend.

## 📋 Prerequisites

- **Python 3.8+** installed
- **Node.js 16+** and **npm** installed
- Two terminal windows/command prompts

## 🚀 Quick Start

### Step 1: Install Python Dependencies

Open a terminal in the project root directory and run:

```bash
pip install -r requirements.txt
```

This installs:
- Flask (web server)
- flask-cors (for React to communicate with Flask)
- All other Python dependencies

### Step 2: Install React Dependencies

Navigate to the frontend folder and install Node.js packages:

```bash
cd frontend
npm install
```

This will install:
- React
- React DOM
- Axios (for API calls)
- React Scripts

**Note:** This may take a few minutes on first run.

### Step 3: Start the Backend Server

In the **first terminal**, from the project root directory, run:

```bash
python api_server.py
```

You should see:
```
🎬 Movie Recommendation API Server
Server starting on http://localhost:5000
API endpoints available at http://localhost:5000/api/
```

**Keep this terminal open!** The backend must be running for the website to work.

### Step 4: Start the React Frontend

In a **second terminal**, navigate to the frontend folder and run:

```bash
cd frontend
npm start
```

This will:
- Start the React development server
- Automatically open your browser at `http://localhost:3000`
- If it doesn't open automatically, go to `http://localhost:3000` manually

**Keep this terminal open too!**

## ✅ You're All Set!

The website should now be running:
- **Frontend:** http://localhost:3000
- **Backend API:** http://localhost:5000

## 🎯 Using the Website

1. **Search Movies** - Find movies by title, platform, or genre
2. **Get Recommendations** - Choose content-based or hybrid recommendations
3. **Browse All Movies** - Explore all available movies with filters
4. **User Recommendations** - Get collaborative filtering recommendations

## 🛠️ Troubleshooting

### Problem: "ModuleNotFoundError: No module named 'flask'"
**Solution:** Make sure you installed Python dependencies:
```bash
pip install -r requirements.txt
```

### Problem: "npm is not recognized"
**Solution:** 
- Install Node.js from https://nodejs.org/
- Restart your terminal after installation

### Problem: "Cannot connect to API"
**Solution:**
- Make sure the backend server is running (`python api_server.py`)
- Check that it's running on port 5000
- Make sure there are no firewall issues

### Problem: Port 3000 or 5000 already in use
**Solution:**
- **For React (port 3000):** The terminal will ask if you want to use a different port. Type 'Y'
- **For Flask (port 5000):** Edit `api_server.py` and change `port=5000` to another port (e.g., `port=5001`), then update `frontend/src/services/api.js` to use the new port

### Problem: CORS errors in browser console
**Solution:** 
- Make sure `flask-cors` is installed: `pip install flask-cors`
- Restart the backend server

### Problem: "npm install" fails
**Solution:**
- Try: `npm install --legacy-peer-deps`
- Or: `npm cache clean --force` then `npm install`

## 📁 Project Structure

```
movies-recommendations-project/
├── api_server.py              # Flask backend API
├── movie_data.py              # Movie dataset
├── recommendation_engine.py   # Recommendation algorithms
├── requirements.txt           # Python dependencies
├── frontend/
│   ├── package.json          # React dependencies
│   ├── public/
│   │   └── index.html        # HTML template
│   └── src/
│       ├── App.js            # Main React component
│       ├── components/       # React components
│       └── services/
│           └── api.js        # API service
└── WEBSITE_SETUP.md          # This file
```

## 🔧 Development Tips

### Making Changes

- **Frontend changes:** React will automatically reload when you save files
- **Backend changes:** You need to restart the Flask server (Ctrl+C, then run again)

### Testing the API

You can test the API directly in your browser or using curl:

```bash
# Health check
curl http://localhost:5000/api/health

# Get all movies
curl http://localhost:5000/api/movies

# Get platforms
curl http://localhost:5000/api/platforms
```

### Building for Production

To create a production build of the React app:

```bash
cd frontend
npm run build
```

This creates an optimized build in the `frontend/build` folder.

## 🎨 Features

- ✅ Modern, responsive design
- ✅ Search and filter movies
- ✅ Content-based recommendations
- ✅ Collaborative filtering
- ✅ Hybrid recommendations
- ✅ Browse all movies
- ✅ Beautiful UI with gradients and animations

## 📝 Notes

- The backend and frontend must run simultaneously
- The React app communicates with Flask via REST API
- All movie data is generated locally (no external API needed)
- The system uses simulated user ratings for collaborative filtering

## 🆘 Need Help?

1. Check that both servers are running
2. Check browser console for errors (F12)
3. Check terminal output for backend errors
4. Make sure all dependencies are installed
5. Try restarting both servers

---

**Enjoy your Movie Recommendation Website! 🎬🍿**

