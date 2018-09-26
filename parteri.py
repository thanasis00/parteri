# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 16:25:46 2018

@author: kathan, angelakis, athinab, ksarlou
"""

"""Module importation"""
import serial
from time import sleep

"""Opening of the serial port"""
try:
    arduino = serial.Serial("/dev/ttyACM0",timeout=1)
except:
    print('Please check the port')

"""Initialising variables""" 
with open("data.txt",mode="w") as f:
	while True:
		f.write(str(arduino.readline()))
		sleep(1)
