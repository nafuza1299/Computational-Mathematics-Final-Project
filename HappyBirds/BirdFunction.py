from pygame import *
from BirdClass import *
'''This module contains Custom Built Functions'''

def text_button(textname, mainscreen, screen_type, fontstyle, text, size, xpos, ypos):

    ''' This function changes the text's color and plays a sound effect when it is hovered'''

    if textname.rect.collidepoint(mouse.get_pos()):
        txt = textsprite(fontstyle, text, size, xpos, ypos, 0, 255, 0)
        grouping = Group(txt)
        if screen_type == "Image":
            grouping.draw(mainscreen.display)
        if screen_type == "Fill":
            grouping.draw(mainscreen)
    display.update()

def call_sprite(text, screen_type, mainscreen):

    '''This function displays the sprite into the screen'''

    text_group = Group(text)
    if screen_type == "Image":
        text_group.draw(mainscreen.display)
    if screen_type == "Fill":
            text_group.draw(mainscreen.screen)
    display.update()

def transition_screen(text):

    '''Creates a transitional screen with black background and a text'''

    black = coloredbackground(0, 0, 0)
    transition_text = textsprite("Times", text, 100, 440, 170, 255, 255, 255)
    call_sprite(transition_text, "Fill", black)
    display.update()
