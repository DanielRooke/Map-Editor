import pygame
from globalVariables import *


'''ANYFILE is a third party program to open other file types in google drive'''

class Button(pygame.sprite.Sprite):
    '''Text_Button(path, pos)
    image found @ path displayed @ position pos
    Sub class of pygame.sprite.Sprite'''    
    def __init__(self, path, pos, size=35, centered=False, command=None):
        pygame.sprite.Sprite.__init__(self)
        self.pos = (size*pos[0], size*pos[1])
        self.image = pygame.transform.scale(pygame.image.load(path), (size, size))
        self.rect = self.image.get_rect()
        self.rect.topleft = self.pos
        if command != None:
            self.function = {'command' : command}
    def draw(self, destination):
        destination.blit(self, self.pos)


"""
class Text_Button(pygame.sprite.Sprite):
    '''Text_Button(text, font, colour, pos)
    Text Object that displays the text centered at tuple pos
    Sub class of pygame.sprite.Sprite'''
    def __init__(self, text, font, colour, pos):
        '''Button.__init__(text, font, colour, pos) -> None
        Initialize the Button object'''
        pygame.sprite.Sprite.__init__(self)
        self.image = font.render(text, True, colour)
        self.rect = self.image.get_rect()
        self.rect.center = pos

    def draw(self, screen):
        '''Button.draw(screen) -> None
        blit the Button to screen'''
        screen.blit(self.image, self.rect.topleft)
"""


class Cursor(pygame.sprite.Sprite):
    '''Cursor Object Models Pygame Sprite class to use pygame.sprite.collide with mousepoint'''
    def __init__(self):
        """ takes no arguments construct off mouse input"""
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1],1,1)
        self.set_colour = (0,162,0) 
        
    def update(self):
        """C.update(self) --> None updates location of rect to mousepoint""" 
        self.rect = pygame.Rect(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1],1,1)
        
    def col(self,col):
        """C.col(tupple) --> changes colour of "Brush" to passed tupple"""
        self.set_colour = col


class MicroBlock(pygame.sprite.Sprite):
    """MicroBlock Models pygame.sprite.Sprite to make 1/4 pixel"""
    def __init__(self,pos):
        """constructs MB at top left corner passed by tupple"""
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((56,56))
        self.image.fill(white)
        
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
        
    def fill(self,col):
        """MB.fill(col_tupple) --> None changes colour of self.image to passed col_tupple"""
        self.image.fill(col)


class MapSave(object):
    '''Object representing the structure of a map's save file'''
    def __init__(self, path=None):
        #coordinate counting starts from 0
        self.lines = []
        self.path = path
        self.is_saved = False
        
        # format is ((x1, y1), (x2, y2)) relative to blocks | x and y values are block counts NOT pixel counts
        # where the first sub tuple is where the block appears on the map
        #and the second is where it will move to
        self.movingTiles = []
    
    def __str__(self):
        '''MapSave.__str__() <==> str(MapSave) -> str
        return the string version of the MapSave object'''
        out = 'APPLICATION MAP'
        for line in self.lines:
            out += '{}\n'.format(line)
        for tile in self.movingTiles:
            out += '{},{}\n'.format(tile[0],tile[1])
        return out
    
    def add_block(line, key):
        self.lines[line] += key
    
    def save(self):
        self.is_saved = True
    
    def modify(self):
        self.is_saved = False