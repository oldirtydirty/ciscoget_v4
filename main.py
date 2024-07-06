'''Main program'''
import sys
from colorama import Fore,Style,init
import entry
from google_auth import g_auth
from onclick import OnClick
from display_menu import display_menu
from show_menu import show_menu
import ciscoget as CiscoGet

init()
def menu() -> None:
    '''Menu'''

    entry_dictionary = entry.entry()
    addr = entry_dictionary['addr']
    username = entry_dictionary['user']
    passwd = entry_dictionary['passwd']
    secret = entry_dictionary['secret']

    try:
        while True:
            display_menu()
            option = show_menu()
            if option == '1':
                for i in addr:
                    CiscoGet.CiscoGet(i,
                             username,
                             passwd,
                             secret
                             ).get_run()
            elif option == '2':
                for i in addr:
                    CiscoGet.CiscoGet(i,
                             username,
                             passwd,
                             secret
                             ).get_cdp()
            elif option == '3':
                for i in addr:
                    CiscoGet.CiscoGet(i,
                             username,
                             passwd,
                             secret
                             ).get_int()
            elif option == '4':
                for i in addr:
                    CiscoGet.CiscoGet(i,
                             username,
                             passwd,
                             secret
                             ).get_spt()
            elif option == '5':
                for i in addr:
                    CiscoGet.CiscoGet(i,
                             username,
                             passwd,
                             secret
                             ).get_ver()
            elif option == '6':
                for i in addr:
                    CiscoGet.CiscoGet(i,
                             username,
                             passwd,
                             secret
                             ).roundup()
            elif option == '7':
                for i in addr:
                    CiscoGet.CiscoGet(i,
                             username,
                             passwd,
                             secret
                             ).write_mem()
            elif option == '8':
                return menu()
            elif option == '99':
                g_auth(addr,username,passwd,secret)
            elif option == '0':
                print('\nYou are exiting the program.')
                print(Style.BRIGHT,Fore.CYAN,
                      '[1]',Style.RESET_ALL,
                      'Save and Exit'
                      )
                print(Style.BRIGHT,Fore.CYAN,
                      '[2]',Style.RESET_ALL,
                      'Exit. '
                      )
                opt = input("Enter: ")
                if opt == '1':
                    for i in addr:
                        cisco_get = CiscoGet.CiscoGet(i,
                                             username,
                                             passwd,
                                             secret)
                        cisco_get.write_mem()
                    cisco_get.net_connect.disconnect()
                    sys.exit(9)
                elif opt == '2':
                    print('GoodBye!')
                    for i in addr:
                        cisco_get = CiscoGet.CiscoGet(i,
                                             username,
                                             passwd,
                                             secret)
                        cisco_get.net_connect.disconnect()
                        sys.exit(9)
    except ValueError:
        print('\nYou hit a invalid key\nPlease Try Again\n\n')
        return menu()
    except KeyboardInterrupt:
        try:
            print(Style.BRIGHT,Fore.RED,
                  "[-] CTL C was detected.",
                  Style.RESET_ALL
                  )
            print(Style.BRIGHT,Fore.RED,
                  "To Exit press Y",
                  Style.RESET_ALL
                  )
            print(Style.BRIGHT,Fore.RED,
                  "To Continue press N ",
                  Style.RESET_ALL
                  )
            opt = input('Y or N: ')
            if opt.capitalize() == 'N':
                return menu()
            elif opt.capitalize() == 'Y':
                sys.exit(9)
        except KeyboardInterrupt:
            pass
    finally:
        pass


def main():
    '''Runs Menu'''
    OnClick().onclick()
    menu()

if __name__ == '__main__':
    main()
