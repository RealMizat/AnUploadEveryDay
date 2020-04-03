import pygame


pygame.init()


win = pygame.display.set_mode((800, 800))


pygame.display.set_caption("Katana BOMB-Sniper!")


#Sprite and Image Loading
walk_right = [pygame.image.load('right1.png'),pygame.image.load('right2.png'),pygame.image.load('right3.png'),pygame.image.load('right4.png'),
                pygame.image.load('right5.png')]

walk_left = [pygame.image.load('left1.png'),pygame.image.load('left2.png'),pygame.image.load('left3.png'),pygame.image.load('left4.png'),
             pygame.image.load('left5.png')]

walk_backward = [pygame.image.load('forward1.png'), pygame.image.load('forward2.png'), pygame.image.load('forward3.png'),pygame.image.load('forward1.png'),
                pygame.image.load('forward2.png')]

walk_forward = [pygame.image.load('backward1.png'), pygame.image.load('backward2.png'), pygame.image.load('backward3.png'),pygame.image.load('backward1.png'),
                 pygame.image.load('backward2.png')]

bg = pygame.image.load('backround2.png')

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
        self.jump_count = 10
        self.left = False
        self.right = False
        self.up = False
        self.down = False
        self.walk_count = 0
        self.standing = True


    def draw(self, win):
        if self.walk_count + 1 >= 15:
            self.walk_count = 0
        if not(self.standing):
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
            if self.right:
                win.blit(walk_right[0], (self.x, self.y))
            elif self.up:
                win.blit(walk_forward[0], (self.x, self.y))
            elif self.down:
                win.blit(walk_backward[0], (self.x, self.y))
            elif self.left:
                win.blit(walk_left[0], (self.x, self.y))
            else:
                win.blit(char, (self.x, self.y))


#Bullet Class / Weapon Snier
class projectile(object):
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 6 * facing

    def draw(self, win):
        pygame.draw.circle(win,self.color, (self.x, self.y), self.radius)


def redrawGameWindow():
    win.blit(bg, (0, 0))
    man.draw(win)
    for bullet in bullets:
        bullet.draw(win)

    
    pygame.display.update()

#Mainloop
man = player(60, 640, 12, 32)  # Instatiate the class - player(x, y, width, height)
run = True
bullets = []            #Creating Bullet List
while run:
    clock.tick(25)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    #Bullets on screen, movement. 
    for bullet in bullets:
        if bullet.x < 800 and bullet.x > 0:
            bullet.x += bullet.vel           #Move in direction facing (neg or positive)
        else:
            bullets.pop(bullets.index(bullet))  #remove bullet place in list
        
    keys = pygame.key.get_pressed()

    if keys[pygame.K_b]:  #Press Key for Bullet
        if man.left: # or man.up:
            facing = -1

        #elif man.right

        #elif man.up

    else:  #man.down
            facing = 1
       
    if len(bullets) < 5:             #len of bullet list
            bullets.append(projectile(round(man.x + man.width//2),round(man.y + man.height//2), 10, (30, 32, 33), facing))
    

    if keys[pygame.K_LEFT] and man.x > man.vel - 8:     #Barrier Stop walking at edge
        man.x -= man.vel
        man.left = True
        man.right = False
        man.up = False
        man.down = False
        man.standing = False
    elif keys[pygame.K_RIGHT] and man.x < 800 - man.width - man.vel: 
        man.x += man.vel
        man.right = True
        man.left = False
        man.up = False
        man.down = False
        man.standing = False
    elif keys[pygame.K_UP] and man.y > man.vel -12:  #man.vel + width/15
        man.y -= man.vel
        man.up = True
        man.down = False
        man.left = False
        man.right = False
        man.standing = False
    elif keys[pygame.K_DOWN] and man.y < 800 - man.height - man.vel :
        man.y += man.vel
        man.down = True
        man.up = False
        man.left = False
        man.right = False
        man.standing = False
    else:
        man.standing = True
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
