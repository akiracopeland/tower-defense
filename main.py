#!/usr/bin/python3

import pygame as pg

from enemy import Enemy
import constants as c

pg.init()

clock = pg.time.Clock()

screen = pg.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HEIGHT))
pg.display.set_caption("Tower Defense")

enemy_image = pg.image.load('assets/images/enemies/enemy_1.png').convert_alpha()

enemy = Enemy((200, 300), enemy_image)

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