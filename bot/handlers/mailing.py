from aiogram.types import Message 
from aiogram.fsm.context import FSMContext
from state.mailing import Mailing


async def mailing_messanges(message: Message, state: FSMContext):
    await message.answer(f'Вы бы хотели получать рассылку о мероприятиях НГУЭУ?(Да/Нет)')
    if message.text == "Да":
        msg='Теперь вы будете получать рассылку о мероприятиях НГУЭУ'
        await state.set_state(Mailing.mail)
        await message.answer(msg)
        await state.clear()
    elif message.text == "Нет":
        await message.answer('Вам не будет приходить рассылка.')
    await state.clear()
