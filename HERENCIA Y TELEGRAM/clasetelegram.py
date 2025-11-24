import time
import datetime
import RPi.GPIO as GPIO
import telepot
from telepot.loop import MessageLoop


class BotLED:
    def __init__(self, token, led_pin):
        self.token = token
        self.led_pin = led_pin
        self.now = datetime.datetime.now()

        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.led_pin, GPIO.OUT)
        GPIO.output(self.led_pin, 0)

        self.telegram_bot = telepot.Bot(self.token)
        print(self.telegram_bot.getMe())

        self.message_loop = MessageLoop(self.telegram_bot, self.action)
        self.message_loop.run_as_thread()
        print('Up and Running....')

    def action(self, msg):
        chat_id = msg['chat']['id']
        command = msg['text']

        print('Received:', command)

        if 'on' in command:
            message = "Turned on", "led"
            GPIO.output(self.led_pin, 1)
            self.telegram_bot.sendMessage(chat_id, message)

        if 'off' in command:
            message = "Turned off", "led"
            GPIO.output(self.led_pin, 0)
            self.telegram_bot.sendMessage(chat_id, message)

    def run(self):
        while True:
            time.sleep(10)


bot = BotLED('8374308621:AAEhpi0U1A4AkZPxQVzqObSXiuni6vHdzqA', 18)
bot.run()


