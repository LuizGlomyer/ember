import datetime
import sys
from time import sleep
from colorama import Fore, Back, Style

break_sequences = [0, '0', 'q', 'Q', 'quit', 'exit']

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
