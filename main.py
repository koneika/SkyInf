# version 0.0.1
import numpy
import time
import math
import pygame
import os

# Looks like something custome.
# Sure, because in python we
# don't have a lot of perfect
# things which from c++ or java.
# So, that's why i use these
# functions, because i want
# feel free, when i write a
# code

# its easy to use this functions
# here is two dimentional array, like in c++
def createIntMatrix(rows, cols, value=0):
    return numpy.full((rows, cols), value, dtype=int)

# for fps counting
real_time = int(time.time())
real_time_float = time.time()
counter = 0
counterForAverage = 0
counterForAverage2 = 0

def fpsCounter(x, y):
    global real_time
    global real_time_float
    global counter
    global counterForAverage
    global counterForAverage2

    # # # print(real_time_float)
    # # if real_time == int(time.time()):
    # counter += 1
    #     # for i in range():
    # # else:
    
    # counterForAverage += 1
    # counterForAverage2 += 1
    # counter = 0
    # # real_time += 1




















    
    # os.system("cls")
    # os.system("clear")

    # counter += 1

    # counter -= 10
    # if counter == 10:
    #     print("fps: ", counter)
    #     return counter
    

    # print(real_time, "==", int(time.time()))

    # if real_time == int(time.time()):
    #     print("hi every 1 sec")
    #     real_time += 1

    #     if real_time == ((int(time.time())) + 10):
    #         real_time -= 10

    # counter += 10
    # if counter == 10:
    #     print("fps: ", counter)
    #     counter = 0
    # for i in range():
    # else:
        # for beautiful show my fps counter and etc.
        # os.system("cls")
        # os.system("clear")

    
    # counterForAverage += 1
    # counterForAverage2 += counter
    
    # real_time += 1
    # print("average fps: ", counterForAverage2/counterForAverage)
    print("coordinates: ", x, y)


    

























    # else:
        # for beautiful show my fps counter and etc.
        # os.system("cls")
        # os.system("clear")
    
    # if real_time == int(time.time()):
    #     print("fps: ", counter)
    # else:
    #     print("fps: ", counter)
    
    # print("coordinates: ", x, y)
    # os.system("cls")
    # os.system("clear")
    
        
    # print("average fps: ", counterForAverage2/counterForAverage)
    
    
def coordinateCounter(x, y):
    # global real_time

    # print(real_time)

    # await fpsCounter(x, y)
    # time.sleep(0.1)
    # print("coordinates: ", x, y)
    # if real_time == int(time.time()):
    #     print("fps: ", counter)
    #     real_time += 1
    # if real_time == int(time.time()):
    #     print("hi")
    time.sleep(0.1)


def main():
    global real_time
    global real_time_float
    global counter
    global counterForAverage
    global counterForAverage2
    
    width, height = 800, 600
    black = (0, 0, 0)
    white = (255, 255, 255)
    x, y = 0, 0

    pygame.init()
    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()
    

    while True:
        time.sleep(0.1)
        
        pygame.event.pump()
        x, y = pygame.mouse.get_pos()
        # map = createIntMatrix(100, 100, 1)
        # width += 1

        screen.fill(black)

        for i in range(int(math.pow(2, 10))):
            pygame.draw.line(screen, white, (0,0), (width//2, height//2))
        
        #await coordinateCounter(x, y)
        print(fpsCounter(x, y))
        # counter += 1
        # print(counter)
        pygame.display.flip()
        
        # clock.tick(60)
    
        

if __name__ == "__main__":
    main()
    
    



    

    



    
    

        











































