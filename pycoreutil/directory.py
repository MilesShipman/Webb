__author__ = 'milesshipman'
from preference.sysInfo import *

import os
import re


#Todo: I need to take in accound Windows vs UNIX/LINUX
class Navigate():
    """
    This navigate class works now.
    """
    #TODO: Implement the rest of this navigation logic.
    def __init__(self, parentSession):
        self.session = parentSession

    def ls(self, args):
        #TODO: Add the rest of the LS ability. View Source
        print(args)
        if(len(args) < 2):
                return('\n'.join(os.listdir(self.session.getLocation()))) #Don't need windows/mac difference
        return("Working LS")

    #TODO: Add error handling, can this function have an error
    def pwd(self, args):
        return self.session.getLocation()


   #TODO:  Check that Full path works on Windows.
    """
    Note for above:  This could be done with a check searching for the first letter
    of args being '/' or I could do os.path.exists on that path to see if the path actually
    exists. It might be best to do a combination of both, and If I'm on windows Need to check
    for a letter.
    """
    def chdir(self,args):
        print(args)
        #TODO:  How do we go back.. This method doesn't work.
        if(len(args) < 2):
            return "No Path Given" #Todo this need
        elif(args[1][0] == "/"):
            print("Inside path")
            if(os.path.exists(args[1])):
                self.session.setLocation(args[1])
            return 0;
        else:
            print("Valid Command")
            #Set up Variables
            orig = re.findall(r'[^\\/]+|[\\/]',self.session.getLocation())
            argv = re.findall(r'[^\\/]+|[\\/]',args[1])
            print(orig)
            orig = self.remove(orig,"//")
            orig = self.remove(orig,"\\")
            orig = self.remove(orig, '/')
            argv = self.remove(argv,'/') #I prolly need to add another
            print(orig)

            count = argv.count("..")
            #Go Backwards
            if(count > 0):
                print("Going backwards")  #As I go backwards remove
                while ".." in argv:
                    argv.remove("..")
                    orig = orig[:len(orig)-1]
                    if(len(orig) == 1):
                        while ".." in argv:
                            argv.remove("..")
                        break

            #Rebuild Path and set
            newPath = ""
            if not isWindows():
                newPath = newPath + "/"
            for item in orig:
                newPath = newPath + item + "/"

            for item in argv:
                newPath = newPath + item + "/"

            self.session.setLocation(newPath)
            print(newPath)
            #Return path.
            return(0)

    def remove(self,l,token):
        while token in l:
            l.remove(token)
        return l








#TODO Finish creating the remove function
def rm(args):
    return("Working on the Remove function")


"""
This function is responsible for a file/name address
"""
#TODO: REWRITE THIS, Session changes caused more issues.
def autoAddress(base):
    words = base.split('$')
    words = words[1].split()
    if(len(words) < 2):
        #TODO Add logic if we want auto-complete for Functions
        print("Do nothing")
        return ""
    else:
        breakdown = words[1].split("/")
        size = len(breakdown)
        if(size > 1):
            #pull from the existing folder
            location = ""
            for i in range(0, size-1):
                print(breakdown[i])
                location = location + breakdown[i]+"/"
            if(os.path.exists(location)):
                options = os.listdir(location)
                #print(options)
            else:
                return ""

        else:
            #Pull from current folder.
            options = os.listdir(".")
            #print(options)

        #print(options)
        #This is the autocomplete.
        #print(breakdown[size-1])
        results = diff(breakdown[size-1], options)
        if(len(results) == 1):
            print("Go ahead and cut the excess here")
            size = len(breakdown[size-1])
            results[0] = results[0][size:]
            print(results)

        return results




"""
What is the best way to go about this. I need to diff but I would also provide a list of diff options
Not sure how to do this the right way.
I believe that this is correct and will work.
"""
def diff(word, options):
    print("Diff this")
    print(word)
    #Accurate
    size = len(word)
    results = list()
    position = 0;
    for item in options:
        if(word == item[0:size]):
            results.append(item)
    return results


