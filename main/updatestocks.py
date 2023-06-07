from random import *
import yaml

PATH = "./main/stocks.yaml"

# OS
def file_exists(file_path):
    try:
        with open(file_path, 'r'):
            pass
    except FileNotFoundError:
        return False
    return True

def yaml_read():
    with open(PATH, 'r') as file:
        return yaml.safe_load(file)

def yaml_write(filedata):
    with open(PATH, 'w') as file:
        yaml.safe_dump(filedata, file)

def launch():
    if file_exists(PATH):
        file = yaml_read()
        # ACTION HERE
        weightquantity = 100
        while weightquantity > 0:
            for stock in file:
                if weightquantity < 0:
                    break
                weight = file[stock]["weight"]
                price = file[stock]["price"]
                weight = round(weight * (randrange(98, 105)/100), 3)
                if weight > 20: weight -= 2
                if weight < 1: weight += 1
                price = price * (randrange(round(80 + weight), round(130 - weight))/100)
                if price > 10000: price = 10000
                if price < 1: price += 1
                file[stock]["weight"] = weight
                file[stock]["price"] = round(price, 2)
                weightquantity -= weight
        yaml_write(file)
    else:
        print("Non-fatal error: stocks update was unreachable")
        input()