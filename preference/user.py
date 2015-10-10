__author__ = 'milesshipman'

#Imports
import getpass




"""
Ideally this function would be the first one called when initializing a terminal.
This will provide the necessary information like desired screen size.
NOTE: This is not the function that read/contains Alias and all that
"""
class UserSetting():

    #Init
    def __init__(self):
        print("Reading User Info")

        #read function that reads in the user preferences

    def username(self):
        return getpass.getuser()
