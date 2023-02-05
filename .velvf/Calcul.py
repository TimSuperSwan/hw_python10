import telebot
import import_words as imword
token='6172888920:AAHbYb_j6B2qXgqCex5KAAqB46C5k2EMF9o'
bot=telebot.TeleBot(token)
result = ""
result_first = 0.0
result_second = 0.0
to_do = ""
abc = []
count = 0
@bot.message_handler(commands=['start'])
def controller(message):
    start(message)
    
def start (message):
    my_start_murkup = telebot.types.ReplyKeyboardMarkup(resize_keyboard = True)
    but_complex = telebot.types.KeyboardButton('комплексные')
    but_ratio = telebot.types.KeyboardButton('рациональные')
    my_start_murkup.row(but_complex,but_ratio)
    bot.send_message(message.chat.id, 'Выбери тип числа', reply_markup=my_start_murkup)
    bot.register_next_step_handler(message,My_KeyBoard)

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
    but16 = telebot.types.KeyboardButton('9')
    but13 = telebot.types.KeyboardButton('0')
    but14 = telebot.types.KeyboardButton('=')
    but15 = telebot.types.KeyboardButton('j')
    choise = message.text
    my_markup.row(but1, but2, but3,but4)
    my_markup.row(but5,but6,but7,but8)
    my_markup.row(but9,but10,but11,but12)
    if choise == 'комплексные':
        my_markup.row(but16,but13,but15,but14)
    else:
        my_markup.row(but16,but13,but14)
    bot.send_message(message.chat.id,'Калькулятор:', reply_markup=my_markup)
    if choise == 'комплексные':
        bot.register_next_step_handler(message,process_complex)
    else:
        bot.register_next_step_handler(message,process)




def process_complex(message):
    global result
    global result_first
    global result_second
    global to_do
    global abc
    global count
    number = message.text
    if number == 'j' and count == 0:
        count += 1
        result += number
        print(result)
        bot.register_next_step_handler(message,process_complex)
    elif count == 1 and (number == '+' or number == '-' or number == '/' or number == '*'):
        to_do = number
        print(f'ту ду тако1: {to_do}')
        result_first = result
        result = ""
        count = 0
        bot.register_next_step_handler(message,process_complex)
    elif number == '=':
        if to_do == '+':
            otvet = complex(result_first) + complex(result)
        if to_do == '-':
            otvet = complex(result_first) - complex(result)
        if to_do == '*':
            otvet = complex(result_first)*complex(result)
        if to_do == '/':
            otvet = complex(result_first)/complex(result)
        bot.send_message(message.chat.id,otvet)
        abc = [result_first, to_do, result, '=' ,otvet]
        imword.import_data(abc)
        result_first = 0.0
        result = ''
        bot.register_next_step_handler(message,start)
    else:
        result += number
        print(result)
        bot.register_next_step_handler(message,process_complex)
    

def process(message):
    global result
    global result_first
    global result_second
    global to_do
    global abc
    number = message.text
    if number.isdigit() or number == 'j':
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
        abc = [result_first, to_do, result, '=' ,otvet]
        imword.import_data(abc)
        result_first = 0.0
        result = ''
        bot.register_next_step_handler(message,start)
    else:
        to_do = number
        result_first = float(result)
        result = ""
        bot.register_next_step_handler(message,process)


bot.infinity_polling()