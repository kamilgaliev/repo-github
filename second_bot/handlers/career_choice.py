from pkgutil import get_data

from aiogram import Router, types, F
from aiogram.filters.command import Command
from second_bot.keyboards.prof_keyboards import make_row_keyboard
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

router = Router()

available_jobs = [
    "Программист",
    "Дизайнер",
    "Маркетолог",
    "Руководитель",
    "Бухгалтер",
    "Менеджер"
]

available_grades = ['Junior','Middle','Senior']

class ChoiseProfile(StatesGroup):
    job = State()
    grade = State()

@router.message(Command("prof"))
async def command_prof(message: types.Message, state: FSMContext):
    text = "Выберите профессию"
    await message.answer(text, reply_markup=make_row_keyboard(available_jobs))
    await state.set_state(ChoiseProfile.job)

@router.message(ChoiseProfile.job, F.text.in_(available_jobs))
async def grade_chosen(message: types.Message, state: FSMContext):
    await state.update_data(profession= message.text)
    text = "Выберите уровень"
    await message.answer(text, reply_markup=make_row_keyboard(available_grades))
    await state.set_state(ChoiseProfile.grade)

@router.message(ChoiseProfile.job)
async def prof_chosen_incorrect(message: types.Message):
    text = "Выберите профессию"
    await message.answer(text, reply_markup=make_row_keyboard(available_jobs))

@router.message(ChoiseProfile.grade, F.text.in_(available_grades))
async def grade_chosen(message: types.Message, state: FSMContext):
    user_data = await state.get_data()
    text = (f"Ваша профессия: {user_data['profession']}\n"
            f"Ваш уровень: {message.text}")
    await message.answer(text, reply_markup=types.ReplyKeyboardRemove())
    await state.clear()

@router.message(ChoiseProfile.grade)
async def grade_chosen_incorrect(message: types.Message):
    text = "Выберите уровень"
    await message.answer(text, reply_markup=make_row_keyboard(available_grades))