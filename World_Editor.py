from objects import *

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


#______________________ FOR SAVING

filePath = False


#______________________ FOR HOME

#buttons

screen.fill(white)

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
    
#______________________ FOR EDITOR

overlay = pygame.Surface((100,1080)).convert()
overlay.fill((165,165,165))
overlay_rect = overlay.get_rect()
overlay_rect.topleft = (0,0)

find_next = 0
moving = MovingBlock()

lock = 0

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
                               Button("editor_09.bmp",(1,3),50),
                               Button("save.png",(0,9),50),
                               Button("new.png",(1,9),50)
                               ])
left_click = 0
right_click = 0

scroll_count = 0
user = Cursor()


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
                            
                            
                            state = 'editor'
                            screen.fill(black)
                            

                            #need for editor
                            platform = new_world()
                            map_length = platform[1]
                            platform = platform[0]
                            save = MapSave()
                            
                            
                            
                            
                            
                        
                        elif openButton.rect.collidepoint(event.pos):#click collision with open file button
                            
                            #search file directory for a saved txt
                            filePath = fileopenbox(filetypes=['.txt'])
                            if filePath != '.':
                                save = MapSave(filePath) 
                                platform = read_file(filePath)
                                if platform != None:
                                        
                                    map_length = platform[1]
                                    print(type(platform[2]))
                                    save.movingTiles = (platform[2])
                                    platform = platform[0]
                                    screen.fill(black)
                                    state = 'editor'
                                
                
                
                elif event.type == pygame.VIDEORESIZE:  #Window resizing event
                    window = pygame.display.set_mode(event.size, pygame.RESIZABLE)
                    screen = pygame.Surface(event.size).convert()
            
            
            #visual updates to the screen
            
            homeGroup.update()
            homeGroup.draw(screen)
            window.blit(screen, (0, 0))
            pygame.display.flip()
        
       
        '''EDITOR'''
        while state == 'editor':
            for event in pygame.event.get(): 
            
                if event.type == QUIT:
                    end_task()
                
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
                            if button.path == "editor_00.bmp" and not lock:
                                #white "Erase"
                                user.col((255,255,255))
                                user.set_char = " "
                           
                            elif button.path == "editor_01.bmp" and not lock:
                                #Baricade or seafoam green
                                user.col((90,127,113))
                                user.set_char = "W"
        
                            elif button.path == "editor_02.bmp" and not lock:
                                #lava 
                                user.col((96,33,16))  
                                user.set_char = "L"
                                
                            elif button.path == "editor_03.bmp"and not lock:
                                #falling
                                user.col((90,83,113))  
                                user.set_char = "F"
                                
                            elif button.path == "editor_04.bmp"and not lock:
                                #start lime green
                                user.col((136,198,44))
                                user.set_char = "S"
                                
                            elif button.path == "editor_05.bmp"and not lock:
                                #end tile gold
                                user.col((151,126,44))
                                user.set_char = "G"
                                
                            elif button.path == "editor_06.bmp"and not lock:
                                #one way blue
                                user.col((0, 0, 140))
                                user.set_char = ">"
                                
                                    
                                    
                                
                            elif button.path == "editor_07.bmp"and not lock:
                                #expand by two
                                for y in range(2):
                                    for x in range(9):
                                        #MicroBlock(((map_length*60 - 60*scroll_count*2,225)))
                                        
                                        temp = pygame.sprite.OrderedUpdates([
                                            MicroBlock(((map_length*60+104-scroll_count*120,4+x*60))),
                                            MicroBlock(((map_length*60+132-scroll_count*120,4+x*60))),
                                            MicroBlock(((map_length*60+104-scroll_count*120,32+x*60))),
                                            MicroBlock(((map_length*60+132-scroll_count*120,32+x*60)))
                                        ])
                                                
                                        platform.append(temp)
                                    map_length += 1
                                    
                            elif button.path == "editor_08.bmp"and not lock:
                                
                                #decrease by two (map_length has to be maintaind to add on after )
                                map_length -= 2
                                platform = platform[:-18]
                                
                                
                            elif button.path == "editor_09.bmp" :
                                buttons.add(Button("editor_10.bmp",(1,4),50))
                                user.col((44,44,44))
                                user.set_char = "M"
                                lock = True
                                find_next = 1
                                moving = MovingBlock()
                                
                                
                            elif button.path == "editor_10.bmp":
                                button.kill()
                                user.col((90,127,113))  
                                user.set_char = "W"         
                                lock = 0
                                find_next = 0
                                
                                delta = multenterbox("Enter the delta","Editor",("x:","y:"))
                                if delta != None:                                    
                                    moving.delta = (int(delta[0]),int(delta[1]))
                                    
                                save.movingTiles.append(moving)
                                
                                  
                                
                                
                                
                            elif button.path == "save.png"and not lock:
                                
                                for block in save.movingTiles:
                                    if block.isEmpty():
                                        save.movingTiles.remove(block)
                                
                                if save.path == None:
                                    filePath = filesavebox(filetypes=['\*.txt']) #ask for file path
                                    
                                
                                if filePath != None:
                                                                  
                                    map_list = maptotextlist(platform,map_length)
                                                               
                                    for col in map_list:
                                        for row in range(18):
                                            save.add_block(row,col[row])
                                    
                                    
                                    write_file(filePath,save)
                                    
                                    end_task()
                            
                            
                            elif button.path == "new.png"and not lock:
                                save = MapSave()  
                                confirm = boolbox("Are you Sure:")
                                
                                if confirm:
                                        
                                    platform = new_world()
                                    map_length = platform[1]
                                    platform = platform[0]
                                    
                                    
                                    
                        if  not overlay_rect.colliderect(user.rect):
                            left_click = 1
         
                           
                        #enables drag to paint macro         
                        
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
                        
                        if scroll_count < (map_length*2):
                            #pan right while leaving room at end
                        
                            for group in platform:
                                group.update(-1)
                                
                            scroll_count += 1       
                
                if left_click:
                    
                    
                    for group in platform:
                        if pygame.sprite.spritecollide(user,group,0):
                            #for each sprite in the group collided fill current with brush 
                            
                            for sprite in group.sprites():
                                if sprite.image.get_at((0,0)) != user.set_colour:
                                    sprite.fill(user.set_colour)
                                    sprite.char = user.set_char
                                    
                                    
                                    
                                    
                                    #REMOVE or Overwrite a moving tile
                                    if user.set_colour != (44,44,44):
                                        
                                        
                                        group_pos = platform.index(group)
                                        y_pos = (9-group_pos%9)*2
                                        while group_pos%9 != 0:
                                            group_pos -= 1
                                        x_pos = (group_pos//9+1)*2
                                        
                                        if sprite == group.sprites()[0]:
                                            x_pos -= 1
                                        elif sprite == group.sprites()[2]:
                                            x_pos -= 1 
                                            y_pos -= 1
                                            
                                        elif sprite == group.sprites()[3]:
                                            y_pos -= 1
                                                    
                                        if (x_pos,y_pos) in moving.storage:
                                            moving.storage.remove((x_pos,y_pos))                                    
                                        
                                        
                                        #makes erase work on all MovingBlock objects
                                        else:
                                            for i in save.movingTiles:
                                                for cord in i.storage:
                                                    if (x_pos,y_pos) == cord:
                                                        i.storage.remove(cord)                                         
                                            
                                            
                                    if find_next:
                                        group_pos = platform.index(group)
                                        y_pos = (9-group_pos%9)*2
                                        while group_pos%9 != 0:
                                            group_pos -= 1
                                        x_pos = (group_pos//9+1)*2
                                        
                                        if sprite == group.sprites()[0]:
                                            x_pos -= 1
                                        elif sprite == group.sprites()[2]:
                                            x_pos -= 1 
                                            y_pos -= 1
                                            
                                        elif sprite == group.sprites()[3]:
                                            y_pos -= 1
                                            
                                        moving.storage.append((x_pos,y_pos))
                                        
                elif right_click:
                    for group in platform:
                        #for each sprite being collided with user fill current
                        for sprite in pygame.sprite.spritecollide(user,group,0):
                            
                            if sprite.image.get_at((0,0)) != user.set_colour:
                                
                                
                                sprite.fill(user.set_colour)           
                                sprite.char = user.set_char                                
                            
                                #REMOVE or Overwrite a moving tile
                                if user.set_colour != (44,44,44):
                                    #save.movingTiles
                                    group_pos = platform.index(group)
                                    y_pos = (9-group_pos%9)*2
                                    while group_pos%9 != 0:
                                        group_pos -= 1
                                    x_pos = (group_pos//9+1)*2
                                    
                                    if sprite == group.sprites()[0]:
                                        x_pos -= 1
                                    elif sprite == group.sprites()[2]:
                                        x_pos -= 1 
                                        y_pos -= 1
                                        
                                    elif sprite == group.sprites()[3]:
                                        y_pos -= 1
                                                    
                                    if (x_pos,y_pos) in moving.storage:
                                        moving.storage.remove((x_pos,y_pos))                                    
                                    
                                    else:
                                        for i in save.movingTiles:
                                            for cord in i.storage:
                                                if (x_pos,y_pos) == cord:
                                                    i.storage.remove(cord)
                                                    
                                
                                
                            
                            
                                if find_next:
                                    group_pos = platform.index(group)
                                    y_pos = (9-group_pos%9)*2
                                    while group_pos%9 != 0:
                                        group_pos -= 1
                                    x_pos = (group_pos//9+1)*2
                                    
                                    if sprite == group.sprites()[0]:
                                        x_pos -= 1
                                    elif sprite == group.sprites()[2]:
                                        x_pos -= 1 
                                        y_pos -= 1
                                        
                                    elif sprite == group.sprites()[3]:
                                        y_pos -= 1
                                        
                                    moving.storage.append((x_pos,y_pos))
                                    
                    
                        
            #moves Cursor object                
            user.update()
            
            #fixes endless blocks
            window.blit(screen,(0,0))
            
            
            #draws all groups in platform
            for group in platform:
                group.draw(window)
                
            window.blit(overlay,overlay_rect)    
            buttons.draw(window)
        
            pygame.display.flip()
        
        
