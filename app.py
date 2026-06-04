import sys
import os

# Add the nested directory to python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'PROJECT DJ', 'SecureVote', 'Secure', 'project', 'SecureVote'))

# Import the Flask app from the subfolder app.py
from app import app
