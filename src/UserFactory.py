import csv

class UserFactory:
	#initializes with fileName.csv
	def __init__(self, fileName):
		self.fileName = fileName
	
	# returns employee information from fileName.csv
	def read(self, empID):
		with open(self.fileName, "rb") as myFile:
			reader = csv.reader(myFile, delimiter=",",quotechar = "|")
			for row in reader:
				if row[0] == str(empID):
					return row
		return "Employee ID not found"
	
	# writes employee information to fileName.csv
	def write(self, empID, first, last, userName, buzzID):
		with open(self.fileName, "ab") as myFile:
			writer = csv.writer(myFile)
			writer.writerow([empID, first, last, userName, buzzID])
	
	# finds employee and replaces old buzzID for new buzzID in fileName.csv
	# returns True if successful
	def overwrite(self, empID, buzzID):
		boo = False
		rows = []
		with open(self.fileName, "r") as myFile:
			reader = csv.reader(myFile, delimiter=",",quotechar = "|")
			for row in reader:
				if row[0] == str(empID):
					boo = True
					row[4] = str(buzzID)
				rows.append(row)
		with open(self.fileName, "wb") as myFile:
			writer = csv.writer(myFile)
			writer.writerows(rows)
		return boo
			
if __name__ == "__main__":
	demo = UserFactory("stuff.csv")
	#demo.write("empID", "first", "last", "user", "buzzID")
	#print(demo.read("empID6"))
	#print(demo.overwrite("empID", "newBuzzID"))