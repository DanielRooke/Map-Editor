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


'''-----------------------------FUNCTIONS------------------------------------'''


def end_task():
    '''set quit values to exit program'''
    global exit
    global state
    exit, state = True, 'quit'


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
                line=line[3:].strip('\n')
                for char in line:
                    save.add_block(char)
            #find lines displaying start and end postions for moving blocks
            elif line.startswith('('):
                #(x1, y1),(x2, y2)
                #split the values in the line into a list
                line = line.strip(['(',')'])
                line = line.split('),(')
                for i in line:
                    i = i.split(',')
                #string is now [[x1, y1], [xd, yd]]
                #add the moving block to MapSave object
                save.add_moving_block((line[0][0], line[0][1]), (line[1][0], line[1][1]))
        return save
    else:
        #false first line case
        print('ERROR: NOT A MAP FILE')
        return None

def write_file(filePath, save):
    '''write_file(path, MapSave) -> None
    write the string version of MapSave to a txt at path'''
    #check if file pre exists (write or overwrite)
    file = open(filePath, 'w')
    #writei the string version of save to the file
    file.write(str(save))
    #close txt
    file.close()

def maptotextlist(platform,map_length):
    """M2Tl(list,int) --> list 
    maptotextlist turn the unorganized list of groups into list of collums of characters"""
    
    text_list = []
    left_ori = []
    right_ori = []
    counter = 0 
    
    for x in range(map_length):
        for y in range(9):
            for sprite in platform[9*x+y].sprites():
                if counter % 2 == 0:
                    left_ori.append(sprite.char)
                elif counter %2 != 0:
                    right_ori.append(sprite.char)
                
                elif counter == 35:
                    counter == 0
                    
                counter += 1 
        text_list.append(left_ori)
        text_list.append(right_ori)
        
        left_ori = []
        right_ori = []
                   
    return text_list

def new_world():
    '''new_world() -> list, int
    return platform list and map width'''
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




'''--------------------------------Variables---------------------------------'''

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

    
#______________________ FOR EDITOR

overlay = pygame.Surface((100,1080)).convert()
overlay.fill((165,165,165))
overlay_rect = overlay.get_rect()
overlay_rect.topleft = (0,0)

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
                               Button("save.png",(0,9),50),
                               Button("new.png",(1,9),50)
                               ])
left_click = 0
right_click = 0

scroll_count = 0
user = Cursor()


#Main Program Loop (call end_task() to exit program)
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
                            
                            
                        
                        elif openButton.rect.collidepoint(event.pos):#click collision with open file button
                            
                            #search file directory for a saved txt
                            filePath = fileopenbox(filetypes=['\*.txt'])
                            if filePath != '.':
                                save = read_file(filePath)
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
                                
                                if filePath == False or filePath == None:
                                    filePath = filesavebox(filetypes=['\*.txt']) #ask for file path
                                    
                                
                                if filePath != None:
                                    
                                    save = MapSave()                                
                                    map_list = maptotextlist(platform,map_length)
                                                               
                                    for col in map_list:
                                        for row in range(18):
                                            save.add_block(row,col[row])
                                    
                                    
                                    write_file(filePath,save)
                            
                            
                            elif button.path == "new.png":
                                
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
            window.blit(screen,(0,0))
            
            
            #draws all groups in platform
            for group in platform:
                group.draw(window)
            
            
            window.blit(overlay,overlay_rect)    
            buttons.draw(window)
        
            pygame.display.flip()
        
        
