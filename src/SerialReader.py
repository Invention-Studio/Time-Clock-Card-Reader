import serial
import sys

"""
Class to read card from RFID
"""

class SerialReader:
	#Initializes serial with user-specified COM Port
	#in theory should work for all OS, tested with Windows 10
	
	def __init__(self, comPort):
		self.found = False
		try:
			self.ser = serial.Serial(comPort, 9600)
			self.found = True
		except serial.SerialException:
			print("404 Error: RFID not found")

  def __del__(self):
    self.ser.close()

	#Returns the ID associated with the card
	def readCard(self):
		if self.ser.isOpen():
			return self.ser.readline().decode('utf-8')[:-2]

	#Returns boolean if connection was found
	def isFound(self):
		return self.found

"""
Main function to demo the Serial Connection
Test if it is working
"""
if __name__ == "__main__":
	#Change "COM1" to whatever OS specified port you are testing for
	demo = SerialReader("COM1")
	if demo.isFound():
		demo.readCard()
