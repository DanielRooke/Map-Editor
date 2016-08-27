
from globalVariables import *

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
        
        #used to compare buttons
        self.path = path
        
        
        if command != None:
            self.function = {'command' : command}
    def draw(self, destination):
        destination.blit(self, self.pos)
    
    def update(self):
        pass
    
class Cursor(pygame.sprite.Sprite):
    '''Cursor Object Models Pygame Sprite class to use pygame.sprite.collide with mousepoint'''
    def __init__(self):
        """ takes no arguments construct off mouse input"""
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1],1,1)
        self.set_colour = (90,127,113) 
        self.set_char = "W"
        
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
        self.image = pygame.Surface((26,26))
        self.image.fill(white)
        
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
    
        self.char = " "
        
    def fill(self,col):
        """MB.fill(col_tupple) --> None changes colour of self.image to passed col_tupple"""
        self.image.fill(col)
        
    def update(self,scale):
        self.rect.move_ip((120*scale,0))
        






class MapSave(object):
    '''Object representing the structure of a map's save file'''
    def __init__(self, path=None):
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
            out += '{},{}\n'.format(tile[0],tile[1])
        return out
    
    def add_block(self, line, key):

        self.lines[line] += key
    
    def set_saved(self, state):
        self.is_saved = state
        
        
        



        
def read_file(path):
    '''read_file(path) -> MapSave()
    read a map txt file and return a MapSave object.
    return None if ad error is encountered'''
    file = open(path)
    save = MapSave(path)
    #check each line
    if file[0] == 'APPLICATION MAP\n':
        for line in file:
            #lines representing map blocks
            if line[0] in '0123456789':
                line.strip('\n')
                for char in line:
                    save.add_block(char)
            #find lines displaying start and end postions for moving blocks
            elif line.startswith('('):
                #(x1, y1),(x2, y2)
                pass
        return save
    else:
        #false first line case
        print('ERROR: NOT A MAP FILE')
        return None
        





def new_world():
    platform = []
    
    for x in range(64):
        """builds in collums! ignore gobbly goop 
        12
        34
        56
        78    
        
        need to make interpreter to turn platform into list of lists of chars that will be used for writing
        """
        for y in range(9):
            
            temp = pygame.sprite.OrderedUpdates([
                MicroBlock(((x*60+104,4+y*60))), 
                MicroBlock(((x*60+132,4+y*60))), 
                MicroBlock(((x*60+104,32+y*60))),
                MicroBlock(((x*60+132,32+y*60)))
            ])
            
            platform.append(temp)
            length = x + 1
    
    return platform, length

