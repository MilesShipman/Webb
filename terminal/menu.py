__author__ = 'milesshipman'


#Imports
import sys
import platform
import preference.sysInfo
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

def _showAbout(self):
    print('About')

def wtf(self):
    print('WTF About')

class Options(QWidget):
    def __init__self(self, parent =None):
        super(Options,self).__init__(parent)
        print("Whats up")
        self.setWindowTitle("Options")
        self.setMinimumSize(QSize(200,200))
        print("debug")

"""
Class won't work because the functions get hidden and won't run.
That is fine, This file will just become functisons.
"""
class menu():
    def __init__(self,parent):
        print("Create Menu")
        #self.createMenu(parent)


def changeFilePath(self):
        print('changeFilePath')
        print(sys.platform)
        print(platform.mac_ver())
        # self.userFilePath = functions_classes.changeFilePath()
        # functions_classes.storeFilePath(self.userFilePath, 1)


def copyOption(self):
    print("Copy")




class Menu():
    def __init__(self,parent):
        self.parent = parent


    def createNewTab(self):
        print("Adding new tab")
        self.parent.tabContainer.test()
        self.parent.tabContainer.add() #This adds a new tab.

    def createMenu(self):
        self.parent.setWindowTitle('Webb terminal 0.0.9')
        #parent.setWindowTitle('Webb terminal 0.0.1')

       #rootMenu = PyQt5.QtWidgets.QMenuBar(None)
        rootMenu = self.parent.menuBar()
        #rootMenu = parent.menuBar()

        """
        Create the File Menu
        This doesn't need to be in the Mac Variant does it.
        """
        fileMenu = rootMenu.addMenu('File')

        action = fileMenu.addAction('Change File Path')
        action.triggered.connect(changeFilePath)

        """
        Create the Shell Menu
        """
        shellMenu = rootMenu.addMenu('Shell')

        newTab = shellMenu.addAction('New Tab')
        newTab.triggered.connect(self.createNewTab)



        """
        Create the Edit Menu
        """
        editMenu = rootMenu.addMenu("Edit")

        copyAction = editMenu.addAction('Copy')
        copyAction.triggered.connect(copyOption)


        """
        Create the View Menu
        """
        viewMenu = rootMenu.addMenu("View")

        #Create Help
        helpMenu = rootMenu.addMenu('Help')

        #About
        #Check to see if the Os is Mac eslse build another way.
        if(preference.sysInfo.isMac()):
            print("Building Mac")
        else:
            #Build for everything else
            aboutAction = helpMenu.addAction('About')
            aboutAction.triggered.connect(_showAbout)
"""
Can I put into a class
Should I put into class
So of theses options listing will be different on PC/Mac/Linux
in their locations and structure
"""
def createMenu(parent):
        parent.setWindowTitle('Webb terminal 0.0.9')
        #parent.setWindowTitle('Webb terminal 0.0.1')

       #rootMenu = PyQt5.QtWidgets.QMenuBar(None)
        rootMenu = parent.menuBar()
        #rootMenu = parent.menuBar()

        """
        Create the File Menu
        This doesn't need to be in the Mac Variant does it.
        """
        fileMenu = rootMenu.addMenu('File')

        action = fileMenu.addAction('Change File Path')
        action.triggered.connect(changeFilePath)

        """
        Create the Shell Menu
        """
        shellMenu = rootMenu.addMenu('Shell')

        newTab = shellMenu.addAction('New Tab')
        newTab.triggered.connect(createNewTab)



        """
        Create the Edit Menu
        """
        editMenu = rootMenu.addMenu("Edit")

        copyAction = editMenu.addAction('Copy')
        copyAction.triggered.connect(copyOption)


        """
        Create the View Menu
        """
        viewMenu = rootMenu.addMenu("View")

        #Create Help
        helpMenu = rootMenu.addMenu('Help')

        #About
        #Check to see if the Os is Mac eslse build another way.
        if(preference.sysInfo.isMac()):
            print("Building Mac")
        else:
            #Build for everything else
            aboutAction = helpMenu.addAction('About')
            aboutAction.triggered.connect(_showAbout)