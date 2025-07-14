import asyncio
import logging

from aiogram import Bot, Dispatcher, types
from aiogram.client.default import DefaultBotProperties
from aiogram.filters import Command, CommandStart

import database as db
from config import BOT_TOKEN, ADMIN_ID

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode="HTML"))
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
async def broadcast_handler(message: types.Message):
    if message.from_user.id != ADMIN_ID:
        await message.reply("Эта команда только для админа.")
        return

    users = db.get_all_users()
    if not users:
        await message.answer("Подписчиков нет, отправлять некому.")
        return


    text_from_message = message.text or message.caption or ""

    try:
        command, content_to_send = text_from_message.split(' ', 1)
    except ValueError:
        content_to_send = ""
    if not message.photo and not message.document and not content_to_send:
        await message.reply("Ошибка: нужно указать текст для рассылки.")
        return

    await message.answer(f"Начинаю рассылку для {len(users)} человек...")
    logging.info(f"Запущена рассылка от {message.from_user.id}")

    success_count = 0
    fail_count = 0
    
    for user_id in users:
        try:
            if message.photo:
                await bot.send_photo(user_id, message.photo[-1].file_id, caption=content_to_send)
            elif message.document:
                await bot.send_document(user_id, message.document.file_id, caption=content_to_send)
            else:
                await bot.send_message(user_id, content_to_send)
            
            success_count += 1
            await asyncio.sleep(0.1)
        except Exception as e:
            fail_count += 1
            logging.error(f"Не смог отправить сообщение {user_id}. Причина: {e}")
            
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
