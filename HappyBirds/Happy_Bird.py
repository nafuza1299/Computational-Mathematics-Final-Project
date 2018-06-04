from random import *
import sys
import pygame.mixer
from pygame import *
from pygame.locals import *
from pygame.sprite import *
pygame.init()
display.set_caption ('Happy Bird')
screen = pygame.display.set_mode((1120, 560))

class Birds(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = image.load('bird1.png')
        self.rect = self.image.get_rect()
        #randompos = random.randint(50,750)
        self.rect.center = (50,500)
    def bird1_move_right(self):
        self.rect.left += 10

class Pigpos1(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = image.load('pig.png')
        self.rect = self.image.get_rect()
        #randompos = random.randint(50,750)
        self.rect.center = (200,500)

class Pigpos2(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = image.load('pig.png')
        self.rect = self.image.get_rect()
        #randompos = random.randint(50,750)
        self.rect.center = (400,500)


class Woods(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = image.load('wood.png')
        self.rect = self.image.get_rect()
        #randompos = random.randint(50,750)
        self.rect.center = (500,550)
    def bird1_appear (self):
        #randompos = random.randint(50,750)
        self.rect.top = 0
        self.rect.left = randompos

class button_start(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.font = pygame.font.Font(None,40)
        self.image = self.font.render ('Start',1,(0,0,0))
        self.rect = self.image.get_rect()
        self.rect.center = (100,200)

class button_level(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.font = pygame.font.Font(None,30)
        self.image = self.font.render ('Level',1,(0,0,0))
        self.rect = self.image.get_rect()
        self.rect.center = (100,400)

class button_level1(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.font = pygame.font.Font(None,30)
        self.image = self.font.render ('Level 1',1,(0,0,0))
        self.rect = self.image.get_rect()
        self.rect.center = (100,200)

class button_level2(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.font = pygame.font.Font(None,30)
        self.image = self.font.render ('Level 2',1,(0,0,0))
        self.rect = self.image.get_rect()
        self.rect.center = (100,400)

class button_level3(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.font = pygame.font.Font(None,30)
        self.image = self.font.render ('Level 3',1,(0,0,0))
        self.rect = self.image.get_rect()
        self.rect.center = (100,500)

class button_back(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.font = pygame.font.Font(None,30)
        self.image = self.font.render ('Back',1,(0,0,0))
        self.rect = self.image.get_rect()
        self.rect.center = (200,550)

class button_exit(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.font = pygame.font.Font(None,30)
        self.image = self.font.render ('Exit',1,(0,0,0))
        self.rect = self.image.get_rect()
        self.rect.center = (100,550)

main_game = True
while main_game:
	score = 0
	my_bird = Birds()
	my_pig1 = Pigpos1()
	my_pig2 = Pigpos2()
	my_wood = Woods()
	start = button_start()
	level = button_level()
	level1 = button_level1()
	level2 = button_level2()
	level3 = button_level3()
	back = button_back()
	exit = button_exit()
	groupedpigs = Group(my_pig1, my_pig2)
	groupedbirds = Group(my_bird)
	groupedwoods = Group(my_wood)
	level_buttons = Group(level1, level2, level3, back)
	main_buttons = Group(start, level, exit)
	game_running = False
	secondlayer = False

	firstlayer = True
	while firstlayer:
		startbg = image.load("intro.png")
		screen.blit(startbg,(0,0))
		main_buttons.draw(screen)
		display.update()
		for ev in event.get():
			if ev.type == QUIT:
				pygame.quit()
				sys.exit()
			if ev.type == MOUSEBUTTONDOWN:
				if start.rect.collidepoint(mouse.get_pos()):
					firstlayer = False
					secondlayer = True
					game_running = True
					gamemode = 1
				if level.rect.collidepoint(mouse.get_pos()):
					firstlayer = False
					secondlayer = True
				if exit.rect.collidepoint(mouse.get_pos()):
					pygame.quit()
					sys.exit()

	while secondlayer:
		level1bg = image.load("level1.png")
		screen.blit(level1bg,(0,0))
		level_buttons.draw(screen)
		display.update()
		for i in event.get():
			if i.type == QUIT:
				pygame.quit()
				sys.exit()
			if i.type == MOUSEBUTTONDOWN:
				if level1.rect.collidepoint(mouse.get_pos()):
					game_running = True
					gamemode = 1
				if level2.rect.collidepoint(mouse.get_pos()):
					game_running = True
					gamemode = 2
				if level3.rect.collidepoint(mouse.get_pos()):
					game_running = True
					gamemode = 3
				if back.rect.collidepoint(mouse.get_pos()):
					secondlayer = False
					firstlayer = True

		while game_running:
			level1bg = image.load("level1.png")
			screen.blit(level1bg,(0,0))
			groupedpigs.draw(screen)
			groupedbirds.draw(screen)
			display.update()
			if gamemode == 1:
				for ev in event.get():
					if ev.type == QUIT:
						pygame.quit()
						sys.exit()
					if ev.type == MOUSEBUTTONDOWN:
						my_bird.bird1_move_right()
						for pig in groupedpigs:
							if pig.rect.colliderect(my_bird):
								#pygame.mixer.music.load("Slap-SoundMaster13-49669815.wav")
								#mixer.music.play()
								groupedpigs.remove(pig)
								print("HITTT")
