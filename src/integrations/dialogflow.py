import requests
from ..config import DIALOGFLOW_PROJECT_ID
from ..translations import get_translation

async def process_message(message: str, language: str = 'es') -> str:
    """
    Procesa un mensaje usando Dialogflow CX.
    Placeholder: Implementar integración real con Dialogflow API.
    """
    if not DIALOGFLOW_PROJECT_ID:
        return get_translation(language, 'dialogflow_not_configured')

    # Aquí iría la lógica para llamar a Dialogflow
    # Ejemplo: Usar google-cloud-dialogflowcx
    # response = detect_intent_texts(project_id, location, agent_id, message)
    return get_translation(language, 'dialogflow_response', message=message)
