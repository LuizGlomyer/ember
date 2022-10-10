from colorama import Fore, Back, Style
import os
from time import sleep

from mfrc522 import SimpleMFRC522
from simplejson import load
import json

from rfid_reader import ReaderRFID
from systems import Systems
from utils import cprint, print_separator, slprint, time_now

#log_access(99909, "screen")
#create_card(999, "teste", ["read", "camera", "screen"])


class Ember():
    def __init__(self, name) -> None:
        self.node_name = name
        self.cards = []
        self.reader = ReaderRFID()
        self.systems = Systems()

        self.load_cards()

        
        print_separator()
        slprint("Ember System initiated ", 0.1, Fore.BLACK, Back.WHITE)
        slprint(f"Date: {time_now()}", 0.03)
        slprint(f"Nodename: {self.node_name}", 0.03)
        slprint("...", 0.5)

    def __del__(self) -> None:
        pass

    def load_cards(self) -> None:
        with open("cards.json", "r") as file:
            data = json.load(file)
            self.cards = data

    def save_cards(self) -> None:
        with open("cards.json", "w") as file:
            file.write(json.dumps(self.cards, ensure_ascii=False))

    def create_card(self, name, permissions: list) -> None:
        id = self.reader.read()
        id = str(id)
        # to create a new card its id must not already exist
        assert not self.cards.get(id), "Card already registered"

        new_card = {}
        new_card["creation_date"] = time_now()
        new_card["owner"] = name
        new_card["active"] = True
        new_card["permissions"] = permissions
        new_card["access_log"] = {}

        self.cards[id] = new_card
        self.save_cards()
        cprint("CARD CREATED", Fore.YELLOW)
        print_separator()

    def access(self, resource) -> bool:
        id = self.reader.read()
        id = str(id)

        # to log a new access of a card in the system its id must exist in the card list
        assert self.cards.get(id), "Card must exist"

        card = self.cards.get(id)
        # checks if the user has the permissions necessary to use the resource
        granted = resource in card["permissions"]

        access_date = time_now()
        print(f"{card['owner']} trying to access \"{resource}\"")
        if granted:
            cprint("ACCESS GRANTED", Fore.GREEN)
        else:
            cprint("ACCESS DENIED", Fore.RED)

        print("Date: " + access_date)
        print_separator()

        card["access_log"][access_date] = {
            "at": self.node_name,
            "resource": resource,
            "granted": granted,
            "user_permissions": card["permissions"],
            "environment": os.uname()
        }

        self.save_cards()
        if granted:
            self.reader.blink(True)
        else:
            self.reader.blink(False)
        return granted
    
    def menu(self) -> None:
        while True:
            cprint("Select a module", Fore.CYAN, Back.BLACK)
            print('1 - user mode')
            print('2 - admin mode')
            print('0 - exit')
            print("\nEnter: ", end="")
            user_input = input()
            os.system('cls' if os.name == 'nt' else 'clear')

            if user_input == '1':
                self.user_mode()
            if user_input == '2':
                granted = self.access("admin")
                if granted:
                    self.admin_mode()
            if user_input in [0, '0', 'q', 'Q']:
                break
    
    def user_mode(self) -> None:
        cprint("Please select a system", Fore.CYAN, Back.BLACK)
        print('1 - ac')
        print('2 - browser')
        print('0 - exit')
        print("\nEnter: ", end="")
        user_input = input()
        os.system('cls' if os.name == 'nt' else 'clear')

        if user_input == '1':
            granted = self.access("ac")
            if granted:
                self.systems.ac.menu()
                granted = False
        elif user_input == '2':
            granted = self.access("browser")
            if granted:
                self.systems.browser.browse()

    def admin_mode(self) -> None:
        cprint("Please select a function", Fore.CYAN, Back.BLACK)
        print('1 - Create a new card')
        print('2 - Change card permissions')
        print('3 - Delete a card')
        print('0 - exit')
        print("\nEnter: ", end="")
        user_input = input()
        os.system('cls' if os.name == 'nt' else 'clear')
            

    def connect_to_blockchain():
        pass

    def save_to_blockchain():
        pass
