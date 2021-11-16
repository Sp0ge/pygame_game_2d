from os import walk
from typing import ClassVar
import pygame
from pygame import sprite
from pygame import display
from pygame import image
from game_config import *

pygame.init()
Game = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("THE BEST GAME EVER (Ver 0.1)")
clock = pygame.time.Clock()

    
#player & game animation
game_bg = pygame.image.load('sprite/bg.jpg')

player_stay_right = [pygame.image.load('sprite/stayright/1.png'),
               pygame.image.load('sprite/stayright/2.png'),
               pygame.image.load('sprite/stayright/1.png'),
               pygame.image.load('sprite/stayright/2.png'),
               pygame.image.load('sprite/stayright/1.png'),
               pygame.image.load('sprite/stayright/2.png'),]
player_stay_left = [pygame.image.load('sprite/stayleft/1.png'),
               pygame.image.load('sprite/stayleft/2.png'),
               pygame.image.load('sprite/stayleft/1.png'),
               pygame.image.load('sprite/stayleft/2.png'),
               pygame.image.load('sprite/stayleft/1.png'),
               pygame.image.load('sprite/stayleft/2.png'),]

player_walk_right = [pygame.image.load('sprite/run_right/1.png'),
               pygame.image.load('sprite/run_right/2.png'),
               pygame.image.load('sprite/run_right/3.png'),
               pygame.image.load('sprite/run_right/4.png'),
               pygame.image.load('sprite/run_right/5.png'),
               pygame.image.load('sprite/run_right/6.png'),]

player_walk_left = [pygame.image.load('sprite/run_left/1.png'),
               pygame.image.load('sprite/run_left/2.png'),
               pygame.image.load('sprite/run_left/3.png'),
               pygame.image.load('sprite/run_left/4.png'),
               pygame.image.load('sprite/run_left/5.png'),
               pygame.image.load('sprite/run_left/6.png'),]

player_jump_right = [pygame.image.load('sprite/jump_right/1.png'),
               pygame.image.load('sprite/jump_right/2.png'),
               pygame.image.load('sprite/jump_rigHt/3.png'),
               pygame.image.load('sprite/jump_right/4.png'),
               pygame.image.load('sprite/jump_right/5.png'),
               pygame.image.load('sprite/jump_right/6.png'),]

player_jump_left = [pygame.image.load('sprite/jump_left/1.png'),
               pygame.image.load('sprite/jump_left/2.png'),
               pygame.image.load('sprite/jump_left/3.png'),
               pygame.image.load('sprite/jump_left/4.png'),
               pygame.image.load('sprite/jump_left/5.png'),
               pygame.image.load('sprite/jump_left/6.png'),]





lookright = False
lookleft = False
walkright = False
walkleft = False
jumpright = False
jumpleft = False
animCount = 0
jumpCount = 10
last = True

def draw():
    global animCount
    Game.blit(game_bg, (BG_X,BG_Y))
    if animCount + 1 >= FPS:
        animCount = 0
    
    if walkleft:
        image = pygame.transform.scale(player_walk_left[animCount//5], (PLAYER_WIDTH,PLAYER_HEIGHT))
        Game.blit(image,(PLAYER_X,PLAYER_Y))
        animCount += 1
    elif jumpright:
        image = pygame.transform.scale(player_jump_right[animCount//5], (PLAYER_WIDTH,PLAYER_HEIGHT))
        Game.blit(image,(PLAYER_X,PLAYER_Y))
        animCount += 1
    elif jumpleft:
        image = pygame.transform.scale(player_jump_left[animCount//5], (PLAYER_WIDTH,PLAYER_HEIGHT))
        Game.blit(image,(PLAYER_X,PLAYER_Y))
        animCount += 1
    elif walkright:
        image = pygame.transform.scale(player_walk_right[animCount//5], (PLAYER_WIDTH,PLAYER_HEIGHT))
        Game.blit(image,(PLAYER_X,PLAYER_Y))
        animCount += 1
    elif lookright:
        image = pygame.transform.scale(player_stay_right[animCount//5], (PLAYER_WIDTH,PLAYER_HEIGHT))
        Game.blit(image,(PLAYER_X,PLAYER_Y))
        animCount += 1
    elif lookleft:
        image = pygame.transform.scale(player_stay_left[animCount//5], (PLAYER_WIDTH,PLAYER_HEIGHT))
        Game.blit(image,(PLAYER_X,PLAYER_Y))
        animCount += 1

    pygame.display.update()

bullets = []

#main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
             
    draw()      

    # player controls 
    keys = pygame.key.get_pressed()
    if not(last):
        facing = 1
    else:
        facing = -1


    if keys[pygame.K_d] and PLAYER_X < WIDTH - 2 - PLAYER_WIDTH:
        if keys[pygame.K_LSHIFT]:
            PLAYER_X += PLAYER_SPEED*2
        else:
            PLAYER_X += PLAYER_SPEED
        last = True
        if not(ISJUMP):
            walkleft = False
            walkright = True
            
    elif keys[pygame.K_a] and PLAYER_X > 2:
        if keys[pygame.K_LSHIFT]:
            PLAYER_X -= PLAYER_SPEED*2
        else:
            PLAYER_X -= PLAYER_SPEED
        last = False
        if not(ISJUMP):
            walkleft = True
            walkright = False
    else:
        if not(last):
            lookleft = True
            lookright =False
        else:
            lookleft = False
            lookright =True 
        walkleft = False
        walkright = False
        amimCount = 0
        
    if not(ISJUMP):  
        if keys[pygame.K_SPACE]:
            ISJUMP = True    
    else:
        if not(last):
            jumpleft = True
        else:
            jumpright = True
            
            
        if jumpCount >= -10:
            if jumpCount < 0:
                PLAYER_Y += (jumpCount ** 2) / 2
            else:
                PLAYER_Y -= (jumpCount ** 2) / 2
            jumpCount -= 1
        else:
            ISJUMP = False
            jumpleft = False
            jumpright = False
            jumpCount = 10
            
            
        
        
        
    clock.tick(FPS) 
    pygame.display.flip() 
 