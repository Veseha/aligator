from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardRemove
import random

TOKEN = "1800019447:AAFsE63D7MmSF7BF7gHb_S2Tjx4Wl5IdrRg"
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# Lists -----------------------------------
per = ("Timur", "Alyana", "Temirlan", "Aruzhan", "Dalila")
list_main = {per[0]: '0', per[1]: '0', per[2]: '0', per[3]: '0', per[4]: '0'}
avaible_numbers = ['1', '2', '3', '4', '5']
#avaible_numbers = [1, 2, 3, 4, 5]
curr_answer = {'qqqqqqq': "Timur"}
list = [5, 2, 3, 4, 1]
random.shuffle(list)

def restarting():
    per = ("Timur", "Alyana", "Temirlan", "Aruzhan", "Dalila")
    list_main = {per[0]: '0', per[1]: '0', per[2]: '0', per[3]: '0', per[4]: '0'}
    avaible_numbers = ['1', '2', '3', '4', '5']
    # avaible_numbers = [1, 2, 3, 4, 5]
    curr_answer = {'qqqqqqq': "Timur"}
    list = [5, 2, 3, 4, 1]
    random.shuffle(list)

# Buttons ---------------------------------
deleter = ReplyKeyboardRemove()
ButNumbers = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
#InlineNumbers = InlineKeyboardMarkup()
#ButNumbers = InlineKeyboardMarkup().add('111')
PanelBut = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
PanelBut.add(KeyboardButton(per[0]), KeyboardButton(per[1]), KeyboardButton(per[2]), KeyboardButton(per[3]), KeyboardButton(per[4]))

#@dp.callback_query_handler(func=lambda c: c.data == 'button1')
#async def process_callback_button1(callback_query: types.CallbackQuery):
 #   await bot.answer_callback_query(callback_query.id)
  #  await bot.send_message(callback_query.from_user.id, 'Нажата первая кнопка!')

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(msg: types.Message):
   await msg.answer(f'Это бот по занимаю очереди \nЗанять очередь /queue \nПосмотреть очередь /viewing '
                    f'\nВыдать случайную очередь /random')


@dp.message_handler(content_types=['text'])
async def get_text_messages(msg: types.Message):
   print(msg.text.lower(), msg.from_user.first_name)
   if msg.text.lower() == 'restart':
       restarting()
       random.shuffle(list)
       #await.msg.answer()
       #await msg.answer(f"Сегодняшняя последоватьельность:\nГруппа Альяна - {list[1]}\nГруппа Тимура - {list[0]} \nГруппа Темирлана - {list[2]} \nГруппа Аружан - {list[3]}\nГруппа Далила - {list[4]}")
   elif msg.text.lower() == '/queue':
        await msg.answer('Какая вы группа?', reply_markup=PanelBut)
# -------------------------------------------------------------------QUEUE
   elif msg.text.title() in per:
       if list_main[msg.text.title()] == '0':
           ButNumbers = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
           for i in avaible_numbers:
               ButNumbers.add(str(i))
           curr_answer[msg.from_user.id] = msg.text.title()
           print(curr_answer)
           await msg.answer('Выберете свободный номер очереди', reply_markup=ButNumbers)
       else:
           await msg.answer(f'Ваш номер очереди: {str(list_main[msg.text.title()])}')
           #await msg.answer('Ваш номер очереди:')
           print(list_main[msg.text.title()])
   elif msg.text.title() in avaible_numbers and msg.from_user.id in curr_answer:
       list_main[curr_answer[msg.from_user.id]] = msg.text.title()
       #ButNumbers.
       avaible_numbers.remove(msg.text.title())
       print(list_main, avaible_numbers)
       await msg.answer('Вы успешно заняли очередь!', reply_markup=deleter)


   elif msg.text.lower() == '/viewing':

       await msg.answer("Сегодняшняя последовательность: ")
       sorted_dict = {}
       sorted_keys = sorted(list_main, key=list_main.get)
       for w in sorted_keys:
           sorted_dict[w] = list_main[w]
       for i in sorted_dict:
           if sorted_dict[i] == '0':
               print('не выбрала очередь')
               await msg.answer(f'Группа {i} не выбрала свой номер...')
           else:
               await msg.answer(f'Группа {i} стартует под номером {sorted_dict[i]}')
   elif msg.text.lower() == '/random':
       random.shuffle(list)
       new_listt = dict()
       for i in range(5):
           new_listt[list[i]] = per[i]
       print(new_listt)
       print(new_listt.keys())

       list.sort()
       a = ''
       for i in list:
           a += f'\n{i} - {new_listt[i]}'
       await msg.answer(f"Сегодняшняя последовательность:{a}")
   else:
       await msg.answer(f'Это бот по занимаю очереди \nЗанять очередь /queue \nПосмотреть очередь /viewing '
                        f'\nВыдать случайную очередь /random')
       #await msg.answer('Покупка очереди 150 тг, Kaspi +77073411199')

if __name__ == '__main__':
   executor.start_polling(dp)