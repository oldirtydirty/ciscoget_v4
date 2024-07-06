'''Cisco CLI'''
from netmiko import ConnectHandler

def menu(addr):
    '''Menu List'''
    print('Main menu\n' + '-'*40)
    for menuitem in enumerate(addr):
        print(str(menuitem[0]) + ': ' + menuitem[1].lstrip())
    print('-'*40)

    choice = input('Please enter your choice: ')
    print('\nYou selected menu item ' + choice.upper() + ':')
    return addr[tuple(x[0] for x in enumerate(addr)).index(int(choice))]

def conn(addr,username,passwd,secret):
    '''Shell Function'''
    ip_addr = menu(addr)
    cisco = {'device_type': 'cisco_ios',
             'ip': ip_addr,
             'username': username,
             'password': passwd,'secret': secret}
    try:

        with ConnectHandler(**cisco) as connection:
            while True:
                prompt = connection.find_prompt()
                cmd = input(prompt)
                out = connection.send_command_timing(cmd)
                print(prompt, out)
    except OSError:
        return
