
from globalVariables import *

class Button(pygame.sprite.Sprite):
    '''Text_Button(path, pos)
    image found @ path displayed @ position pos
    Sub class of pygame.sprite.Sprite'''    
    def __init__(self, path, pos, size=50, centered=False, command=None):
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
        
        
class MovingBlock(object):
    """models a moving block in game keeping the cords and change in dirrection"""
    def __init__(self):
        """creats MovingBlock with no cords and no delta"""
        self.storage = []
        self.delta = None
        
    def isEmpty(self):
        return len(self.storage) == 0
    
    def __str__(self):
        out = ""
        for cord in self.storage():
            out += "{},{}|".format(cord[0],cord[1])
        
        return out 
    
class MapSave(object):
    '''Object representing the structure of a map's save file'''
    def __init__(self, path=None):
        #coordinate counting starts from 0
        
        self.lines = ['01:','02:','03:','04:','05:','06:','07:','08:','09:',
                      '10:','11:','12:','13:','14:','15:','16:','17:','18:']

        self.path = path
        
        # format is ((x1, y1), (x2, y2)) relative to blocks | x and y values are block counts NOT pixel counts
        # where the first sub tuple is where the block appears on the map
        #and the second is where it will moveto
        
        self.is_saved = False
        
        self.movingTiles = []
        #[[],()]
    
    def __str__(self):
        '''MapSave.__str__() <==> str(MapSave) -> str
        return the string version of the MapSave object'''
        out = 'APPLICATION MAP\n'

        for line in self.lines:
            out += '{}\n'.format(line)
            
        for tile in self.movingTiles:
        
            for cord in tile.storage:
                out += "|{},{}".format(cord[0],cord[1])
            out += "|:{}\n".format(tile.delta)
        return out
    
    def add_block(self, line, key):

        self.lines[line] += key
    
    def set_saved(self):
        self.is_saved = not self.is_saved
        
        
        



        
def read_file(path):
    '''read_file(path) -> MapSave()
    read a map txt file and return a MapSave object.
    return None if ad error is encountered'''
    if path != None:
            
        
        file = open(path)
        isFile = False
        counter = 0
        save = MapSave(path)
    
        #check each line
        ListOfMoving = []
        ListOfLines =[]
        platform = []
        
    
    
        
        
        
    
        for line in file:
            if counter == 0:
                if line == "APPLICATION MAP\n":
                    isFile = True
            if line[0] in "0123456789":
                line = line[3:-1]
                ListOfLines.append(line)
            counter += 1
            
            
            
            
            if line[0] == "|":
                temp = MovingBlock()
                delta = line[line.find(":")+2:-2]
                line = line[1:line.find(":")]
                
                
                for char in line:
                    if char == "|":
                        new = line.find("|")
                        cord = line[:new].split(",")
                        cord = (int(cord[0]),int(cord[1]))
                        line = line[new+1:]
                        temp.storage.append(cord)
                
                delta = delta.split(",")
                delta = (int(delta[0]),int(delta[1]))
                temp.delta = delta
                ListOfMoving.append(temp)
                
                
            
        
    
        if not isFile:
            print('ERROR: NOT A MAP FILE')
        else:
            maplength = len(ListOfLines[0]) //2
            #take list of rows turn into platform
            #take [0] and [1] then remove
            temp = pygame.sprite.OrderedUpdates()
            #in range of map length // 2
            
            
            
            for x in range(maplength):
                for y in range(18):
                    
                    twochars = ListOfLines[y][:2]
                    ListOfLines[y] = ListOfLines[y][2:]
                    
                    for char in range(2):
                        if y%2 == 0:
                            #top half
                            if char == 0:
                                #top left
                                block = MicroBlock(((x*60+104,4+y*30)))
                                
                            else:
                                #top right
                                block = MicroBlock(((x*60+132,4+y*30)))
                        else:
                            #bottom half
                            if char == 0:
                                #bottom left
                                block = MicroBlock(((x*60+104,2+y*30)))
                                
                            else:
                                #bottom right
                                block = MicroBlock(((x*60+132,2+y*30)))                       
                        
                        if twochars[char] == "W":
                            block.fill((90,127,113))
                            block.char = "W"
                        
                        elif twochars[char] == " ":
                            block.fill(white)
                            block.char = " "
                            
                        elif twochars[char] == "L":
                            block.fill((96,33,16))
                            block.char = "L"
                            
                        elif twochars[char] == "S":
                            block.fill((136,198,44))
                            block.char = "S"
                            
                        elif twochars[char] == "F":
                            block.fill((90,83,113))
                            block.char = "F"
                            
                        elif twochars[char] == "G":
                            block.fill((151,126,44))
                            block.char = "G"
                            
                        elif twochars[char] == "M":
                            block.fill((44,44,44))
                            block.char = "M"
                        
                        
                            
                        elif twochars[char] == ">":
                            block.fill((0, 0, 140))
                            block.char = ">"
                        temp.add(block)        
                    
                    if len(temp.sprites()) == 4:
                        platform.append(temp)
                        temp = pygame.sprite.OrderedUpdates()
                        
            return (platform,maplength,ListOfMoving)
        





def new_world():
    platform = []
    
    for x in range(64):
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


