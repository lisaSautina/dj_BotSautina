from aiogram.types import Message 
from aiogram.fsm.context import FSMContext
from state.register import RegisterState
from utils.api import create_user
import re
from aiogram import types
from keyboards.register_kb import get_yes_no_keyboard

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
        msg='Хотели ли получать рассылку о новых мероприятиях НГУЭУ?(да/нет)'
        await message.answer(msg, reply_markup=get_yes_no_keyboard)
        await state.set_state(RegisterState.answer)
    else:
        await message.answer(f'Номер указан в неправильном формате ')


async def process_answer(message: types.Message, state: FSMContext):
    answer = message.text.lower()
    if answer == 'да':
        await state.update_data(reganswer= message.text)
        reg_data = await state.get_data()
        reg_name = reg_data.get('regname')
        reg_phone = reg_data.get('regphone')
        reg_course = reg_data.get('regcource')
        reg_group = reg_data.get('reggroup')
        reg_answer = reg_data.get('reganswer')
        msg=f'Приятно познакомится {reg_name} \n\n Телефон: {reg_phone} '
        await message.answer(msg)
        await create_user(message.from_user.id, reg_name, reg_course, reg_group, reg_phone, reg_answer)
        await message.answer("Вы успешно зарегистрированы и подписаны на рассылку!")
      
            
    elif answer == 'нет':
        await state.update_data(reganswer= message.text)
        reg_data = await state.get_data()
        reg_name = reg_data.get('regname')
        reg_phone = reg_data.get('regphone')
        reg_course = reg_data.get('regcource')
        reg_group = reg_data.get('reggroup')
        reg_answer = reg_data.get('reganswer')
        msg=f'Приятно познакомится {reg_name} \n\n Телефон: {reg_phone} '
        await message.answer(msg)
        await create_user(message.from_user.id, reg_name, reg_course, reg_group, reg_phone, reg_answer)
        await message.answer("Вы успешно зарегистрированы, но не подписаны на рассылку.")
    

    

