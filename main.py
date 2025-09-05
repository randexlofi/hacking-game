import misc # own
import sys, os # system
from colorama import init, Fore, Style 
init() # init colorama

cur_dir = "CD:"
money = 100

def main():
    while True:
        print("""
    1. Console
    
    x. Quit Game
""")
        cmd = input("> ")

        os.system("cls")
        if cmd == "1":
            os.system("cls")
            console()
        if cmd == "x":
            sys.exit()


def console():
    print(Fore.GREEN + "(c) 23-OS [ver. 18.944.12].\nType 'help' for the command list." + Style.RESET_ALL)
    while True:
        command = input(cur_dir + " > ").split(' ', 1)
        cmd = command[0].lower()

        if cmd == "exit": 
            os.system("cls")
            main() # Exit game
        elif cmd == "clr": os.system("cls") # Clear console
        elif cmd == "help": misc.help_file() # Display available commands
        elif cmd == "ping": misc.ping(command) # Start ping operation
        elif cmd == "scan": pass 
        else: print(f"'{cmd}' is not a recognized command.\n") # Unrecognized command


if __name__ == "__main__":
    main()
