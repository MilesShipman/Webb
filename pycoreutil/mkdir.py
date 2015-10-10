__author__ = 'milesshipman'


"""
This file represents my implementation of mkdir.
Options -p also create all directoryes leading up
        -v verbose displays each directory
        -m specify the octal permissions

example mkdir -p tmdir/{trunk/sources/{includes,docs}, branches, tags)
          tmpdir
    ________|______
   |        |      |
branches   tags  trunk
                   |
                 sources
               ____|_____
              |          |
          includes     docs
"""


class Options():
    def __init__(self):
        self.verbose = 0
        self.full = 0
        self.permissions = 0

    def print(self):
        print("Verbose " + str(self.verbose))
        print("Full " + str(self.full))
        print("permission " + str(self.permissions))

class folder():
    def __init__(self):
        self.name = ""
        self.subFolders = list()

    def push(self, folder):
        self.subFolders.push(folder)

    def pop(self,folder):
        self.subFolders.pop()


def mkdir(args):
    options = Options()
    position = 1;
    #Parse args for options.
    for arg in args:
        print(arg)
        if(arg[0] == '-'):
            position = position + 1
            for letter in arg:
                if(letter == "v"):
                    options.verbose = 1
                elif(letter == "p"):
                    options.full = 1
                elif(letter == "m"):
                    options.permissions = 1
    options.print()

    #Need to be intelligent with how I do this.
    toMake = (args[position:])

    #Parse the builds.
    #mkdir -p tmdir/{trunk/sources/{includes,docs}, branches, tags)
    f = folder()
    print(toMake)
    for item in toMake:
        words = item.split("/")  #This direction must change..
        for word in words:
            print(word)
            if(word.find("{") >= 0):
                print("Multiple")

    return 0


