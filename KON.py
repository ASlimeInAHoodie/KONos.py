#!/usr/bin/python

## PY STUFF
from random import *
import random
import colorama
import time
import yaml

# If using Windows, init() will cause anything sent to stdout or stderr
# will have ANSI color codes converted to the Windows versions. Hooray!
# If you are already using an ANSI compliant shell, it won't do anything
colorama.init()

## Text
# Main
CLR = '\033[2J' # Clear
RSET = '\033[0m' # Reset
BOLD = '\033[1m' # Bold
UNDR = '\033[2m' # Underline
# Colors
RED = '\033[31m' # Red
GRN = '\033[32m' # Green
YLW = '\033[33m' # Yellow
BLU = '\033[34m' # Blue
PRPL = '\033[35m' # Purple
WHT = '\033[37m' # White
## Background
# Colors
BG_RED = '\033[41m' # Red

## KONOS STUFF
# Required imports
import main.updatestocks as updatestocks
import apps
# Required variables
skip = False
#logindetals = ["guest", "password"] # Guest Account for Debugging
logindetals = [False, False] # Enable login browser
prevtime = time.time()
programs = []

# File system
def dataUpdate(filedata, loginUsername):
    global data
    global programs
    var_path = "./users/" + loginUsername + ".yaml"
    with open(var_path, 'w') as file:
        yaml.safe_dump(filedata, file)
    with open(var_path, 'r') as file:
        data = yaml.safe_load(file)
    programs = []
    for i in data["programs"]:
        if i == apps.SCARARnet.name: programs.append(apps.SCARARnet)
        elif i == apps.EDITtxt.name: programs.append(apps.EDITtxt)
        elif i == apps.STOCKbroker.name: programs.append(apps.STOCKbroker)

# Main system
def launch():
    global programs
    global prevtime
    global data
    while True:
        print(CLR)
        print(GRN)
        print("Welcome, " + data["login"]["username"])
        print("──────────────────────────────────────────────")
        print("─██╗░░██╗░█████╗░███╗░░██╗░░░░█████╗░░██████╗─")
        print("─██║░██╔╝██╔══██╗████╗░██║░░░██╔══██╗██╔════╝─")
        print("─█████═╝░██║░░██║██╔██╗██║░░░██║░░██║╚█████╗░─")
        print("─██╔═██╗░██║░░██║██║╚████║░░░██║░░██║░╚═══██╗─")
        print("─██║░╚██╗╚█████╔╝██║░╚███║██╗╚█████╔╝██████╔╝─")
        print("─╚═╝░░╚═╝░╚════╝░╚═╝░░╚══╝╚═╝░╚════╝░╚═════╝░─")
        print("──────────────────────────────────────────────"+ RSET)
        news = "News: "
        if time.time() - prevtime > 59 and apps.STOCKbroker in programs:
            updatestocks.launch()
            prevtime = time.time()
            news += "STOCK.broker: stock prices updated"
        else:
            news += "none."
        print(YLW + news + RSET)
        print("")
        print("Available Programs:")
        print("")
        i = 0
        while i < len(programs):
            print(GRN + str(i) + " █ " + programs[i].name + RSET)
            i+=1
        print(" ")
        cmd = input().upper()
        for a in programs:
            for b in a.commands:
                if b == cmd:
                    time.sleep(randrange(1, 2))
                    if a == apps.SCARARnet: dataUpdate(a.launch(data), data["login"]["username"])
                    else: a.launch()

# Run launcher
if skip == False:
    import main.launcher as launcher
    launcher.launch()
elif skip == "Virus":
    open("virus.py")

# Run main system DO NOT EDIT
import main.login as login
data = login.launch(logindetals[0], logindetals[1])
programs = []
dataUpdate(data, data["login"]["username"])
updatestocks.launch()
launch()
