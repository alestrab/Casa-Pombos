import pygame as pg
from classes import *

pombo_img = pg.image.load('.\imgs\pombo.png')
house_img = pg.image.load('.\imgs\casa.png')
windown = Screen(0.8,'white')
windown.title('Casa dos Pombos')

def create_pombos(n,screen,img_pombo,img_house):
    list_obj=[]
    house_obj=[]
    w,h = screen.width,screen.height
    pombo_img=pg.transform.scale(img_pombo, (600/n, 600/n))
    house_img=pg.transform.scale(img_house, (1200/n, 1200/n))
    for i in range(n):
        list_obj.append(img_Button(pombo_img,(w*i/n,h/2),None))
        if i!=0:
            house_obj.append(img_Button(house_img,(w*(i-1)/(n-1),0),None))
    return list_obj,house_obj

n=6
pombos,casas = create_pombos(n,windown,pombo_img,house_img)
pg.init()
pg.font.init()
rectangle_draging=False
running = True
while running:
    windown.screen.fill(windown.bg_color)
    for event in pg.event.get():

        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.MOUSEBUTTONDOWN:
            for obj in pombos:
                if obj.rect.collidepoint(event.pos):
                    pombo=obj
            if event.button == 1:      
                for obj in pombos:
                    if obj.rect.collidepoint(event.pos):
                        rectangle_draging = True
                        mouse_x, mouse_y = event.pos
                        offset_x = pombo.rect.x - mouse_x
                        offset_y = pombo.rect.y - mouse_y

        elif event.type == pg.MOUSEBUTTONUP:
            for obj in pombos:
                if obj.rect.collidepoint(event.pos):
                    pombo=obj
            if event.button == 1:            
                rectangle_draging = False

        elif event.type == pg.MOUSEMOTION:
            if rectangle_draging:
                mouse_x, mouse_y = event.pos
                x = mouse_x + offset_x
                y = mouse_y + offset_y  
                pombo.position([x,y])
    for obj in casas:
        windown.screen.blit(obj.image, obj.rect)
    for obj in pombos:
        windown.screen.blit(obj.image, obj.rect)
    pg.display.update()