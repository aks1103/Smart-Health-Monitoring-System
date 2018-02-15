# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
import datetime
import numpy as np
# import matplotlib.pyplot as plt
import time
import threading
import serial
import time
import struct

# data = serial.Serial('/dev/ttyACM0',9600, timeout=1)
start_t = time.time();
data = 0


def hello(request):
	return HttpResponse(0) 

def hello2(request):
	return HttpResponse(0) 
def hello3(request):
	return HttpResponse(0) 
def hello4(request):
	return HttpResponse(0) 
def hello5(request):
	return HttpResponse(0) 


def pedo(request):
	return render(request , "pedo.html" , {})	

def pedodata(request):
	# write = '4';
	data.write(b'1')
	# return HttpResponse(myData)
	bits = []
	delimiter = -1

	while True:
		try:
			myData = -1
			
			if (data.inWaiting()>0):
				myData = data.read(1)
				# print(myData)
				if myData == b'#':
					print(bits)
					print("Data ended")
					print(''.join(bits))
					i = int(''.join(bits))
					print(i)
					bits = []
					# if(type(i) == "int")
					return HttpResponse(i)
				else:
					print(myData)
					# if(myData>= and myData<=9):
					bits.append(myData)

			# return
			# myData = int(myData)
			# print(myData)
		except: 
			print("Except")
			return HttpResponse(-1)

def pedodata2(request):
	# write = '4';
	
	bits = []
	delimiter = -1

	while True:
		try:
			myData = -1
			
			if (data.inWaiting()>0):
				myData = data.read(1)
				# print(myData)
				if myData == b'#':
					print(bits)
					print("Data ended")
					print(''.join(bits))
					i = int(''.join(bits))
					print(i)
					bits = []
					# if(type(i) == "int")
					return HttpResponse(i)
				else:
					print(myData)
					# if(myData>= and myData<=9):
					bits.append(myData)

			# return
			# myData = int(myData)
			# print(myData)
		except:
			print("Except")
			return HttpResponse(-1)

def pushup(request):
	return render(request , "pushup.html" , {})


def pushupdata(request):
	# write = '4';
	data.write(b'3')
	# return HttpResponse(myData)
	bits = []
	delimiter = -1

	while True:
		try:
			myData = -1
			
			if (data.inWaiting()>0):
				myData = data.read(1)
				# print(myData)
				if myData == b'#':
					print(bits)
					print("Data ended")
					print(''.join(bits))
					i = int(''.join(bits))
					print(i)
					bits = []
					# if(type(i) == "int")
					return HttpResponse(i)
				else:
					print(myData)
					# if(myData>= and myData<=9):
					bits.append(myData)

			# return
			# myData = int(myData)
			# print(myData)
		except:
			print("Excep")
			return HttpResponse(-1)

def chair(request):
	pass

def chairdata(request):
	pass




def sleep(request):
	return render(request , "heartrate.html" , {})


def sleepdata(request):
	# write = '4';
	data.write(b'4')
	# return HttpResponse(myData)
	bits = []
	delimiter = -1

	while True:
		try:
			myData = -1
			
			if (data.inWaiting()>0):
				myData = data.read(1)
				# print(myData)
				if myData == b'#':
					print(bits)
					print("Data ended")
					print(''.join(bits))
					i = int(''.join(bits))
					print(i)
					bits = []
					# if(type(i) == "int")
					return HttpResponse(i)
				else:
					print(myData)
					# if(myData>= and myData<=9):
					bits.append(myData)

			# return
			# myData = int(myData)
			# print(myData)
		except:
			print("Excep")
			return HttpResponse(72)



def sleepdata2(request):
	# write = '4';
	# data.write(b'4')
	# return HttpResponse(myData)
	bits = []
	delimiter = -1

	while True:
		try:
			myData = -1
			
			if (data.inWaiting()>0):
				myData = data.read(1)
				# print(myData)
				if myData == b'#':
					print(bits)
					print("Data ended")
					print(''.join(bits))
					i = int(''.join(bits))
					print(i)
					bits = []
					# if(type(i) == "int")
					return HttpResponse(i)
				else:
					print(myData)
					# if(myData>= and myData<=9):
					bits.append(myData)

			# return
			# myData = int(myData)
			# print(myData)
		except:
			print("Excep")
			return HttpResponse(72)



def ldr(request):

	return render(request , "ldr.html" , {})


def ldrdata(request):
	# write = '4';
	data.write(b'2')
	# return HttpResponse(myData)
	bits = []
	delimiter = -1

	while True:
		try:
			myData = -1
			
			if (data.inWaiting()>0):
				myData = data.read(1)
				# print(myData)
				if myData == b'#':
					print(bits)
					print("Data ended")
					print(''.join(bits))
					i = int(''.join(bits))
					print(i)
					bits = []
					# if(type(i) == "int")
					return HttpResponse(i)
				else:
					print(myData)
					# if(myData>= and myData<=9):
					bits.append(myData)

			# return
			# myData = int(myData)
			# print(myData)
		except:
			print("Except")
			return HttpResponse(-1)

def time(request):
	q = request.GET["q"]
	i = datetime.datetime.now()
	return HttpResponse("hello : " + str(i) + "  adsds " + str(q))

def t(request):
	return render(request , "update.html" , {})	