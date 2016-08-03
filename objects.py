#!c:/python34/python.exe
# -*- coding: utf-8 -*-
import pygame as pg
pg.init()
spaceDisplay = pg.display.set_mode((600,600))
pg.display.update()
quit = False
move = 1
clock = pg.time.Clock()
while not quit:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            quit = True
        print(event)
    spaceDisplay.fill((0,0,0))
    pg.draw.circle(spaceDisplay, (255,255,255),[100+move,100], 10)
    pg.draw.circle(spaceDisplay, (255,255,255),[200-move,100], 10)
    pg.display.update()
    clock.tick(30)
    move+=1
    
