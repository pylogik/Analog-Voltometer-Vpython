#!/bin/python3
#Author: PyLogik, Title: All New 

import serial
from vpython import *
import time
import numpy as np

scene.background = color.green

# Refresh rate.
vPythonRate = 500

# Voltage meter chassis.
frame = box(color=color.black,length=2.2, width=.35, height=1.65, 
        pos = vector(0,.6,-.25)) 
bx = box(color=color.blue, length=1, width=.2, height=1.3, 
         pos=vector(0,.55,-.1))
bx2 = box(color=color.blue, length=2, width=.2, height=1, 
         pos=vector(0,.8,-.1))
glass = box(color=color.blue, opacity=.1, length=2.2, width=.35, height=1.65, 
         pos=vector(0,.6,0))
arm_cylinder = cylinder(axis=vector(0,0,1), size=vector(.1,.05,.05), 
        color=color.black, shininess=0)

txt = 0
arrlen = 1
arrwid = .015
arr = arrow(length=arrlen, shaftwidth=arrwid, color=color.red,
            axis=vector(1,1,0), pos=vector(0,0,.09))

digital_reading = label(text='0 Volts', color=color.black, box=False, pos=vector(0,-.35,0))

# Major clock marker points.
for theta in np.linspace(2.618, 0.524, 6):
    tick = box(color=color.yellow, pos=vector(arrlen*np.cos(theta),
                    arrlen*np.sin(theta), 0), size=vector(.1,.05,.1), 
                    axis = vector(arrlen*np.cos(theta), 
                    arrlen * np.sin(theta), 0))

# Minor clock marker points.
for theta in np.linspace(2.618, 0.524, 31):
    small_tick = box(color=color.yellow, pos=vector(arrlen*np.cos(theta),
                    arrlen*np.sin(theta), 0), size=vector(.1,.01,.1), 
                    axis = vector(arrlen*np.cos(theta), 
                    arrlen * np.sin(theta), 0))

# Numbers on the voltometers face.
for theta in np.linspace(2.618, 0.524, 6):
    number = text(text=str(txt), align='center', height=.1, depth = .05, pos=vector(1.1*np.cos(theta),
        1.1*np.sin(theta), 0), color=color.yellow) 
    txt = txt+1

# Read arduino serial data.
arduino_data = serial.Serial('/dev/ttyUSB0', 9600)
time.sleep(1)

while True:
    while arduino_data.in_waiting == 0:
        pass  

    ard = arduino_data.readline()
    ard = str(ard.decode('utf-8'))
    pval = int(ard)
    zap = (5./1023.)  * pval
    theta=-2 * np.pi/3069 * pval+5 * np.pi/6
    arr.axis=vector(arrlen*np.cos(theta), arrlen*np.sin(theta),0)
    
    
    # Apply voltage value to the label.
    if zap:
       zap = .0001
    zap = .00489 * pval 
    zap = round(zap, 2)
    digital_reading.text = f'{zap} Volts' 
