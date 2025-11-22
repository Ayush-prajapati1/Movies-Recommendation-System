# 🎬 Movie Recommendation System - Website Version

A beautiful, modern web application for movie recommendations built with **React** (frontend) and **Flask** (backend API).

## ✨ Features

- 🎨 **Modern UI** - Beautiful gradient design with smooth animations
- 🔍 **Search Movies** - Find movies by title, platform, or genre
- 💡 **Smart Recommendations** - Multiple recommendation algorithms
- 📊 **Browse Movies** - Explore all movies with filters and sorting
- 👤 **User-Based Recommendations** - Collaborative filtering
- 📱 **Responsive Design** - Works on desktop, tablet, and mobile

## 🚀 Quick Start

### Option 1: Using Batch Files (Windows)

1. **Install dependencies first:**
   ```bash
   pip install -r requirements.txt
   cd frontend
   npm install
   cd ..
   ```

2. **Start Backend:**
   - Double-click `start_backend.bat` or run it from terminal

3. **Start Frontend:**
   - Open a new terminal
   - Double-click `start_frontend.bat` or run it from terminal

### Option 2: Manual Start

**Terminal 1 - Backend:**
```bash
python api_server.py
```

**Terminal 2 - Frontend:**
```bash
cd frontend
npm start
```

Then open http://localhost:3000 in your browser.

## 📖 Detailed Setup

See [WEBSITE_SETUP.md](WEBSITE_SETUP.md) for complete setup instructions.

## 🏗️ Architecture

```
┌─────────────────┐         HTTP/REST API         ┌─────────────────┐
│                 │ ◄─────────────────────────────► │                 │
│  React Frontend │                                 │  Flask Backend  │
│  (Port 3000)    │                                 │  (Port 5000)    │
│                 │                                 │                 │
└─────────────────┘                                 └─────────────────┘
                                                           │
                                                           ▼
                                                  ┌─────────────────┐
                                                  │ Recommendation  │
                                                  │     Engine      │
                                                  └─────────────────┘
```

## 🎯 API Endpoints

The Flask backend provides these REST API endpoints:

- `GET /api/health` - Health check
- `GET /api/movies` - Get all movies (with filters)
- `GET /api/movies/search` - Search movies
- `POST /api/recommendations/content-based` - Content-based recommendations
- `POST /api/recommendations/collaborative` - Collaborative filtering
- `POST /api/recommendations/hybrid` - Hybrid recommendations
- `GET /api/platforms` - Get all platforms
- `GET /api/genres` - Get all genres
- `GET /api/movie-titles` - Get all movie titles
- `GET /api/users` - Get all user IDs

## 🛠️ Technologies

### Frontend
- **React 18** - UI framework
- **Axios** - HTTP client
- **CSS3** - Styling with gradients and animations
- **Google Fonts (Poppins)** - Typography

### Backend
- **Flask** - Web framework
- **Flask-CORS** - Cross-origin resource sharing
- **Pandas** - Data manipulation
- **Scikit-learn** - Machine learning algorithms
- **NumPy & SciPy** - Numerical computations

## 📱 Screenshots

The website includes:
- Beautiful gradient header
- Tab-based navigation
- Movie cards with platform badges
- Search and filter forms
- Recommendation forms with sliders
- Responsive grid layouts

## 🔧 Development

### Frontend Development
```bash
cd frontend
npm start
```
Runs on http://localhost:3000 with hot reload.

### Backend Development
```bash
python api_server.py
```
Runs on http://localhost:5000 with debug mode.

### Building for Production
```bash
cd frontend
npm run build
```

## 📝 Notes

- Both servers must run simultaneously
- Backend must start before frontend
- React app automatically connects to Flask API
- All data is generated locally (no external APIs)

## 🐛 Troubleshooting

See [WEBSITE_SETUP.md](WEBSITE_SETUP.md) for troubleshooting guide.

## 📄 License

This project is open source and available for educational purposes.

---

**Built with ❤️ using React and Flask**

