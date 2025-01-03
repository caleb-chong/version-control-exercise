# This is app/alpha_service.py

import os
from dotenv import load_dotenv

load_dotenv() # looks in the ".env" file for env vars

API_KEY = os.getenv("ALPHAVANTAGE_API_KEY", default="demo")