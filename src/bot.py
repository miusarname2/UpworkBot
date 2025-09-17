# src/bot.py
import logging
from telegram.ext import Application, CommandHandler, MessageHandler, CallbackQueryHandler, filters
from .config import TELEGRAM_TOKEN, ENV
from .handlers import start, handle_message, button_callback

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

def main() -> None:
    """Ejecutar en local con polling (solo si ENV == 'LOCAL')."""
    if ENV != "LOCAL":
        logger.error("Modo polling solo permitido en ENV=LOCAL. Para producción usa webhook (Cloud Run).")
        return

    if not TELEGRAM_TOKEN:
        logger.error("TELEGRAM_TOKEN no está configurado.")
        return

    application = Application.builder().token(TELEGRAM_TOKEN).build()

    # Registrar handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    application.add_handler(CallbackQueryHandler(button_callback))

    logger.info("Bot iniciado en modo polling (LOCAL).")
    application.run_polling()

if __name__ == '__main__':
    main()