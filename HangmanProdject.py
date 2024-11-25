#Final Hangman Prodject
#By: Matthew Shawn Oliveira Krischlunas
#Input box source
# https://www.youtube.com/watch?app=desktop&v=Rvcyf4HsWiw

import pygame, random, sys
from pygame.locals import *

pygame.init()

#setting up window
WIDTH = 1000
HEIGHT = 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman")

#setting up colors
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (5,118,54)
BLUE = (0,0,255)
PURPLE = (172, 94, 192)
ROSEWINE = (215, 21, 144)
TEAL = (67, 195, 209)
color_active = pygame.Color('lightskyblue3')
color_passive = pygame.Color('gray15')
color = color_passive

#Other variables
BASICFONT = pygame.font.Font(None, 32)
COUNTER = 0
WRONGITEMS = []
WRONGITEMS_STR = ''
NUM = random.randint(1, 100)
GUESS = []
GUESS_INT =''
ATEMPTS = 6
active = False
CLOCK = pygame.time.Clock()
FPS = 30
USER_TEXT = ''
color = color_passive
input_rect = pygame.Rect(10,50,140,32)
display_rect = pygame.Rect(500, 50, 500, 32)
GAMES = 0
WINS = 0
LOSSES = 0

#Text
TEXT1 = BASICFONT.render("Guess a Number between 1 and 100", True, BLACK)
TEXT2 = BASICFONT.render("Guess Higher", True, BLUE)
TEXT3 = BASICFONT.render("Guess Lower", True, RED)
TEXT5 = BASICFONT.render(f"You have {ATEMPTS} guesses left", True, BLACK)
TEXT4 = BASICFONT.render("You guessed the correct Number, You WIN!!! To play again press the spacebar", True, GREEN)
TEXT6 = BASICFONT.render(f"You Lose, {NUM} was the Number, hit the spacebar to reset game", True, BLACK)
TEXT0 = TEXT1
TEXT7 = BASICFONT.render(f"Wins : {WINS}", True, TEAL)
TEXT8 = BASICFONT.render(f"Losses : {LOSSES}", True, ROSEWINE)
#Drawing the hangging post and background
def Post():
    pygame.draw.line(SCREEN, BLACK, (50, 500), (450, 500),5)
    pygame.draw.line(SCREEN, BLACK, (250, 500), (250, 50),5)
    pygame.draw.line(SCREEN, BLACK, (250, 50), (350, 50),5)
    pygame.draw.line(SCREEN, BLACK, (350, 50), (350, 100),5)

#drawing the man
def TheMan(COUNTER):
    if COUNTER == 1:
        pygame.draw.circle(SCREEN, BLACK, (350, 150),50, 5) #Head
    elif COUNTER == 2:
        pygame.draw.circle(SCREEN, BLACK, (350, 150),50, 5) #Head
        pygame.draw.line(SCREEN, BLACK, (350, 200), (350, 400), 5) #Body
    elif COUNTER == 3:
        pygame.draw.circle(SCREEN, BLACK, (350, 150),50, 5) #Head
        pygame.draw.line(SCREEN, BLACK, (350, 200), (350, 400), 5) #Body
        pygame.draw.line(SCREEN, BLACK, (350, 400), (375, 475), 5) #Left-Leg
    elif COUNTER == 4:
        pygame.draw.circle(SCREEN, BLACK, (350, 150),50, 5) #Head
        pygame.draw.line(SCREEN, BLACK, (350, 200), (350, 400), 5) #Body
        pygame.draw.line(SCREEN, BLACK, (350, 400), (375, 475), 5) #Left-Leg
        pygame.draw.line(SCREEN, BLACK, (350, 400), (325, 475), 5) #Right-Leg
    elif COUNTER == 5:
        pygame.draw.circle(SCREEN, BLACK, (350, 150),50, 5) #Head
        pygame.draw.line(SCREEN, BLACK, (350, 200), (350, 400), 5) #Body
        pygame.draw.line(SCREEN, BLACK, (350, 400), (375, 475), 5) #Left-Leg
        pygame.draw.line(SCREEN, BLACK, (350, 400), (325, 475), 5) #Right-Leg
        pygame.draw.line(SCREEN, BLACK, (350, 275), (375, 350), 5) #Left-Arm
    elif COUNTER == 6:
        pygame.draw.circle(SCREEN, BLACK, (350, 150),50, 5) #Head
        pygame.draw.line(SCREEN, BLACK, (350, 200), (350, 400), 5) #Body
        pygame.draw.line(SCREEN, BLACK, (350, 400), (375, 475), 5) #Left-Leg
        pygame.draw.line(SCREEN, BLACK, (350, 400), (325, 475), 5) #Right-Leg
        pygame.draw.line(SCREEN, BLACK, (350, 275), (375, 350), 5) #Left-Arm
        pygame.draw.line(SCREEN, BLACK, (350, 275), (325, 350), 5) #Right-Arm

