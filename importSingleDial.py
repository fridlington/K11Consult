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



import os
import time
#import math
import dashDials as dd
import pygame
from pygame.locals import *



os.environ['SDL_VIDEO_WINDOW_POS'] = 'center'

size = width, height = 400, 400

monitorX = pygame.display.Info().current_w
monitorY = pygame.display.Info().current_h



surface5FullscreenX = (monitorX / 2) - 150
surface5FullscreenY = (monitorY / 2) - 150

surface5WindowedX = (width / 2) - 150
surface5WindowedY = (height / 2) -150

surface5X = surface5WindowedX
surface5Y = surface5WindowedY



screen = pygame.display.set_mode(size)


surface5 = pygame.Surface((300,300))



surface5.set_colorkey(0x0000FF)


screen.fill(0x000000)

MPH_Value = 1
RPM_Value = 10
TEMP_Value = 100
BATT_Value = 1
AAC_Value = 1
MAF_Value = 1

while True:

    for event in pygame.event.get():

        if event.type==pygame.QUIT:
            dd.sys.exit()

        if event.type is KEYDOWN and event.key == K_q:
            sys.exit()

        if event.type is KEYDOWN and event.key == K_w:
            pygame.display.set_mode((width,height))
            pygame.mouse.set_visible(False)

            surface5X = surface5WindowedX
            surface5Y = surface5WindowedY

            screen.fill(0x000000)

        if event.type is KEYDOWN and event.key == K_f:
            pygame.display.set_mode((monitorX,monitorY), FULLSCREEN)

            surface5X = surface5FullscreenX
            surface5Y = surface5FullscreenY

            screen.fill(0x000000)
            pygame.mouse.set_visible(False)


    surface5.fill(0x000000)



    dd.indicatorNeedle(surface5,TEMP_Value,148,150,150,dd.twenty,dd.BLACK,-45,45,16,6,3,1,True,False,"Temperature",dd.degree)

    screen.blit(surface5,(surface5X,surface5Y))


    time.sleep(0.02)
    
    if MPH_Value < 99:
        MPH_Value = MPH_Value + 0.5
    else:
        MPH_Value = 1
    
    if RPM_Value < 5000:
        RPM_Value = RPM_Value + 10
    else:
        RPM_Value = 10
    
    if MAF_Value < 400:
        MAF_Value = MAF_Value + 1.5
    else:
        MAF_Value = 1
        
    if AAC_Value < 100:
        AAC_Value = AAC_Value + 1
    else:
        AAC_Value = 1
        
    if BATT_Value < 18:
        BATT_Value = BATT_Value + 0.2
    else:
        BATT_Value = 1
        
    if TEMP_Value < 140:
        TEMP_Value = TEMP_Value + 1
    else:
        TEMP_Value = 1

    pygame.display.update()
