# Telegram Mailing Bot 📮

## 🇷🇺 Описание / 🇬🇧 Description

🇷🇺 Простой Telegram-бот для рассылки сообщений подписчикам. Администратор может отправить команду, и бот разошлет сообщение всем пользователям, которые его когда-либо запускали. Реализован на Python с использованием библиотеки aiogram и SQLite для хранения подписчиков.

🇬🇧 A simple Telegram bot for broadcasting messages to subscribers. An administrator can send a command, and the bot will send the message to all users who have ever started it. Implemented in Python using the aiogram library and SQLite for subscriber storage.

---

## ✨ Возможности / ✨ Features

* **🇷🇺 Автоматическая подписка:** Пользователи автоматически добавляются в базу данных при первом запуске бота командой `/start`.
* **🇬🇧 Automatic Subscription:** Users are automatically added to the database when they first start the bot with the `/start` command.

* **🇷🇺 Команда для рассылки:** Администратор может разослать любое сообщение всем подписчикам с помощью команды `/рассылка`.
* **🇬🇧 Broadcast Command:** The administrator can broadcast any message to all subscribers using the `/рассылка` command.

* **🇷🇺 База данных SQLite:** Используется легкая и надежная файловая база данных SQLite для хранения ID пользователей.
* **🇬🇧 SQLite Database:** Uses a lightweight and reliable file-based SQLite database to store user IDs.

* **🇷🇺 Панель администратора:** Только администратор, чей ID указан в конфигурации, может выполнять рассылку и проверять статистику.
* **🇬🇧 Admin Panel:** Only the administrator whose ID is specified in the configuration can perform broadcasts and check statistics.

* **🇷🇺 Статистика:** Команда `/stats` показывает общее количество подписчиков в базе.
* **🇬🇧 Statistics:** The `/stats` command shows the total number of subscribers in the database.

---

## 🛠️ Установка и запуск / 🛠️ Installation and Launch

1.  **🇷🇺 Клонируйте репозиторий / 🇬🇧 Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/mailing-bot.git](https://github.com/your-username/mailing-bot.git)
    cd mailing-bot
    ```

2.  **🇷🇺 Установите зависимости / 🇬🇧 Install dependencies:**
    *(Рекомендуется использовать виртуальное окружение / Virtual environment recommended)*
    ```bash
    pip install -r requirements.txt
    ```

3.  **🇷🇺 Настройте конфигурацию / 🇬🇧 Configure the settings:**
    Откройте файл `config.py`.
    * **🇷🇺 Токен бота:** Вставьте токен вашего бота в `BOT_TOKEN` (получите у [@BotFather](https://t.me/BotFather)).
    * **🇬🇧 Bot Token:** Insert your bot's token into the `BOT_TOKEN` variable (get it from @BotFather).
    * **🇷🇺 ID админа:** Укажите свой Telegram User ID в `ADMIN_ID` (узнайте у [@userinfobot](https://t.me/userinfobot)).
    * **🇬🇧 Admin ID:** Specify your Telegram User ID in the `ADMIN_ID` variable (find it by messaging @userinfobot).

4.  **🇷🇺 Запустите бота / 🇬🇧 Launch the bot:**
    ```bash
    python main.py
    ```

---

## ⚙️ Как пользоваться / ⚙️ How to Use

* **🇷🇺 /start:** (Для всех пользователей) Начать взаимодействие с ботом и подписаться на рассылку.
* **🇬🇧 /start:** (For all users) Start interacting with the bot and subscribe to the mailing list.

* **🇷🇺 /рассылка [ваше сообщение]:** (Только для админа) Отправить сообщение всем подписчикам.
* **🇬🇧 /рассылка [your message]:** (Admin only) Send a message to all subscribers.

* **🇷🇺 /stats:** (Только для админа) Посмотреть, сколько всего пользователей подписано на рассылку.
* **🇬🇧 /stats:** (Admin only) See how many users have subscribed to the mailing list.

---

## ✏️ Кастомизация / ✏️ Customization

🇷🇺 Этот бот создан как легко редактируемая основа. Вы можете легко изменить:

🇬🇧 This bot is designed as an easily editable foundation. You can easily change:

* **🇷🇺 Тексты сообщений:** Все тексты находятся в файле `main.py` и могут быть легко изменены под ваши нужды.
* **🇬🇧 Message texts:** All texts are located in `main.py` and can be easily modified to suit your needs.

* **🇷🇺 Имя файла базы данных:** Имя файла `users.db` можно изменить в файле `database.py`.
* **🇬🇧 Database file name:** The `users.db` filename can be changed in the `database.py` file.