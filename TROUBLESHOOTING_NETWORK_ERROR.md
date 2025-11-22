# 🔧 Fixing Network Error - Step by Step

## The Error You're Seeing
```
AxiosError: Network Error
```

This means the React frontend **cannot connect** to the Flask backend API.

---

## ✅ Solution Steps

### Step 1: Check if Backend is Running

**Open a terminal and check:**

1. Look for a terminal window running `python api_server.py`
2. You should see:
   ```
   🎬 Movie Recommendation API Server
   Server starting on http://localhost:5000
   ```

**If backend is NOT running:**

1. Open Command Prompt or PowerShell
2. Navigate to project folder:
   ```bash
   cd "C:\movies recommendations project"
   ```
3. Start backend:
   ```bash
   python api_server.py
   ```
4. **Keep this terminal open!**

---

### Step 2: Verify Backend is Working

**Test the backend in your browser:**

1. Open a new browser tab
2. Go to: `http://localhost:5000/api/health`
3. You should see:
   ```json
   {"status":"ok","message":"Movie Recommendation API is running"}
   ```

**If you see an error:**
- Backend is not running → Go back to Step 1
- Port 5000 is in use → See "Port Issues" below

---

### Step 3: Restart Frontend

**After backend is running:**

1. Go to the terminal running React (where you ran `npm start`)
2. Press `Ctrl + C` to stop it
3. Restart it:
   ```bash
   cd frontend
   npm start
   ```

**Or if using batch file:**
- Close the frontend terminal
- Double-click `start_frontend.bat` again

---

### Step 4: Clear Browser Cache

**Sometimes the browser caches old errors:**

1. Press `Ctrl + Shift + R` (hard refresh)
2. Or press `F12` → Right-click refresh button → "Empty Cache and Hard Reload"

---

## 🔍 Common Issues & Fixes

### Issue 1: Backend Not Running
**Symptom:** Network Error in browser console

**Fix:**
```bash
# Terminal 1
python api_server.py
```

**Verify:** Open `http://localhost:5000/api/health` in browser

---

### Issue 2: Port 5000 Already in Use
**Symptom:** Backend won't start, shows "Address already in use"

**Fix Option A - Close the program using port 5000:**
```bash
# Windows - Find what's using port 5000
netstat -ano | findstr :5000

# Kill the process (replace PID with the number from above)
taskkill /PID <PID> /F
```

**Fix Option B - Use a different port:**

1. Edit `api_server.py`:
   - Change line 161: `app.run(debug=True, port=5001)`

2. Edit `frontend/src/services/api.js`:
   - Change line 3: `const API_BASE_URL = 'http://localhost:5001/api';`

3. Restart both servers

---

### Issue 3: CORS Error
**Symptom:** CORS policy error in browser console

**Fix:** The code has been updated to fix CORS. Make sure:
1. `flask-cors` is installed: `pip install flask-cors`
2. Restart the backend server

---

### Issue 4: Firewall Blocking Connection
**Symptom:** Backend runs but frontend can't connect

**Fix:**
1. Windows Firewall may be blocking Python
2. When backend starts, Windows may ask for permission
3. Click "Allow access"

---

### Issue 5: Wrong API URL
**Symptom:** Network error persists

**Check:**
1. Open `frontend/src/services/api.js`
2. Make sure line 3 says: `const API_BASE_URL = 'http://localhost:5000/api';`
3. If you changed the port, update this too

---

## 🧪 Testing Checklist

Run through this checklist:

- [ ] Backend terminal shows "Server starting on http://localhost:5000"
- [ ] `http://localhost:5000/api/health` works in browser
- [ ] Frontend terminal shows "Compiled successfully!"
- [ ] Browser is at `http://localhost:3000`
- [ ] No errors in backend terminal
- [ ] Browser console (F12) shows no CORS errors

---

## 🚀 Quick Fix Command Sequence

**If nothing works, try this complete restart:**

```bash
# Terminal 1 - Backend
cd "C:\movies recommendations project"
python api_server.py

# Terminal 2 - Frontend (wait for backend to start first)
cd "C:\movies recommendations project\frontend"
npm start
```

**Then:**
1. Wait for both to start
2. Open browser to `http://localhost:3000`
3. Press `Ctrl + Shift + R` to hard refresh

---

## 📞 Still Not Working?

**Check these:**

1. **Python version:**
   ```bash
   python --version
   ```
   Should be 3.8 or higher

2. **Node.js version:**
   ```bash
   node --version
   ```
   Should be 16 or higher

3. **Dependencies installed:**
   ```bash
   pip list | findstr flask
   npm list --depth=0
   ```

4. **Backend logs:**
   - Check the backend terminal for any error messages
   - Look for import errors or missing modules

5. **Browser console:**
   - Press F12 in browser
   - Check Console tab for detailed errors
   - Check Network tab to see if requests are being made

---

## ✅ Success Indicators

You'll know it's working when:

1. ✅ Backend terminal shows: "Running on http://127.0.0.1:5000"
2. ✅ Frontend terminal shows: "Compiled successfully!"
3. ✅ Browser shows the website with purple gradient header
4. ✅ No errors in browser console (F12)
5. ✅ You can search for movies and get results

---

**Most common fix: Just make sure the backend is running!** 🎯




