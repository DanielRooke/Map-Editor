import pygame
from easygui import *
import os
from objects import *
from pygame.locals import *
from globalVariables import *
pygame.init()
pygame.joystick.init()


'''
ACII VALUES
Block types:
spawn : Z
goal : X
wall : W
speed : S
bounce : B
moving : M
extend from top : U
extend from left : L
background : [space]
'''



#buttons
newButton = Button("new.png", (2, 2))
openButton = Button("open.png", (132, 2))
homeGroup = pygame.sprite.Group(newButton, openButton)

def create_new_file():
    pass

def save_file_as():
    pass

#Main Program Loop (Set exit to true to quit program)
if __name__ == '__main__':
    while not exit:
        
        while state == 'home':
            
            for event in pygame.event.get():
                if event.type == QUIT:
                    state = 'quit'
                    exit = True
                #mouse input
                elif event.type == MOUSEBUTTONDOWN:
                    #left click
                    if event.button == 1:
                        #check mouse collision with buttons in homeGroup
                        if newButton.rect.collidepoint(event.pos):
                            screen.fill(white)
                            state = 'editor'
                        #click collision with open file button
                        elif openButton.rect.collidepoint(event.pos):
                            #search file directory for a saved txt
                            filePath = fileopenbox(filetypes='\*.txt')
                            if filePath != '.':
                                state = 'editor'

            screen.fill(white)
            homeGroup.update()
            homeGroup.draw(screen)
            window.blit(screen, (0, 0))
            pygame.display.flip()
        
        while state == 'editor':
            for event in pygame.event.get():
                if event.type == QUIT:
                    state = 'quit'
                    exit = True
            window.blit(screen, (0, 0))
            pygame.display.flip()
    
    
    
    
        window.blit(screen, (0,0))
        pygame.display.flip()