
from cgi import print_arguments
from glob import glob
from multiprocessing.connection import wait
from operator import contains
import os 
import time
import getpass
import json


#Variables:

#Declares if the console should repeat itself
global activate 
activate = False

#goes before user input
nfname = "nf1 >>> "

#contains chosen input
chose = ""

#determines if the user had an exploit before 
hadexploit = False

#determines what exploit is active currently
currentexploit = "none"

#side variable for the run command
runcommand = False

exploitcollections = """Exploit collections:

        Nuke - Basic Nuke framework tools
        Nukeware - Malware collection of the Nuke Framework"""

#confirm if a command was activated
confirmcommand = False

currentdir = os.getcwd()

newname = "None"

nukecontents = """
        Exploits in Nuke:
        Nukemail (Email Spammer) 
        Nukesms (SMS Spammer)
        Nukesherlock (A Nuke modification build on top of sherlock - Username lookup)
        Nukenewsletter (Also a Email Spammer, but it signs the target up for multiple newsletters)
        Nukegram (A Instagram mass bot control tool)
        """

User = getpass.getuser()



#Functions:

# define a clear command

# going to current dir
os.chdir(os.path.dirname(os.path.realpath(__file__)))
def clr():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
def animation():
    animation = ["="]
    for i in range(66):
        print("".join(animation))
        print("".join(animation))
        animation.append("═")
        time.sleep(0.015)
        clr()
    print("═══════════════════════════════════════════════════════════════════")
    print("═══════════════════════════════════════════════════════════════════")
    time.sleep(0.3)


def askrun():
    global chose
    runcommand = True
    chose = input("Type the Name of your wanted exploit here: ")

def startinputter():
    global activate
    activate = True

def stopinputter():
    global activate
    activate = False

def confirm(x):
    global confirmcommand
    confirmcommand = x

def nowrunning(exploit, file):
    clr()
    print("Now running " + exploit)
    time.sleep(1)
    os.chdir(currentdir + "/Exploits")
    os.system("python3 " + file)
    exit()

def getlocaluser():
    try:
        global User
        User = getpass.getuser()
    except:
        User = "(Could not get local user)"
    return User

def printuser():
    if namedata["standard"] == True:
        return getlocaluser()
    else:
        return namedata["name"]

def openjson(file):
    
    os.chdir (currentdir + "/Saves")
    with open(file) as f:
        data = json.load(f)
    
    return data
    
    

    


#Variables which require declared methods:
namedata = openjson("Name.json")
isnewdata = openjson("New.json")

if isnewdata["isnew"] == True:
    clr()
    print("Hey! This is the first time you are using nf1! Make sure you type help as soon as nf1 starts get a list of commands! (nf1 will start in 3 seconds)")
    time.sleep(3)
    changeisnewdata = {"isnew": False}
    with open("New.json", "w") as f:
        json.dump(changeisnewdata, f)
    




animation()
clr()
print("═══════════════════════════════════════════════════════════════════")
os.system("figlet -f smslant Nuke Framework")
print("═══════════════════════════════════════════════════════════════════")

time.sleep(0.1)
print("W")
time.sleep(0.015)
clr()

print("═══════════════════════════════════════════════════════════════════")
os.system("figlet -f smslant Nuke Framework")
print("═══════════════════════════════════════════════════════════════════")
print("We")
time.sleep(0.015)
clr()

print("═══════════════════════════════════════════════════════════════════")
os.system("figlet -f smslant Nuke Framework")
print("═══════════════════════════════════════════════════════════════════")
print("Wel")
time.sleep(0.015)
clr()

print("═══════════════════════════════════════════════════════════════════")
os.system("figlet -f smslant Nuke Framework")
print("═══════════════════════════════════════════════════════════════════")
print("Welc")
time.sleep(0.015)
clr()

print("═══════════════════════════════════════════════════════════════════")
os.system("figlet -f smslant Nuke Framework")
print("═══════════════════════════════════════════════════════════════════")
print("Welco")
time.sleep(0.015)
clr()
print("═══════════════════════════════════════════════════════════════════")
os.system("figlet -f smslant Nuke Framework")
print("═══════════════════════════════════════════════════════════════════")
print("Welcom")
time.sleep(0.015)
clr()
print("═══════════════════════════════════════════════════════════════════")
os.system("figlet -f smslant Nuke Framework")
print("═══════════════════════════════════════════════════════════════════")
print("Welcome")
time.sleep(0.015)
clr()
print("═══════════════════════════════════════════════════════════════════")
os.system("figlet -f smslant Nuke Framework")
print("═══════════════════════════════════════════════════════════════════")
print("Welcome b")
time.sleep(0.015)
clr()
print("═══════════════════════════════════════════════════════════════════")
os.system("figlet -f smslant Nuke Framework")
print("═══════════════════════════════════════════════════════════════════")
print("Welcome ba")
time.sleep(0.015)
clr()
print("═══════════════════════════════════════════════════════════════════")
os.system("figlet -f smslant Nuke Framework")
print("═══════════════════════════════════════════════════════════════════")
print("Welcome bac")
time.sleep(0.015)
clr()
print("═══════════════════════════════════════════════════════════════════")
os.system("figlet -f smslant Nuke Framework")
print("═══════════════════════════════════════════════════════════════════")
print("Welcome back")
time.sleep(0.015)
clr()
print("═══════════════════════════════════════════════════════════════════")
os.system("figlet -f smslant Nuke Framework")
print("═══════════════════════════════════════════════════════════════════")
print("Welcome back!")
time.sleep(1)
clr()
print("═══════════════════════════════════════════════════════════════════")
os.system("figlet -f smslant Nuke Framework")
print("═══════════════════════════════════════════════════════════════════")

