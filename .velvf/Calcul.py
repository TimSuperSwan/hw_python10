import telebot
token='6172888920:AAHbYb_j6B2qXgqCex5KAAqB46C5k2EMF9o'
bot=telebot.TeleBot(token)
result = ""
result_first = 0.0
result_second = 0.0
to_do = ""
@bot.message_handler(commands=['start'])
def controller(message):
    My_KeyBoard(message)
    

def My_KeyBoard(message):
    my_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard = True)
    but1 = telebot.types.KeyboardButton('+')
    but2 = telebot.types.KeyboardButton('-')
    but3 = telebot.types.KeyboardButton('*')
    but4 = telebot.types.KeyboardButton('/')
    but5 = telebot.types.KeyboardButton('1')
    but6 = telebot.types.KeyboardButton('2')
    but7 = telebot.types.KeyboardButton('3')
    but8 = telebot.types.KeyboardButton('4')
    but9 = telebot.types.KeyboardButton('5')
    but10 = telebot.types.KeyboardButton('6')
    but11 = telebot.types.KeyboardButton('7')
    but12 = telebot.types.KeyboardButton('8')
    but13 = telebot.types.KeyboardButton('0')
    but14 = telebot.types.KeyboardButton('=')
    my_markup.row(but1, but2, but3,but4)
    my_markup.row(but5,but6,but7,but8)
    my_markup.row(but9,but10,but11,but12)
    my_markup.row(but13,but14)
    bot.send_message(message.chat.id,'Калькулятор:', reply_markup=my_markup)
    bot.register_next_step_handler(message,process)

def process(message):
    global result
    global result_first
    global result_second
    global to_do
    number = message.text
    if number.isdigit():
        result += number
        print(result)
        bot.register_next_step_handler(message,process)
    elif number == '=':
        if to_do == '+':
            otvet = float(result_first) + float(result)
        if to_do == '-':
            otvet = float(result_first) - float(result)
        if to_do == '*':
            otvet = float(result_first)*float(result)
        if to_do == '/':
            otvet = float(result_first)/float(result)
        bot.send_message(message.chat.id,otvet)
        result_first = 0.0
        result = ''
        bot.register_next_step_handler(message,process)
    else:
        to_do = number
        result_first = float(result)
        result = ""
        bot.register_next_step_handler(message,process)


bot.infinity_polling()