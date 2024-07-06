'''loging entry point'''
import sys
from getpass import getpass
import argparse
from colorama import Style,Fore,init
from display_menu import display_menu
from multi_addr import multi_addr
import ciscoget as CiscoGet

__version__= '4.1'

parser = argparse.ArgumentParser()
parser.add_argument("-s",
                    "--secret",
                    action="store_true",
                    dest="secret",
                    help="use if enable secret is needed."
                    )
parser.add_argument("-V",
                    "--version",
                    action="version",
                    version=f'Cisco Get Version {__version__}'
                    )
args = parser.parse_args()


def entry() -> None:
    '''Initial function'''
    init()
    try:
        display_menu()
        addr = multi_addr()
        username = input('Username: ')
        passwd =  getpass('Password: ')
        if args.secret:
            secret = getpass('Secret: ')
        else:
            secret = passwd
        print('Checking credentials')
        addresses = []
        for i in addr:
            cisco_get = CiscoGet.CiscoGet(i,username,passwd,secret)
            cred_check = cisco_get.hostname
            if 'Bad Username/Password' not in cred_check:
                print(Style.BRIGHT,Fore.CYAN,
                      f"[+] Credentials are good for {i}",
                      cred_check,
                      Style.RESET_ALL
                      )
                addresses.append(i)

        return {'addr' : addresses,
                'user' : username ,
                'passwd' : passwd,
                'secret' : secret
                }
    except ValueError:
        print(Style.BRIGHT,Fore.RED,
              '[-] IP Address must be set!',
              Style.RESET_ALL
              )
        # menu()
    except KeyboardInterrupt:
        print("\nCtl C was pressed!\nGoodbye!")
        sys.exit(9)
