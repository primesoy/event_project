""""
Diese Datei lädt die Umgebungsvariablen aus der .env-Datei

"""
import environ
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
env = environ.Env()

