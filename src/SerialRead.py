import serial
import sys

ser = 0

"""
    Establishing connection with the RFID reader
    Note that this script only works with Windows
    Future releases will accommodate for OSX and Linux
"""
def iniSetup():
    global ser
    #change COM number to whatever number is connected
    comPort = "COM6"
    try:
        ser = serial.Serial(comPort, 9600, timeout = 1)
    except serial.SerialException:
        print ("404 Error: RFID not found")
        return False
    return True

"""
    Reading the card information and returning
    the card ID to the caller
"""
def readCard():
    global ser
    if(iniSetup()):
		line = ser.readline().decode('utf-8')[:-1]
		return line

""" 
    Test function to read and print the ID.
    Just to make sure that it works
"""
if __name__ == "__main__":
    while True:
		line = readCard()
		if(line != ""):
			print(line)
		ser.close()