import os
import telebot
import requests

BOT_TOKEN = os.environ.get("BOT_TOKEN")  # stored in Render
WEBHOOK_URL = os.environ.get("WEBHOOK_URL")  # stored in Render

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "👋 Hi! Send me a link or text and I’ll save it to Google Sheets.")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    text = message.text.strip()
    data = {"link": text}
    response = requests.post(WEBHOOK_URL, json=data)

    if response.status_code == 200:
        bot.reply_to(message, "✅ Added to Google Sheets!")
    else:
        bot.reply_to(message, f"⚠️ Error {response.status_code}: could not add.")

print("🤖 Bot is running...")
bot.polling(none_stop=True)
