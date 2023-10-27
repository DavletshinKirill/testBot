from aiogram.types import Message
from core.keyboards.reply import reply_keyboard_token, binary_keyboard
from aiogram.fsm.context import FSMContext
from core.utils.stateform import StepsForm
from core.parser.check_exist import check_exist
from core.parser.write import create_document, run_command
from core.parser.delete_file import delete_file
from aiogram import Bot
from aiogram.types.input_file import BufferedInputFile


async def get_start(message: Message):
    await message.answer(f'Привет, {message.from_user.first_name}, я так рад тебя видеть',
                         reply_markup=reply_keyboard_token)


async def set_chat_id(message: Message, state: FSMContext):
    await state.update_data(TOKEN=message.text)
    await message.answer(f"Ваш TOKEN: {message.text}")
    await message.answer(f"Введите chat_id")
    await state.set_state(StepsForm.GET_CHAT_ID)


async def input_result(message: Message, state: FSMContext):
    if message.text.lower() == "да":
        await message.answer(f"Введите ожидаемый результат")
        await state.set_state(StepsForm.GET_FINAL)
        return
    elif message.text.lower() == "нет":
        await show_data(message, state)
        await state.set_state(StepsForm.GET_FINAL)
        return
    await message.answer(f"Ваша команда: {message.text}")
    await state.update_data(command=message.text)
    await message.answer("Хотите ввести результат?", reply_markup=binary_keyboard)


async def set_TOKEN(message: Message, state: FSMContext):
    await message.answer("Ведите  TOKEN")
    await state.set_state(StepsForm.GET_TOKEN)


async def set_command(message: Message, state: FSMContext):
    await message.answer(f"Ваш chat_id: {message.text}")
    await state.update_data(chat_id=message.text)
    await message.answer(f"Введите команду")
    await state.set_state(StepsForm.GET_COMMAND)


async def check_going_on(message: Message, state: FSMContext, bot: Bot):
    context_data = await state.get_data()
    if message.text.lower() == "да":
        await message.answer(f"Введите команду")
        await state.set_state(StepsForm.GET_COMMAND)
        return
    elif message.text.lower() == "нет":

        with open(f"{context_data.get('TOKEN')}.doc", 'rb') as file:
            input_file = BufferedInputFile(file.read(), f"{context_data.get('TOKEN')}.doc")
            await message.reply_document(input_file)

        await delete_file(f"{context_data.get('TOKEN')}.doc")
        await message.answer(f'Ввести TOKEN?',
                             reply_markup=reply_keyboard_token)
        return
    await state.update_data(result=message.text)
    await show_data(message, state)


async def show_data(message: Message, state: FSMContext):
    context_data = await state.get_data()
    await message.answer(f"Ваш TOKEN: {context_data.get('TOKEN')}")
    await message.answer(f"Ваш chat_id: {context_data.get('chat_id')}")
    await message.answer(f"Ваша команда: {context_data.get('command')}")
    await message.answer(f"Ожидаемый результат: {context_data.get('result')}")
    await message.answer(f"Продолжить?", reply_markup=binary_keyboard)
    await state.update_data(result=None)

    if await check_exist(f"{context_data.get('TOKEN')}.doc"):
        await run_command(context_data.get('document'), context_data.get('TOKEN'), context_data.get('command'),
                          context_data.get('result'), context_data.get('result'), 'Тест не пройден.', 'Тест пройден')
    else:
        document = await create_document(context_data.get('TOKEN'), context_data.get('chat_id'))
        await state.update_data(document=document)
        await run_command(document, context_data.get('TOKEN'), context_data.get('command'),
                          context_data.get('result'), context_data.get('result'), 'Тест не пройден.', 'Тест пройден')


