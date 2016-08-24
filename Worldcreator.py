from Worldcreator_class import *

size = (1280,720)
clock = pygame.time.Clock()

keep_going = True	
screen = pygame.display.set_mode(size)
pygame.display.set_caption("World Editor") #initial screen caption


#construct Cursor for collisions of platform Group
user = Cursor()

#use to hold left and right arrow
left = False
right = False

#used to click to paint
edit = False

#count used to keep from scrolling off the platform 
count = 0

#Game Loop
while keep_going:
    clock.tick(30)

    
    #event loop    
    for event in pygame.event.get():
        if event.type == QUIT:
            keep_going = False
            
        elif event.type == KEYDOWN:
            
            if event.key == K_LEFT:
                left = 1
            elif event.key == K_RIGHT:
                right = 1
                
                        
            elif event.key == K_q:
                #q sets colour green (Landscape)
                user.col((0,162,0))
                
            elif event.key == K_w:
                #w sets colour Pink (Power-up)
                user.col((163,11,172))
                
            elif event.key == K_e:
                #e sets colour red (lava)
                user.col((143,42,0))
                
            elif event.key == K_r:
                #r sets colout grey (moving block)
                user.col((130,130,130))
                
            elif event.key == K_t:
                #t sets colour blue (Misc Block)
                user.col((0,40,130))            
                
                
            elif event.key == K_s:
                #save image resize my screen to capture all of the pygame.image
                size = (5120,720)
                pygame.display.set_mode(size)
               
                #pans all the way to the left to center image
                for i in range(count):
                    background_rect.move_ip((80,0))
                    platform.update(1)                    
                    
                #build new Surface to save
                temp = pygame.Surface((5120,720))
                
                for i in platform.sprites():
                    temp.blit(i.image,i.rect)
                    #blit all sprites in platform to temp
       
                pygame.image.save(temp,"game_mapV{}.png".format(file_ending))
                
                #close application
                keep_going = 0

                file = open("data.txt","w")
                file.write(str(file_ending + 1))
                file.close()                
            

        elif event.type == KEYUP:
            if event.key == K_LEFT:
                left = 0
            elif event.key == K_RIGHT:
                right = 0        
            
        elif event.type == MOUSEBUTTONDOWN:
            #enable draw
            edit = True
            #click is used to pass on the button that is pressed be it 1(left),2(middle),3(right)
            click = event.button
            
        elif event.type == MOUSEBUTTONUP:
            #disable draw
            edit = False        
            click = event.button
            
    if edit:        
        for i in pygame.sprite.spritecollide(user,platform,False):
            if click == 3:
                #erase if right click all the collided Blocks 
                i.erase()
                
            if click == 1:
                #fill current colour determined from mousebutton downevents events 
                i.fill(user.current)

            
    #panning
    if right and count < 48:
        
        platform.update(-1)
        count += 1
        
    elif left and count != 0:

        platform.update(1)
        count -= 1
        
    #moves Cursor sprite to pyagame.mouse.get_pos()    
    user.update()

    platform.draw(screen)
    pygame.display.flip()
                
