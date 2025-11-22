# 🚀 Quick Start Guide

## Step-by-Step Instructions to Run the Movie Recommendation System

### Prerequisites
- Python 3.8 or higher installed on your system
- pip (usually comes with Python)

### Step 1: Open Terminal/Command Prompt

**On Windows:**
- Press `Win + R`, type `cmd` or `powershell`, and press Enter
- Or search for "Command Prompt" or "PowerShell" in the Start menu

**Navigate to the project folder:**
```bash
cd "C:\movies recommendations project"
```

### Step 2: Install Required Packages

Install all the necessary Python libraries:

```bash
pip install -r requirements.txt
```

**Note:** If you get permission errors, try:
```bash
pip install --user -r requirements.txt
```

**Or if you're using Python 3 specifically:**
```bash
python -m pip install -r requirements.txt
```

Wait for the installation to complete. This may take a few minutes.

### Step 3: Choose How to Run

You have **3 options** to run the project:

---

## Option 1: Web Interface (Recommended) 🌐

Run the Streamlit web application:

```bash
streamlit run app.py
```

**What happens:**
- A browser window will automatically open
- If it doesn't, go to: `http://localhost:8501`
- You'll see a beautiful web interface with all features

**To stop:** Press `Ctrl + C` in the terminal

---

## Option 2: Command Line Interface 💻

Run the interactive CLI:

```bash
python cli_app.py
```

**What happens:**
- An interactive menu will appear in your terminal
- Follow the on-screen prompts to use the system
- Type numbers to select options

**To exit:** Choose option 6 or press `Ctrl + C`

---

## Option 3: Run Example Script 📝

See how the system works programmatically:

```bash
python example_usage.py
```

**What happens:**
- Shows example outputs of all recommendation types
- Demonstrates the system's capabilities
- Good for understanding how it works

---

## Troubleshooting

### Problem: "pip is not recognized"
**Solution:** 
- Make sure Python is installed: `python --version`
- Try: `python -m pip install -r requirements.txt`

### Problem: "ModuleNotFoundError" when running
**Solution:**
- Make sure you installed requirements: `pip install -r requirements.txt`
- Check if you're in the correct directory

### Problem: Port 8501 already in use (Streamlit)
**Solution:**
- Close other Streamlit apps
- Or use a different port: `streamlit run app.py --server.port 8502`

### Problem: Installation takes too long
**Solution:**
- This is normal for the first time
- The packages (especially scikit-learn and numpy) are large
- Be patient, it should complete in 2-5 minutes

---

## First Time Usage Tips

1. **Start with the Web Interface** - It's the easiest to use
2. **Try Content-Based Recommendations** - Select a movie you like (e.g., "Inception")
3. **Explore Search** - Search for movies by title, platform, or genre
4. **Try Hybrid Recommendations** - Rate 3-5 movies for personalized suggestions

---

## Need Help?

- Check the `README.md` file for detailed documentation
- Review `example_usage.py` to see code examples
- Make sure all files are in the same folder

---

**Enjoy your movie recommendations! 🎬🍿**

