import subprocess
import time
import RPi.GPIO as gpio
import lib.alert as alert
import lib.settings as settings_file
from getpass import getpass
from threading import Thread


class StartUp:
    def __init__(self):
        self.xmpp_password = ''
        
        self.start_security()
        
    def start_security(self):
        self.xmpp_password = getpass('XMPP Password: ')
        # after getting the pass save it to settings file for access from other classes in the service bus
        settings_file.passwords['xmpp_password'] = str(self.xmpp_password)
        subprocess.call('')
        

class MainService:
    def __init__(self):
        self.gpio_state = None
        self.xmpp_password = settings_file.passwords['xmpp_password']

        self.gpio_mon_thread()

    ######################
    # GPI Threads       #
    ######################
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
                time.sleep(10)



class GarageRemote:
    def __init__(self):
        self.door_state = None

    def remote_door_thread(self):
        remote_door_thread_run = Thread(self.remote_door)
        remote_door_thread_run.start()

    # def remote_door(self):


if __name__ == '__main__':
    StartUp()
    MainService()
