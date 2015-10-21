#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
A simple client to start getting some ideas for an alert solution

Server has been pre configured at 45.32.245.71. Will add how to docs once solution decision made.
"""

import sys
import logging
from getpass import getpass
import settings as settings_file  # must be used as settings_file due to XMPPSettings conflict

from pyxmpp2.jid import JID
from pyxmpp2.message import Message
from pyxmpp2.client import Client
from pyxmpp2.settings import XMPPSettings
from pyxmpp2.interfaces import EventHandler, event_handler, QUIT
from pyxmpp2.streamevents import AuthorizedEvent, DisconnectedEvent

class MyHandler(EventHandler):
    def __init__(self, target_jid, message):
        self.target_jid = target_jid
        self.message = message

    @event_handler(AuthorizedEvent)
    def handle_authorized(self, event):
        message = Message(to_jid = self.target_jid, body = self.message)
        event.stream.send(message)
        event.stream.disconnect()

    @event_handler(DisconnectedEvent)
    def handle_disconnected(self, event):
        return QUIT

    @event_handler()
    def handle_all(self, event):
        logging.info(u"-- {0}".format(event))

logging.basicConfig(level = logging.INFO)  # change to 'DEBUG' to see more


class SendMessage:
    def __init__(self, arg_message):
        self.message = str(arg_message)
        self.your_jid = settings_file.users['system']['secsys']
        self.your_password = getpass()
        self.target_jid = ''

        self.submit()

    def submit(self):
        for admin in settings_file.users['administrators']:
            self.target_jid = settings_file.users['administrators'][admin]
            if sys.version_info.major < 3:
                self.your_jid = self.your_jid.decode("utf-8")
                self.your_password = self.your_password.decode("utf-8")
                self.target_jid = self.target_jid.decode("utf-8")
                self.message = self.message.decode("utf-8")

                handler = MyHandler(JID(self.target_jid), self.message)
                settings = XMPPSettings({
                    u"password": self.your_password,
                    u"starttls": True,
                    u"tls_verify_peer": False,
                })

                client = Client(JID(self.your_jid), [handler], settings)
                client.connect()
                client.run()
