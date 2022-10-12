import datetime
import sys
from time import sleep
from colorama import Fore, Back, Style


def time_now():
    return f"{datetime.datetime.now()}"


def cprint(string, foreground_color, background_color="", end='\n'):
    # prints colored text onto the terminal
    print(
        foreground_color +
        background_color +
        string
        + Style.RESET_ALL,
        end=end
    )


def slprint(string, interval, foreground_color="", background_color=""):
    for char in string:
        sys.stdout.write(foreground_color + background_color + char)
        sys.stdout.flush()
        sleep(interval)
    print(Style.RESET_ALL)


def print_separator():
    print("=" * 40)


def print_system_separator():
    print("-" * 30)

def is_break_sequence(user_input):
    user_input = str(user_input).lower()
    if user_input in [0, '0', 'q', 'quit', 'exit']:
        return True
    else:
        return False