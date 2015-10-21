import os
import RPi.GPIO as gpio
import lib.alert as alert
from threading import Thread


class StartUp:
    def __init__(self):
        self.place_holder = 'First Run Functions to go here'

class MainService:
    def __init__(self):
        self.gpio_state = None

        self.gpio_mon_thread()

    def gpio_mon_thread(self):
        gpio_mon_thread_run = Thread(target=self.gpio_mon)
        gpio_mon_thread_run.start()

    def gpio_mon(self):
        gpio.setmode(gpio.BCM)
        gpio.setwarnings(False)
        gpio.setup(21, gpio.IN)
        while 1:
            if gpio.input(21) == 1:
                alert.SendMessage('SecSys: GPIO Service Trigger SendMessage() I/O')


if __name__ == '__main__':
    MainService()
