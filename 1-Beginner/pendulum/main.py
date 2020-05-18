import pygame
import math
pygame.init()
clock = pygame.time.Clock()

# DISPLAY 
screen_width = 500
screen_height = 500
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Pendulum Animation")

# COLORS
white = pygame.Color(255,255,255)
black = pygame.Color(0,0,0)
red = pygame.Color(255,0,0)
grey = pygame.Color(112,128,144)
# VARIABLES
length  = 250
angle = 90
acceleration  = 0
velocity = 0

# RECT FOR STORING COORDINATES
class bob:
    def __init__(self,x,y,angle):
        self.x = x
        self.y = y
        self.angle = angle
    def draw(self):
        #circle = pygame.draw.circle(screen,(112,128,144),[(int(screen_width/2)),50],250)
        rod = pygame.draw.aalines(screen,white,False,[(int(screen_width/2),50),(self.x,self.y)])
        riley = pygame.draw.circle(screen,(47,79,79),[self.x,self.y],20)
        #pygame.draw.arc(screen,(0,0,0),[0,50,500,250],0,self.angle)

def length_calc(length,angle):
    ball.x = int(screen_width/2 + length * math.sin(angle))
    ball.y = int(50+ length * math.cos(angle))
    ball.angle = angle

ball  = bob(250,250,0)
while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            break

    screen.fill((220,220,220))
    ball.draw()
    length_calc(length,angle)
    
    acceleration = -0.005 * math.sin(angle)
    velocity += acceleration
    velocity *= 0.99
    angle += velocity

    pygame.display.flip()
    clock.tick(30)
