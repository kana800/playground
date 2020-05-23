# needs a code cleanup

import pygame
import math
import random
import time

pygame.init()
clock = pygame.time.Clock()
screen_size = (height,width) = (800,800)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Hypotrochoid")
color = [(255,0,0),(255,165,0),(255,255,0),(0,128,0),(0,0,255),(75,0,130),(230,130,238)]


# color
red = (255,0,0)
white = (255,255,255)
black = (0,0,0)
r2 = 100/(math.pi) # THIS IS a/b

kp = []
for rad in range(0,10160,10):
    rads = math.radians(rad)
    a = 400
    b = 400
    r = int(100-round(r2))
    x = a + r * math.cos(rads)
    y = b + r * math.sin(rads)
    kp.append((int(x),int(y)))

def circle(center,end_pos):
    pygame.draw.circle(screen,white,(400,400),100)
    pygame.draw.circle(screen,red,center,round(r2),2)
    pygame.draw.circle(screen,black,center,2)
    pygame.draw.aaline(screen,red,center,end_pos) 

class curve:
    def configure(self,k):
        global six_k,five_k,four_k,three_k,two_k
        six_k = []
        five_k = []
        four_k = []
        three_k = []
        two_k = []
        #r1 = 300
        R = 100
        r = round(r2)
        i = 0
        self.k6 = math.pi
        self.k5 = k-1
        self.k4 = k-2
        self.k3 = k-3
        self.k2 = k-4
        for rads in range(0,10160,10):
            rad = math.radians(rads)
            x6 = r*(self.k6-1)*math.cos(rad) + r*math.cos((self.k6-1)*rad)
            y6 = r*(self.k6-1)*math.sin(rad) - r*math.sin((self.k6-1)*rad)
            x5 = r*(self.k5-1)*math.cos(rad) + r*math.cos((self.k5-1)*rad)
            y5 = r*(self.k5-1)*math.sin(rad) - r*math.sin((self.k5-1)*rad)
            x4 = r*(self.k4-1)*math.cos(rad) + r*math.cos((self.k4-1)*rad)
            y4 = r*(self.k4-1)*math.sin(rad) - r*math.sin((self.k4-1)*rad)
            x3 = r*(self.k3-1)*math.cos(rad) + r*math.cos((self.k3-1)*rad)
            y3 = r*(self.k3-1)*math.sin(rad) - r*math.sin((self.k3-1)*rad)
            x2 = r*(self.k2-1)*math.cos(rad) + r*math.cos((self.k2-1)*rad)
            y2 = r*(self.k2-1)*math.sin(rad) - r*math.sin((self.k2-1)*rad)
            
            six_k.append((int(400+x6),int(400+y6)))
            five_k.append((int(400+x5),int(400+y5)))
            four_k.append((int(400+x4),int(400+y4)))
            three_k.append((int(400+x3),int(400+y3)))
            two_k.append((int(400+x2),int(400+y2)))

            if len(six_k) >= 2:
                #pygame.draw.lines(screen,color[random.randint(0,6)],False,six_k,6)
                #pygame.draw.lines(screen,color[random.randint(0,6)],False,five_k,6)
                #pygame.draw.lines(screen,color[random.randint(0,6)],False,four_k,6)
                #pygame.draw.lines(screen,color[random.randint(0,6)],False,three_k,6)
                circle(kp[i],six_k[i])
                #pygame.draw.circle(screen,white,(400,400),100)
                #pygame.draw.circle(screen,red,center,50)
                #pygame.draw.circle(screen,black,center,2)
                #pygame.draw.aaline(screen,black,center,two_k[len(two_k)-1]) 
                #pygame.draw.lines(screen,color[2],False,two_k,2)
                #pygame.draw.lines(screen,color[random.randint(0,6)],False,six_k,6)
                #pygame.draw.lines(screen,color[random.randint(0,6)],False,five_k,6)
                #pygame.draw.lines(screen,color[random.randint(0,6)],False,four_k,6)
                pygame.draw.lines(screen,color[3],False,six_k,2)
                time.sleep(0.05)
                pygame.display.update()
                i += 1




c = curve()
running  = True
while running: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(black)
    c.configure(6)
    pygame.display.flip()
    clock.tick(5)
