import pygame
from pygame.locals import *
from easygui import fileopenbox, filesavebox
from objects import *
from globalVariables import *
import reader
import writer
#import Worldcreator #do Worldcreator.main() to run editor window

pygame.init()

'''
ASCII VALUES

BlankTile : [Space]
NormalTile : W
FallingTile : F
MovingTile : M
OneWayTile : V,<,>,^
LavaTile : L
'''

#buttons
newButton = Button("new.png", (0, 0))
openButton = Button("open.png", (1, 0))
saveButton = Button("save.png", (2, 0))
homeGroup = pygame.sprite.Group(newButton, openButton)
editorGroup = pygame.sprite.Group(newButton, openButton, saveButton)


def end_task():
    '''set quit values to exit program'''
    global exit
    global state
    exit, state = True, 'quit'

#Main Program Loop (Set exit to true to quit program)
if __name__ == '__main__':
    while not exit:
        
        while state == 'home':
            
            for event in pygame.event.get():
                
                if event.type == QUIT:  #Big Red X
                    #break out of main program loops
                    end_task()
                
                
                elif event.type == MOUSEBUTTONDOWN:#check mouse click events
                    
                    if event.button == 1:  #left clicks
                        
                        if newButton.rect.collidepoint(event.pos):  #check mouse collision with buttons in homeGroup
                            
                            screen.fill(white)
                            save = MapSave()
                            state = 'editor'
                            
                        
                        elif openButton.rect.collidepoint(event.pos):#click collision with open file button
                            
                            #search file directory for a saved txt
                            filePath = fileopenbox(filetypes=['\*.txt'])
                            if filePath != '.':
                                save = reader.open_file(filePath)
                                state = 'editor'
                
                
                elif event.type == pygame.VIDEORESIZE:  #Window resizing event
                    window = pygame.display.set_mode(event.size, pygame.RESIZABLE)
                    screen = pygame.Surface(event.size).convert()
            
            
            #visual updates to the screen
            screen.fill(white)
            homeGroup.update()
            homeGroup.draw(screen)
            window.blit(screen, (0, 0))
            pygame.display.flip()
        
        
        
        
        
        
        
        '''EDITOR'''
        while state == 'editor':
            for event in pygame.event.get():
                
                if event.type == QUIT:
                    end_task()
                
                elif event.type == MOUSEBUTTONDOWN:  #Mouse click
                    
                    if event.button == 1:#left click
                        
                        #check mouse collision with buttons in homeGroup
                        
                        #NEW FILE BUTTON
                        if newButton.rect.collidepoint(event.pos):
                            #clear current file if open and create new map object
                            if not save.is_saved:
                                filePath = filesavebox(filetypes=['\*.txt'])
                                if filePath != None:
                                    writer.write_file(filePath, save)
                            if save.is_saved:
                                save = MapSave()
                        
                        
                        #OPEN FILE BUTTON
                        elif openButton.rect.collidepoint(event.pos):
                            if not save.is_saved:
                                filePath = filesavebox(filetypes=['\*.txt'])
                                if filePath != '.':
                                    writer.write_file(filePath)
                            if save.is_saved:
                                #search file directory for a saved txt
                                filePath = fileopenbox(filetypes=['\*.txt'])
                                save = reader.read_file(filePath)
                                
                        
                        #SAVE AS FILE BUTTON
                        elif saveButton.rect.collidepoint(event.pos):
                            filePath = filesavebox(filetypes=['\*.txt'])
                            writer.write_file(filePath, save)

                elif event.type == pygame.VIDEORESIZE:
                    # V THIS FUCKING LINE SAVED MY LIFE V
                    window = pygame.display.set_mode(event.size, pygame.RESIZABLE)
                    screen = pygame.Surface(event.size).convert()
            
            
            
            
            screen.fill(white)
            editorGroup.update()
            editorGroup.draw(screen)
            window.blit(screen, (0, 0))
            pygame.display.flip()

        window.blit(screen, (0,0))
        pygame.display.flip()
