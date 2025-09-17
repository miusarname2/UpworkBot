from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ContextTypes
from .integrations import dialogflow, n8n
from .translations import get_language_code, get_translation

def get_main_menu_keyboard(language: str) -> InlineKeyboardMarkup:
    """Crea el teclado principal del menú."""
    keyboard = [
        [InlineKeyboardButton(get_translation(language, 'action1_button'), callback_data="action1")],
        [InlineKeyboardButton(get_translation(language, 'action2_button'), callback_data="action2")],
        [InlineKeyboardButton(get_translation(language, 'help_button'), callback_data="help")]
    ]
    return InlineKeyboardMarkup(keyboard)

async def send_main_menu(update: Update, language: str) -> None:
    """Envía el menú principal al usuario."""
    reply_markup = get_main_menu_keyboard(language)
    greeting = get_translation(language, 'greeting')

    if update.message:
        await update.message.reply_text(greeting, reply_markup=reply_markup)
    elif update.callback_query:
        # Para callbacks, enviamos un nuevo mensaje en lugar de editar el existente
        await update.callback_query.message.reply_text(greeting, reply_markup=reply_markup)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handler para el comando /start."""
    language = get_language_code(update.effective_user.language_code)
    await send_main_menu(update, language)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handler para mensajes de texto."""
    language = get_language_code(update.effective_user.language_code)
    text = update.message.text.lower()

    # Traducciones de comandos para comparación
    action1_text = get_translation(language, 'action1_button').lower()
    action2_text = get_translation(language, 'action2_button').lower()
    help_text = get_translation(language, 'help_button').lower()

    if text == action1_text:
        result = await n8n.call_workflow("action1", language)
        # Mostrar resultado y luego menú
        result_message = get_translation(language, 'action1_confirmed', result=result)
        await update.message.reply_text(result_message)
        await send_main_menu(update, language)
    elif text == action2_text:
        result = await n8n.call_workflow("action2", language)
        # Mostrar resultado y luego menú
        result_message = get_translation(language, 'action2_confirmed', result=result)
        await update.message.reply_text(result_message)
        await send_main_menu(update, language)
    elif text == help_text:
        help_message = get_translation(language, 'help_text')
        await update.message.reply_text(help_message)
        await send_main_menu(update, language)
    else:
        # Procesar con Dialogflow si es necesario
        response = await dialogflow.process_message(text, language)
        await update.message.reply_text(response or get_translation(language, 'message_received'))
        await send_main_menu(update, language)

async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handler para callbacks de botones inline."""
    query = update.callback_query
    await query.answer()

    language = get_language_code(update.effective_user.language_code)
    print(update.effective_user.language_code)

    if query.data == "action1":
        result = await n8n.call_workflow("action1", language)
        # Enviar resultado como mensaje separado
        result_message = get_translation(language, 'action1_confirmed', result=result)
        await query.message.reply_text(result_message)
        # Enviar nuevo mensaje con menú
        await send_main_menu(update, language)
    elif query.data == "action2":
        result = await n8n.call_workflow("action2", language)
        # Enviar resultado como mensaje separado
        result_message = get_translation(language, 'action2_confirmed', result=result)
        await query.message.reply_text(result_message)
        # Enviar nuevo mensaje con menú
        await send_main_menu(update, language)
    elif query.data == "help":
        help_message = get_translation(language, 'help_text')
        await query.message.reply_text(help_message)
        # Enviar nuevo mensaje con menú
        await send_main_menu(update, language)
    else:
        unknown_message = get_translation(language, 'unknown_option', data=query.data)
        await query.message.reply_text(unknown_message)
        # Enviar nuevo mensaje con menú
        await send_main_menu(update, language)