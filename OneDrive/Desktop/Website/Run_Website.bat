@echo off
REM Quick Start for Candle Bliss Website
REM This opens the website after starting the server

echo Starting Candles Website...
cd /d "c:\Users\Hp\OneDrive\Desktop\Website"

REM Start Flask in background and give it time to start
start "" python app.py

REM Wait 3 seconds for server to start
timeout /t 3 /nobreak

REM Open the website in default browser
start http://localhost:5000

echo.
echo Website opened in your browser!
echo Server is running at http://localhost:5000
echo.
echo To stop the server, close the Flask console window
