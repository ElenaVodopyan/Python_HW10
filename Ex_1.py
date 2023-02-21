import telebot

token = '6234136637:AAGw4Kuni2pCVY9N1pLYWOO0l1nJGPDuSFc'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.reply_to(message, 'Вас приветствует бот техподдержки. Введите команду /question, чтобы задать вопрос')

@bot.message_handler(commands=['question'])
def prepare_to_question(message):
    bot.reply_to(message, 'Задайте свой вопрос одним сообщением, я передам его в тех службу')
    bot.register_next_step_handler(message, write_question)

def write_question(message):
    data = open('questions.txt', 'a', encoding='utf-8')
    data.write(f'{message.from_user.id}| {message.from_user.first_name} {message.from_user.last_name}: {message.text}\n')
    data.close()
    bot.reply_to(message, 'Ваш вопрос отправлен оператору. Ожидайте ответа')

bot.polling(non_stop=True)