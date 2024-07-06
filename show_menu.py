'''options list'''
from colorama import Fore,Style,init

init()
def show_menu() -> None:
    '''Menu'''
    print(Style.BRIGHT,Fore.CYAN,
          '[1]',
          Style.RESET_ALL,
          'Get Running-Config'
          )
    print(Style.BRIGHT,Fore.CYAN,
          '[2]',
          Style.RESET_ALL,
          'Get CDP Neighbors'
          )
    print(Style.BRIGHT,Fore.CYAN,
          '[3]',
          Style.RESET_ALL,
          'Get Interface Status'
          )
    print(Style.BRIGHT,Fore.CYAN,
          '[4]',
          Style.RESET_ALL,
          'Get Spanning-Tree'
          )
    print(Style.BRIGHT,Fore.CYAN,
          '[5]',
          Style.RESET_ALL,
          'Get Version'
          )
    print(Style.BRIGHT,Fore.CYAN,
          '[6]',
          Style.RESET_ALL,
          'Get All'
          )
    print(Style.BRIGHT,Fore.CYAN,
          '[7]',
          Style.RESET_ALL,
          'Write Memory'
          )
    print(Style.BRIGHT,Fore.CYAN,
          '[8]',
          Style.RESET_ALL,
          'Log into a new switch'
          )
    print(Style.BRIGHT,Fore.CYAN,
          '[9]',
          Style.RESET_ALL,
          'Zip SwitchConfigs'
          )
    print(Style.BRIGHT,Fore.CYAN,
          '[0]',
          Style.RESET_ALL,
          'Exit the program.'
          )
    return input("Enter your option: ")
