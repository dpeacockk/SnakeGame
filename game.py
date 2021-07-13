#Created by: Daniel Peacock

#The classic Snake Game in Python.

#Rules: Move up, down, left, right with W, S, A, D, respectively.
#       You cannot run into yourself or the walls, or you must restart.
#       The objective is to eat apples until you are as long as the entire screen.

import pygame
import sys
import time
import random
pygame.init()
pygame.display.set_caption('Snake Game Classic')

#Setting Screen
screen_width = 1000
screen_height = 700
screen = pygame.display.set_mode((screen_width,screen_height))

#TEST DIFFERENT FONTS: 'dejavuserif', 'dejavusansmono', 'freesans', 'dejavusans', 'freeserif', 'freemono'
print(pygame.font.get_fonts())
font = pygame.font.Sysfont(freesans)

#Sets some standard colors for later usage:
snake_color = (150,240,0)
menu_text_color = (0,50,0)
title_color = (150,240,50)
black = (0,0,0)



#Functions
#Function to create text on the screen
def create_text(text, font_input, color,surface,x,y):
    textobj = font_input.render(text,1,color)
    textrect = textobj.get_rect()
    textrect.topleft = (x,y)
    surface.blit(textobj,textrect)

#MAIN MENU
def main_menu():
    while True:
        screen = pygame.image.load('soft_green_back.png').convert()
        create_text("Snake Game Classic", font, title_color, screen, )


#GAME
def game_loop():
