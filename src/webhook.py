# src/webhook.py
import os
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, CallbackQueryHandler, filters

from .config import TELEGRAM_TOKEN, BASE_URL, ENV
from .handlers import start, handle_message, button_callback

if not TELEGRAM_TOKEN:
    raise RuntimeError("TELEGRAM_TOKEN no configurado en variables de entorno.")

# Crear aplicación de telegram (sin polling)
application = Application.builder().token(TELEGRAM_TOKEN).build()
application.add_handler(CommandHandler("start", start))
application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
application.add_handler(CallbackQueryHandler(button_callback))

app = FastAPI()

# Startup: inicializar y registrar webhook (si BASE_URL está configurada)
@app.on_event("startup")
async def startup_event():
    # Inicializar internals del Application
    await application.initialize()
    await application.start()

    # Si tenemos BASE_URL, intentamos setear webhook automáticamente
    if BASE_URL:
        webhook_url = f"{BASE_URL}/webhook/{TELEGRAM_TOKEN}"
        try:
            await application.bot.set_webhook(webhook_url)
        except Exception as e:
            # No fatal: solo logueamos y seguimos; el webhook puede fijarse con curl externamente
            print("Error al setear webhook automáticamente:", e)

@app.on_event("shutdown")
async def shutdown_event():
    await application.stop()
    await application.shutdown()

@app.post("/webhook/{token}")
async def telegram_webhook(token: str, request: Request):
    """Recibe updates de Telegram en formato JSON y los procesa."""
    if token != TELEGRAM_TOKEN:
        raise HTTPException(status_code=401, detail="Invalid token")

    try:
        body = await request.json()
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid JSON")

    update = Update.de_json(body, application.bot)
    await application.process_update(update)
    return JSONResponse({"ok": True})

@app.get("/health")
async def health():
    return {"status": "ok", "env": ENV}
