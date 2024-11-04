# version 0.0.7
import numpy
import time
import pygame
import os

class SkyInf:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.width, self.height = self.screen.get_size()
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 36)

    def color(self, color):
        return pygame.Color(color)

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

    def debug(self, x, y, fpsForLimit):
        print(self.fpsCounter(fpsForLimit), self.coordinateCounter(x, y))

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

    def rect(self, size=0):

        cx, cy = self.width // 2, self.height // 2

        pygame.draw.rect(self.screen, self.color("white"), (0, 0, size, size), width=0)

    def main(self):

        self.x, self.y = 0, 0
        self.size = 0

        running = True
        while running:
            pygame.event.pump()
            keys = pygame.key.get_pressed()
            x, y = pygame.mouse.get_pos()
            text = self.font.render("Hello, Pygame!", True, (255, 255, 255))
            text_rect = text.get_rect(center=(200, 300))

            self.debug(x, y, 60)

            if keys[pygame.K_ESCAPE]:
                running = False

            self.screen.fill(self.color("black"))
            self.screen.blit(text, text_rect)

            # why should i use it pygame.draw.rect(self.screen, self.color("white"), (0, 0, 200+self.size, 200+self.size)
            # if it's not sized like my normal funtion self.square() ?
            pygame.draw.rect(self.screen, self.color("white"), (0, 0, 200+self.size, 200+self.size), width=0)
            self.square(self.color("red"), 200+self.size)
            self.size += 1
            pygame.display.flip()
        
            

if __name__ == "__main__":
    skyinf = SkyInf()
    skyinf.main()
    
    



    

    



    
    

        











































