import os
from os.path import join, dirname
from dotenv import load_dotenv

load_dotenv(verbose=True)

dotenv_path = join(dirname(__file__), ".env")
load_dotenv(dotenv_path)

CHROME_DRIVER_DIR = os.environ.get("CHROME_DRIVER_DIR")
ECS_ID = os.environ.get("ECS_ID")
PASSWORD = os.environ.get("PASSWORD")
BASE_DIR = os.environ.get("BASE_DIR")