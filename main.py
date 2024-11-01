import pygame
import numpy
import time

# Looks like something custome.
# Sure, because in python we
# don't have a lot of perfect
# things which from c++ or java.
# So, that's why i use these
# functions, because i want
# feel free, when i'll writing a
# code

# its easy to use this functions
# here is two dimentional array, like in c++

# updateMatrix(firstSize, secondSize)
def updateMatrix(firstVariable, secondVariable):
    for i in range(0, firstVariable):
        for j in range(0, secondVariable):
            pass

# createIntMatrix(firstSize, secondSize)
def createIntMatrix(firstVariable, secondVariable):
    return numpy.zeros((firstVariable, secondVariable), dtype=int)

# createIntMatrixAndPutValue(firstSize, secondSize, yourValue)
def createIntMatrixAndPutValue(firstVariable, secondVariable, value):
    Matrix = createIntMatrix(firstVariable, secondVariable)
    for i in range(0, firstVariable):
        for j in range(0, secondVariable):
            Matrix[i, j] = value
    return Matrix

# frameRate(60)
def frameRate(variable):
    time.sleep(variable/1000)




def fpsCounter(putConstIntTimeTime, counter, counterForAverage, counterForAverage2):
    if putConstIntTimeTime == int(time.time()):
        counter += 1
        # for i in range():
    else:
        print("fps: ", counter)
        counterForAverage += 1
        counterForAverage2 += counter
        counter = 0
        putConstIntTimeTime += 1
        print("average fps: ", counterForAverage2/counterForAverage)
















































# for fps counting
real_time = int(time.time())
counter = 0
counterForAverage = 0
counterForAverage2 = 0

def fpsLimit(count):
    global real_time
    global counter
    global counterForAverage
    global counterForAverage2

    time.sleep(1)
    for i in range(count):
        # for fps counting
        if real_time == int(time.time()):
            counter += 1
            # for i in range():
        else:
            print("fps: ", counter)
            counterForAverage += 1
            counterForAverage2 += counter

            # time.sleep(60/counter)

            counter = 0
            real_time += 1
            print("average fps: ", counterForAverage2/counterForAverage)

# main

while True:
    fpsLimit(60)

    



    
    

        











































# we create matrix
# map = createIntMatrixAndPutValue(100, 100, 1)
# print(map)
# fpsCounter(constTime, 0, 0, 0)

# fpsCounter(not function)

# real_time = int(time.time())
# counter = 0
# counterForAverage = 0
# counterForAverage2 = 0

# counter, counterForAverage, counterForAverage2 = 0, 0, 0

# pygame.init()

# for i in range(0, 100):
#     for j in range(0, 100):
#         map[i, j] = 0

# while True:
#     time.sleep(0.01)

# pygame.init()

# for j in range(0, 100):   
#     for i in range(0, 100):
#         if i == 100-1:
#             pass