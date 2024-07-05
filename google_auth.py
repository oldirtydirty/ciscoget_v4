'''Google Authenticator'''
import pyotp
from shell import conn

def g_auth(addr,username,passwd,secret):
    '''Function'''
    token = 'L6ENELVWYEQO7O7UVSK6CAD4JVGC2IGZ'
    email = 'ECHTechnicalTeam@motorolasolutions.com'
    pyotp.totp.TOTP(token).provisioning_uri(name=email,issuer_name='Secure App')
    totp= pyotp.totp.TOTP(token)
    r = input('Token: ')
    result = totp.verify(r)
    if result:
        conn(addr,username,passwd,secret)
    else:
        return
