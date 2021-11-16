from os import walk
import pygame
from pygame import sprite
from pygame import display
from pygame import image
from game_config import *
import this
pygame.init()
Game = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("THE BEST GAME EVER (Ver 0.1)")
clock = pygame.time.Clock()

    
#player & game animation
game_bg = pygame.image.load('sprite/bg.jpg')
player_stay = [pygame.image.load('sprite/stay/1.png'),
               pygame.image.load('sprite/stay/2.png'),
               pygame.image.load('sprite/stay/3.png'),
               pygame.image.load('sprite/stay/4.png'),
               pygame.image.load('sprite/stay/5.png'),
               pygame.image.load('sprite/stay/6.png'),]

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
               pygame.image.load('sprite/jump_rihgt/3.png'),
               pygame.image.load('sprite/jump_right/4.png'),
               pygame.image.load('sprite/jump_right/5.png'),
               pygame.image.load('sprite/jump_right/6.png'),]

player_jump_left = [pygame.image.load('sprite/jump_left/1.png'),
               pygame.image.load('sprite/jump_left/2.png'),
               pygame.image.load('sprite/jump_left/3.png'),
               pygame.image.load('sprite/jump_left/4.png'),
               pygame.image.load('sprite/jump_left/5.png'),
               pygame.image.load('sprite/jump_left/6.png'),]







walkright = False
walkleft = False
animCount = 0


def draw():
    global animCount
    Game.blit(game_bg, (0,-600))
    if animCount + 1 >= FPS:
        animCount = 0

    if walkleft:
        image = pygame.transform.scale(player_walk_left[animCount//5], (PLAYER_WIDTH,PLAYER_HEIGHT))
        Game.blit(image,(PLAYER_X,PLAYER_Y))
        animCount += 1
    elif walkright:
        image = pygame.transform.scale(player_walk_right[animCount//5], (PLAYER_WIDTH,PLAYER_HEIGHT))
        Game.blit(image,(PLAYER_X,PLAYER_Y))
        animCount += 1
    else:
        image = pygame.transform.scale(player_stay[animCount//5], (PLAYER_WIDTH,PLAYER_HEIGHT))
        Game.blit(image,(PLAYER_X,PLAYER_Y))
        animCount += 1

    pygame.display.update()

#main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
      
    draw()      

    # player controls 
    keys = pygame.key.get_pressed()
    if keys[pygame.K_d] and PLAYER_X < WIDTH - 2 - PLAYER_WIDTH:
        PLAYER_X += PLAYER_SPEED
        walkleft = False
        walkright = True
              
    elif keys[pygame.K_a] and PLAYER_X > 2:
        PLAYER_X -= PLAYER_SPEED
        walkleft = True
        walkright = False
        
    else:
        walkleft = False
        walkright = False
        amimCount = 0
        
        
    clock.tick(FPS) 
    pygame.display.flip() 
 