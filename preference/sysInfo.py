__author__ = 'milesshipman'

import sys
import platform
import os


class Session():
    def __init__(self):
        """
        This function establish the terminal's Location and other self contained data.
        """
        print("Setting up the terminal Info")
        self.whereAmI = ""
        self.establishDefault()

    def establishDefault(self):
        """
        Currently this function goes tho the default directories defined as Home in the systems.
        There will be a setting that will allow the user to manually define home.
        """
        print("Default address")
        if isWindows():
            self.home = os.path.expanduser("~")
            self.whereAmI = self.home
            print(self.home)
        elif isMac():
            self.home = os.getenv("HOME")
            self.whereAmI = self.home


    def getHome(self):
        return self.home

    def setLocation(self, newLocation):
        self.whereAmI = newLocation

    def getLocation(self):
        return self.whereAmI


"""
This function will contain various OS Defining functions that will
let the Program know in an easier to read format if they are on Windows
Mac or Linux.  This will dictate of so of the interaction will occur.
"""

#Returns 1 if Windows
def isWindows():
    if(platform.system() == "Windows"):
        return 1;
    else:
        return 0

#TODO Improve this section of code, the system will be some sort of debian
def isMac():
    if(sys.platform == "darwin"):
        return 1
    else:
        return 0

#Returns 1 if Linux
def isLinux():
    if(platform.system() == "Linux"):
        return 1
    else:
        return 0