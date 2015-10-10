__author__ = 'MilesShipman'


from PyQt5 import QtWidgets
import sys
from terminal.command import *
from terminal.menu import *
from terminal.terminal import *
from pycoreutil.directory import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


"""
See notebook for full list of ideas of what I wish to implement in this application.
"""

#TODO I need to comment the hell out of my code.

"""
This will be my custom QTabWidget that will allow me to handle everything needed for the tab
"""
class TabWidget(QTabWidget):
    def __init__(self,parent):
        super(TabWidget,self).__init__(parent)
        self.tabBar().setVisible(False)#This bit of code will hide the Tab bar.
        self.setStyleSheet("QTabWidget::pane{ border-top: 1px solid; }") #I need to keep the top part of the frame
        #Set the Tabs Closeable and create the trigger to close
        self.setTabsClosable(True)
        self.tabCloseRequested.connect(self.closeTab)



    def closeTab(self,index):
        print("TODO: write a proper close segment")

    def add(self):
        """
        Function creates a brand new tab for running in the program
        :return: Noe
        """
        tab = QWidget(self)
        te  = TextArea()  #Need to find the way to access this later to clean up.
        tabLayout = QVBoxLayout(tab)
        tab.setLayout(tabLayout)
        tabLayout.addWidget(te)
        self.addTab(tab, "Tab 1") #Create a single Tab. Can I hide the tab bar.
        self.setCurrentIndex(self.count())
        if(self.count() > 1):
            self.tabBar().setVisible(True) #Bring back the tabbar

    def remove(self):
        """
            Removes the selected Tab from the current program
            TODO: add a way to recognize which tab is being deleted.
        """
        print("Remove tab")


    def adjust(self):
        """

        """
        print(self.count)



    #I Need a function to pull off a tab and make independent.

    def test(self):
        print(self.count())
        print("This is a test")




"""
This function creates the main window for operating the terminal.  The Tabs will control the ability to migrate to
multiple terminal sessions during a hosting event.  This will allow multi-tasking within one screen.  Eventually user
will be able to drag the tab out of the window to make a standalone window.
"""
class Window(QMainWindow):
    def __init__(self,parent=None):
        super(Window,self).__init__(parent)
        self.menu = Menu(self)
        self.menu.createMenu()
        #createMenu(self) #Create the Menu
        centralWidget = QWidget(self)
        centralWidgetLayout = QVBoxLayout(centralWidget)
        centralWidget.setLayout(centralWidgetLayout)


        self.setMinimumSize(QSize(640,300))
        centralWidget.setContentsMargins(-15,0,-15,-15) #I believe I need to change this when sizes are different
        centralWidget.setContextMenuPolicy(Qt.NoContextMenu)

        self.tabContainer = TabWidget(centralWidget)

        tab1 = QWidget(self.tabContainer)
        te = TextArea()
        tab1layout = QVBoxLayout(tab1)
        tab1.setLayout(tab1layout)
        tab1layout.addWidget(te)

        #TODO: a)Figure out how to hide the Tab bar when there is one tab
        #TODO: b)Figure out how to get rid of Border on Tab
        self.tabContainer.addTab(tab1, "Tab 1") #Create a single Tab. Can I hide the tab bar.
        self.tabContainer.setCurrentIndex(0)
        centralWidgetLayout.addWidget(self.tabContainer)

        self.setCentralWidget(centralWidget)

        """
        I don't need these two settings except in a tab setting.
        """

#        #tabContainer.setStyleSheet("QTabBar::tab{width:100px; }") #make this code dynamic
        #tabContainer.resize(1000, 1000)
        #self.createTabs() #Create the Tabs
        #self.show() #Show the Window

    """
    How do I add this to my project.
    """
    def createTabs(self):
        tabs   = QTabWidget()
        pushButton1 = QPushButton("QPushButton 1")
        pushButton2 = QPushButton("QPushButton 2")

        tab1   = QWidget()
        tab2   = QWidget()
        tab3   = QWidget()

        vBoxlayout   = QVBoxLayout()
        vBoxlayout.addWidget(pushButton1)
        vBoxlayout.addWidget(pushButton2)

        #Resize width and height
        tabs.resize(250, 150)

        #Move QTabWidget to x:300,y:300
        tabs.move(300, 300)

        #Set Layout for Third Tab Page
        tab3.setLayout(vBoxlayout)

        tabs.addTab(tab1,"Tab 1")
        tabs.addTab(tab2,"Tab 2")
        tabs.addTab(tab3,"Tab 3")









"""
This will represent the core layout of my program.
"""
#Temporary Main for testing purposes
def main():
    print("Starting terminal Application")
    app    = QApplication(sys.argv)

    #Main Widget Gui
    window = Window()
    window.show()


    #rootMenu = QtWidgets.QMenuBar(None)
    #fileMenu = rootMenu.addMenu('File')

    #rootMenu.show()
    #tabs.show()


    sys.exit(app.exec_())


main()

