from decouple import config
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Cargar las variables de entorno
BOT_TOKEN = config('BOT_TOKEN')
API_ID = config('API_ID')
API_HASH = config('API_HASH')

# ... Resto de tu código ...

def main():
    updater = Updater(
        token=BOT_TOKEN,
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
