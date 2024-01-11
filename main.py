import pygame as pg

import constants as c

pg.init()

#game window
screen = pg.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HEIGHT))
pg.display.set_caption("Tower Defense")

#create clock
clock = pg.time.Clock()



#game loop
run = True
while run:
    
    clock.tick(c.FPS)
    
    #event handler
    for event in pg.event.get():
        #quit program
        if event.type == pg.QUIT:
            run = False
            
            
            
            
pg.quit()