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
red = (255,0,0)

#Variable to control audio
pygame.mixer.Sound(SnoopDogg.mp3)
pygame.mixer.Sound.play(-1,0,0)

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
        screen.image.load('soft_green_back.png').convert()
        create_text("Snake Game Classic", font, title_color, screen, screen_width/2, 100)

        mx, my = pygame.mouse.get_pos()

        #Buttons 1,2,3 are Start, Options, Exit, respectively
        button_start = pygame.Rect(200, screen_height-200, 100, 50)
        button_audio = pygame.Rect(400, screen_height-200, 100, 50)
        button_exit = pygame.Rect(600, screen_height - 200, 100, 50)
        button_cosmetics = pygame.Rect(800 ,500, 50, 50)

        #Exit game
        if button_exit.collidepoint((mx,my)):
            if click:
                quit()

        #Audio
        if button_options.collidepoint((mx,my)):
            if click:
                audio()

        #Start game
        if button_start.collidepoint((mx,my)):
            if click:
                game()

        #Cosmetics menu
        if button_cosmetics.collidepoint((mx, my)):
            if click:
                cosmetics()

        click = False
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click == True


#OPTIONS MENU (possibly delete if unnecessary)
def options():
    running = True
    while running:
        screen.image.load('soft_green_back.png').convert()
        create_text("Options", font, title_color, screen, screen_width / 2, 100)

        mx, my = pygame.mouse.get_pos()

        # Buttons
        button_audio = pygame.Rect(200, screen_height - 200, 100, 50)
        button_back = pygame.Rect(400, screen_height - 200, 100, 50)
        button_credits = pygame.Rect(600, screen_height - 200, 100, 50)
        button_cosmetics = pygame.Rect(800, 500, 50, 50)


#Audio Settings(if audio is on before click, turn it off)
def audio():
    if pygame.mixer.get_busy():
        pygame.mixer.pause()
    else:
        pygame.mixer.unpause()



#COSMETICS MENU
def cosmetics():
    running = True
    while running:
        screen.image.load('soft_green_back.png').convert()



#EXIT CALL
def quit():
    running = True
    while running:
        screen.fill(black)
        create_text("Are you sure you want to exit Snake Game Classic?", font, title_color, screen, screen_width / 2, 100)
        mx, my = pygame.mouse.get_pos()

        button_exit = pygame.Rect(screen_width/3, screen_height/2, 100, 50)
        button_return = pygame.Rect(2 * screen_width/3, screen_height/2, 100, 50)

        #EXIT THE PROGRAM
        if button_exit.collidepoint((mx,my)):
            if click:
                pygame.quit()
                sys.exit()

        #Return to the main menu
        if button_return.collidepoint((mx,my)):
            if click:
                main_menu()




#GAME
def game():
    running = True
    while running:
        for event in pygame.event.get()
            if event.type==pygame.QUIT:
                running = False

        #creating the snake
        pygame.draw.rect(screen,snake_color, [screen_width/2,screen_height/2,10,10])
    #Offer option to go to main menu, and if "quit" clicked, exit game

    pygame.quit()
    quit()
