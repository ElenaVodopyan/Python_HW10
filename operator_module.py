import telebot

def send_answer(id, question, answer):
    bot.send_message(id, f'{question}\nОтвет: {answer}')

token = '6234136637:AAGw4Kuni2pCVY9N1pLYWOO0l1nJGPDuSFc'
bot = telebot.TeleBot(token)

data = open('questions.txt', 'r', encoding='utf-8')
questions_list = data.readlines()
data.close()

answered_questions = []

for row in questions_list:
    split_row = row.split('|')
    id = split_row[0]
    question = split_row[1]
    print(question[:-1])
    answer = input('Введите ответ: ')
    if answer != 'пропустить':
        send_answer(id, question, answer)
        answered_questions.append(row)
    print('___________')

for answer in answered_questions:
    questions_list.remove(answer)

data = open('questions.txt', 'w', encoding='utf-8')
data.writelines(questions_list)
data.close()