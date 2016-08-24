import pygame
from globalVariables import *

class Button(pygame.sprite.Sprite):
    '''Text_Button(path, pos)
    image found @ path displayed @ position pos
    Sub class of pygame.sprite.Sprite'''    
    def __init__(self, path, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
        self.pos = pos
    def draw(self, destination):
        destination.blit(self, self.pos)
    
    def update(self):
        pass

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