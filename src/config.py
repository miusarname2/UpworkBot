import os
import json
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# Configuración desde .env
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')

# Configuración desde settings.json
def load_settings():
    settings_path = os.path.join(os.path.dirname(__file__), '..', 'config', 'settings.json')
    if os.path.exists(settings_path):
        with open(settings_path, 'r') as f:
            return json.load(f)
    return {}

SETTINGS = load_settings()

# Configuraciones de integraciones (placeholders)
DIALOGFLOW_PROJECT_ID = os.getenv('DIALOGFLOW_PROJECT_ID')
N8N_WEBHOOK_URL = os.getenv('N8N_WEBHOOK_URL')