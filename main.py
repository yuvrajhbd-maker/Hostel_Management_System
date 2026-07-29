"""
Entry point for the Hostel Management System.

Run with:
    python main.py

This simply launches the login screen (view/login.py), which then opens
the dashboard and other modules as separate windows.
"""

import os
import sys
import subprocess

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOGIN_SCRIPT = os.path.join(BASE_DIR, "view", "login.py")

if __name__ == "__main__":
    subprocess.run([sys.executable, LOGIN_SCRIPT])