print("NukeFramework is ready! You are logged in as " + printuser() + " (Type help to get Options)\n")

startinputter()
while activate == True:
    confirm(False)
    inputter = input(nfname)
    if inputter.startswith(" "):
        while inputter.startswith(" "):
            inputter = inputter.removeprefix(" ")
    #basics
    if inputter.startswith("help") == True:
        print("""
        Basics:

        help - shows this menu
        exit - exits the program
        clear - clears the console
        restart - restarts the program
        ce *ARGUMENT* - change Exploit collection (if left blank will exit current Exploit collection)
        run *ARGUMENT* - run an exploit (if in collection)
        
        Misc:
        name *New Name* - changes your name that gets displayed when you open nf1
        name *-r* - changes your name to the default login name of your Computer
        """ + exploitcollections)
        confirm(True)
    if inputter.startswith("exit") == True:
        clr()
        print("exiting...")
        exit()
    if inputter.startswith("clear") == True:
        clr()
        confirm(True)
    if inputter.startswith("restart") == True:
        stopinputter()
        
        print("Restarting...")
        time.sleep(1)
        animation()
        clr()
        print("═══════════════════════════════════════════════════════════════════")
        os.system("figlet -f smslant Nuke Framework")
        print("═══════════════════════════════════════════════════════════════════")
        namedata = openjson("Name.json")
        print("Restarted Nuke Framework! logged in as " + printuser() + " (Type help to get Options)\n")
        time.sleep(1)
        startinputter()
        confirm(True)
    
    #exploit collection changers
    if inputter.startswith("ce") == True:
        inputter = inputter.removeprefix("ce ")
        inputter = inputter.replace(" ", "")
        if hadexploit == True:
            print("removed current exploit collection " + currentexploit)
            hadexploit = False
            currentexploit = "none"
        nfname = "nf1 >>> "
        confirm(True)
    if inputter.startswith("Nukeware") == True:
        print("changed exploit collection to Nukeware")
        nfname = "nf1 /Nukeware >>> "
        hadexploit = True
        currentexploit = "Nukeware"
        confirm(True)
    if inputter.startswith("Nuke") == True:
        print("changed exploit collection to Nuke")
        nfname = "nf1 /Nuke >>> "
        hadexploit = True
        currentexploit = "Nuke"
        confirm(True)
   

    #ls commands
    if inputter.startswith("ls") == True:
        inputter = inputter.removeprefix("ls")
        inputter = inputter.replace(" ", "")
        if inputter == "" and currentexploit == "none":
            print(nukecontents)
            confirm(True)
        if currentexploit == "Nukeware":
            print("""
            Exploits in Nukeware:
            
            """)
            confirm(True)
        if currentexploit == "Nuke":
            print(nukecontents)
            confirm(True)
    # run command(s)
    runcommand = False
    if inputter.startswith("run") == True and currentexploit == "none":
        print("You are not in a exploit collection yet! (Type ce *ARGUMENT* to change. If you search for a list of commands type help)")
        confirm(True)
    if inputter.startswith("run") == True and currentexploit == "Nuke":
        inputter = inputter.removeprefix("run ")
        if inputter == "Nukemail":
            nowrunning("Nukemail", "Nukemail.py")
        elif inputter == "Nukesms":
            pass
        elif inputter == "Nukesherlock":
            nowrunning("Nukesherlock", "Nukesherlock.py")
        elif inputter == "Nukenewsletter":
            nowrunning("Nukenewsletter", "Nukenewsletter.py")
        elif inputter == "Nukegram":
            nowrunning("Nukegram", "Nukegram.py")
        elif runcommand == True:
            print("This is no valid exploit")
            runcommand = False
        confirm(True)
    if inputter.startswith("name") == True and not "-r" in inputter:
        inputter = inputter.removeprefix("name ")
        newname = inputter
        newnamedata = {
            "standard": False,
            "name": newname,
        }
        os.chdir("../Saves")
        with open("Name.json", "w") as f:
            json.dump(newnamedata, f)
        print("New Name showed at login: " + newname)
        confirm(True)
    if "-r" in inputter and inputter.startswith("name") == True:
        newnamedata = {
            "standard": True,
            "name": newname,
        }
        os.chdir("../Saves")
        with open("Name.json", "w") as f:
            json.dump(newnamedata, f)
        print("Name has been resetted to your login name")
        confirm(True)





    if confirmcommand == False:
        print(inputter + " is no valid command!")


    
        
            

    
    
    
    





