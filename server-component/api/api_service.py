"""
API Server application file ## add more details when complete and functionality decided
"""
import cherrypy
import requests
import json
import RPi.GPIO as gpio

import cherrypy.wsgiserver.wsgiserver3

ip = None

class Root:
    @cherrypy.expose
    def index(self, ip_entry=''):
        gpio.setmode(gpio.BCM)
        gpio.setwarnings(False)
        gpio.setup(21, gpio.IN)


        html = """
<!DOCTYPE html>
<html>
<head>
    <link rel="stylesheet" href="http://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.3/leaflet.css" />
    <script src="http://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.3/leaflet.js"></script>
    <style>
        body {background: #000000;}
    </style>
</head>
<body>
    <h1>Door Command Executed</h1>
</body>
</html>
"""
        return html

    @cherrypy.expose
    def ip_grab(self):
        global ip
        return str(ip)

cherrypy.quickstart(Root(), '/', config='api-service.conf')