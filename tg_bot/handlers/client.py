from aiogram import Dispatcher, types
from create_bot import dp,bot
from keyboards import kb_clint
from aiogram.types import ReplyKeyboardRemove

# @dp.message_handler(commands=['start','help'])
async def commands_start(message : types.message):
    try:
        await bot.send_message(message.from_user.id,'Привет,я могу тебе помочь?',reply_markup=kb_clint)
        await message.delete()
    except:
        await message.reply('Чтобы общаться с ботом через ЛС,напишите ему:\nhttps://t.me/you_tube_save_videoBot')


# @dp.message_handler(commands=['Стиль тренировки'])
async def trening_style_command(message : types.message):
    await bot.send_message(message.from_user.id,'Воркаут')


# @dp.message_handler(commands=['Время'])
async def trening_time_command(message : types.message):
    await bot.send_message(message.from_user.id,'Вечером')
    

# @dp.message_handler(commands=['Длительность'])
async def trening_interval_command(message : types.message):
    await bot.send_message(message.from_user.id,'20 минут')#,reply_markup=ReplyKeyboardRemove())
    

#Регистрируем хендлеры
def register_handlers_client(dp : Dispatcher):
    dp.register_message_handler(commands_start, commands=['start','help'])
    dp.register_message_handler(trening_style_command, commands=['Стиль_тренировки'])
    dp.register_message_handler(trening_time_command, commands=['Время'])
    dp.register_message_handler(trening_interval_command, commands=['Длительность'])