import asyncio
import logging

from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command, CommandStart

import database as db
from config import BOT_TOKEN, ADMIN_ID

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: types.Message):
    db.add_user(message.from_user.id)
    logging.info(f"Новый подписчик: {message.from_user.id}")
    await message.answer("Вы подписались на рассылку!")


@dp.message(Command("stats"))
async def get_stats(message: types.Message):
    if message.from_user.id != ADMIN_ID:
        return

    user_count = db.count_users()
    await message.answer(f"Всего подписчиков: {user_count}")


@dp.message(Command("рассылка"))
async def broadcast_message(message: types.Message):
    if message.from_user.id != ADMIN_ID:
        await message.reply("Эта команда только для админа.")
        return

    try:
        text = message.text.split(' ', 1)[1]
    except IndexError:
        await message.reply("Неправильный формат. Пример: /рассылка Привет всем!")
        return

    users = db.get_all_users()
    if not users:
        await message.answer("Подписчиков нет, отправлять некому.")
        return

    await message.answer(f"Начинаю рассылку для {len(users)} человек...")
    logging.info(f"Запущена рассылка с текстом: '{text}'")
    
    success_count = 0
    fail_count = 0

    for user_id in users:
        try:
            await bot.send_message(user_id, text)
            success_count += 1
            await asyncio.sleep(0.1)
        except Exception as e:
            fail_count += 1
            logging.error(f"Не смог отправить {user_id}. Причина: {e}")
            
    report = (
        f"Рассылка завершена!\n\n"
        f"✅ Успешно: {success_count}\n"
        f"❌ Неудачно: {fail_count}"
    )
    await message.answer(report)
    logging.info("Рассылка окончена.")


async def main():
    db.init_db()
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())