#!/usr/bin/env python3
"""
Candle Bliss Website Launcher
Desktop Executable Script - Double-click to run!
"""

import os
import sys
import webbrowser
import time
from subprocess import Popen, PIPE

def main():
    project_dir = r"c:\Users\Hp\OneDrive\Desktop\Website"
    
    print("\n" + "="*50)
    print("     ✨  CANDLES WEBSITE  ✨")
    print("="*50 + "\n")
    
    # Change to project directory
    os.chdir(project_dir)
    
    print("Starting Flask server...")
    print("Website: http://localhost:5000\n")
    
    # Start Flask process
    try:
        process = Popen([sys.executable, "app.py"], 
                       stdout=PIPE, 
                       stderr=PIPE,
                       cwd=project_dir)
        
        # Wait a moment for server to start
        time.sleep(3)
        
        # Open browser
        print("Opening website in your browser...\n")
        webbrowser.open("http://localhost:5000")
        
        print("✓ Server is running!")
        print("✓ Website opened in your default browser")
        print("\nPress CTRL+C in the console to stop the server\n")
        
        # Keep process running
        process.wait()
        
    except Exception as e:
        print(f"❌ Error: {e}")
        input("\nPress Enter to exit...")

if __name__ == "__main__":
    main()
