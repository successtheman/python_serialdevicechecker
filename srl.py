from time import time, sleep
import serial.tools.list_ports

while True:
 sleep(1)
 for i in serial.tools.list_ports.comports():
  print(i) 