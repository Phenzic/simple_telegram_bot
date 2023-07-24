from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN: Final = '6359006989:AAHxLgtavBt989u2t2Soj6v6c2RbhCqLSgA'
BOT_USERNAME: Final = '@PhenzBot'

# Commands
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello, What meme would you like to concore?')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("I am a MemeBot! Say Hi, lets get your meme out there")

async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("This is a Custom Command !")

# Responses

def handle_response(text: str) -> str:
    processed: str = text.lower()

    if 'hello' in processed:
        return "Hey there!"
    
    if 'how are you' in processed:
        return "I'm great, how about you?"
    
    if 'Sup, I love memes' in processed:
        return "I love memes too, lets get to work!"
    
    return "Heyooo so i don't understand what you are saying..."


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f"User ({update.message.chat.id}) in {message_type} says: {text}")

    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, '').strip()
            response: str = handle_response(new_text)
        else:
            return
    else:
        response: str = handle_response(text) 

    print("Bot:", response)
    await update.message.reply_text(response)


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
        print(f"Update {update} caused error {context.error}")

if __name__ == "__main__":
    app = Application.builder().token(TOKEN).build()
    print("polling started...")
# Commands

app.add_handler(CommandHandler('start', start_command))
app.add_handler(CommandHandler('help', help_command))
app.add_handler(CommandHandler('custom', custom_command))


# Messages 

app.add_handler(MessageHandler(filters.TEXT, handle_message))

# Errors

app.add_error_handler(error)
 
# Polls the bot
print("Bot is polling...")
app.run_polling(poll_interval = 3)

