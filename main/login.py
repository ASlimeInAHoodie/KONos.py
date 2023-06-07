import yaml
import colorama
import time

colorama.init()
## Text
# Main
CLR = '\033[2J' # Clear
RSET = '\033[0m' # Reset
# Colors
RED = '\033[31m' # Red
GRN = '\033[32m' # Green

# OS
def file_exists(file_path):
    try:
        with open(file_path, 'r'):
            pass
    except FileNotFoundError:
        return False
    return True

def launch(preusername, prepassword):
    logged = False
    if preusername != False and preusername != "" and prepassword != False and prepassword != "":
        if file_exists("./users/" + preusername.lower() + ".yaml"):
            with open('./users/' + preusername.lower() + ".yaml", 'r') as file:
                details = yaml.safe_load(file)
                if prepassword == details["login"]["password"]:
                    logged = True
                    print(CLR)
                    print(GRN + "Logged in!" + RSET)
                    print("Username: " + preusername.lower())
                    print("Password: " + ("*" * len(prepassword)))
                    time.sleep(1)
    while logged == False:
        if logged:
            break
        print(CLR)
        print("Please login:")
        print("Username:")
        username = input()
        if file_exists("./users/" + username.lower() + ".yaml"):
            with open('./users/' + username.lower() + ".yaml", 'r') as file:
                details = yaml.safe_load(file)
                while True:
                    if logged:
                        break
                    print(CLR)
                    print("Please login:")
                    print("Username: " + username.lower())
                    print("Password: ")
                    password = input()
                    if password == details["login"]["password"]:
                        logged = True
                        print(CLR)
                        print(GRN + "Logged in!" + RSET)
                        print("Username: " + username.lower())
                        print("Password: " + ("*" * len(password)))
                        time.sleep(2)
        else:
            print(RED + "Login failed: Invalid username." + RSET)
            time.sleep(1)
    return details
