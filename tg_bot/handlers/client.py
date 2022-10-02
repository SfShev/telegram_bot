from aiogram import Dispatcher, types
from create_bot import dp,bot

# @dp.message_handler(commands=['start','help'])
async def commands_start(message : types.message):
    try:
        await bot.send_message(message.from_user.id,'Привет,я могу тебе помочь?')
        await message.delete()
    except:
        await message.reply('Чтобы общаться с ботом через ЛС,напишите ему:\nhttps://t.me/you_tube_save_videoBot')




def register_handlers_client(dp : Dispatcher):
    dp.register_message_handler(commands_start, commands=['start','help'])