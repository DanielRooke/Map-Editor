from objects import *


"""THIS is building empty world which needs to be over written when reading files"""

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
        
        temp = pygame.sprite.Group([
            MicroBlock(((4+x*60+100,4+y*60))),
            MicroBlock(((x*60+132,4+y*60))),
            MicroBlock(((x*60+104,32+y*60))),
            MicroBlock(((x*60+132,32+y*60)))
        ])
        
        platform.append(temp)
        map_length = x + 1


    