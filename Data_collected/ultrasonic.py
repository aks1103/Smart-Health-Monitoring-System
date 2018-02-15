import numpy as np
# import matplotlib.pyplot as plt
import time
import threading
import serial
import time
data = serial.Serial('/dev/ttyACM0',9600, timeout=1)
# plt.ion()

start_t = time.time();


myData = 0

while True:

	try:
		myData = -1
		if (data.inWaiting()>0):
			myData = data.readline()

		if(myData == -1):
			continue
		# y = int(myData.split("\n")[0])
	
		if(float(myData) < 40):
			f = float(myData)/8;
		else:
			f = ((float(myData) - 32 )/3.03403698);
		print("Flux Equivalent : " + str(f))
		y = int(myData)
		x = time.time() - start_t
		# print(y)
		if(y < 40):
			print("Very Dim")
		elif(y < 80):
			print("Dim")
		elif(y < 120):
			print("Normal")
		elif(y < 180):
			print("Normal")
		elif(y < 250):
			print("Bright")
		else:
			print("Very Bright")
	except:
		print("Some Error")
		continue
	# plt.scatter(x, f)
	# plt.pause(0.1)
			# plt.clf()
		# plt.plot(x, y)
		# plt.draw()
# plt.plot(x, y)
# use thread


# plt.show() # blocking but thread will update figure.
	
