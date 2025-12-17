import telebot
import json
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = "YOUR_BOT_TOKEN"
bot = telebot.TeleBot(TOKEN)

def load_movies():
    with open("movies.json", "r", encoding="utf-8") as f:
        return json.load(f)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(
        message,
        "🎬 Movie Index Bot Active!\n\n"
        "Movie name send කරන්න\n"
        "Example: Avengers"
    )

@bot.message_handler(func=lambda m: True)
def search_movie(message):
    query = message.text.lower()
    movies = load_movies()

    for movie in movies:
        if query in movie["name"].lower():
            markup = InlineKeyboardMarkup()
            for link in movie["links"]:
                markup.add(
                    InlineKeyboardButton(
                        link["title"],
                        url=link["url"]
                    )
                )
            bot.reply_to(
                message,
                f"🎬 {movie['name']}\n\n👇 Available Links",
                reply_markup=markup
            )
            return

    bot.reply_to(message, "❌ Movie not found")

bot.polling()
