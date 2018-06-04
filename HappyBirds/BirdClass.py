from pygame import *
from pygame.sprite import *
import time
from math import*
import math
import numpy
#This module contains all the custom classes needed for the game'''


class imagesprite(Sprite):

    '''This class is used to create and display an image as a sprite onto the screen'''

    def __init__(self, filename, xpos, ypos):  #fill in the parameters so that it is reusable
        Sprite.__init__(self)
        self.image = image.load(filename)
        self.rect = self.image.get_rect()
        self.rect.x = xpos
        self.rect.y = ypos


#This class is used to spawn the pigs and woods for the first level
class level1(Sprite):
    def __init__(self, screen):
        Sprite.__init__(self)
        self.screen = screen
        self.points = 0
        self.pig1 = imagesprite('pig.png', 800, 310)
        self.pig2 = imagesprite('pig.png', 900, 310)
        self.wood1 = imagesprite('Wood.png', 815, 346)
        self.wood2 = imagesprite('Wood.png', 915, 346)
        self.bird_call = Group(self.pig1, self.pig2)
        self.wood_call = Group(self.wood1, self.wood2)
        self.wood_call.draw(screen)
        self.bird_call.draw(screen)
    #function to recall the bird for each frame change
    def show(self):
        self.bird_call.draw(self.screen)
        self.wood_call.draw(self.screen)

    #removes the sprites from the group
    def remove(self, removal):
        self.removal = removal
        if removal == "pig1":
            self.pig1.rect.top += 10
            self.pig1.rect.left += 3
            if self.pig1.rect.top >= 320:
                Sprite.kill(self.pig1)


        elif removal == "pig2":
            self.pig2.rect.top += 10
            self.pig2.rect.left += 3
            if self.pig2.rect.top >= 320:
                Sprite.kill(self.pig2)

#This class is used to spawn the pigs and woods for the second level
class level2(Sprite):
    def __init__(self, screen):
        Sprite.__init__(self)
        self.screen = screen

        self.pig1 = imagesprite('pig.png', 800, 295)
        self.pig2 = imagesprite('pig.png', 900, 310)
        self.pig3 = imagesprite('pig.png', 700, 310) 
        self.wood1 = imagesprite('Wood.png', 815, 346)
        self.wood2 = imagesprite('Wood.png', 915, 346)
        self.wood3 = imagesprite('Wood.png', 715, 346)
        self.woodblock1 = imagesprite('WoodBlock.png', 785, 287)

        self.bird_call = Group(self.pig1, self.pig2, self.pig3)
        self.wood_call = Group(self.wood1, self.wood2, self.wood3)
        self.woodblock_call1 = Group(self.woodblock1)
        self.wood_call.draw(screen)
        self.bird_call.draw(screen)
        self.woodblock_call1.draw(screen)

    #function to recall the bird for each frame change
    def show(self):
        self.bird_call.draw(self.screen)
        self.wood_call.draw(self.screen)
        self.woodblock_call1.draw(self.screen)


    #removes the sprites from the group
    def remove(self, removal):
        self.removal = removal
        if removal == "pig1":

            self.pig1.rect.top += 10
            self.pig1.rect.left += 3
            if self.pig1.rect.top >= 320:
                Sprite.kill(self.pig1)

        elif removal == "pig2":
            self.pig2.rect.top += 10
            self.pig2.rect.left += 3
            if self.pig2.rect.top >= 320:
                Sprite.kill(self.pig2)

        elif removal == "pig3":
            self.pig3.rect.top += 10
            self.pig3.rect.left += 3
            if self.pig3.rect.top >= 320:
                Sprite.kill(self.pig3)

        elif removal == "woodblock1":
            Sprite.kill(self.woodblock1)
            self.pig1.rect.top = 310


#This class is used to spawn the pigs and woods for the third level
class level3(Sprite):
    def __init__(self, screen):
        Sprite.__init__(self)
        self.screen = screen

        self.pig1 = imagesprite('pig.png', 800, 295)
        self.pig2 = imagesprite('pig.png', 900, 295)
        self.pig3 = imagesprite('pig.png', 700, 158)
        self.pig4 = imagesprite('pig.png', 1000, 295)

        self.wood1 = imagesprite('Wood.png', 815, 346)
        self.wood2 = imagesprite('Wood.png', 915, 346)
        self.wood3 = imagesprite('Wood.png', 715, 346)
        self.wood4 = imagesprite('Wood.png', 1015, 346)
        self.wood5 = imagesprite('Wood.png', 715, 212)

        self.woodblock1 = imagesprite('WoodBlock.png', 785, 287)
        self.woodblock2 = imagesprite('WoodBlock.png', 885, 287)
        self.woodblock3 = imagesprite('WoodBlock.png', 685, 151)
        self.woodblock4 = imagesprite('WoodBlock.png', 985, 287)



        self.bird_call = Group(self.pig1, self.pig2, self.pig3, self.pig4)
        self.wood_call = Group(self.wood1, self.wood2, self.wood3, self.wood4, self.wood5)
        self.woodblock_call = Group(self.woodblock1)
        self.woodblock_call2 = Group(self.woodblock2)
        self.woodblock_call3 = Group(self.woodblock3)
        self.woodblock_call4 = Group(self.woodblock4)

        self.woodblock_call.draw(self.screen)
        self.woodblock_call2.draw(self.screen)
        self.woodblock_call3.draw(self.screen)
        self.woodblock_call4.draw(self.screen)

        self.wood_call.draw(screen)
        self.bird_call.draw(screen)

    #function to recall the bird for each frame change
    def show(self):
        self.bird_call.draw(self.screen)
        self.wood_call.draw(self.screen)
        self.woodblock_call.draw(self.screen)
        self.woodblock_call2.draw(self.screen)
        self.woodblock_call3.draw(self.screen)
        self.woodblock_call4.draw(self.screen)


    #removes the sprites from the group
    def remove(self, removal):
        self.removal = removal
        if removal == "pig1":
            self.pig1.rect.top += 10
            self.pig1.rect.left += 3
            if self.pig1.rect.top >= 320:
                Sprite.kill(self.pig1)

        elif removal == "pig2":
            self.pig2.rect.top += 10
            self.pig2.rect.left += 3
            if self.pig2.rect.top >= 320:
                Sprite.kill(self.pig2)

        elif removal == "pig3":
            Sprite.kill(self.pig3)
        elif removal == "pig4":
            self.pig4.rect.top += 10
            self.pig4.rect.left += 3
            if self.pig4.rect.top >= 320:
                Sprite.kill(self.pig4)


        elif removal == "woodblock1":
            Sprite.kill(self.woodblock1)
            self.pig1.rect.top = 310

        elif removal == "woodblock2":
            Sprite.kill(self.woodblock2)
            self.pig2.rect.top = 310

        elif removal == "woodblock3":
            Sprite.kill(self.woodblock3)
            self.pig3.rect.top = 174

        elif removal == "woodblock4":
            Sprite.kill(self.woodblock4)
            self.pig4.rect.top = 310



