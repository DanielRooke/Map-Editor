from new_map_setup import *

clock = pygame.time.Clock()

keep_going = True	

pygame.display.set_caption("READER") #initial screen caption
window = pygame.display.set_mode(size,RESIZABLE)

#background refresh

#main surface
screen = pygame.Surface(size).convert()

overlay = pygame.Surface((100,1080)).convert()
overlay.fill((165,165,165))

buttons = pygame.sprite.Group([Button("editor_00.bmp",(0,0),50),Button("editor_01.bmp",(1,0),50),Button("editor_02.bmp",(0,1),50),Button("editor_03.bmp",(1,1),50)])
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
                
        elif event.type == VIDEORESIZE:
            window = pygame.display.set_mode(event.size,)
            
            
        elif event.type == MOUSEBUTTONUP:
            if event.button == 1:
                left_click = 0
            elif event.button == 3:
                right_click = 0
                

        elif event.type == MOUSEBUTTONDOWN:
            
            if event.button == 1:
                for button in pygame.sprite.spritecollide(user,buttons,0):
                    if button.path == "editor_00.bmp":
                        user.col((255,255,255))
                   
                    elif button.path == "editor_01.bmp":
                        user.col((90,127,113))

                    elif button.path == "editor_02.bmp":
                        user.col((96,33,16))  
                        
                left_click = 1
                
            elif event.button == 3:
                for button in pygame.sprite.spritecollide(user,buttons,0):
                    if button.path == "editor_00.bmp":
                        user.col((255,255,255))
                        
                    elif button.path == "editor_01.bmp":
                        user.col((90,127,113))

                    elif button.path == "editor_02.bmp":
                        user.col((96,33,16))         
                    
                    
                right_click = 1

            
            
            elif event.button == 4:
                if scroll_count != 0 :
                        
                    for group in platform:
                        group.update(1)
                        
                    scroll_count += 1 
                    
            elif event.button == 5:
                if scroll_count > -1* (map_length - 15):
                        
                    for group in platform:
                        group.update(-1)
                        
                    scroll_count -= 1       
        
        if left_click:
            for group in platform:
                if pygame.sprite.spritecollide(user,group,0):
                    for i in group.sprites():
                        i.fill(user.set_colour)
            
        
        elif right_click:
            for group in platform:
                for sprite in pygame.sprite.spritecollide(user,group,0):
                    sprite.fill(user.set_colour)            
                    
            
                
                
    user.update()
    window.blit(erase,(0,0))
    for group in platform:
        group.draw(window)
    
    window.blit(overlay,(0,0))    
    buttons.draw(window)
    pygame.display.flip()
                
