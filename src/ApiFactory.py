import os
import shift_planning
import json
import credentials as creds

def getUsers():
	s = shift_planning.ShiftPlanning(creds.HUMANITY_KEY, creds.HUMANITY_LOGIN, creds.HUMANITY_PASSWORD)
	s.do_login()
	s.get_employees()
	print s.get_public_data()

if __name__ == "__main__":
	getUsers()
