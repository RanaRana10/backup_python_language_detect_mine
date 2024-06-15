
import sys
sys.dont_write_bytecode = True

from telegram import ForceReply, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
from custom_language_detector import CustomLanguageDetector


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    text = f"Hello {user.mention_html()} Thanks For this is for Custom CustomLanguageDetector By @RanaUniverse"
    await update.message.reply_html(
        text=text,
        reply_markup=ForceReply(input_field_placeholder=f"Hello Boss {user.first_name} Send A Message:  Thanks",))
    

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Help! This is For Language Detect")




async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_message = update.message.text
    # await update.message.reply_text(f"You Send\n\n{user_message}")

    detected_languages = CustomLanguageDetector().detect_language(user_message)
    # user_language = '\n'.join(detected_languages) if detected_languages else 'Unknown Language⚠⚠⚠'
    language_names = [CustomLanguageDetector().language_names.get(lang, lang) for lang in detected_languages]
    user_language = '\n'.join(language_names) if language_names else 'Unknown Language⚠⚠⚠'


    response = f"Your Detected language from this text: \n\n\n{user_language}"
    await update.message.reply_text(response)



def main() -> None:
    application = Application.builder().token("6780033449:AAFKWBuWlPcBHLm303owSEvDriPZjCxs9ZU").build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()
