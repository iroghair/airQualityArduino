import serial
import matplotlib.pyplot as plt
import numpy as np
import time 

arduinoData = serial.Serial('/dev/ttyUSB0',9600)

plt.ion()
fig = plt.figure()

i = 0
x = list()
y = list()
time.sleep(3) 
arduinoData.close()
arduinoData.open()

while True:
  data = arduinoData.readline()
  print(data.decode())
  x.append(i)
  y.append(data.decode())
  plt.scatter(i,float(data.decode()))
  i+=1
  plt.show()
  plt.pause(0.1)
  

# def led_on():
#   arduinoData.write(b'1')

# def led_off():
#   arduinoData.write(b'0')

