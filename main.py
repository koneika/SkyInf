# version 0.0.3
import numpy
import time
import math
import pygame
import os

width, height = 800, 800
black = (0, 0, 0)
white = (255, 255, 255)
screen = pygame.display.set_mode((width, height))

def createIntMatrix(rows, cols, value=0):
    return numpy.full((rows, cols), value, dtype=int)

def coordinateCounter(x, y):
    os.system("clear")
    return "coordinates: ", x, y

def fpsLimit(fpsForLimit: float = 0):

    if fpsForLimit == 0:
        # counter += 1
        # if (1*fpsLimit) <= counter:
            
        #     counter -= fpsLimit 
        pass
    elif(fpsForLimit != 0):
        time.sleep(1/fpsForLimit)
        os.system("clear")
        return "ms: ", 1/fpsForLimit, "fps: ", "haha, where your time?"
    #elif()
    # fps counter
    # not work, because time in python = don't care
    # try to figur out about "time.perf_counter" the next time
    # for solving that problem
    # return true ms from fps counter here
    # but im the next time or good mood

    # also i wanted to do optimized counter
    # for example
    # update my x and y 10 times per second
    # but fps
    # update it every 1 time per second

def debug(x, y):
    print(fpsLimit(60), coordinateCounter(x, y))

def square(size=0):
    global width, height
    global black, white
    global screen

    cx, cy = width // 2, height // 2
    firstRectPoint = (cx - size, cy - size)
    secondRectPoint = (cy + size, cy + size)


    print(firstRectPoint[0], firstRectPoint[1])
    print(secondRectPoint[0], secondRectPoint[1])
    pygame.draw.line(screen, white, (firstRectPoint[0], firstRectPoint[1]), (secondRectPoint[0], secondRectPoint[1]))
    # pygame.draw.line(screen, color, (x1, y1), (x2, height-y2))
    # pygame.draw.line(screen, color, (x1, y1), (x2, height-y2))
    # pygame.draw.line(screen, color, (x1, y1), (x2, y2))
    # pygame.draw.line(screen, color, (x1+x2, y1), (x2, y2))
    # pygame.draw.line(screen, color, (x1+x2, y1+y2), (x2-x2, y2))
    # pygame.draw.line(screen, color, (x1, y1+y2), (x2-x2, y2))

def main():
    global width, height
    global black, white
    global screen

    x, y = 0, 0
    counter = 0
    # fpsLimit = 10

    pygame.init()
    
    clock = pygame.time.Clock()
    print(pygame.display.set_mode((width, height)))

    while True:
        pygame.event.pump()

        x, y = pygame.mouse.get_pos()
        debug(x, y)

        screen.fill(black)

        # for i in range(int(math.pow(2, 10))):
        square(600)

        
        pygame.display.flip()
    
        

if __name__ == "__main__":
    main()
    
    



    

    



    
    

        











































