from PyQt5 import QtWidgets
from preference.user import *
from terminal.command import *
from terminal.menu import *
from pycoreutil.directory import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *



####################################################
#This should represent my own instance of QTextEdit
#IE We should over be able to override the keyEventPress
#of the QT object to allow my own usage of the keys.
####################################################

#TODO: Figure out how to make the stdout go to the GUI.
#TODO: Prevent backspace from erasing everything down prior.
#TODO: Figure out how to highlight text but now allow text to be re-written
class TextArea(QtWidgets.QTextEdit):
    def __init__(self, parent=None):
        QtWidgets.QTextEdit.__init__(self, parent)
        self.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.test = QtWidgets.QTextEdit.insertPlainText #This works for future reference.
        self.start = 0;

        #Define the Session first
        self.user = UserSetting()
        self.session = Session()
        self.process = Command(self);
        self.escapeCount = 0;

        self.insertPlainText(self.user.username() + " $")
       #Create the stand alone process

        """
        Processes do not work with QT, the way it would work with say X-Motif.  The only thread that is capable
        of editing the GUI is the main GUI thread that was used to create the GUI. It is suggested that I use
        Signal's to push communication across as a means to update the GUI.  There has to be a quick and easy
        way to do this, I need to read the source code examples online for how to do this.  I really how that
        I don't have to restructure my code to make this work.
        """
       #ServerCom(self)


    """
    This function is reposible for emulating the autofill feature found in Linux/Mac terminal
    It may also exists in Windows Command Line but not sure.
    ##TODO: I need to add the ability to have change the button from escape to something else if the users
        wishes for that ability.
    """
    def autoFill(self):
        #Push
        position = QtWidgets.QTextEdit.textCursor(self) #No need to pull the full data in the window.
        position.setPosition(self.start,position.selectionEnd())
        results = autoAddress(position.selectedText())
        if(len(results) == 1):
            #Appends the result to the end
            QtWidgets.QTextEdit.insertPlainText(self,results[0])
            QtWidgets.QTextEdit.verticalScrollBar(self).setValue(QtWidgets.QTextEdit.verticalScrollBar(self).maximum())
        else:
            """
            There is a bug in this code: that the moment a Delete/Backspace is hit the
            program fails to maintain inserting the code instead deletes it.
            """
            #PART A
            #Set the cursor position, with the help of self.start
            cursor = self.textCursor()
            current = cursor.selectionEnd()
            #I'm using this wrong.. Is this the issue
            cursor.setPosition(self.start)

            #Part B Add text to the front of this
            #Reformat this to be a more Unix like response
            for item in results:
                cursor.insertText(item + "\n")

            #Scroll down towards the bottom of the screen.
            QtWidgets.QTextEdit.verticalScrollBar(self).setValue(QtWidgets.QTextEdit.verticalScrollBar(self).maximum())

    def keyPressEvent(self, event):
        #Handle the Enter key to enter the command.
        if(event.key() == Qt.Key_Escape): #TODO Make this a choiceable decision.
            #Make the Code within the if a function for organization
            if(self.escapeCount == 1):
                self.autoFill() #Call the autofill
                self.escapeCount = 0; #Reset the counter for double press.
            else:
                self.escapeCount = 1; #Count for the first escape press
        else:
            self.escapeCount = 0;

        #Todo: I need to fix this logic. Make it cleaner.
        if(event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return):
            QtWidgets.QTextEdit.keyPressEvent(self, event)

            #Get command and Run command
            position = QtWidgets.QTextEdit.textCursor(self) #No need to pull the full data in the window.
            #Because of this blocking system I have to remember the position
            position.setPosition(self.start,position.selectionEnd())
            test = position.selectedText()

            #strip name. TODO Add the logic
            test = test[len(self.user.username()) + 2:] #TODO Fix this logic to use USERNAME Len
            test = str(test)
            #print(test) #TODO Fix encoding. Why does this not work on windows.

            #Process the command and figure out what is going wrong.


            text = self.process.processCommand(test)
            if(text == 0):
                self.insertPlainText("") #No need for a new line.
            elif(text != -1):
                self.insertPlainText(text + "\n")
            else:
                args = test[:len(test)-1].split(" ")
                command = args[0]
                self.insertPlainText(str(command) + ": Command not Found\n")

            #position
            position = QtWidgets.QTextEdit.textCursor(self)
            #QtWidgets.QTextEdit.setCursor(self,position)
            self.start = position.selectionEnd()


            self.insertPlainText(str(self.user.username()) + " $") #TODO set to be the username.
            self.verticalScrollBar().setValue(QtWidgets.QTextEdit.verticalScrollBar(self).maximum()) #Scroll to the bottom




        #The up key will recall the previous command, but this will be editable
        #through the prefrences.
        elif(event.key() == Qt.Key_Up):
            print("recall")
        else:
            QtWidgets.QTextEdit.keyPressEvent(self,event)
            position = QtWidgets.QTextEdit.textCursor(self)


    """
    At this point I need limit the mouse actions in this window.
    By default this only limits the mouse press in this window
    TODO: Add the logic to move the cursor to the automatic end position.
    """
    def mousePressEvent(self, QMouseEvent):
        print("Ignore the mouse press for now")



