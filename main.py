import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
from core.handlers.basic import get_start, set_TOKEN, set_chat_id, check_going_on, set_command, input_result
from core.settings import settings
from core.utils.stateform import StepsForm


async def start_bot(bot: Bot):
    await bot.send_message(settings.bot.admin_id, "Бот запущен")


# async def send_message_to_other_bot(other_bot, chat_id, text):
#     await other_bot.send_message(chat_id, text)
#     await message.answer(response.text)
#
#
# async def handle_message(message: types.Message):
#     # Отправляем запрос другому боту
#     other_bot_chat_id = 123456789  # Идентификатор чата другого бота
#     response = await bot.send_message(other_bot_chat_id, message.text)
#
#     # Обрабатываем ответ от другого бота
#     await message.answer(response.text)


async def stop_bot(bot: Bot):
    await bot.send_message(settings.bot.admin_id, "Бот остановлен")


async def start():
    bot = Bot(settings.bot.bot_token)
    other_bot = Bot(token='6893023383:AAHChZSyeoMjEFPjewmyyhhpdjikEIGqx68')
    db = Dispatcher()
    #db.message.register(send_message_to_other_bot)
    db.message.register(get_start, Command(commands=['start', 'run']))
    db.message.register(set_TOKEN, F.text.lower() == "ввести token")
    db.message.register(set_chat_id, StepsForm.GET_TOKEN)
    db.message.register(input_result, StepsForm.GET_COMMAND)

    db.message.register(check_going_on, StepsForm.GET_FINAL)
    db.message.register(set_command, StepsForm.GET_CHAT_ID)

    db.startup.register(start_bot)
    db.shutdown.register(stop_bot)

    #await send_message_to_other_bot(other_bot=other_bot, chat_id='2010267515', text='/request1')
    try:
        await db.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(start())
