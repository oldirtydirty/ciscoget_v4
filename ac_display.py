'''Header'''
from colorama import init,Fore,Style

def display():
    '''Display'''
    init()
    print(Fore.CYAN ,r'''    _    ____   _____           _
    / \  / ___| |_   _|__   ___ | |
   / _ \| |       | |/ _ \ / _ \| |
  / ___ \ |___    | | (_) | (_) | |
 /_/   \_\____|   |_|\___/ \___/|_|''',Style.RESET_ALL,'\n')


def ini_lic():
    '''Select Menu'''
    print(Fore.CYAN,'[1]',Style.RESET_ALL,'Get License to File.')
    print(Fore.CYAN,'[2]',Style.RESET_ALL,'Get ini to File.\n')
    return input('Select Option: ')
