#!/usr/bin/python
# dashboard.py

#Copyright (C) 2014 Eilidh Fridlington http://eilidh.fridlington.com

#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.

#You should have received a copy of the GNU General Public License
#along with this program.  If not, see <http://www.gnu.org/licenses/

import time
import math
import serial
import threading
import datetime

PORT = serial.Serial('/home/eilidh/K11Consult/SCRIPT', 9600, timeout=None)

class ReadStream(threading.Thread):

    def __init__(self, daemon):
        threading.Thread.__init__(self)
        self.daemon = daemon
        self.start()

    def run(self):
        PORT.write('\x5A\x0B\x5A\x01\x5A\x08\x5A\x0C\x5A\x0D \
                    \x5A\x03\x5A\x05\x5A\x09\x5A\x13\x5A\x16 \
                    \x5A\x17\x5A\x1A\x5A\x1C\x5A\x21\xF0')

        global MPH_Value
        global RPM_Value
        global TEMP_Value
        global BATT_Value
        global MAF_Value
        global AAC_Value
        global INJ_Value
        global TIM_Value

        MPH_Value = 0
        RPM_Value = 0
        TEMP_Value = 0
        BATT_Value = 0
        MAF_Value = 0
        AAC_Value = 0
        INJ_Value = 0
        TIM_Value = 0


        fileName = datetime.datetime.now().strftime("%d-%m-%y-%H-%M")

        while READ_THREAD == True:

            incomingData = PORT.read(16)

            #self.logToFile(incomingData,fileName)

            if incomingData:

                dataList = map(ord,incomingData)
                Header = 255
                returnBytes = 14

                try:
                    if dataList[-4] == Header and dataList[-3] == returnBytes:


                        try:
                            MPH_Value = self.convertToMPH(int(dataList[-2]))
                            RPM_Value = self.convertToRev(int(dataList[-1]))
                            TEMP_Value = self.convertToTemp(int(dataList[0]))
                            BATT_Value = self.convertToBattery(float(dataList[1]))
                            AAC_Value = self.convertToAAC(int(dataList[8]))
                            MAF_Value = self.convertToMAF(int(dataList[5]))

                            time.sleep(0.002)


                        except (ValueError, IndexError):
                            pass

                    else:
                        pass

                except (ValueError, IndexError):
                    pass

            else:
                pass


    def convertToMPH(self,inputData):

        return int(round ((inputData * 2.11) * 0.621371192237334))

    def convertToRev(self,inputData):

        return int(round((inputData * 12.5),2))

    def convertToTemp(self,inputData):

        return inputData - 50

    def convertToBattery(self,inputData):

        return round(((inputData * 80) / 1000),1)

    def convertToMAF(self,inputData):

        return inputData * 5

    def convertToAAC(self,inputData):

        return inputData / 2

    def convertToInjection(self,inputData):

        return inputData / 100

    def convertToTiming(self,inputData):

        return 110 - inputData

    def logToFile(self,data,fileName):

        logFile = open(fileName + '.hex', 'a+')

        logFile.write(data)





READ_THREAD = False
MPH_Value = 0
RPM_Value = 0
TEMP_Value = 0
BATT_Value = 0
AAC_Value = 0
MAF_Value = 0

while READ_THREAD == False:

    try:

        PORT.flushInput()
        PORT.write('\xFF\xFF\xEF')
        time.sleep(2)
        Connected = PORT.read(1)
        if Connected == '\x10':

            READ_THREAD = True
            ReadStream(True)

    except ValueError:

            PORT.open()


while READ_THREAD == True:

    pygame.time.Clock().tick(60)

    for event in pygame.event.get():

        if event.type==pygame.QUIT:
            PORT.flushInput()
            PORT.close()
            sys.exit()

        if event.type is KEYDOWN and event.key == K_q:
            PORT.flushInput()
            PORT.close()
            sys.exit()

        if event.type is KEYDOWN and event.key == K_w:
            pygame.display.set_mode((width,height))
            pygame.mouse.set_visible(False)
            surface1X = surface1WindowedX
            surface1Y = surface1WindowedY
            surface2X = surface2WindowedX
            surface2Y = surface2WindowedY
            surface3X = surface3WindowedX
            surface3Y = surface3WindowedY
            surface4X = surface4WindowedX
            surface4Y = surface4WindowedY
            surface5X = surface5WindowedX
            surface5Y = surface5WindowedY
            surface6X = surface6WindowedX
            surface6Y = surface6WindowedY
            screen.fill(0x000000)

        if event.type is KEYDOWN and event.key == K_f:
            pygame.display.set_mode((monitorX,monitorY), FULLSCREEN)
            surface1X = surface1FullscreenX
            surface1Y = surface1FullscreenY
            surface2X = surface2FullscreenX
            surface2Y = surface2FullscreenY
            surface3X = surface3FullscreenX
            surface3Y = surface3FullscreenY
            surface4X = surface4FullscreenX
            surface4Y = surface4FullscreenY
            surface5X = surface5FullscreenX
            surface5Y = surface5FullscreenY
            surface6X = surface6FullscreenX
            surface6Y = surface6FullscreenY
            screen.fill(0x000000)
            pygame.mouse.set_visible(False)

    surface1.fill(0x000000)
    surface2.fill(0x0000FF)
    surface3.fill(0x0000FF)
    surface4.fill(0x0000FF)
    surface5.fill(0x0000FF)
    surface6.fill(0x0000FF)

    indicatorNeedle(surface1,MPH_Value,648,650,650,sixty,BLACK,0,0,10,12,6,1,False,False)
    indicatorNeedle(surface2,RPM_Value,488,500,500,sixty,BLACK,0,0,500,10,5,100,False,False)
    indicatorNeedle(surface3,MAF_Value,168,170,170,twenty,BLACK,-45,-45,50,6,3,10,True,False,"MAF",millivolt)
    indicatorNeedle(surface4,AAC_Value,168,170,170,twenty,BLACK,45,45,10,6,3,1,True,False,"AAC",percent)
    indicatorNeedle(surface5,TEMP_Value,148,150,150,twenty,BLACK,-45,45,16,6,3,1,True,False,"Temperature",degree)
    indicatorNeedle(surface6,BATT_Value,148,150,150,twenty,BLACK,-45,45,2,6,3,1,True,False,"Battery",volt)


    screen.blit(surface1,(surface1X,surface1Y))
    screen.blit(surface2,(surface2X,surface2Y))
    screen.blit(surface3,(surface3X,surface3Y))
    screen.blit(surface4,(surface4X,surface4Y))
    screen.blit(surface5,(surface5X,surface5Y))
    screen.blit(surface6,(surface6X,surface6Y))

    #time.sleep(0.02)

    pygame.display.update()
