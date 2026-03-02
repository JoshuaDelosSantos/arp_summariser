from pathlib import Path
import os
from dotenv import load_dotenv

load_dotenv()

CHAT_MODEL = os.getenv("CHAT_MODEL")
API_KEY = os.getenv("API_KEY")
CONTEXT_DIR = os.getenv("CONTEXT_DIR")