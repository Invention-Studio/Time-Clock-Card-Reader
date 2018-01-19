import os
import shift_planning
import credentials as creds
from UserFactory import UserFactory

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

if __name__ == "__main__":
    getUsers()
