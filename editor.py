from objects import *

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


#run this if creatinf a new world 
platform = new_world()
map_length = platform[1]
platform = platform[0]



#or run reader to load platform and length


clock = pygame.time.Clock()

keep_going = True	

pygame.display.set_caption("READER") #initial screen caption
window = pygame.display.set_mode(size,RESIZABLE)

#background refresh

#main surface
screen = pygame.Surface(size).convert()

#overlay surface is the grey background that sits ontop of the blocks
overlay = pygame.Surface((100,1080)).convert()
overlay.fill((165,165,165))

#buttons group holds all the buttons at their respective location
buttons = pygame.sprite.Group([Button("editor_00.bmp",(0,0),50),
                               Button("editor_01.bmp",(1,0),50),
                               Button("editor_02.bmp",(0,1),50),
                               Button("editor_03.bmp",(1,1),50),
                               Button("editor_04.bmp",(0,2),50),
                               Button("editor_05.bmp",(1,2),50),
                               Button("editor_06.bmp",(0,3),50),
                               Button("editor_07.bmp",(1,7),50),
                               Button("editor_08.bmp",(0,7),50),
                               Button("save.png",(0,9),50)
                               ])
left_click = 0
right_click = 0

erase = pygame.Surface((2000,2000)).convert()
erase.fill(black)

scroll_count = 0
user = Cursor()


while keep_going:
    
    clock.tick(30)
    
    #event loop    
    for event in pygame.event.get(): 
        if event.type == QUIT:
            keep_going = False
        
        #if release mouse then leftclick and rightclick = False        
        elif event.type == MOUSEBUTTONUP:
            if event.button == 1:
                left_click = 0
            elif event.button == 3:
                right_click = 0

        elif event.type == MOUSEBUTTONDOWN:
            
            if event.button == 1:
            
                #if leftclick
                
                for button in pygame.sprite.spritecollide(user,buttons,0):
                    #if leftclick collides with any buttons it checks the tags to set appropriate colour
                    if button.path == "editor_00.bmp":
                        #white "Erase"
                        user.col((255,255,255))
                        user.set_char = " "
                   
                    elif button.path == "editor_01.bmp":
                        #Baricade or seafoam green
                        user.col((90,127,113))
                        user.set_char = "W"

                    elif button.path == "editor_02.bmp":
                        #lava 
                        user.col((96,33,16))  
                        user.set_char = "L"
                        
                    elif button.path == "editor_03.bmp":
                        #falling
                        user.col((90,83,113))  
                        user.set_char = "F"
                        
                    elif button.path == "editor_04.bmp":
                        #start lime green
                        user.col((136,198,44))
                        user.set_char = "S"
                        
                    elif button.path == "editor_05.bmp":
                        #end tile gold
                        user.col((151,126,44))
                        user.set_char = "G"
                        
                    elif button.path == "editor_06.bmp":
                        #one way blue
                        user.col((0, 0, 140))
                        user.set_char = ">"
                        
                    elif button.path == "editor_07.bmp":
                        #expand by two
                        for y in range(2):
                            for x in range(9):
                                #MicroBlock(((map_length*60 - 60*scroll_count*2,225)))
                                
                                temp = pygame.sprite.Group([
                                    MicroBlock(((map_length*60+104-scroll_count*120,4+x*60))),
                                    MicroBlock(((map_length*60+132-scroll_count*120,4+x*60))),
                                    MicroBlock(((map_length*60+104-scroll_count*120,32+x*60))),
                                    MicroBlock(((map_length*60+132-scroll_count*120,32+x*60)))
                                ])
                                
                                        
                                platform.append(temp)
                            map_length += 1
                            
                    elif button.path == "editor_08.bmp":
                        #decrease by two (map_length has to be maintaind to add on after )
                        map_length -= 2
                        platform = platform[:-18]
                        
                    elif button.path == "save.png":
                        
                        map_list = maptotextlist(platform,map_length)
                        tobesaved = MapSave()
                        
                        for i in range(map_length):
                            for row in range(18):
                                tobesaved.add_block(row,map_list[i][row])
                                
                        print(tobesaved)
                        
                        #file_write(path,tobesaved)
                        
                   
                #enables drag to paint macro         
                left_click = 1
                
            elif event.button == 3:
                #enables drag to paint micro
                right_click = 1

            
            
            elif event.button == 4:
                #scroll up to pan left 
                
                #if not at far left then you can pan left 
                if scroll_count != 0 :
                        
                    for group in platform:
                        group.update(1)
                        
                    scroll_count -= 1 
                    
            elif event.button == 5:
                #scroll down
                
                if scroll_count < (map_length//2 - 7):
                    #pan right while leaving room at end
                
                    for group in platform:
                        group.update(-1)
                        
                    scroll_count += 1       
        
        if left_click:
            
            
            for group in platform:
                if pygame.sprite.spritecollide(user,group,0):
                    #for each sprite in the group collided fill current with brush 
                    for i in group.sprites():
                        i.fill(user.set_colour)
                        i.char = user.set_char
            
        
        elif right_click:
            for group in platform:
                #for each sprite being collided with user fill current
                for sprite in pygame.sprite.spritecollide(user,group,0):
                    sprite.fill(user.set_colour)            
                    sprite.char = user.set_char
                    
            
                
    #moves Cursor object                
    user.update()
    
    #fixes endless blocks
    window.blit(erase,(0,0))
    
    
    #draws all groups in platform
    for group in platform:
        group.draw(window)
    
    
    window.blit(overlay,(0,0))    
    buttons.draw(window)

    pygame.display.flip()
                
