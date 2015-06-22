#!/usr/bin/python

import serial
import serialThread

PORT = serial.Serial('/home/eilidh/K11Consult/SCRIPT', 9600, timeout=None)



bla = serialThread.ReadStream(PORT)
#try:
while True:
    #PORT.flushInput()
    #PORT.write('\xFF\xFF\xEF')
    #serialThread.time.sleep(2)
    #Connected = PORT.read(1)
    #if Connected == '\x10':
        #print 'connected'
        #READ_THREAD = True
    #serialThread.ReadStream(PORT).convertToMPH
    print bla.returnMPH()
    #serialThread.time.sleep(0.002)

#except ValueError:

    #PORT.open()