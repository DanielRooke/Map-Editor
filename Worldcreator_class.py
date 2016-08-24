import pygame
from pygame.locals import *
pygame.init()

#file stores a number every time you save it adds one to make every save a diffrent title  
file = open("data.txt")

for line in file:
    line = line.strip("\n")
    #file_ending is var for said number
    file_ending = int(line)
    

file.close()

class Cursor(pygame.sprite.Sprite):
    '''Cursor Object Models Pygame Sprite class to use pygame.sprite.collide with mouse'''
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1],1,1)
        self.current = (0,162,0)
    def update(self):
        self.rect = pygame.Rect(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1],1,1)
        
    def col(self,col):
        self.current = col
        
    
    

class Block(pygame.sprite.Sprite):
    '''Block object models pygame Sprite to represent one scalar block of '''
    def __init__(self,pos):
        """Block(tupple) constructs Block object at the top left given position"""
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((32,32))
        self.image.fill((255,255,255))
        self.rect = self.image.get_rect()
        self.rect.topleft = (pos[0],pos[1])
        
    def fill(self,col):
        """B.fill(rgb) --> None changes colour of surface of Block object to passed rgb value"""
        self.image.fill(col)
        
    def erase(self):
        """B.fill() --> None changes colour of surface to white"""
        self.image.fill((255,255,255))
    
    def update(self,mult):
        """B.update(int) --> None moves Block objects position mult number of blocks right"""
        self.rect.move_ip(mult*80,0)
        
        
    
# construct 576 Block objects in (four 9*16 grids) or 9*64
#platform is my Group of all these Sprites
platform = pygame.sprite.Group()

for y in range(18):
    for x in range(128):
        platform.add(Block((40*x+4,40*y+4)))
        
