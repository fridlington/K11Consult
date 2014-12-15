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
#along with this program.  If not, see <http://www.gnu.org/licenses/>







import sys
import os
import pygame
import time
import math
from pygame.locals import *
import pygame.gfxdraw

os.environ['SDL_VIDEO_WINDOW_POS'] = 'center'

pygame.init()

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


#########################################################################

size = width, height = 1320, 740

monitorX = pygame.display.Info().current_w
monitorY = pygame.display.Info().current_h

surface1FullscreenX = (monitorX / 2) - 650
surface1FullscreenY = (monitorY / 2) - 360

surface1WindowedX = (width / 2) - 650
surface1WindowedY = (height / 2) - 360

surface1X = surface1WindowedX
surface1Y = surface1WindowedY

surface2FullscreenX = (monitorX / 2) - 500
surface2FullscreenY = (monitorY / 2) - 210

surface2WindowedX = (width / 2) - 500
surface2WindowedY = (height / 2) - 210

surface2X = surface2WindowedX
surface2Y = surface2WindowedY

surface3FullscreenX = (monitorX / 2) - 650
surface3FullscreenY = (monitorY / 2) - 360

surface3WindowedX = (width / 2) - 650
surface3WindowedY = (height / 2) - 360

surface3X = surface3WindowedX
surface3Y = surface3WindowedY

surface4FullscreenX = (monitorX / 2) + 310
surface4FullscreenY = (monitorY / 2) - 360

surface4WindowedX = (width / 2) + 310
surface4WindowedY = (height / 2) - 360

surface4X = surface4WindowedX
surface4Y = surface4WindowedY

surface5FullscreenX = (monitorX / 2) - 310
surface5FullscreenY = (monitorY / 2) + 60

surface5WindowedX = (width / 2) - 310
surface5WindowedY = (height / 2) + 60

surface5X = surface5WindowedX
surface5Y = surface5WindowedY

surface6FullscreenX = (monitorX / 2) + 10
surface6FullscreenY = (monitorY / 2) + 60

surface6WindowedX = (width / 2) + 10
surface6WindowedY = (height / 2) + 60

surface6X = surface6WindowedX
surface6Y = surface6WindowedY

screen = pygame.display.set_mode(size)

surface1 = pygame.Surface((1300,720))
surface2 = pygame.Surface((1000,600))
surface3 = pygame.Surface((340,340))
surface4 = pygame.Surface((340,340))
surface5 = pygame.Surface((300,300))
surface6 = pygame.Surface((300,300))

surface2.set_colorkey(0x0000FF)
surface3.set_colorkey(0x0000FF)
surface4.set_colorkey(0x0000FF)
surface5.set_colorkey(0x0000FF)
surface6.set_colorkey(0x0000FF)

screen.fill(0x000000)

fifeteen = pygame.font.SysFont("Droid Sans", 15)

twenty = pygame.font.SysFont("Droid Sans", 18)

sixty = pygame.font.SysFont("Droid Sans", 60)

BLACK = (0,0,0)
RED = (30,0,0)
PINK = (255,105,180)
PURPLE = (128,0,128)
WHITE = (255,255,255)
BLUE = (136,196,255)

#degree = u'\N{DEGREE CELSIUS}'
percent = u'\N{PERCENT SIGN}'
millivolt = 'mV'
volt = 'V'

degree = u"\u00B0"

pygame.mouse.set_visible(False)

def indicatorLegend(
                    legendValue,
                    displayValue,
                    positionX,
                    positionY,
                    length,
                    destination,
                    fontSize,
                    doubleLength=False,
                    drawLine=True,
                    doubleLine=6,
                    singleLine=3,
                    displayDivision=1,
                    backgroundColour = RED,
                    dialType = False

    ):

        position = (positionX,positionY)

        if doubleLength:
            lineLength = doubleLine
        else:
            lineLength = singleLine

        x = position[0] - math.cos(math.radians(legendValue)) * length
        y = position[1] - math.sin(math.radians(legendValue)) * length
        xa = position[0] - math.cos(math.radians(legendValue)) * (length - int(length / lineLength))
        ya = position[1] - math.sin(math.radians(legendValue)) * (length - int(length / lineLength))
        xlabel = position[0] - math.cos(math.radians(legendValue)) * (length - int(length / singleLine))
        ylabel = position[1] - math.sin(math.radians(legendValue)) * (length - int(length / singleLine))

        if drawLine:
            pygame.draw.line(destination, BLUE, (x,y),(xa,ya), True)

        if dialType:
            label = fontSize.render(("%s%s" % ((displayValue / displayDivision),dialType)),
                                    1, BLUE, backgroundColour)
        else:
            label = fontSize.render((str(displayValue / displayDivision)),
                                    1, BLUE, backgroundColour)

        labelRect = label.get_rect()
        labelRect.centerx = int(xlabel)
        labelRect.centery = int(ylabel)# + 5
        destination.blit(label, (labelRect))


