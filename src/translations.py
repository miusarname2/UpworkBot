# Sistema de traducciones para el bot multilingüe

TRANSLATIONS = {
    'es': {
        'greeting': '¡Hola! Soy tu bot. Elige una opción:',
        'action1_button': 'Confirmar Acción 1',
        'action2_button': 'Confirmar Acción 2',
        'help_button': 'Ayuda',
        'action1_confirmed': 'Acción 1 confirmada. Resultado: {result}',
        'action2_confirmed': 'Acción 2 confirmada. Resultado: {result}',
        'help_text': 'Envía un mensaje o elige una opción.',
        'unknown_option': 'Opción desconocida: {data}',
        'message_received': 'Mensaje recibido.',
        'n8n_not_configured': 'n8n no configurado.',
        'dialogflow_not_configured': 'Dialogflow no configurado.',
        'dialogflow_response': 'Respuesta de Dialogflow para: {message}'
    },
    'en': {
        'greeting': 'Hello! I am your bot. Choose an option:',
        'action1_button': 'Confirm Action 1',
        'action2_button': 'Confirm Action 2',
        'help_button': 'Help',
        'action1_confirmed': 'Action 1 confirmed. Result: {result}',
        'action2_confirmed': 'Action 2 confirmed. Result: {result}',
        'help_text': 'Send a message or choose an option.',
        'unknown_option': 'Unknown option: {data}',
        'message_received': 'Message received.',
        'n8n_not_configured': 'n8n not configured.',
        'dialogflow_not_configured': 'Dialogflow not configured.',
        'dialogflow_response': 'Dialogflow response for: {message}'
    },
    'fr': {
        'greeting': 'Salut! Je suis votre bot. Choisissez une option:',
        'action1_button': 'Confirmer Action 1',
        'action2_button': 'Confirmer Action 2',
        'help_button': 'Aide',
        'action1_confirmed': 'Action 1 confirmée. Résultat: {result}',
        'action2_confirmed': 'Action 2 confirmée. Résultat: {result}',
        'help_text': 'Envoyez un message ou choisissez une option.',
        'unknown_option': 'Option inconnue: {data}',
        'message_received': 'Message reçu.',
        'n8n_not_configured': 'n8n non configuré.',
        'dialogflow_not_configured': 'Dialogflow non configuré.',
        'dialogflow_response': 'Réponse Dialogflow pour: {message}'
    },
    'de': {
        'greeting': 'Hallo! Ich bin Ihr Bot. Wählen Sie eine Option:',
        'action1_button': 'Aktion 1 bestätigen',
        'action2_button': 'Aktion 2 bestätigen',
        'help_button': 'Hilfe',
        'action1_confirmed': 'Aktion 1 bestätigt. Ergebnis: {result}',
        'action2_confirmed': 'Aktion 2 bestätigt. Ergebnis: {result}',
        'help_text': 'Senden Sie eine Nachricht oder wählen Sie eine Option.',
        'unknown_option': 'Unbekannte Option: {data}',
        'message_received': 'Nachricht erhalten.',
        'n8n_not_configured': 'n8n nicht konfiguriert.',
        'dialogflow_not_configured': 'Dialogflow nicht konfiguriert.',
        'dialogflow_response': 'Dialogflow-Antwort für: {message}'
    }
}

DEFAULT_LANGUAGE = 'es'

def get_language_code(language_code: str) -> str:
    """Convierte el código de idioma de Telegram a nuestro código de idioma soportado."""
    if language_code:
        # Tomar solo las primeras 2 letras (ej: 'es-ES' -> 'es')
        lang = language_code.lower()[:2]
        if lang in TRANSLATIONS:
            return lang
    return DEFAULT_LANGUAGE

def get_translation(language: str, key: str, **kwargs) -> str:
    """Obtiene la traducción para una clave específica."""
    lang_dict = TRANSLATIONS.get(language, TRANSLATIONS[DEFAULT_LANGUAGE])
    text = lang_dict.get(key, f"[{key}]")  # Si no encuentra la clave, muestra [key]
    return text.format(**kwargs) if kwargs else text