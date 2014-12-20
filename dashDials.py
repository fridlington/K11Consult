#!/usr/bin/python
# dashDials.py module

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

import pygame
import math
from pygame.locals import *
import pygame.gfxdraw
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


fifeteen = pygame.font.SysFont("Sans", 15)

twenty = pygame.font.SysFont("Sans", 18)

sixty = pygame.font.SysFont("Sans", 60)

BLACK = (0,0,0)
RED = (255,0,0)
WHITE = (255,255,255)
BLUE = (136,196,255)


percent = u'\N{PERCENT SIGN}'
millivolt = 'mV'
volt = 'V'
degree = u"\u00B0"


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
                    backgroundColour = WHITE,
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
            pygame.draw.aaline(destination, BLUE, (x,y),(xa,ya), False)

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
                    backgroundColour = RED,
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
    dialType = dialType


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
        pygame.draw.circle(destination, backgroundColour, (position[0],position[1]), length , 0)

    if dialLabel:
        showLabel = fontSize.render(dialLabel, 1, BLUE, backgroundColour)
        labelRect = showLabel.get_rect()
        labelRect.centerx = position[0]
        labelRect.centery = position[1] - (length / 5)
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
        pygame.draw.aalines(destination, BLUE, True, ((x,y), (x2,y2), (x3, y3), (x4, y4)), False)


    pygame.gfxdraw.arc(destination,position[0],position[1],
                       (length - int(length / singleLine)),(180 + value),endPosition,  BLUE)

    pygame.draw.aaline(destination, BLUE, (x,y),(xa,ya), False)

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
	
