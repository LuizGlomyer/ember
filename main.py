import sys
import traceback

from ember import Ember
from utils import print_separator


if __name__ == "__main__":
    node_name = "Raspberry Pi"
    # if the user passes an argument, make it the node_name
    if len(sys.argv) > 1:
        node_name = sys.argv[1]

    ember = Ember(node_name)
    while True:
        try:
            ember.menu()

        except AssertionError as e:
            traceback.print_exc()
            ember.reader.blink(False)
            print_separator()
        except KeyboardInterrupt:
            print("\nKeyboard interrupt. Exiting...")
            exit()
        except SystemExit:
            print("\nExiting...")
