import os
from colorama import Back, Fore

from utils import cprint, print_system_separator


class Systems:
    def __init__(self) -> None:
        self.ac = AC()
        self.tv = TV()
        self.stereo = Stereo()
        self.fridge = Fridge()
        self.browser = Browser()

    def __del__(self) -> None:
        pass


class AC:
    def __init__(self) -> None:
        self.temperature = 20

    def change_temperature(self, temperature) -> None:
        self.temperature = temperature
        cprint("New temperature set", Fore.YELLOW, Back.BLACK)

    def view_temperature(self) -> None:
        cprint(
            f"Current temperature: {self.temperature} °C", Fore.YELLOW, Back.BLACK)

    def menu(self) -> None:
        cprint("This is the AC menu", Fore.CYAN, Back.BLACK)
        self.view_temperature()

        while True:
            try:
                print('1 - change current temperature')
                print('2 - view current temperature')
                print('0 - exit')
                print("\nEnter: ", end="")
                user_input = input()
                os.system('cls' if os.name == 'nt' else 'clear')

                if user_input in ['0', 'q', 'Q', 'exit']:
                    print("Exiting AC menu...")
                    break
                elif user_input == '1':
                    print("Enter your desired temperature: ", end="")
                    new_temperature = int(input())
                    self.change_temperature(new_temperature)
                elif user_input == '2':
                    self.view_temperature()
                print_system_separator()

            except KeyboardInterrupt:
                print("\nExiting AC menu")
                break
            except ValueError:
                print("Please enter a valid value")


class TV:
    pass


class Stereo:
    pass


class Fridge:
    pass


class Browser:
    @staticmethod
    def browse() -> None:
        cprint("This is the Web Browser", Fore.CYAN, Back.BLACK)
        print("Enter a website. Defaults to google.com")
        print("url: ", end="")
        website = input()
        print(website)

        if website == "":
            website = "google.com"

        os.system(f"w3m {website}")
