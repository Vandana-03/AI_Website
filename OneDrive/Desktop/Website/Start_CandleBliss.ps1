# PowerShell script to run Candle Bliss Website
# Right-click and select "Run with PowerShell"

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "     ✨  CANDLES WEBSITE  ✨" -ForegroundColor Magenta
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Navigate to project directory
Set-Location "c:\Users\Hp\OneDrive\Desktop\Website"

# Check if Python is installed
try {
    $pythonVersion = python --version 2>&1
    Write-Host "✓ Python found: $pythonVersion" -ForegroundColor Green
} catch {
    Write-Host "✗ ERROR: Python is not installed!" -ForegroundColor Red
    Write-Host "Please install Python from https://www.python.org" -ForegroundColor Yellow
    Read-Host "Press Enter to exit"
    exit
}

Write-Host ""
Write-Host "Starting Flask server..." -ForegroundColor Yellow
Write-Host "Website will be available at: http://localhost:5000" -ForegroundColor Cyan
Write-Host "Press CTRL+C to stop the server" -ForegroundColor Yellow
Write-Host ""

# Run Flask
python app.py
