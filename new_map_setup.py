from objects import *


"""THIS is building empty world which needs to be over written when reading files"""


#size = (1920,1080)



platform = []

for y in range(9):
    for x in range(64):
        
        temp = pygame.sprite.Group([
            MicroBlock(((4+x*60+100,4+y*60))),
            MicroBlock(((x*60+132,4+y*60))),
            MicroBlock(((x*60+104,32+y*60))),
            MicroBlock(((x*60+132,32+y*60)))
        ])
        
        platform.append(temp)

map_length = 64
    