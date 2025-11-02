import os
import logging
from flask import Flask, request
from telegram import Update, Bot
from telegram.ext import Dispatcher, CommandHandler, MessageHandler, Filters

# Configuration du logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

# Initialisation de l'application Flask
app = Flask(__name__)

# Récupération du Token depuis les variables d'environnement
BOT_TOKEN = os.environ.get('BOT_TOKEN')
if not BOT_TOKEN:
    logger.error("La variable d'environnement BOT_TOKEN n'est pas définie !")

bot = Bot(token=BOT_TOKEN)
# Le 'use_context=True' est important pour la version actuelle de la librairie
dispatcher = Dispatcher(bot, None, use_context=True, workers=0)

# Définition des handlers (commandes du bot)
def start(update, context):
    """Handler pour la commande /start."""
    update.message.reply_text('Bonjour ! Je suis un bot Telegram hébergé sur Vercel.')

def echo(update, context):
    """Handler qui répète le message de l'utilisateur."""
    update.message.reply_text(update.message.text)

def error(update, context):
    """Handler pour les erreurs."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

# Enregistrement des handlers dans le dispatcher
dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))
dispatcher.add_error_handler(error)

# Route principale pour le webhook
 @app.route('/', methods=['POST'])
def webhook_handler():
    if request.method == "POST":
        # Récupère le JSON envoyé par Telegram
        update = Update.de_json(request.get_json(force=True), bot)
        # Traite la mise à jour
        dispatcher.process_update(update)
    return 'ok'

# Route optionnelle pour vérifier que le serveur fonctionne
 @app.route('/', methods=['GET'])
def index():
    return 'Hello, World! Your bot is running.'

# La fonction 'handler' de Vercel utilise l'objet 'app' de Flask.
# Vercel s'attend à trouver une variable 'app' ou une fonction 'handler'.
# Dans ce cas, il trouvera et utilisera 'app'.
