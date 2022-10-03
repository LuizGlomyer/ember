#!/usr/bin/env python
from colorama import Fore, Back, Style
import datetime
import os
from time import sleep
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from simplejson import load
import json

GPIO.setmode(GPIO.BCM)

reader = SimpleMFRC522()

buzzer = 14
led_verde = 21
led_vermelho = 26

GPIO.setup(buzzer, GPIO.OUT)
GPIO.setup(led_verde, GPIO.OUT)
GPIO.setup(led_vermelho, GPIO.OUT)

buzz = GPIO.PWM(buzzer, 1000)




node_name = "Home"

def time_now():
    return f"{datetime.datetime.now()}"


def load_cards():
        with open("cards.json", "r") as file:
            data = json.load(file)
            return data


def save_card(card_id):
    with open("cards.json", "a+") as file:
        lines = file.read()
        print(f"{datetime.datetime.now()}")
        file.writelines(f"{datetime.datetime.now()}")
        print(lines) 


def save_cards(cards):
    with open("cards.json", "w") as file:
            file.write(json.dumps(cards, ensure_ascii=False))


def create_card(id, name, permission_list):
    assert not cards.get((str(id))), "Card already registered"
    
    new_card = {}
    new_card["creation_date"] = time_now()
    new_card["owner"] = name
    new_card["active"] = True
    new_card["permissions"] = permission_list
    new_card["access_log"] = {}

    cards[id] = new_card
    save_cards(cards)


def log_access(id, resource):
    id = str(id)
    assert cards.get(id), "Card must exist"
    card = cards.get(id)

    date = time_now()
    print(f"{card['owner']} trying to access \"{resource}\"")
    if resource in card["permissions"]:
        print(
            Fore.GREEN + 
            "ACCESS GRANTED" +
            Style.RESET_ALL
        )
    else:
        print(
            Fore.RED + 
            "ACCESS DENIED" +
            Style.RESET_ALL
        )
    print("Date: " + date)
    print("=" * 40)

    card["access_log"][date] = {
        "at": node_name,
        "resource": resource,
        "granted": resource in card["permissions"],
        "user_permissions": card["permissions"],
        "environment": os.uname()
    }
    
    save_cards(cards)
    # if not granted


cards = load_cards()
#print("Read: ")
#print(cards)

#log_access(99909, "screen")
#create_card(999, "teste", ["read", "camera", "screen"])


try:
    while True:
        id, text = reader.read()
        GPIO.output(led_verde, GPIO.HIGH)
        buzz.start(10)
        
        sleep(0.25)
        GPIO.output(led_verde, GPIO.LOW)
        buzz.stop()
        print("Card id:")
        print(id)
        
        
        sleep(1.5)
except KeyboardInterrupt:
        print("\nKeyboard interrupt. Exiting...")
except SystemExit:
    print("exiting")
#except:
 #       print("Erro")
finally:  
        GPIO.cleanup()
    

