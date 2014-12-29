import os
import time
import pygame
from pygame.locals import *


os.environ['SDL_VIDEO_WINDOW_POS'] = 'center'

SIZE = 800, 700
pygame.init()
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption('K11Consult / RPM')

#surface1 = pygame.Surface((1250,720))


done = False
screen.fill((0, 0, 255))
needle = pygame.image.load("needle.png").convert_alpha()
background = pygame.image.load("dial2.png").convert_alpha()
backgroundRect = background.get_rect()
#needle2 = needle
counter = 120
RPM_Value = 0

fontFifty = pygame.font.SysFont("Digital-7 Mono", 86)
surface1 = pygame.Surface((300,300))

while not done:
    pygame.time.Clock().tick(30)
    for e in pygame.event.get():
        if e.type == QUIT or (e.type == KEYDOWN and e.key == K_ESCAPE):
            done = True
            break
    screen.fill((0,0,0))

    needleNew = pygame.transform.rotozoom(needle, (120 - (RPM_Value  / 33.33)),1)
    #needleNew2 = pygame.transform.rotozoom(needle, (120 - (RPM_Value  / 66.66)),1)

    needle_rect = needleNew.get_rect()
    needle_rect.center = (400,350)
    #needle2_rect = needleNew2.get_rect()
    #needle2_rect.center = (895,360)

    displayValue = fontFifty.render(("%s" % RPM_Value), 1, (255,0,255))
    labelRect = displayValue.get_rect()
    labelRect.centerx = 400
    labelRect.centery = 523


    screen.blit(background, (100,50))
    screen.blit(needleNew, needle_rect)
    screen.blit(displayValue, (labelRect))
    #screen.blit(needleNew2, needle2_rect)

    pygame.display.update()


    print RPM_Value
    if RPM_Value >= 8000:
        counter = 120
        RPM_Value = 0
    else:
        #counter -=3
        RPM_Value += 50




    #time.sleep(0.02)