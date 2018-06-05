from pygame import *
from BirdClass import *
from BirdFunction import *

pygame.init()
'''This module contains the hub area for the game such as menu, levelscreen, intro and outro.'''

def start_screen():
    while True:
        menuscreen = MainScreen("intro.jpg")
        start_screen_wait = event.wait()
        if start_screen_wait.type == MOUSEBUTTONDOWN:
            menu()
        display.update()

def menu():

    '''Opens the menu screen containing, the features, play, levels and quit'''
    #music = sound("Background.wav")

    menuscreen = MainScreen("level1.jpg")
    play = textsprite("AngryBirds", "Play", 60, 100, 100, 255, 255, 255)
    quit = textsprite("AngryBirds", "Quit", 60, 100, 300, 255, 255, 255)
    level = textsprite("AngryBirds", "Level", 60, 100, 200, 255, 255, 255)
    while True:

        #'''Creates the text with rect features, and changes colors when hovered.'''
        play_text = Group(play)
        play_text.draw(menuscreen.display)
        text_button(play, menuscreen, "Image", "AngryBirds", "Play", 60, 100, 100)
        quit_text = Group(quit)
        quit_text.draw(menuscreen.display)
        text_button(quit, menuscreen, "Image", "AngryBirds", "Quit", 60, 100, 300)
        level_text = Group(level)
        level_text.draw(menuscreen.display)
        text_button(level, menuscreen, "Image", "AngryBirds", "Level", 60, 100, 200)
        menu_wait = event.wait()
        if play.rect.collidepoint(mouse.get_pos()):
            Hit = pygame.mixer.Sound('Click2.wav').play()
            if menu_wait.type == MOUSEBUTTONDOWN:
                Hit = pygame.mixer.Sound('Click.wav').play()
                import Level1; Level1.transition_screen1()
        if quit.rect.collidepoint(mouse.get_pos()):
            Hit = pygame.mixer.Sound('Click2.wav').play()
            if menu_wait.type == MOUSEBUTTONDOWN:
                Hit = pygame.mixer.Sound('Click.wav').play()
                pygame.quit()
                break
        if level.rect.collidepoint(mouse.get_pos()):
            Hit = pygame.mixer.Sound('Click2.wav').play()
            if menu_wait.type == MOUSEBUTTONDOWN:
                Hit = pygame.mixer.Sound('Click.wav').play()
                level_screen()
        if menu_wait.type == QUIT:
            pygame.quit()
    display.update()

#Creates the level screen
def level_screen():
    menuscreen = MainScreen("level1.jpg")
    level1 = textsprite("AngryBirds", "Level 1", 60, 100, 100, 255, 255, 255)
    level2 = textsprite("AngryBirds", "Level 2", 60, 100, 200, 255, 255, 255)
    level3 = textsprite("AngryBirds", "Level 3", 60, 100, 300, 255, 255, 255)
    while True:

        level1_text = Group(level1)
        level1_text.draw(menuscreen.display)
        text_button(level1, menuscreen, "Image", "AngryBirds", "Level 1", 60, 100, 100)
        level2_text = Group(level2)
        level2_text.draw(menuscreen.display)
        text_button(level2, menuscreen, "Image", "AngryBirds", "Level 2", 60, 100, 200)
        level3_text = Group(level3)
        level3_text.draw(menuscreen.display)
        text_button(level3, menuscreen, "Image", "AngryBirds", "Level 3", 60, 100, 300)
        menu_wait = event.wait()
        if level1.rect.collidepoint(mouse.get_pos()):
            Hit = pygame.mixer.Sound('Click2.wav').play()
            if menu_wait.type == MOUSEBUTTONDOWN:
                Hit = pygame.mixer.Sound('Click.wav').play()
                import Level1; Level1.transition_screen1()
        if level2.rect.collidepoint(mouse.get_pos()):
            Hit = pygame.mixer.Sound('Click2.wav').play()
            if menu_wait.type == MOUSEBUTTONDOWN:
                Hit = pygame.mixer.Sound('Click.wav').play()
                import Level2; Level2.transition_screen2()
        if level3.rect.collidepoint(mouse.get_pos()):
            Hit = pygame.mixer.Sound('Click2.wav').play()
            if menu_wait.type == MOUSEBUTTONDOWN:
                Hit = pygame.mixer.Sound('Click.wav').play()
                import Level3; Level3.transition_screen3()
        if menu_wait.type == QUIT:
            pygame.quit()
        if menu_wait.type == KEYDOWN:
            if menu_wait.key == K_ESCAPE:
                menu()
        display.update()
