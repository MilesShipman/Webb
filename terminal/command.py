__author__ = 'milesshipman'


from pycoreutil.directory import *
from preference.sysInfo import *
from pycoreutil.mkdir import *


class Command():
    def __init__(self,parent):
        self.parent = parent#Not sure if I need all this, but it might be useful
        #Set the default directory to Home

        #Create Dictionary
        self.createDictionary()
        #Eventually send preference in so the default location is known.

    def createDictionary(self):
        print("Creating Dictionary of commands") #This might be the fast method, not sure.
        directory = Navigate(self.parent.session)
        self.dictionary = {}
        self.dictionary['pwd'] = directory.pwd
        self.dictionary['cd']  = directory.chdir
       # self.dictionary['chdir'] = chdir
        self.dictionary['ls']  = directory.ls
        self.dictionary['mkdir'] = mkdir

    def processCommand(self, command):
        #Get the command
        args = command[:len(command)-1].split(" ")
        command = args[0]

        print(command)

        if(command in self.dictionary):
            print("Command is valid")
            return self.dictionary[command](args)
        else:
            return -1
