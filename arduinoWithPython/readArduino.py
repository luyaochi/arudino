import serial
ser = serial.Serial('/dev/ttyACM0',9600)
while 1:
	string = ser.readlin()
	print(string)
