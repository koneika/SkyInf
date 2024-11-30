import numpy
import time
import pygame
import os

class SkyInf:
    def __init__(self, x, y, fullscreen=False):
        pygame.init()
        if(fullscreen):
            self.screen = pygame.display.set_mode((x, y), pygame.FULLSCREEN)
        else:
            self.screen = pygame.display.set_mode((x, y))
        self.width, self.height = self.screen.get_size()
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 36)
        
    def createIntMatrix(self, value=0):
        return numpy.full((self.rows, self.cols), self.value, dtype=int)

    def coordinateCounter(self, x, y):
        os.system("clear")
        return "coordinates: ", x, y

    def fpsCounter(self, fpsForLimit: float = 0):
        if fpsForLimit == 0:
            pass
        elif(fpsForLimit != 0):
            time.sleep(1/fpsForLimit)
            os.system("clear")
            return "ms: ", 1/fpsForLimit, "fps: ", "haha, where is your time?"
        #elif()

    def square(self, x, y, color, size=0):        
        pygame.draw.line(self.screen, color, (x+50, y+50),(x, y))

    def main(self):
        self.x, self.y = self.width // 2, self.height // 2
        self.size = 0
        fpsLimit = 60 # but its not work as you expected, use clock for it

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                running = False
            
            x, y = pygame.mouse.get_pos()
            print(self.fpsCounter(fpsLimit), self.coordinateCounter(x, y))
            self.screen.fill(pygame.Color("black"))

            self.square(self.x, self.y, pygame.Color("red"), self.size)
            self.square(self.x+50, self.y+50, pygame.Color("red"), self.size)
            self.size += 1
            pygame.display.flip()

if __name__ == "__main__":
    fullscreen = False
    setScreenX, setScreenY = 800, 600
    skyinf = SkyInf(setScreenX, setScreenY, fullscreen)
    skyinf.main()
    
    



    

    



    
    

        











































