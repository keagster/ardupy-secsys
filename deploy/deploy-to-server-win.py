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
        subprocess.call('putty root@45.32.245.205 -m remotecommands')
        subprocess.call('pscp -r ..\server-component root@devour.solutions:/root/code/python/')


if __name__ == '__main__':
    Deploy()
