# probably see version 0.0.4-0.0.6
# for more understand your wishes 
# and just the comments
import numpy
import time
import pygame
import os

class SkyInf:
    # def setScreenSize(self, x, y, fullscreen=False):
    # there is a problem on x and y
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

    def square(self, color, size=0):
        # i'm not sure is it okay or bad
        # x, y = self.x, self.y
        self.x, self.y = self.width // 2, self.height // 2
        firstRectPoint = (self.x - size, self.y - size)
        secondRectPoint = (self.x + size, self.y + size)
        
        pygame.draw.line(self.screen, color, (firstRectPoint[0], firstRectPoint[1]), (secondRectPoint[0], self.height-secondRectPoint[1]))
        pygame.draw.line(self.screen, color, (secondRectPoint[0], self.height-secondRectPoint[1]), (secondRectPoint[0], secondRectPoint[1]))
        pygame.draw.line(self.screen, color, (secondRectPoint[0], secondRectPoint[1]), (firstRectPoint[0], self.height-firstRectPoint[1]))
        pygame.draw.line(self.screen, color, (firstRectPoint[0], self.height-firstRectPoint[1]), (firstRectPoint[0], firstRectPoint[1]))

    def main(self):
        self.x, self.y = 0, 0
        self.size = 0
        fpsLimit = 60 # but its not work as you expected, use clock for it

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            # pygame.event.pump()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                running = False
            
            x, y = pygame.mouse.get_pos()
            print(self.fpsCounter(fpsLimit), self.coordinateCounter(x, y))
            self.screen.fill(pygame.Color("black"))

            # text = self.font.render("Hello, Pygame!", True, (255, 255, 255))
            # text_rect = text.get_rect(center=(200, 300))
            # self.screen.blit(text, text_rect)

            self.square(pygame.Color("red"), 
                        self.size+10)
            self.size += 1
            pygame.display.flip()

if __name__ == "__main__":
    fullscreen = False
    setScreenX, setScreenY = 800, 600
    skyinf = SkyInf(setScreenX, setScreenY, fullscreen)
    skyinf.main()
    
    



    

    



    
    

        











































