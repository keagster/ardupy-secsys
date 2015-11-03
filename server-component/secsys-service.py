import time
import RPi.GPIO as gpio
import lib.alert as alert
import api.api_service as api_service
import lib.settings as settings_file
from getpass import getpass
from threading import Thread


class StartUp:
    def __init__(self):
        self.xmpp_password = ''
        # Start initial security prompts and any other input required
        self.start_security()
        # Start the API or secsys-webui and other components API dependant components
        StartApi()
        # Start Main to start live monitoring of the GPIO's
        # Main will soon be replaced allowing for every feature to be developed and
        # managed through individual class's
        MainService()
        
    def start_security(self):
        self.xmpp_password = getpass('XMPP Password: ')
        # after getting the pass save it to settings file for access from other classes in the service bus
        settings_file.passwords['xmpp_password'] = str(self.xmpp_password)
        

class StartApi:
    def __init__(self):
        self.io = ''
        self.start_api_thread()

    def start_api_thread(self):
        start_api_thread_run = Thread(target=self.start_api)
        start_api_thread_run.start()

    def start_api(self):
        api_service()


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
        self.api_action_place_holder = None

    def remote_door_thread(self):
        remote_door_thread_run = Thread(self.remote_door)
        remote_door_thread_run.start()

    def remote_door(self):
        gpio.setup(20, gpio.OUT)
        if self.api_action_place_holder == 0:
            print('Activate Door Button')
        else:
            print('Dont if API does not work or key is wrong more detail will be added')


if __name__ == '__main__':
    StartUp()
