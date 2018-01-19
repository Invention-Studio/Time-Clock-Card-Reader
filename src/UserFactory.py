import csv

class UserFactory:
	#userID, username, first, last, buzzID
	def __init__(self, fileName):
		self.fileName = fileName
	
	# returns employee information
	def read(self, empID):
		with open(self.fileName, "rb") as myFile:
			reader = csv.reader(myFile, delimiter=",",quotechar = "|")
			for row in reader:
				if row[0] == str(empID):
					return row
		return "Employee ID not found"
	
	# writes employee information to a csv
	def write(self, empID, first, last, userName, buzzID):
		with open(self.fileName, "ab") as myFile:
			writer = csv.writer(myFile)
			writer.writerow([empID, first, last, userName, buzzID])
	
	# finds employee and replaces old buzzID for new buzzID in csv
	def overwrite(self, empID, buzzID):
		with open(self.fileName, "r+")
			
if __name__ == "__main__":
	demo = UserFactory("stuff.csv")
	#demo.write("empID", "first", "last", "user", "buzzID")
	#print(demo.read("empID6"))
	