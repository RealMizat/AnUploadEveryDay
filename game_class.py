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


class player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 6
        self.is_jump = False
        self.jump_count = 8
        self.left = False
        self.right = False
        self.up = False
        self.down = False
        self.walk_count = 0


    def draw(self, win):
        if self.walk_count + 1 >= 15:
            self.walk_count = 0
            
        if self.left:
            win.blit(walk_left[self.walk_count//3], (self.x, self.y))
            self.walk_count += 1
            
        elif self.right:
            win.blit(walk_right[self.walk_count//3], (self.x, self.y))
            self.walk_count += 1
        elif self.up:
            win.blit(walk_forward[self.walk_count//3], (self.x, self.y))
            self.walk_count += 1
        elif self.down:
            win.blit(walk_backward[self.walk_count//3], (self.x, self.y))
            self.walk_count += 1
        else:
            win.blit(char, (self.x, self.y))



def redrawGameWindow():
    win.blit(bg, (0, 0))
    man.draw(win)

    
    pygame.display.update()

#Mainloop
man = player(60, 640, 12, 32)
run = True
while run:
    clock.tick(30)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and man.x > man.vel:
        man.x -= man.vel
        man.left = True
        man.right = False
    elif keys[pygame.K_RIGHT] and man.x < 800 - man.width - man.vel: #  X < Screen Width - Width - vel
        man.x += man.vel
        man.right = True
        man.left = False
    elif keys[pygame.K_UP] and man.y > man.vel:
        man.y -= man.vel
        man.up = True
        man.down = False
    elif keys[pygame.K_DOWN] and man.y < 800 - man.height - man.vel :
        man.y += man.vel
        man.down = True
        man.up = False
    else:
        man.right = False
        man.left = False
        man.walk_count = 0

        
    if not(man.is_jump):
       if keys[pygame.K_SPACE]:
            man.is_jump = True
            man.right = False
            man.left = False
            man.walk_count = 0 



        
    else:
        if man.jump_count >= -8:
            neg = 1
                                # positive neg here to keep -10 to increase y axis (thats backwords)
            if man.jump_count < 0:
                neg = -1         # neg is -1 so when multiplied inverses, next line.
            man.y -= (man.jump_count ** 2 ) * 0.5 * neg
            man.jump_count -= 1
        else:
            man.is_jump = False
            man.jump_count = 8
           
         
    redrawGameWindow()



pygame.quit()
