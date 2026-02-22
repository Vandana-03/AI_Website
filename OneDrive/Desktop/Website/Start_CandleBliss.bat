@echo off
REM Candles Website Launcher
REM This batch file starts the Flask development server

echo.
echo ========================================
echo     ✨  CANDLES WEBSITE  ✨
echo ========================================
echo.

REM Navigate to the project directory
cd /d "c:\Users\Hp\OneDrive\Desktop\Website"

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python from https://www.python.org
    pause
    exit /b 1
)

echo Starting Candle Bliss Website...
echo.
echo Server will run at: http://localhost:5000
echo Press CTRL+C to stop the server
echo.

REM Run the Flask app
python app.py

REM Pause if there's an error
if errorlevel 1 (
    echo.
    echo An error occurred. Press any key to exit...
    pause
)
