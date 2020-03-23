import pygame
import time

pygame.init()

win = pygame.display.set_mode((700, 680))

pygame.display.set_caption("Game Title")

#clock = pygame.time.Clock()

x = 64
y = 92
width = 18
height = 34
vel = 7


is_jump = False
jump_count = 10 


run = True
while run:
    pygame.time.delay(10)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
    if keys[pygame.K_RIGHT] and x < 700 - width - vel: #  X < Screen Width - Width - vel
        x += vel
    if not(is_jump):
        if keys[pygame.K_UP] and y > vel:
            y -= vel
        if keys[pygame.K_DOWN] and y < 680 - height - vel:  #Subtract vel for the pixles in that frame
            y+= vel
        if keys[pygame.K_SPACE]:
            is_jump = True
    else:
        if jump_count >= -10:
            neg = 1
                                # positive neg here to keep -10 to increase y axis (thats backwords)
            if jump_count < 0:
                neg = -1         # neg is -1 so when multiplied inverses, next line.
            y -= (jump_count ** 2 ) * 0.5 * neg
            jump_count -= 1
        else:
            is_jump = False
            jump_count = 10
           
         

            
    win.fill((90,87,81))

    pygame.draw.rect(win, (95, 230, 110), (x, y, width, height))
    pygame.display.update()



pygame.quit()
