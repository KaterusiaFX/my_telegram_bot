# Импортируем модуль updater (Updater соединяется с платформой telegram и
# проверяет, есть ли для бота новые сообщения).

from telegram.ext import Updater # из библиотеки telegram берем модуль est с компоненнтом Updater
from telegram.ext import CommandHandler # импорт модуля CommandHandler для обработки команд для бота
from telegram.ext import MessageHandler # импорт модуля MessageHandler для обработки сообщений для бота
from telegram.ext import Filters # выбирает тип сообщений, с которыми бот будет взаимодействовать
import logging # импорт модуля logging, отвечает за логирование бота (ведет журнал событий о том, что происходит с ботом)
import ephem # модуль для определения в каком созвездии находится планета на определенную дату
import settings


# Настройки прокси: создаем переменную PROXY, присваиваем ей словарь
PROXY = {'proxy_url': 'socks5://t1.learn.python.ru:1080', # по ключу proxy_url лежит ссылка на прокси
         'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}} # по ключу urllib3... лежит словрь с именем пользователя и паролем

# format - конфигурируем (форматируем) logging. В нем будет дата - время, когда что-то произошло (%(asctime)s);
# уровень важности события ((levelname)s);
# сообщение о том, что произошло, само событие (%(message)s)
logging.basicConfig(format = '%(asctime)s - %(levelname)s - %(message)s',
                    level = logging.INFO, # уровни логирования (в виде сообщений: info, warning, error)
                    filename='bot.log' # название самого файла
                    )

# Функция, которая соединяется с платформой Telegram, "тело" бота
def main():
    # mybot - переменная для взаимодействия с ботом, принадлежит к классу Updater
    mybot = Updater(settings.API_KEY, request_kwargs = settings.PROXY)  # передаем Updater-у ключ бота и в параметр ..kwargs кладем PROXY

    logging.info('Бот запускается') # при запуске бота в файл bot.log будет записано сообщение: Бот запускается

    # перем-ой mybot ранее присвоен класс Updater. У Updater есть атрибут dispatcher. Он распределяет входящие сообщения по событиям
    dp = mybot.dispatcher # говорим пер-ой mybot реагировать на событие и помещаем в перем-ю dp

    # атрибут ad_handler означает добавить обработчик, в него кладем CommandHandler с 2 параметрами: 1 - название команды (без /), 2 - название вызываемой ф-ии.
    dp.add_handler(CommandHandler("start", greet_user)) # когда придет команда start, запустится ф-ия greet_user

    # перем-й dp через атрибут add_handler передаем MessageHandler с параметрами:
    # 1 - Filters.tex - фильтр сообшений по типу text (работать только с текстовыми сообщениями);
    # 2 - talk_to_me - название функции
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    dp.add_handler(CommandHandler("planet", planet_f)) # когда будет команда planet, запустится ф-я planet_f

    mybot.start_polling() # "говорим" переменной mybot начать ходить на telegram и проверять сообщения
    mybot.idle() # бот будет работать до тех пор, пока его принудит. не остановить


# ф-я принимает на вход 2-а параметра. Их принято называть bot и update.
# через bot будем передавать боту команды
# в update помещаем сообщение от пользователя
# Меньше 2-х нельзя, будет ошибка.
def greet_user(bot, update):
    text = 'Вызвана команда /start'
    print(text) # при вызове команды start пользователем в консоли появится сообще-е: Вызвана команда /start
    update.message.reply_text('Привет, Друг!') # при вызове команды start пользователем бот ответит: Привет, Друг!


# ф-ия для обработки сообщений пользователя
def talk_to_me(bot, update):
    # кладем в пер-ю user_text сообщение пользователя
    user_text = update.message.text # в user_text кладем update.message с атрибутом text (это текстовое сообщение пользователя)
    print(user_text) # после отправки сообщения пользователем в консоли появится это сообще-е пользователя
    update.message.reply_text(user_text) # после отправки сообщения пользователем бот ответит тем же сообщением (типа эхо бот!)


# ф-я для обработки команды "planet" с помощью модуля ephem
def planet_f(bot, update):
    # Словарь с названиями планет и соотв-ми им параметрами для ephem
    planets = {'Mars': ephem.Mars, 'Mercury': ephem.Mercury, 'Venus': ephem.Venus, 'Jupiter': ephem.Jupiter,
               'Saturn': ephem.Saturn,
               'Uranus': ephem.Uranus, 'Neptune': ephem.Neptune, 'Pluto': ephem.Pluto, 'Sun': ephem.Sun,
               'Moon': ephem.Moon
               }
    text = 'Вызвана команда /planet'
    print(text)  # при вызове команды planet пользователем в консоли появится сообще-е: Вызвана команда /planet
    user_planet = update.message.text.split() # в user_planet кладем список из '/planet' и 'название планеты'
    planet_name = user_planet[1] # в planet_name кладем название планеты из списка user_planet
    planet_method = planets[planet_name] # в planet_method - значение ephem по ключу название планеты
    constellation1 = planet_method(ephem.now()) # применяем метод ephem.now к ephem.планета
    planet_constellation = ephem.constellation(constellation1) # примен. метод constellation
    update.message.reply_text(planet_constellation) # вывод результата сообщением от бота


# Вызываем функцию - эта строчка собственно запускает бота
main()
