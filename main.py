import telebot
from telebot import types

TOKEN = 8533921484:AAGQRTbvY8iq8ocoSyHu0hP_4wBMXGJ294w

bot = telebot.TeleBot(TOKEN)

# Товари
products = {
    "organizer": ("Органайзер авто", 1200),
    "lamp": ("LED лампа", 800),
    "holder": ("Тримач телефону", 500),
    "inverter": ("Авто інвертор", 2500),
}

@bot.message_handler(commands=["start"])
def start(message):
    markup = types.InlineKeyboardMarkup()
    for key, value in products.items():
        btn = types.InlineKeyboardButton(
            text=f"{value[0]} — {value[1]} грн",
            callback_data=key
        )
        markup.add(btn)

    bot.send_message(
        message.chat.id,
        "🚗 AutoHub — магазин автотоварів\n\nОберіть товар:",
        reply_markup=markup
    )

@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    name, price = products[call.data]
    bot.send_message(
        call.message.chat.id,
        f"✅ Ви обрали: {name}\n💰 Ціна: {price} грн\n\nОплата:\n• Онлайн (WayForPay)\n• Післяплата НП"
    )

bot.polling(none_stop=True)
