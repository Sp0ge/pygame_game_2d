def draw():
    # game drawing         
    Game.fill(WHITE)
    pygame.draw.rect(Game, (BLACK), (PLAYER_X,PLAYER_Y,PLAYER_WIDTH,PLAYER_HEIGHT))
    pygame.display.update()
    
    #player & game animation
    game_bg = pygame.image.load('sprite/bg.jpg')
    player_stay = pygame.image.load('sprite/stay_right.png')
    player_wlak_right = [pygame.image.load('sprite/run1.png'),
                  pygame.image.load('sprite/run2.png'),
                  pygame.image.load('sprite/run3.png'),
                  pygame.image.load('sprite/run4.png')]  