'''Main Function'''
from colorama import init,Style,Fore
from requests import ConnectionError as ce
from ac_display import display, ini_lic
from ac_tool import ACTool

def ac_main():
    '''Main'''
    try:
        init()
        while True:
            display()
            options = ini_lic()
            if ('1' == options or '2' == options):
                ac = input("AC IP address: ")
                audiocodes = []
                for i in ac.split(","):
                    audiocodes.append(i.strip())
                try:
                    if options == '1':
                        for i in audiocodes:
                            try:
                                ACTool(i,user='Admin',passwd='Admin').lic_run()
                                print(Fore.CYAN,
                                      Style.BRIGHT,
                                      '[+]',
                                      Style.RESET_ALL,
                                      f'Writing {i} License to File.\n'
                                      )
                            except ce:
                                print(Fore.RED,
                                      Style.BRIGHT,
                                      '[-]',
                                      Style.RESET_ALL,
                                      f'Issue Accessing: {i}'
                                      )
                        break

                    elif options == '2':
                        for i in audiocodes:
                            try:
                                ACTool(i,user='Admin',passwd='Admin').ini_run()
                                print(Fore.CYAN,
                                      Style.BRIGHT,
                                      '[+]',
                                      Style.RESET_ALL,
                                      f'Writing {i} INI to File.\n'
                                      )
                            except ce:
                                print(Fore.RED,
                                      Style.BRIGHT,
                                      '[-]',
                                      Style.RESET_ALL,
                                      f'Issue Accessing: {i}'
                                      )
                        break
                    else:
                        print('option no valid')

                except ce:
                    print(Fore.RED,
                          Style.BRIGHT,
                          '[-]',
                          Style.RESET_ALL,
                          'Check the IP address.'
                          )
                    print(Fore.RED,
                          Style.BRIGHT,
                          '[-]',
                          Style.RESET_ALL,
                          'Re-Run the commands\n'
                          )
            else:
                print(Fore.RED,
                      Style.BRIGHT,
                      '[-]',
                      Style.RESET_ALL,
                      'Invalid Option Pressed:'
                      )
                break
    except KeyboardInterrupt:
        return
