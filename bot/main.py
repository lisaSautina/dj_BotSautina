from aiogram import Bot, Dispatcher, F, types
import asyncio
from dotenv import load_dotenv
import os
from aiogram.filters import Command
 
from utils.commands import set_commands
from handlers.start import get_start
from state.register import RegisterState
from handlers.register import start_register, register_name, register_course, register_group, register_phone, process_answer


load_dotenv()

token = os.getenv('TOKEN')
admin_id = os.getenv('ADMIN_ID')

bot = Bot(token=token, parse_mode='HTML')
dp=Dispatcher()

async def start_bot(bot: Bot):
    await bot.send_message(admin_id, text='Я запустил бота')



dp.startup.register(start_bot)
dp.message.register(get_start, Command(commands='start')) 


dp.message.register(start_register, F.text=='Записаться на мероприятие')
dp.message.register(register_name, RegisterState.regName)
dp.message.register(register_course, RegisterState.regCourse)
dp.message.register(register_group, RegisterState.regGroup)
dp.message.register(register_phone, RegisterState.regPhone)
dp.message.register(process_answer, RegisterState.answer)


async def start():
    await set_commands(bot)
    try:
        await dp.start_polling(bot, skip_updates=True)
    finally:
        await  bot.session.close()



if __name__ == '__main__':
    asyncio.run(start())
