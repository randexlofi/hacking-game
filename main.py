import misc, vars # own
import sys, os, time # system
from colorama import init, Fore, Style 
init() # init colorama

cur_dir = "CD:"
money = 100

def choose_name():
    if misc.player['name'] == "undefined":
        while True:
            p_name = input("Choose your nickname: ")
            confirm = input(f"Do you want to save the name: {p_name}? [y]: ")
            if confirm.lower() == "y":
                misc.player['name'] = p_name
                misc.save_player(misc.player)
                break 
    else:
        print(f"Welcome back {misc.player['name']}.")
        time.sleep(2)
        os.system("cls")

def main():
    # Choose the player name on the first time.
    choose_name()

    while True:
        print(f"""{vars.GAME_ASCII} {Fore.LIGHTBLACK_EX}by randexlofi{Style.RESET_ALL}

    1. Console
    2. Quests
    {Fore.LIGHTBLACK_EX}3. Store (unavailable){Style.RESET_ALL}
    
    x. Quit Game
""")
        cmd = input("> ")

        os.system("cls") 
        if cmd == "1": # Console
            os.system("cls")
            console()
        elif cmd == "2": quest() # Quest menu
        elif cmd == "3": pass # Store
        elif cmd == "x": sys.exit() # Quit game


def quest():
    os.system("cls")
    misc.show_quests()

    while True:
        cmd = input("> ")
        if cmd == "x":
            os.system("cls")
            main()
        else:
            quest()



def console():
    print(Fore.GREEN + "(c) 23-OS [ver. 18.944.12].\nType 'help' for the command list." + Style.RESET_ALL)
    while True:
        command = input(cur_dir + " > ").split(' ', 1)
        cmd = command[0].lower()

        if cmd == "exit": 
            os.system("cls")
            main() # Exit game
        elif cmd == "quit": sys.exit()
        elif cmd == "clr": os.system("cls") # Clear console
        elif cmd == "help": misc.help_file() # Display available commands
        elif cmd == "ping": misc.ping(command) # Ping adress
        elif cmd == "scan": misc.scan(command) # Scan the adress
        else: print(f"'{cmd}' is not a recognized command.\n") # Unrecognized command


if __name__ == "__main__":
    main()
