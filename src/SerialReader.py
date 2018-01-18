import serial
import sys

class SerialReader:
	def __init__(self, comPort):
		try:
			self.ser = serial.Serial(comPort, 9600)
		except serial.SerialException:
			print("404 Error: RFID not found")

	def readCard(self):
		if self.ser.isOpen():
			return self.ser.readline().decode('utf-8')[:-2]