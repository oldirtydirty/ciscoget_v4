'''Audio codes tool to get License file'''
import base64
from os import getlogin,path,makedirs
import requests

class ACTool:
    ''''AC TOOL'''
    def __init__(self,addr,user,passwd) -> None:
        self.addr = addr
        self.license = ''.join(['http://',addr,'/api/v1/license'])
        self.ini = ''.join(['http://',addr,'/api/v1/files/ini'])
        self.cred = ''.join([user,':',passwd])
        self.cred_encoded = base64.b64encode(self.cred.encode()).decode()
        self.headers = {'Authorization': 'Basic ' + self.cred_encoded}
        self.ini_request = requests.get(self.ini, headers=self.headers, timeout=5)
        self.lic_request = requests.get(self.license, headers=self.headers, timeout=5)
        self.dir_location = f'/home/{getlogin()}/Desktop/AC_Backup/'
        self.file = f'{self.dir_location}{self.addr}'

    def check_dir(self) -> None:
        '''Check if Directory Exists'''
        check_folder = path.isdir(self.dir_location)
        if not check_folder:
            makedirs(self.dir_location)

    def ini_run(self):
        '''Get INI'''
        self.check_dir()
        with open("".join([self.file,'.ini']),
                  'w',encoding='utf-8') as file:
            file.write(self.ini_request.text)

    def lic_run(self):
        '''Get Lic'''
        self.check_dir()
        with open("".join([self.file,'.txt']),
                  'w',encoding='utf-8') as file:
            file.write(self.lic_request.text)
