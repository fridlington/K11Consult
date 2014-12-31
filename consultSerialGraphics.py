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
import os
import sys
import time
import math
import serial
import threading
import datetime
import pygame

from pygame.locals import *
import pygame.gfxdraw
pygame.init()


# Uncomment for live:
#PORT = serial.Serial('/dev/ttyUSB0', 9600, timeout=None)
# Below is for local testing with a pair of virtual serial
# ports.
#
# This is initialised by:
# $ socat PTY,link=CUTECOM PTY,link=SCRIPT
#
# The address for cutecom is:
# /home/$USER/K11Consult/CUTECOM
PORT = serial.Serial('SCRIPT', 9600, timeout=None)

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

os.environ['SDL_VIDEO_WINDOW_POS'] = 'center'

size = width, height = 1320, 740

pygame.display.set_caption('K11Consult: %s' % __file__)

monitorX = pygame.display.Info().current_w
monitorY = pygame.display.Info().current_h

backgroundFullscreenX = (monitorX / 2) - 340
backgroundFullscreenY = (monitorY / 2) - 340

backgroundWindowedX = (width / 2) - 340
backgroundWindowedY = (height / 2) -340

needleFullscreenX = monitorX / 2
needleFullscreenY = monitorY / 2

needleWindowedX = width / 2
needleWindowedY = height / 2

dial1FullscreenX = monitorX / 2
dial1FullscreenY = backgroundFullscreenY + 535

dial1WindowedX = width / 2
dial1WindowedY = backgroundWindowedY + 535

backgroundX = backgroundWindowedX
backgroundY = backgroundWindowedY

needleX = needleWindowedX
needleY = needleWindowedY

dial1X = dial1WindowedX
dial1Y = dial1WindowedY



screen = pygame.display.set_mode(size)

needle = pygame.image.load("needle.png").convert_alpha()
background = pygame.image.load("dial.png").convert_alpha()

fontFifty = pygame.font.SysFont("Digital-7 Mono", 87)

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

    for event in pygame.event.get():

        if event.type==pygame.QUIT:
            PORT.write('\x30')
            PORT.flushInput()
            PORT.close()
            sys.exit()
            pygame.quit()

        if event.type is KEYDOWN and event.key == K_q:
            PORT.write('\x30')
            PORT.flushInput()
            PORT.close()
            sys.exit()
            pygame.quit()

        if event.type is KEYDOWN and event.key == K_w:
            pygame.display.set_mode(size)
            pygame.mouse.set_visible(True)
            backgroundX = backgroundWindowedX
            backgroundY = backgroundWindowedY
            needleX = needleWindowedX
            needleY = needleWindowedY
            dial1X = dial1WindowedX
            dial1Y = dial1WindowedY


        if event.type is KEYDOWN and event.key == K_f:
            pygame.display.set_mode((monitorX,monitorY), FULLSCREEN)
            pygame.mouse.set_visible(False)
            backgroundX = backgroundFullscreenX
            backgroundY = backgroundFullscreenY
            needleX = needleFullscreenX
            needleY = needleFullscreenY
            dial1X = dial1FullscreenX
            dial1Y = dial1FullscreenY


    needleNew = pygame.transform.rotozoom(needle, (120 - (RPM_Value  / 33.33)),1)
    displayValue = fontFifty.render(("%s" % RPM_Value), 1, (255,0,255))
    labelRect = displayValue.get_rect()
    labelRect.centerx = dial1X
    labelRect.centery = dial1Y

    needle_rect = needleNew.get_rect()
    needle_rect.center = (needleX,needleY)

    screen.blit(background, (backgroundX,backgroundY))
    screen.blit(needleNew, needle_rect)
    screen.blit(displayValue, (labelRect))

    time.sleep(0.02)
    pygame.display.update()