class textsprite (Sprite):

    '''This class is used to create and display a text as a sprite onto the screen'''

    def __init__(self, fontstyle, text, fontsize, xpos, ypos, R, G, B):
        Sprite.__init__(self)
        self.font = pygame.font.SysFont(fontstyle, fontsize)
        self.image = self.font.render(text, False, (R, G, B))
        self.rect = self.image.get_rect()
        self.rect.x = xpos
        self.rect.y = ypos

class MainScreen():

    '''This class is used to set an image as the background'''

    def __init__(self, imagefile):
        self.display  = pygame.display.set_mode((1120, 590))
        pygame.display.set_caption("Happy Bird")
        self.image = image.load(imagefile)
        self.display.blit(self.image, (0,0))


class coloredbackground():

    '''This class is used to create a colored background'''

    def __init__(self, R, G, B):
        self.screen  = pygame.display.set_mode((1120, 590))
        pygame.display.set_caption("Happy Bird")
        self.screen.fill((R, G, B))


#Generates the sprite for the bird
class happy(Sprite):
    def __init__(self, screen, x, y, speed):
        Sprite.__init__(self)
        self.speed = speed
        self.x = x
        self.y = y
        self.image = pygame.image.load("Bird1.png")
        self.rect = self.image.get_rect()
        self.rect.left = x
        self.rect.top = y
        self.screen = screen

        self.s = []
        self.n = 10

        #gets the value of each interpolated points
        X = numpy.linspace(0, math.pi, self.n)
        self.scale = 40
        self.scalex = 0

        #appends each point into new array
        for i in range(self.n):
            self.s.append(math.sin(X[i]))

        #gets the distance between each interpolation and appends it into a new array
        self.distancetop = []
        for dis in range(9):
            dis += 1
            self.distancetop.append(self.s[dis] - self.s[dis-1])



    def setleft(self, value):
        self.rect.left = value

    def settop(self, value):
        self.rect.top = value


    def setscalex(self, value):
        self.scalex = value
        self.xcoor = 0.34202014332566877 * self.scalex #the width and x value for the sprites x position

    def setscaley(self, value):
        self.scale = value



    #adds distance between each interpolation into the sprites y scale. (posi1 - nega4)
    def posi1(self):
        self.rect.top -= self.distancetop[0] * self.scale

        self.rect.left += self.xcoor

    def posi2(self):
        self.rect.top -= self.distancetop[1] * self.scale
        self.rect.left += self.xcoor

    def posi3(self):
        self.rect.top -= self.distancetop[2] * self.scale
        self.rect.left += self.xcoor

    def posi4(self):
        self.rect.top -= self.distancetop[3] * self.scale
        self.rect.left += self.xcoor

    def posi5(self):
        self.rect.top -= self.distancetop[4] * self.scale
        self.rect.left += self.xcoor

    def nega1(self):
        self.rect.top -= self.distancetop[5] * self.scale
        self.rect.left += self.xcoor

    def nega2(self):
        self.rect.top -= self.distancetop[6] * self.scale
        self.rect.left += self.xcoor
    def nega3(self):
        self.rect.top -= self.distancetop[7] * self.scale
        self.rect.left += self.xcoor
    def nega4(self):
        self.rect.top -= self.distancetop[8] * self.scale
        self.rect.left += self.xcoor


class background:
    #resourse of the backgound setting
    def __init__(self,background):
        self.background=image.load(background)
        self.background=pygame.transform.scale(self.background,(1120,560))
        self.background_size=self.background.get_size()
        self.background_rect=self.background.get_rect()
        self.width,self.height=self.background_size
    def draw(self,screen,x,y):
        screen.blit(self.background,(x,y))

class sound():

    '''This class is used to play the music continously without interrruptions'''

    def __init__(self, musicfile):
        pygame.mixer.Sound(musicfile).play() #Use Sound instead of music as it won't be interrupted
