from aiogram.fsm.state import StatesGroup, State


class StepsForm(StatesGroup):
    GET_TOKEN = State()
    GET_CHAT_ID = State()
    GET_COMMAND = State()
    GET_FINAL = State()
    GET_BACK = State()
    GET_FILE = State()

    GET_RESULT = State()
