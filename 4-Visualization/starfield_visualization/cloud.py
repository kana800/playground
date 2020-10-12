import pygame
import random
import math
# COLORS & CONSTANTS
white = (255,255,255)
black = (0,0,0)
grey = (169,169,169)
red = (255,0,0)
color = [(255, 0, 0),(255, 165, 0) ,(255, 255, 0),(0, 128, 0),(0, 0, 255) ,(75, 0, 130) ,(238, 130, 238)]
number_of_stars = 500

pygame.init()
clock = pygame.time.Clock()
screen_size = (height,width) = (500,500)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("STARCLUSTER VISUALIZATION")


class Star:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.z = 1
    def draw(self):
        center = (int(self.x),int(self.y))
        pygame.draw.circle(screen,color[random.randint(0,6)],center,0)

def star_array():
    global star_coordinates
    star_coordinates=[]
    for i in range(0,number_of_stars):
        degree = random.randint(0,360)
        degree = 2.0 * degree * math.pi / 360.0 #converting to rads
        #distribution = 0.001
        distribution = float(random.randint(0,10000)/10000)
        distribution = (distribution)**2
        xpos = (math.sin(degree)*distribution*200) #radius is 10
        ypos = (math.cos(degree)*distribution*350) 
        star_coordinates.append([250+xpos,200+ypos])

def calculate(XY):
    star.x = XY[0]
    star.y = XY[1]

running  = True
star = Star(0,0)
star_array()
print(star_coordinates)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(black)
    for i in star_coordinates:
        calculate(i)
        star.draw()
    
    pygame.display.flip()
    clock.tick(10)
