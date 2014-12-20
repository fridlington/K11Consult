#!/usr/bin/python
# importSingleDial.py

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
import sys
import time
import dials as dd
import pygame
import pygame.camera
from pygame.locals import *

pygame.camera.init()

os.environ['SDL_VIDEO_WINDOW_POS'] = 'center'

size = width, height = 640, 480

cam = pygame.camera.Camera("/dev/video0",(640,480))
# start the camera
cam.start()

pygame.display.set_caption('K11Consult')

monitorX = pygame.display.Info().current_w
monitorY = pygame.display.Info().current_h



surface1FullscreenX = (monitorX / 2) - 150
surface1FullscreenY = (monitorY / 2) - 60

surface1WindowedX = (width / 2) - 150
surface1WindowedY = (height / 2) - 60

surface1X = surface1WindowedX
surface1Y = surface1WindowedY

surface2FullscreenX = (monitorX / 2) - 320
surface2FullscreenY = (monitorY / 2) - 240

surface2WindowedX = 0 #(width / 2) - 150
surface2WindowedY = 0 #(height / 2) -150

surface2X = surface2WindowedX
surface2Y = surface2WindowedY


screen = pygame.display.set_mode(size)


surface1 = pygame.Surface((300,300))
#cam = pygame.Surface((640,480))


surface1.set_colorkey(0x0000FF)


#screen.fill(0x000000)


TEMP_Value = 1
TEMP_Max_Value = 140
imageCounter = 0


while True:
    pygame.time.Clock().tick(30)
    image = cam.get_image().convert()
    for event in pygame.event.get():

        if event.type==pygame.QUIT:
            sys.exit()
            pygame.quit()

        if event.type is KEYDOWN and event.key == K_q:
            sys.exit()
            pygame.quit()

        if event.type is KEYDOWN and event.key == K_w:
            pygame.display.set_mode(size)
            #pygame.mouse.set_visible(False)

            surface1X = surface1WindowedX
            surface1Y = surface1WindowedY
            surface2X = surface2WindowedX
            surface2Y = surface2WindowedY

            #screen.fill(0x000000)

        if event.type is KEYDOWN and event.key == K_f:
            pygame.display.set_mode((monitorX,monitorY), FULLSCREEN)

            surface1X = surface1FullscreenX
            surface1Y = surface1FullscreenY
	    surface2X = surface2FullscreenX
            surface2Y = surface2FullscreenY
            #screen.fill(0x000000)
            #pygame.mouse.set_visible(False)
            

# Setting the surface fill to the surface color key fixes transparency
    surface1.fill(0x0000FF)



    dd.Dials().indicatorNeedle(surface1,TEMP_Value,148,150,280,dd.Dials.twenty,dd.Dials.BLACK,0,0,(TEMP_Max_Value / 10),6,3,1,True,True,"Temperature",dd.Dials.degree)
    
    
    if imageCounter % 1 == 0:
	screen.blit(image,(surface2X,surface2Y))
    
    
    screen.blit(surface1,(surface1X,surface1Y))
    

    #time.sleep(0.08)

        
    if TEMP_Value < TEMP_Max_Value:
        TEMP_Value = TEMP_Value + 1
    else:
        TEMP_Value = 1
    if imageCounter <= 100:
	imageCounter += 1
    else:
	imageCounter = 0
    pygame.display.update()
    #print imageCounter