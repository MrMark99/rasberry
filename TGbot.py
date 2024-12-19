import telebot
import RPi.GPIO as GPIO
import time

# Токен для Telegram-бота
TOKEN = '6883853221:AAHrq38JnvOwLP-hUSCPkHSe-gUAnDIdJ7A'  # Замініть на свій токен

# Ініціалізація Telegram-бота
bot = telebot.TeleBot(TOKEN)

# GPIO налаштування
SERVO_PIN_1 = 1  # Пін для першого сервомотора
SERVO_PIN_2 = 7  # Пін для другого сервомотора

GPIO.setmode(GPIO.BCM)
GPIO.setup(SERVO_PIN_1, GPIO.OUT)
GPIO.setup(SERVO_PIN_2, GPIO.OUT)

# Ініціалізація PWM для сервомоторів (частота 50 Гц)
pwm1 = GPIO.PWM(SERVO_PIN_1, 50)
pwm2 = GPIO.PWM(SERVO_PIN_2, 50)

# Початковий стан: сервомотори вимкнені
pwm1.start(0)
pwm2.start(0)

# Функція для запуску сервомоторів
def start_servos():
    pwm1.ChangeDutyCycle(7.5)  # Позиція для обертання (приблизно 90°)
    pwm2.ChangeDutyCycle(7.5)

# Функція для зупинки сервомоторів
def stop_servos():
    pwm1.ChangeDutyCycle(0)  # Зупинка PWM-сигналу
    pwm2.ChangeDutyCycle(0)

# Обробник команди /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_on = telebot.types.KeyboardButton("ON")
    btn_off = telebot.types.KeyboardButton("OFF")
    markup.add(btn_on, btn_off)
    bot.send_message(message.chat.id, "Вітаю! Натискай ON для запуску сервомоторів та OFF для їх зупинки.", reply_markup=markup)

# Обробник натискань кнопок
@bot.message_handler(func=lambda message: True)
def handle_buttons(message):
    if message.text == "ON":
        bot.send_message(message.chat.id, "Сервомотори запущено.")
        start_servos()  # Запуск сервомоторів
    elif message.text == "OFF":
        bot.send_message(message.chat.id, "Сервомотори зупинено.")
        stop_servos()  # Зупинка сервомоторів
    else:
        bot.send_message(message.chat.id, "Використовуй кнопки ON або OFF.")

# Основний цикл програми
try:
    print("Бот запущено. Чекаємо на команди...")
    bot.polling(none_stop=True)  # Запуск бота
except KeyboardInterrupt:
    print("Зупинка програми...")
finally:
    pwm1.stop()
    pwm2.stop()
    GPIO.cleanup()
