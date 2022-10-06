from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State,StatesGroup
from aiogram import Dispatcher, types
from create_bot import dp,bot


class FSMAdmin(StatesGroup):
    photo = State()
    name = State()
    description = State()
    time = State()


#Начало диалога загрузки нового упражнения
# @dp.message_handler(commands='Загрузить',state=None)
async def cm_start(message : types.Message):
    await FSMAdmin.photo.set()
    await message.reply('Загрузи фото')

#Ловим первый ответ 
# @dp.message_handler(context_types=['photo'], state=FSMAdmin.photo)
async def load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['фото'] = message.photo[0].file_id
        await FSMAdmin.next()
        await message.reply('Теперь введи название')

#Ловим второй ответ 
# @dp.message_handler(state=FSMAdmin.name)
async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['упражнение'] = message.text
        await FSMAdmin.next()
        await message.reply('Теперь введи описание')

#Ловим третий ответ 
# @dp.message_handler(state=FSMAdmin.description)
async def load_description(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['описание'] = message.text
        await FSMAdmin.next()
        await message.reply('Теперь введи цену')

#Ловим последний ответ 
# @dp.message_handler(state=FSMAdmin.time)
async def load_time(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['время'] = float(message.text)

    async with state.proxy() as data:
        await message.reply(str(data))
    
    await state.finish()


#Регистрируем хендлеры

def register_handlers_admin(dp : Dispatcher):
    dp.register_message_handler(cm_start, commands=['Загрузить'], state=None)
    dp.register_message_handler(load_photo, content_types=['фото'], state=FSMAdmin.photo)
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_description, state=FSMAdmin.description)
    dp.register_message_handler(load_time, state=FSMAdmin.time)