import telebot

bot = telebot.TeleBot(token = "7962829269:AAE3s1Un2RPiKB4NlCUoFCxespPNYWqEgU4")
@bot.message_handler(commands=["start","help"])
def start(message):
    user_id = message.from_user.id
    bot.send_message(user_id, "Вас приветствует Prosto_bot!")
    bot.register_next_step_handler(message, help_command)
def help_command(message):
    user_id = message.from_user.id
    bot.send_message(user_id, "Справочная информация!")
    bot.register_next_step_handler(message, start)

bot.infinity_polling()

