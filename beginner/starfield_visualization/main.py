import pygame
import random



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
pygame.display.set_caption("STARFIELD VISUALIZATION")

class Star:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.z = 1
    def draw(self):
        center = (int(self.x-self.z),int(self.y-self.z))
        pygame.draw.circle(screen,color[random.randint(0,6)],center,0)

def star_array():
    global star_coordinates
    star_coordinates = []
    for i in range(0,number_of_stars):
        star_coordinates.append([random.randrange(0,width),random.randrange(0,width)])

def move_star(stars,start_range,end_range,substractor):
    for i in range(start_range,end_range):
        if stars[i][0] > 1: #X-COORDINATE IS GREATER THAN 1 
            stars[i][0] = stars[i][0] - substractor
        else:
            stars[i][0] = width - 1
            stars[i][1] = random.randint(0,height)
s = Star(0,0)
running = True
star_array()
screen.fill(black)
counter = 0 #slowing down or speeding up the other fields

# fill the screen with the first 50 stars
for i in range(0,50):
    screen.set_at(star_coordinates[i],color[random.randint(0,6)])

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running  = False

    for i in range(0,250):
        screen.set_at(star_coordinates[i],black)
    move_star(star_coordinates,0,250,1)
    for i in range(0,250):
        screen.set_at(star_coordinates[i],color[random.randint(0,6)])
    counter += 1

    if counter % 2 == 0:
        for i in range(251,499):
            screen.set_at(star_coordinates[i],black)
        move_star(star_coordinates,251,499,2)
        for i in range(251,499):
            screen.set_at(star_coordinates[i],color[4])
    '''
    if counter % 7 == 0:
        for i in range(102,400):
            screen.set_at(star_coordinates[i],black)
        move_star(star_coordinates,102,400,7)
        for i in range(102,400):
            screen.set_at(star_coordinates[i],color[3])

    if counter % 11 == 0:
        for i in range(400,499):
            screen.set_at(star_coordinates[i],black)
        move_star(star_coordinates,400,499,11)
        for i in range(400,499):
            screen.set_at(star_coordinates[i],color[6])
    '''

    pygame.display.flip()
    clock.tick(5)













