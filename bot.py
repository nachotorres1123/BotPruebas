from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Reemplaza con tus propias credenciales
BOT_TOKEN = '6476747450:AAG00vg3M2eYmMxBzu7wETXpIkxa6IC378Q'
API_ID = '21590558'
API_HASH = '9767814b790f12ad9a333a20bcaf1200'

# Manejador para el comando /start
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("¡Hola! Soy tu bot de prueba. ¡Escribe /hola para saludar!")

# Manejador para el comando /hola
def hola(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("¡Hola! ¿Cómo estás?")

def main():
    updater = Updater(
        token=BOT_TOKEN,  # Cambio realizado aquí
        api_id=API_ID,
        api_hash=API_HASH,
        use_context=True
    )

    dispatcher = updater.dispatcher

    # Agregar manejadores de comandos aquí
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("hola", hola))

    # Iniciar el bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
