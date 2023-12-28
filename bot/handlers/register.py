from aiogram.types import Message 
from aiogram.fsm.context import FSMContext
from state.register import RegisterState
from utils.api import create_user
import re



async def start_register(message: Message, state: FSMContext):
    await message.answer(f'Подскажите как могу к вам обращаться?')
    await state.set_state(RegisterState.regName)

async def register_name(message: Message, state: FSMContext):
    await message.answer(f'{message.text}, теперь укажите ваш курс')
    await state.update_data(regname= message.text)
    await state.set_state(RegisterState.regCourse)

async def register_course(message: Message, state: FSMContext):
    await message.answer('Укажите вашу группу')
    await state.update_data(regcource= message.text)
    await state.set_state(RegisterState.regGroup)

async def register_group(message: Message, state: FSMContext):
    await message.answer('Теперь укажите ваш номер телефона, начиная с +7')
    await state.update_data(reggroup= message.text)
    await state.set_state(RegisterState.regPhone)



async def register_phone(message: Message, state: FSMContext):
    if (re.findall('^\+?[7][-\()]?\d{3}\)?-?\d{3}-?\d{2}-?\d{2}$', message.text)):
        await state.update_data(regphone= message.text)
        reg_data = await state.get_data()
        reg_name = reg_data.get('regname')
        reg_phone = reg_data.get('regphone')
        reg_course = reg_data.get('regcourse')
        reg_group = reg_data.get('reggroup')
        msg=f'Приятно познакомится {reg_name} \n\n Телефон: {reg_phone} \n Регистрация завершена'
        await message.answer(msg)
        await create_user(message.from_user.id, reg_name, reg_course, reg_group, reg_phone)
        await state.clear()
        
    else:
        await message.answer(f'Номер указан в неправильном формате ')



    