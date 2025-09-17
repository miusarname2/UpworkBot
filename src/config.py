# src/config.py
import os
import json
from dotenv import load_dotenv

# Cargar variables de entorno (útil en local)
load_dotenv()

# Entorno: "LOCAL" (desarrollo) o "PROD" (por defecto)
ENV = os.getenv("ENV", "PROD").upper()

# Token Telegram y otras integraciones
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
DIALOGFLOW_PROJECT_ID = os.getenv("DIALOGFLOW_PROJECT_ID")
N8N_WEBHOOK_URL = os.getenv("N8N_WEBHOOK_URL")

# URL pública donde correrá el servicio (ej: https://mi-servicio-xxx-uc.a.run.app)
BASE_URL = os.getenv("BASE_URL", "")  

# Cargar settings.json (ruta relativa al root/config/settings.json)
def load_settings():
    settings_path = os.path.join(os.path.dirname(__file__), '..', 'config', 'settings.json')
    if os.path.exists(settings_path):
        with open(settings_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}

SETTINGS = load_settings()