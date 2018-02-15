import numpy as np
# import matplotlib.pyplot as plt
import time
import threading
import serial
import time
data = serial.Serial('/dev/ttyUSB0',9600, timeout=1)
# plt.ion()

start_t = time.time();


myData = 0

while True:
	myData = -1
	if (data.inWaiting()>0):
		myData = data.readline()
	if(myData == -1):
		continue
	print(myData)
