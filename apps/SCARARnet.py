
from random import *
import colorama
import time

colorama.init()

## Text
# Main
CLR = '\033[2J' # Clear
RSET = '\033[0m' # Reset
# Colors
BLU = '\033[34m' # Blue

# ABOUT
name = "SCARAR.net"
description = "Browse the internet!"
commands = ["SCARAR", "NET"]

def launch(file):
    while True:
        print(CLR)
        print(BLU)
        print("Welcome, " + file["login"]["username"])
        print("■■■■  ■■■■  ■■■■■  ■■■■■  ■■■■■  ■■■■■")
        print("■     ■     ■   ■  ■   ■  ■   ■  ■   ■      ■  ■ ■■■■ ■■■■")
        print("■■■■  ■     ■■■■■  ■■■■   ■■■■■  ■■■■       ■■ ■ ■■■   ■")
        print("   ■  ■     ■   ■  ■  ■   ■   ■  ■  ■   ■■  ■ ■■ ■     ■")
        print("■■■■  ■■■■  ■   ■  ■   ■  ■   ■  ■   ■  ■■  ■  ■ ■■■■  ■" + RSET)
        print("")
        print("")
        print("Available Sites:")
        print("AppStore | Bank | News | Blogs")
        print(" ")
        cmd = input().upper()
        if cmd == "APPSTORE" or cmd == "STORE" or cmd == "APP":
            time.sleep(0.5)
            appstore(file)
        elif cmd == "BANK" or cmd == "BNK":
            time.sleep(0.5)
            return file
        elif cmd == "EXIT":
            return file

def appstore(file):
    while True:
        print(CLR)
        print(BLU)
        print("■■■■  ■■■■  ■■■■■  ■■■■■  ■■■■■  ■■■■■")
        print("■     ■     ■   ■  ■   ■  ■   ■  ■   ■      ■  ■ ■■■■ ■■■■")
        print("■■■■  ■     ■■■■■  ■■■■   ■■■■■  ■■■■       ■■ ■ ■■■   ■")
        print("   ■  ■     ■   ■  ■  ■   ■   ■  ■  ■   ■■  ■ ■■ ■     ■")
        print("■■■■  ■■■■  ■   ■  ■   ■  ■   ■  ■   ■  ■■  ■  ■ ■■■■  ■")
        print("")
        print("■■■■  ■■■■  ■■■■■  ■■■■■  ■■■■■  ■■■■■  ■■■■■  ■■■■■")
        print("■  ■  ■  ■  ■   ■  ■        ■    ■   ■  ■   ■  ■")
        print("■■■■  ■■■■  ■■■■■  ■■■■■    ■    ■   ■  ■■■■   ■■■ ")
        print("■  ■  ■     ■          ■    ■    ■   ■  ■  ■   ■")
        print("■  ■  ■     ■      ■■■■■    ■    ■■■■■  ■   ■  ■■■■■" + RSET)
        print("")
        print("")
        print("Downloadable Programs:")
        print("Chat | ProgramMaker | KONGuard | Stocks")
        print(" ")
        cmd = input().upper()
        if cmd == "PROGRAMMAKER" or cmd == "PROGRAM" or cmd == "MAKER":
            if app_programMaker == False:
                time.sleep(0.5)
                app_programMaker = True
                download("ProgramMaker ")
        elif cmd == "KONGUARD" or cmd == "KON":
            if app_konGuard == False:
                time.sleep(0.5)
                app_konGuard = True
                download("KONGuard ")
        elif cmd == "CHAT":
            if app_chat == False:
                time.sleep(0.5)
                app_chat = True
                download("Chat ")
        elif cmd == "STOCKS" or cmd == "STOCK":
            import apps.STOCKbroker as STOCKbroker
            file["programs"].append(STOCKbroker.name)
            time.sleep(0.5)
            download("Stocks ")
        elif cmd == "EXIT":
            time.sleep(0.3)
            break

def download(app):
    global programs
    print(CLR)
    print("APPLICATION DOWNLOADER")
    print("Beginning Download of: " + app)
    var_perc = 0
    while var_perc < 90:
            time.sleep((randrange(1, 5))/10)
            var_perc += randrange(1,9)
            print(app + str(var_perc) + "%")
    time.sleep(0.3)
    print(app + "100%")
    print(app + "Finished Downloading")
    print("Returning to SCARAR.NET APPSTORE...")
    time.sleep(1)