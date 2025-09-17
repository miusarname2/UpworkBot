import requests
from ..config import N8N_WEBHOOK_URL
from ..translations import get_translation

async def call_workflow(action: str, language: str = 'es') -> str:
    """
    Llama a un flujo de trabajo en n8n.
    Placeholder: Implementar llamada real a webhook de n8n.
    """
    if not N8N_WEBHOOK_URL:
        return get_translation(language, 'n8n_not_configured')

    # Aquí iría la lógica para llamar al webhook
    # response = requests.post(N8N_WEBHOOK_URL, json={"action": action})
    # return response.json().get("result", "Resultado de n8n")
    return get_translation(language, 'dialogflow_response', message=f"acción: {action}")