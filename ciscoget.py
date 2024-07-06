"""Cisco tool to get all the output needed to submit switch configs"""
from os import makedirs,getlogin,path
from netmiko import ConnectHandler, NetmikoAuthenticationException, NetmikoTimeoutException
from colorama import Fore,Style

__author__ = 'Michael Urbani'
__version__ = '4.0'

class CiscoGet:
    '''Cisco Get class'''
    def __init__(self,addr,username,passwd,secret) -> None:
        try:
            self.current_user =  getlogin()
            self.cisco = {'device_type': 'cisco_ios',
                            'ip': addr,
                            'username': username, 
                            'password': passwd, 
                            'secret': secret
                            }
            self.net_connect = ConnectHandler(**self.cisco)
            self.net_connect.enable()
            self.hostname = self.net_connect.send_command('sh run | i host').split()[1]
            self.dir_location = "".join([f'/home/{self.current_user}/',
                                         'Desktop/SwitchConfigs/', #linux
                                           self.hostname,
                                           '/'])
            # self.dir_location = "".join([f'C:\\Users\\{self.current_user}\\',
            #                              'Desktop\\',
            #                              'SwitchConfigs\\',
            #                              self.hostname,'\\'])

        except NetmikoAuthenticationException:
            print(Style.BRIGHT,Fore.RED,
                  '\n [-] Bad Username/Password.',
                  Style.RESET_ALL
                  )
            print(Style.BRIGHT,Fore.RED,
                  f'[-] IP Address = {addr}',
                  Style.RESET_ALL
                  )
            print(Style.BRIGHT,Fore.RED,
                  f'[-] Username = {username}',
                  Style.RESET_ALL
                  )
            print(Style.BRIGHT,Fore.RED,
                  f'[-] Password = {secret}',
                  Style.RESET_ALL
                  )
            print(Style.BRIGHT,Fore.RED,
                  '[-] Try it again',
                  Style.RESET_ALL
                  )
            return
        except NetmikoTimeoutException:
            print(Style.BRIGHT,Fore.RED,
                  '\n[-] Network Timeout!',
                  Style.RESET_ALL
                  )
            print(Style.BRIGHT,Fore.RED
                  ,f'[-] Cannot reach {addr}',
                  Style.RESET_ALL
                  )
            print(Style.BRIGHT,Fore.RED,
                  '[-] Verify IP Address.',
                  Style.RESET_ALL
                  )
            return
    def check_dir(self) -> None:
        '''Check if Directory Exists'''
        check_folder = path.isdir(self.dir_location)
        if not check_folder:
            makedirs(self.dir_location)
            print(Style.BRIGHT,Fore.CYAN,
                  "[+] Created Directory: ",
                  self.dir_location,Style.RESET_ALL
                  )

    def get_run(self) -> None:
        '''Get Running Config'''
        self.check_dir()
        print(Style.BRIGHT,Fore.GREEN,
              "Writing Running-Config",
              Style.RESET_ALL
              )
        filename = "".join([self.hostname,'.config'])
        output = self.net_connect.send_command('show run')
        with open(path.join("".join([self.dir_location,
                                    filename])),
                                    'w',
                                    encoding="utf-8"
                                    ) as file:
            file.write(output)
            print(Style.BRIGHT,Fore.CYAN,
                  '[+} Write Complete',
                  Style.RESET_ALL
                  )

    def get_cdp(self) -> None:
        '''Get CDP Neighbors'''
        self.check_dir()
        print(Style.BRIGHT,Fore.GREEN,
              "Writing CDP Neighbor",
              Style.RESET_ALL
              )
        filename = "".join([self.hostname,'_CDP.txt'])
        output = self.net_connect.send_command('show cdp neighbors')
        with open(path.join("".join([self.dir_location,
                                    filename])),
                                    'w',
                                    encoding="utf-8"
                                    ) as file:
            file.write(f'{__version__}\n' + output)
            print(Style.BRIGHT,Fore.CYAN,
                  '[+} Write Complete',
                  Style.RESET_ALL
                  )

    def get_int(self) -> None:
        '''Get Show Interface Status'''
        self.check_dir()
        print(Style.BRIGHT,Fore.GREEN,
              "Writing Interface Status",
              Style.RESET_ALL
              )
        filename = "".join([self.hostname,'_INT.txt'])
        output = self.net_connect.send_command('show interface status')
        with open(path.join("".join([self.dir_location,
                                    filename])),
                                    'w',
                                    encoding="utf-8"
                                    ) as file:
            file.write(output)
            print(Style.BRIGHT,Fore.CYAN,
                  '[+} Write Complete',
                  Style.RESET_ALL
                  )

    def get_spt(self) -> None:
        '''Get Spanning-Tree'''
        self.check_dir()
        print(Style.BRIGHT,Fore.GREEN,
              "Writing Spanning-Tree",
              Style.RESET_ALL
              )
        filename = "".join([self.hostname,'_STP.txt'])
        output = self.net_connect.send_command('show spanning-tree')
        if 'Peer(STP)' in output:
            print(Style.BRIGHT,Fore.RED,
                  "[-] Spanning-Tree Has been detected on a switch port.",
                  Style.RESET_ALL
                  )
            print(Style.BRIGHT,Fore.RED,
                  "[-] Please check Spanning-Tree and CDP.",
                  Style.RESET_ALL
                  )
        with open(path.join("".join([self.dir_location,
                                    filename])),
                                    'w',
                                    encoding="utf-8"
                                    ) as file:
            file.write(output)
            print(Style.BRIGHT,Fore.CYAN,
                  '[+} Write Complete',
                  Style.RESET_ALL
                  )

    def get_ver(self) -> None:
        '''Get Version'''
        self.check_dir()
        print(Style.BRIGHT,Fore.GREEN,
              "Writing Show Version",
              Style.RESET_ALL
              )
        filename = "".join([self.hostname,'_VER.txt'])
        output = self.net_connect.send_command('show version')
        with open(path.join("".join([self.dir_location,
                                    filename])),
                                    'w',
                                    encoding="utf-8"
                                    ) as file:
            file.write(output)
            print(Style.BRIGHT,Fore.CYAN,
                  '[+} Write Complete',
                  Style.RESET_ALL
                  )

    def write_mem(self) -> None:
        '''Write to Memory'''
        print(Style.BRIGHT,Fore.GREEN,
              'Writing to Memory to',
              self.hostname,
              Style.RESET_ALL
              )
        output = self.net_connect.send_command('write mem')
        if "[OK]" in output:
            print(Style.BRIGHT,Fore.CYAN,
                  '[+} Write Complete',
                  Style.RESET_ALL
                  )
        else:
            print('[-] Error Executing Write to Memory')

    def roundup(self) -> None:
        '''Run all methods'''
        self.write_mem()
        self.get_run()
        self.get_cdp()
        self. get_int()
        self.get_spt()
        self.get_ver()
        print('')
