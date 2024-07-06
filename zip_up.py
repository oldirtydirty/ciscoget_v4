'''Final ZIP'''
import shutil
from os import getlogin
from datetime import date


def lin_zipper():
    '''linux zip funtion'''
    site = input('Site Name: ').strip()
    directory = f'/home/{getlogin()}/Desktop/SwitchConfigs'
    shutil.make_archive(directory+site +'_' +str(date.today()),'zip',directory)
    return


def win_zipper():
    '''Windows zip funtion'''
    site = input('Site Name: ').strip()
    directory = f'C:\\Users\\{getlogin()}\\Desktop\\SwitchConfigs'
    shutil.make_archive(directory+site +'_' +str(date.today()),'zip',directory)
    return
