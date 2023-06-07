
# ABOUT
name = "EDIT.txt"
description = "Edit .txt files with a simple editor."
commands = ["EDIT", "TXT"]

import time
import colorama

colorama.init()
## Text
# Main
CLR = '\033[2J' # Clear
RSET = '\033[0m' # Reset
# Colors
RED = '\033[31m' # Red
GRN = '\033[32m' # Green
PRPL = '\033[35m' # Purple

# OS
def file_exists(file_path):
    try:
        with open(file_path, 'r'):
            pass
    except FileNotFoundError:
        return False
    return True

PATH = "./txt/"

def launch():
    file_type = ""
    text = ""
    while True:
        print(CLR)
        print(PRPL)
        print("───────────────────────────────────────────────────────────────────────")
        print("─████████──██████────████████──████████────────────────────────────────")
        print("─██────────██────██─────██────────██────────────██████──██──██──██████─")
        print("─██████────██────██─────██────────██──────────────██──────██──────██───")
        print("─██────────██────██─────██────────██──────████────██──────██──────██───")
        print("─████████──██████────████████─────██──────████────██────██──██────██───")
        print("────────────────────────────────────────────────────────────────────────"+ RSET)
        print("Welcome to the text editor.")
        print("Closing will store document in memory, but not if KONos shuts down!")
        print("Can only open and save .txt files.")
        print("PRESS (ENTER) for new line.")
        print("Type 'DEL:1' to delete first line (Number 1).")
        print("Type 'SET:1:NEWLINE' to set first line (Number 1) to 'NEWLINE'.")
        print("Type 'CLEAR *' to clear text.")
        print("Type 'SAVE:FILENAME' to save (without .txt at the end).")
        print("Type 'LOAD:FILENAME' to load (without .txt at the end).")
        print("Type 'EXIT' to exit.")
        print("")
        i = 0
        while i < len(text.split("\n")):
            print(PRPL + str(i+1) + " █ " + RSET + text.split("\n")[i])
            i+=1
        print("")
        inpt = input()
        if inpt.startswith("SAVE"):
            if len(inpt.split(":")) > 1:
                confirm = False
                if file_exists(PATH +  inpt.split(":")[1] + ".txt") == True:
                    print(RED + "File Exists..." + RSET)
                    print("Do you want to overide? Y/N")
                    inpt2 = input().upper()
                    if inpt2 == "Y" or inpt2 == "YES":
                        print(RED + "Overwriting..." + RSET)
                        time.sleep(0.5)
                        confirm = True
                elif file_exists(PATH +  inpt.split(":")[1] + ".txt") == False:
                        confirm = True
                if confirm:
                    try:
                        file_manager = open(PATH +  inpt.split(":")[1] + ".txt", "w")
                        file_manager.write(text)
                        file_manager.close()
                        print(GRN + "Saved!" + RSET)
                        time.sleep(1)
                    except:
                        print(RED + "An error occured saving... Please retry." + RSET)
                        time.sleep(3)
            else:
                print(RED + "An error occured." + RSET)
        elif inpt.startswith("LOAD"):
            if len(inpt.split(":")) > 1:
                confirm = False
                if file_exists(PATH +  inpt.split(":")[1] + ".txt") == False:
                    print("File does not exist.")
                    print("Do you want to create it? Y/N")
                    inpt2 = input().upper()
                    if inpt2 == "Y" or inpt2 == "YES":
                        print("Creating...")
                        time.sleep(0.5)
                        confirm = True
                elif file_exists(PATH +  inpt.split(":")[1] + ".txt") == True:
                        confirm = True
                if confirm:
                    try:
                        if file_exists(PATH +  inpt.split(":")[1] + ".txt") == False:
                            file_manager = open(PATH +  inpt.split(":")[1] + ".txt", "w")
                            text = ""
                        else:
                            file_manager = open(PATH +  inpt.split(":")[1] + ".txt", "r")
                            text = file_manager.read()
                        file_manager.close()
                        print(GRN + "Loaded!" + RSET)
                        time.sleep(1)
                    except:
                        print(RED + "An error occured loading... Please retry." + RSET)
                        time.sleep(3)
            else:
                print(RED + "An error occured." + RSET)
        elif inpt.startswith("DEL"):
            try:
                replacedtext = text.split("\n")
                replacedtext.pop(int(inpt.split(":")[1])-1)
                text = ""
                for i in replacedtext:
                    if i == replacedtext[len(replacedtext)-1]:
                        text += i
                    else:
                        text += i + "\n"
            except:
                print(RED + "An error occured." + RSET)
                time.sleep(2)
        elif inpt.startswith("SET"):
            try:
                replacedtext = text.split("\n")
                replacedtext[int(inpt.split(":")[1])-1] = inpt.split(":")[2]
                text = ""
                for i in replacedtext:
                    if i == replacedtext[0]:
                        text = i
                    # if i == replacedtext[len(replacedtext)-1]:
                    #     text += "\n" + i
                    else:
                        text += "\n" + i
            except:
                print(RED + "An error occured." + RSET)
                time.sleep(2)
        elif inpt == "EXIT":
            break
        else:
            if text != "":
                text += "\n" + inpt
            else:
                text = inpt