def indicatorNeedle(
                    needleDestination,
                    needleValue = 0,
                    needleLength = 358,
                    positionX = 600,
                    positionY = 360,
                    fontSize = sixty,
                    backgroundColour = BLACK,
                    startPosition = 0,
                    endPosition = 0,
                    maximumValue = 10,
                    doubleLine = 6,
                    singleLine = 3,
                    displayDivision = 1,
                    displayNeedle = True,
                    displayCircle = True,
                    dialLabel = False,
                    dialType = False
    ):

    position = (positionX,positionY)
    length = needleLength
    length2 = int(needleLength / 20)
    length3 = length2 + 5
    destination = needleDestination
    fontSize = fontSize
    singleLine = singleLine
    doubleLine = doubleLine
    backgroundColour = backgroundColour


    degreesDifference = 360 - (startPosition + (180 - endPosition))
    value = int((needleValue * (degreesDifference / (maximumValue * 10.0))) + startPosition)
    displayValue = (needleValue * (degreesDifference / (maximumValue * 10.0))) + startPosition

    x = position[0] - math.cos(math.radians(value)) * (length - int(length / singleLine))
    y = position[1] - math.sin(math.radians(value)) * (length - int(length / singleLine))
    x2 = position[0] - math.cos(math.radians(value - 90)) * length2
    y2 = position[1] - math.sin(math.radians(value - 90)) * length2
    x3 = position[0] - math.cos(math.radians(value + 180)) * length3
    y3 = position[1] - math.sin(math.radians(value + 180)) * length3
    x4 = position[0] - math.cos(math.radians(value + 90)) * length2
    y4 = position[1] - math.sin(math.radians(value + 90)) * length2

    xa = position[0] - math.cos(math.radians(value)) * length
    ya = position[1] - math.sin(math.radians(value)) * length
    xa2 = x - math.cos(math.radians(value))
    ya2 = y - math.sin(math.radians(value))
    xa3 = x - math.cos(math.radians(value + 180))
    ya3 = y - math.sin(math.radians(value + 180))
    xa4 = x - math.cos(math.radians(value + 90)) * (length2 + 4)
    ya4 = y - math.sin(math.radians(value + 90)) * (length2 + 4)

    if displayCircle:
        #pygame.gfxdraw.aacircle(destination,position[0],position[1], length, RED)
        pygame.draw.circle(destination, RED, (position[0],position[1]), length , 0)

    if dialLabel:
        showLabel = fontSize.render(dialLabel, 1, BLUE, backgroundColour)
        labelRect = showLabel.get_rect()
        labelRect.centerx = position[0]
        labelRect.centery = position[1] - 30
        destination.blit(showLabel, (labelRect))

    valueDivisions = degreesDifference / 10

    indicatorLegend(startPosition, 0, position[0], position[1], length,
                    destination, fontSize,False,True,doubleLine,singleLine,1,backgroundColour)

    for divisions in range(1,10):

        if needleValue >= (maximumValue * divisions):
            indicatorLegend((startPosition + (valueDivisions * divisions)), (maximumValue * divisions),
                            position[0], position[1], length, destination, fontSize,True,True,doubleLine
                            ,singleLine,displayDivision,backgroundColour)

    if displayNeedle:
        pygame.draw.lines(destination, BLUE, True, ((x,y), (x2,y2), (x3, y3), (x4, y4)), True)


    pygame.gfxdraw.arc(destination,position[0],position[1],
                       (length - int(length / singleLine)),(180 + value),endPosition,  BLUE)

    pygame.draw.line(destination, BLUE, (x,y),(xa,ya), True)

    pygame.gfxdraw.arc(destination,position[0],position[1],
                       length,(180 + startPosition), (value - 180), BLUE)

    pygame.gfxdraw.arc(destination,position[0],position[1],
                       (length - int(length / doubleLine)),(180 + startPosition) , (value - 180), BLUE)

    if dialType:
        indicatorLegend((180 + endPosition), needleValue, position[0], position[1],
                        length, destination, fontSize, False, False,
                        doubleLine,singleLine,1,backgroundColour,dialType)
    else:
        indicatorLegend((180 + endPosition), needleValue , position[0], position[1],
                        length, destination, fontSize, False, False,
                        doubleLine,singleLine,1,backgroundColour)


MPH_Value = 1
RPM_Value = 10
TEMP_Value = 100
BATT_Value = 1
AAC_Value = 1
MAF_Value = 1

while True:

    for event in pygame.event.get():

        if event.type==pygame.QUIT:
            sys.exit()

        if event.type is KEYDOWN and event.key == K_q:
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

    time.sleep(0.02)
    
    if MPH_Value < 99:
        MPH_Value = MPH_Value + 1
    else:
        MPH_Value = 1
    
    if RPM_Value < 5000:
        RPM_Value = RPM_Value + 12
    else:
        RPM_Value = 10
    
    if MAF_Value < 400:
        MAF_Value = MAF_Value + 1
    else:
        MAF_Value = 1
        
    if AAC_Value < 100:
        AAC_Value = AAC_Value + 1
    else:
        AAC_Value = 1
        
    if BATT_Value < 16:
        BATT_Value = BATT_Value + 0.2
    else:
        BATT_Value = 1
        
    if TEMP_Value < 140:
        TEMP_Value = TEMP_Value + 1
    else:
        TEMP_Value = 1

    pygame.display.update()
