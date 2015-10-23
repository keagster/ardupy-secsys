"""
Requirement identified to deploy application to server faster for testing

Requirements
- Putty
- PSCP

Both dependencies listed above need to be added to your path
"""

import subprocess


class Deploy:
    def __init__(self):
        self.secure_copy()

    def secure_copy(self):
        subprocess.call('putty pi@192.168.42.121 -m remotecommands')
        subprocess.call('pscp -r ..\server-component pi@192.168.42.121:/home/pi/git/server-component')


if __name__ == '__main__':
    Deploy()
