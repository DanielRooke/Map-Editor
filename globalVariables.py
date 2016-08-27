import pygame
from easygui import fileopenbox,filesavebox,boolbox
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


def maptotextlist(platform,map_length):
    """M2Tl(list,int) --> list 
    maptotextlist turn the unorganized list of groups into list of collums of characters"""
    
    text_list = []
    left_ori = []
    right_ori = []
    counter = 0 
    
    for x in range(map_length):
        for y in range(9):
            for sprite in platform[9*x+y].sprites():
                if counter % 2 == 0:
                    left_ori.append(sprite.char)
                elif counter %2 != 0:
                    right_ori.append(sprite.char)
                
                elif counter == 35:
                    counter == 0
                    
                counter += 1 
        text_list.append(left_ori)
        text_list.append(right_ori)
        
        left_ori = []
        right_ori = []
                   
    return text_list



def write_file(filePath, save):
    '''write_file(path, MapSave) -> None
    write the string version of MapSave to a txt at path'''
    #check if file pre exists (write or overwrite)
    file = open(filePath, 'w')
    #writei the string version of save to the file
    file.write(str(save))
    #close txt
    file.close()

