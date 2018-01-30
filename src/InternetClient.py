import os
import sys
import httplib2
import socket
import ssl
import shift_planning
import credentials as creds
from UserFactory import UserFactory

def isConnected():
    try:
        host = socket.gethostbyname("inventionstudio.humanity.com")
        s = socket.create_connection((host, 80), 2)
        return True
    except:
        e = sys.exc_info()[0]
        print str(e)
    return False

def getUsers():
    s = shift_planning.ShiftPlanning(creds.HUMANITY_KEY, creds.HUMANITY_LOGIN, creds.HUMANITY_PASSWORD)
    s.do_login()
    s.get_employees()
    uf = UserFactory('users.csv')
    for e in s.get_public_data():
        firstname = e["firstname"]
        lastname = e["lastname"]
        if firstname is None:
            firstname = ""
        if lastname is None:
            lastname = ""
        else:
            lastname = lastname + ", "
        uf.write(e['id'], e['firstname'], e['lastname'], e['username'], 0)

def getUserDetails(userid):
    s = shift_planning.ShiftPlanning(creds.HUMANITY_KEY, creds.HUMANITY_LOGIN, creds.HUMANITY_PASSWORD)
    s.do_login()
    s.get_employee_details(str(userid))
    return s.get_public_data()

def getUserStatus(userid, details):
    s = shift_planning.ShiftPlanning(creds.HUMANITY_KEY, creds.HUMANITY_LOGIN, creds.HUMANITY_PASSWORD)
    s.do_login()
    s.get_timeclock_status(str(userid), details)
    return s.get_public_data()

def clockInUser(userid):
    s = shift_planning.ShiftPlanning(creds.HUMANITY_KEY, creds.HUMANITY_LOGIN, creds.HUMANITY_PASSWORD)
    s.do_login()
    s.timeclock_clockin(str(userid))
    print s.get_public_data()
    
def clockOutUser(userid):
    s = shift_planning.ShiftPlanning(creds.HUMANITY_KEY, creds.HUMANITY_LOGIN, creds.HUMANITY_PASSWORD)
    s.do_login()
    s.timeclock_clockout(str(userid))
    print s.get_public_data()


if __name__ == "__main__":
    print "Connection Status: " + str(isConnected())
