'''Final ZIP'''
import shutil
from os import getlogin
from datetime import date

def lin_zipper():
    '''linux zip funtion'''
    user = getlogin()
    site = input('Site Name: ').strip()
    zip_directory = f'/home/{user}/Desktop/SwitchConfigs'
    ouput_zip = f'/home/{user}/Desktop/'
    shutil.make_archive("".join([ouput_zip,site,'_',str(date.today())]) ,'zip', zip_directory)
    return


def win_zipper():
    '''Windows zip funtion'''
    user = getlogin()
    site = input('Site Name: ').strip()
    zip_directory = f'C:\\Users\\{user}\\Desktop\\SwitchConfigs'
    ouput_zip = f'C:\\Users\\{user}\\Desktop\\'
    shutil.make_archive("".join([ouput_zip,site,'_',str(date.today())]) ,'zip', zip_directory)
    return
