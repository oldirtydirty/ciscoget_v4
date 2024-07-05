'''Header'''
from colorama import Fore,init,Style

def display_menu() -> None:
    '''Disply Menu'''
    init()
    print(Style.BRIGHT,Fore.CYAN,r'''
  ____ _                  ____      _     _____           _  
 / ___(_)___  ___ ___    / ___| ___| |_  |_   _|__   ___ | |
| |   | / __|/ __/ _ \  | |  _ / _ \ __|   | |/ _ \ / _ \| |
| |___| \__ \ (_| (_) | | |_| |  __/ |_    | | (_) | (_) | |
 \____|_|___/\___\___/   \____|\___|\__|   |_|\___/ \___/|_|
 ''',Style.RESET_ALL,)
