import RPi.GPIO as GPIO
import time

# Налаштовуємо пін
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

# Створюємо PWM об'єкт
pwm = GPIO.PWM(18, 50)  # 50 Гц для сервомотора
pwm.start(0)

try:
    # Змінюємо кут
    pwm.ChangeDutyCycle(7)  # 7% для 0 градусів
    time.sleep(2)
    pwm.ChangeDutyCycle(12)  # 12% для 180 градусів
    time.sleep(2)
except KeyboardInterrupt:
    pass

pwm.stop()
GPIO.cleanup()