# How to play the game
def Instructions():
    if COUNTER == 0 and GAMES == 0:
        InstructionsText1 = BASICFONT.render("To play Hangman click on the empty box on the top left corner", True, PURPLE)
        SCREEN.blit(InstructionsText1, (260, 100))
        InstructionsText2 = BASICFONT.render("The box will turn from black to light blue.", True, PURPLE)
        SCREEN.blit(InstructionsText1, (260, 130))
        InstructionsText3 = BASICFONT.render("You will be asked to type a number between 1 and 100", True, PURPLE)
        SCREEN.blit(InstructionsText2, (260, 160))
        InstructionsText4 = BASICFONT.render("Once you have typed your number, hit the Enter button", True, PURPLE)
        SCREEN.blit(InstructionsText3, (260, 190))
        InstructionsText5 = BASICFONT.render("Then the game will tell you to guess higher or lower after each input",True, PURPLE)
        SCREEN.blit(InstructionsText4, (260, 220))
        InstructionsText6 = BASICFONT.render(f"You have {ATEMPTS} atempts until you lose", True, PURPLE)
        SCREEN.blit(InstructionsText5, (260, 250))
        InstructionsText7 = BASICFONT.render("To play again just tap the SPACEBAR and type in your new guess", True, PURPLE)
        SCREEN.blit(InstructionsText6, (260, 280))
        InstructionsText8 = BASICFONT.render("The number will randomize after each game, Good luck", True, PURPLE)
        SCREEN.blit(InstructionsText7, (260, 310))

    
#Running the game loop
while True:
    SCREEN.fill(WHITE)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
        if event.type == pygame.MOUSEBUTTONDOWN: #setting up our mouse clicker
                if input_rect.collidepoint(event.pos):
                    active = True
                else:
                    active = False

        if event.type == pygame.KEYDOWN: # setting up our key input
            if active == True:
                if event.key == pygame.K_BACKSPACE: # made a mistake no worries just go back one
                    USER_TEXT = USER_TEXT[:-1]
                elif event.key == pygame.K_RETURN: # Time to send it off
                    try: # Can't break the game now if they enter a blank value or letters.
                        GUESS_INT = int(USER_TEXT)
                        GUESS_STR = str(GUESS)
                        if GUESS_INT < NUM:
                            TEXT1 = TEXT2
                            COUNTER += 1
                            ATEMPTS -= 1
                            print(ATEMPTS)
                            WRONGITEMS += [USER_TEXT]
                            WRONGITEMS_STR = str(WRONGITEMS)# Converting ints into strings
                            USER_TEXT = ''
                            del TEXT5 #Gets rid of TEXT5 because fstring wont update
                            TEXT5 = BASICFONT.render(f"You have {ATEMPTS} guesses left", True, BLACK)
                        elif GUESS_INT == NUM:
                            TEXT1 = TEXT4
                            ATEMPTS = 0
                            WINS += 1
                            del TEXT7
                            TEXT7 = BASICFONT.render(f"Wins : {WINS}", True, TEAL)
                            del TEXT5
                            TEXT5 = BASICFONT.render("", True, BLACK)
                        else:
                            TEXT1 = TEXT3
                            COUNTER += 1
                            ATEMPTS -= 1
                            print(ATEMPTS)
                            WRONGITEMS += [USER_TEXT]
                            WRONGITEMS_STR = str(WRONGITEMS) 
                            USER_TEXT = ''
                            del TEXT5
                            TEXT5 = BASICFONT.render(f"You have {ATEMPTS} guesses left", True, BLACK)
                    except ValueError: # This was the error code that i got and needed to place in the except clause
                        COUNTER += 0
                        
                elif event.key == pygame.K_SPACE:
                    COUNTER = 0
                    ATEMPTS = 6
                    WRONGITEMS = []
                    WRONGITEMS_STR = ''
                    USER_TEXT = ''
                    NUM = random.randint(1, 100)
                    TEXT1 = TEXT0
                    GAMES += 1
                    TEXT5 = BASICFONT.render(f"You have {ATEMPTS} guesses left", True, BLACK)
                    
                    
                else:
                    USER_TEXT += event.unicode

    Post()
    Instructions()
    TheMan(COUNTER)
    if active:
        color = color_active
    else:
        color = color_passive

    # This is out click box to input our numbers
    pygame.draw.rect(SCREEN,color,input_rect,2)

    text_surface = BASICFONT.render(USER_TEXT,True,BLACK)
    SCREEN.blit(text_surface,(input_rect.x + 5, input_rect.y + 5))

    input_rect.w = max(100,text_surface.get_width() + 10)

    # This box is where we will post our incorect numbers
    pygame.draw.rect(SCREEN, BLACK, display_rect, 2)
    text_surface2 = BASICFONT.render(WRONGITEMS_STR, True, BLACK)
    SCREEN.blit(text_surface2, (display_rect.x + 5, display_rect.y + 5))
    
    # This box will grow to the nessary size to fit all the incorrect numbers
    display_rect.w = max(100,text_surface2.get_width() + 10)

    if COUNTER == 6:
        COUNTER = 0
        TEXT6 = BASICFONT.render(f"You Lose, {NUM} was the Number, hit the spacebar to reset game", True, BLACK)
        TEXT1 = TEXT6
        WRONGITEMS = []
        WRONGITEMS_STR = ''
        LOSSES += 1
        GAMES += 1
        TEXT5 = BASICFONT.render("", True, BLACK)
        del TEXT8
        TEXT8 = BASICFONT.render(f"Losses : {LOSSES}", True, ROSEWINE)
        del TEXT6
  
        
    if active:
        SCREEN.blit(TEXT1, (10, 20))
    SCREEN.blit(TEXT7,(20, 525))
    SCREEN.blit(TEXT5, (500, 20))
    SCREEN.blit(TEXT8, (20, 550))
    pygame.display.update()
