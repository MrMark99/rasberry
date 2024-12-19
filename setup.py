import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)  # Використовуємо BCM нумерацію
GPIO.setup(1, GPIO.OUT)  # Налаштовуємо пін 1 як вихід

pwm = GPIO.PWM(1, 50)  # PWM сигнал з частотою 50 Гц
pwm.start(0)  # Початковий скважинний цикл 0%

try:
    pwm.ChangeDutyCycle(7)  # Встановлюємо кут сервомотора
    time.sleep(2)
    pwm.ChangeDutyCycle(12)  # Інший кут
    time.sleep(2)
except KeyboardInterrupt:
    pass

pwm.stop()
GPIO.cleanup()
