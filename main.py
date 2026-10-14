import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Ton bot
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Salut ! 👋 Je suis Aroma Bot 🌸\n"
        "Bot opérationnel et en ligne 24/7 sur Render !"
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Tape /start pour me démarrer.")

def main():
    token = os.getenv("BOT_TOKEN")
    if not token:
        print("ERREUR: BOT_TOKEN non trouvé dans les variables d'environnement !")
        return
    
    app = ApplicationBuilder().token(token).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    
    print("Aroma Bot démarré...")
    app.run_polling()

if __name__ == "__main__":
    main()