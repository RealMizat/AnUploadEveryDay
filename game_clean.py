import pygame


pygame.init()


win = pygame.display.set_mode((800, 800))


pygame.display.set_caption("Katana BOMB-Sniper!")



walk_right = [pygame.image.load('right1.png'),pygame.image.load('right2.png'),pygame.image.load('right3.png'),pygame.image.load('right4.png'),
                pygame.image.load('right5.png')]

walk_left = [pygame.image.load('left1.png'),pygame.image.load('left2.png'),pygame.image.load('left3.png'),pygame.image.load('left4.png'),
             pygame.image.load('left5.png')]

walk_backward = [pygame.image.load('forward1.png'), pygame.image.load('forward2.png'), pygame.image.load('forward3.png'),pygame.image.load('forward1.png'),
                pygame.image.load('forward2.png'), pygame.image.load('forward3.png')]

walk_forward = [pygame.image.load('backward1.png'), pygame.image.load('backward2.png'), pygame.image.load('backward3.png'),pygame.image.load('backward1.png'),
                 pygame.image.load('backward2.png'), pygame.image.load('backward3.png')]

bg = pygame.image.load('backround.png')

char = pygame.image.load('stand1.png')





 
clock = pygame.time.Clock()

x = 60
y = 640
width = 12
height = 32
vel = 6
is_jump = False
jump_count = 8
left = False
right = False
up = False
down = False
walk_count = 0



def redrawGameWindow():
    global walk_count
    win.blit(bg, (0, 0))

    if walk_count + 1 >= 15:
        walk_count = 0
        
    if left:
        win.blit(walk_left[walk_count//3], (x, y))
        walk_count += 1
        
    elif right:
        win.blit(walk_right[walk_count//3], (x, y))
        walk_count += 1
    elif up:
        win.blit(walk_forward[walk_count//3], (x, y))
        walk_count += 1
    elif down:
        win.blit(walk_backward[walk_count//3], (x, y))
        walk_count += 1
    else:
        win.blit(char, (x, y))


    pygame.display.update()
   

    

    

run = True
while run:
    clock.tick(30)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
        left = True
        right = False
    elif keys[pygame.K_RIGHT] and x < 800 - width - vel: #  X < Screen Width - Width - vel
        x += vel
        right = True
        left = False
    elif keys[pygame.K_UP] and y > vel:
        y -=vel
        up = True
        down = False
    elif keys[pygame.K_DOWN] and y < 800 - height - vel :
        y += vel
        down = True
        up = False
    else:
        right = False
        left = False
        walk_count = 0

        
    if not(is_jump):
       if keys[pygame.K_SPACE]:
            is_jump = True
            right = False
            left = False
            walk_count = 0 



        
    else:
        if jump_count >= -8:
            neg = 1
                                # positive neg here to keep -10 to increase y axis (thats backwords)
            if jump_count < 0:
                neg = -1         # neg is -1 so when multiplied inverses, next line.
            y -= (jump_count ** 2 ) * 0.5 * neg
            jump_count -= 1
        else:
            is_jump = False
            jump_count = 8
           
         
    redrawGameWindow()



pygame.quit()
