# version 0.0.6
import numpy
import time
import math
import pygame
import os

pygame.init()
width, height = 1920, 1080
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)
text = font.render("Hello, Pygame!", True, (255, 255, 255))
text_rect = text.get_rect(center=(400, 300))

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)


def createIntMatrix(rows, cols, value=0):
    return numpy.full((rows, cols), value, dtype=int)

def coordinateCounter(x, y):
    os.system("clear")
    return "coordinates: ", x, y

def fpsCounter(fpsForLimit: float = 0):

    if fpsForLimit == 0:
        # counter += 1
        # if (1*fpsLimit) <= counter:
            
        #     counter -= fpsLimit 
        pass
    elif(fpsForLimit != 0):
        time.sleep(1/fpsForLimit)
        os.system("clear")
        return "ms: ", 1/fpsForLimit, "fps: ", "haha, where is your time?"
    #elif()
    # fps counter
    # not work, because time in python = don't care
    # try to figur out about "time.perf_counter" the next time
    # for solving that problem
    # return true ms from fps counter here
    # but im the next time or good mood

    # also i prepare, the ms isn's work as
    # expected, so, don't belive the ms
    # because it isn't true

    # also i wanted to do optimized counter
    # for example
    # update my x and y 10 times per second
    # but fps
    # update it every 1 time per second

def debug(x, y, fpsForLimit):
    print(fpsCounter(fpsForLimit), coordinateCounter(x, y))

def square(size=0):
    global width, height
    global black, white
    global screen

    cx, cy = width // 2, height // 2
    firstRectPoint = (cx - size, cy - size)
    secondRectPoint = (cx + size, cy + size)


    # print(firstRectPoint[0], firstRectPoint[1])
    
    pygame.draw.line(screen, red, (firstRectPoint[0], firstRectPoint[1]), (secondRectPoint[0], height-secondRectPoint[1]))
    pygame.draw.line(screen, red, (secondRectPoint[0], height-secondRectPoint[1]), (secondRectPoint[0], secondRectPoint[1]))
    pygame.draw.line(screen, red, (secondRectPoint[0], secondRectPoint[1]), (firstRectPoint[0], height-firstRectPoint[1]))
    pygame.draw.line(screen, red, (firstRectPoint[0], height-firstRectPoint[1]), (firstRectPoint[0], firstRectPoint[1]))


    # print(rf"pygame.draw.line({screen}, {white}, ({cx}, {cy}), ({secondRectPoint[0]}, {secondRectPoint[1]}))")
    # pygame.draw.line(screen, color, (x1, y1), (x2, height-y2))
    # pygame.draw.line(screen, color, (x1, y1), (x2, height-y2))
    # pygame.draw.line(screen, color, (x1, y1), (x2, y2))
    # pygame.draw.line(screen, color, (x1+x2, y1), (x2, y2))
    # pygame.draw.line(screen, color, (x1+x2, y1+y2), (x2-x2, y2))
    # pygame.draw.line(screen, color, (x1, y1+y2), (x2-x2, y2))

def rect(size=0):
    global width, height
    global black, white
    global screen

    cx, cy = width // 2, height // 2

    pygame.draw.rect(screen, white, (0, 0, size, size), width=0)

def main():
    global width, height
    global black, white
    global screen, clock, font, text, text_rect

    cx, cy = width // 2, height // 2
    x, y = 0, 0
    counter = 0
    # fpsLimit = 10
    size = 0
    # print(pygame.display.set_mode((0, 0), pygame.FULLSCREEN))

    running = True
    while running:
        pygame.event.pump()
        keys = pygame.key.get_pressed()
        x, y = pygame.mouse.get_pos()
        debug(x, y, 60)

        if keys[pygame.K_ESCAPE]:
            running = False

        screen.fill(black)
        screen.blit(text, text_rect)
        # for i in range(int(math.pow(2, 10))):

        
        # no, wait, the first try, just create a move by map, and
        # it should bounded with x + y + mouse + ... 
        ###
        # i mean create a new function like mouse move by map
        # when you in the any of edges in your screen, then
        # your ccordinate in the world - changing
        # so, x_mouse + y_mouse + x + y = should be connected
        # and work together
        # then this, below:
        ###
        # commentar of the next stage: change square() function, by rect
        # function like in pygame
        # that's all
        ### 
        pygame.draw.rect(screen, white, (0, 0, 200+size, 200+size), width=0)
        square(200+size)
        # size += 1

        
        pygame.display.flip()
    
        

if __name__ == "__main__":
    main()
    
    



    

    



    
    

        











































