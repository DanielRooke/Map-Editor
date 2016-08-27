import pygame
from easygui import fileopenbox,filesavebox,boolbox,multenterbox
import os
import pygame
from pygame.locals import *



black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)


exit = False
state = 'home'
size = (960,540)
window = pygame.display.set_mode(size, pygame.RESIZABLE)
#pygame.display.set_icon(pygame.image.load("PATH"))
pygame.display.set_caption("Title")

#main surface
screen = pygame.Surface((2000,2000)).convert()
screen.fill(white)