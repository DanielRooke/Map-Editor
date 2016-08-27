from globalVariables import *

class Button(pygame.sprite.Sprite):
    '''Text_Button(path, pos)
    image found @ path displayed @ position pos
    Sub class of pygame.sprite.Sprite'''    
    def __init__(self, path, pos, size=35):
        '''Button.__init__(path, pos, size) -> None
        Initialize the button object with an image found @ path, position of pos and x/y dimentions of size'''
        pygame.sprite.Sprite.__init__(self)
        self.pos = (size*pos[0], size*pos[1])
        self.image = pygame.transform.scale(pygame.image.load(path), (size, size))
        self.rect = self.image.get_rect()
        self.rect.topleft = self.pos
        
        #used to compare buttons
        self.path = path

    def draw(self, destination):
        '''Button.draw(S) -> None
        blit Button onto pygame.Surface S'''
        destination.blit(self, self.pos)
    

class Cursor(pygame.sprite.Sprite):
    '''Cursor Object Models Pygame Sprite class to use pygame.sprite.collide with mousepoint'''
    def __init__(self):
        """Initialize the Cursor object"""
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1],1,1)
        self.set_colour = (90,127,113) 
        self.set_char = "W"
        
    def update(self):
        """C.update(self) --> None updates location of rect to mousepoint""" 
        self.rect = pygame.Rect(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1],1,1)
        
    def col(self,col):
        """C.col(tuple) --> changes colour of "Brush" to passed tuple"""
        self.set_colour = col
        
        

class MicroBlock(pygame.sprite.Sprite):
    """MicroBlock Models pygame.sprite.Sprite to make 1/4 pixel"""
    def __init__(self,pos):
        """MicroBlock.__init__(pos) -> None
        Initialize the MicroBlock object"""
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((26,26))
        self.image.fill(white)
        
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
    
        self.char = " "
        
    def fill(self,col):
        """MicroBlock.fill(col_tuple) --> None changes colour of self.image to passed col_tuple"""
        self.image.fill(col)
        
    def update(self,scale):
        '''MicroBlock.update(scale) -> None
        update MicroBlock's visual display position'''
        self.rect.move_ip((120*scale,0))
        



class MapSave(object):
    '''Object representing the structure of a map's save file'''
    def __init__(self, path=None):
        '''MapSave.__init__(self, path) -> None
        Initialize the MapSave object.
        path defaults to None'''
        #coordinate counting starts from 0
        
        self.lines = ['01:','02:','03:','04:','05:','06:','07:','08:','09:',
                      '10:','11:','12:','13:','14:','15:','16:','17:','18:']

        self.path = path
        
        # format is ((x1, y1), (x2, y2)) relative to blocks | x and y values are block counts NOT pixel counts
        # where the first sub tuple is where the block appears on the map
        #and the second is where it will move to
        
        self.movingTiles = []
        #[[],()]
    
    def __str__(self):
        '''MapSave.__str__() <==> str(MapSave) -> str
        return the string version of the MapSave object'''
        out = 'APPLICATION MAP\n'

        for line in self.lines:
            out += '{}\n'.format(line)
        for tile in self.movingTiles:
            out += '{}:{}\n'.format(str(tile[0]).strip(['[',']']),tile[1])
        return out
    
    def add_block(self, line, key):
        '''MapSave.add_block(line, key) -> None
        add block value key to line'''
        self.lines[line] += key
    
    def add_moving_block(self, data):
        '''MapSave.add_moving_block(p, d) -> None
        add a moving block with starting position p that moves by a relative position of d'''
        self.movingTiles.append(data)
    
    def set_saved(self, state):
        '''MapSave.set_saved(state) -> None
        set MapSave.is_saved to the value of state'''
        self.is_saved = state
