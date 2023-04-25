import pygame as pg
from classes import *


windown = Screen(0.8,'white')
windown.title('Casa dos Pombos')

def create_pombos(n,screen,img_pombo,img_house):
    list_obj=[]
    house_obj=[]
    w,h = screen.width,screen.height
    w_ratio = w/1536
    h_ratio = h/864
    x_pombo,y_pombo = 85*w_ratio,85*h_ratio  
    x_casa,y_casa = 120*w_ratio,120*h_ratio    
    pombo_img=pg.transform.scale(img_pombo, (x_pombo,y_pombo))
    house_img=pg.transform.scale(img_house, (x_casa,y_casa))
    i,j=0,0
    for k in range(n):
        list_obj.append(img_Button(pombo_img,((3+j)*w/5,h*(i+2)/10),None))
        if k!=(n-1):
            house_obj.append(img_Button(house_img,(j*w/5,h*(i+1)/6),None))
        if j==1:
            j=0
            i=i+1
        else:
            j=j+1
    return list_obj,house_obj

def block_drag(obj,screen):
    w,h = screen.width,screen.height
    x,y = obj.rect.x,obj.rect.y
    w_pombo,h_pombo = obj.rect.w,obj.rect.h
    validate_x = (x>0) and (x<(w-w_pombo))
    validate_y = (y>0) and (y<(h-h_pombo))
    return validate_x and validate_y

pombo_img = pg.image.load('.\imgs\pombo.png')
house_img = pg.image.load('.\imgs\casa.png')

plus_img = pg.image.load('.\imgs\plus.png')
plus_img=pg.transform.scale(plus_img, (40,40))
minus_img = pg.image.load('.\imgs\minus.png')
minus_img=pg.transform.scale(minus_img, (40,40))

plus_img_press = pg.image.load('.\imgs\plus_press.png')
plus_img_press=pg.transform.scale(plus_img_press, (40,40))
minus_img_press = pg.image.load('.\imgs\minus_press.png')
minus_img_press=pg.transform.scale(minus_img_press, (40,40))

pg.init()
pg.font.init()
rectangle_draging=False
running = True



plus_button=img_Button(plus_img,(40,40),None)
plus_button_press=img_Button(plus_img_press,(40,40),None)
minus_button=img_Button(minus_img,(80,40),None)
minus_button_press=img_Button(minus_img_press,(80,40),None)
plus_pressed=False
minus_pressed=False
add_one = True
plus_motion=False
minus_motion=False
n=1
pombos,casas = create_pombos(n,windown,pombo_img,house_img)


pombo_icon_img = pg.transform.scale(pombo_img, (40,40))
pombo_icon=img_Button(pombo_icon_img,(140,40),None)
while running:
    windown.screen.fill(windown.bg_color)
    windown.screen.blit(pombo_icon.image, pombo_icon.rect)        
    if plus_motion:
        windown.screen.blit(plus_button.image, plus_button.rect)
    else:
        windown.screen.blit(plus_button_press.image, plus_button_press.rect)   
    if minus_motion:
        windown.screen.blit(minus_button.image, minus_button.rect)
    else:
        windown.screen.blit(minus_button_press.image, minus_button_press.rect)

    
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
                if (plus_button.rect.collidepoint(event.pos))&(not plus_pressed):
                    plus_pressed=True
                if (minus_button.rect.collidepoint(event.pos))&(not minus_pressed):
                    minus_pressed=True
                    
        elif event.type == pg.MOUSEBUTTONDOWN:
            if (event.button == 1)&(not add_one)&((plus_button.rect.collidepoint(event.pos))|(minus_button.rect.collidepoint(event.pos))):            
                    add_one=True

        elif event.type == pg.MOUSEMOTION:
            if plus_button.rect.collidepoint(event.pos):
                plus_motion=True
                minus_motion=False
            elif minus_button.rect.collidepoint(event.pos):
                minus_motion=True
                plus_motion=False
            else:
                plus_motion=False
                minus_motion=False
                
            mouse_x, mouse_y = event.pos
            if rectangle_draging:
                mouse_x, mouse_y = event.pos
                x = mouse_x + offset_x
                y = mouse_y + offset_y  
                pombo.position([x,y])   
                rectangle_draging=block_drag(pombo,windown)
    
    #create_menu(windown.screen)
    if plus_pressed&(n<10):
        n=n+1
        pombos,casas = create_pombos(n,windown,pombo_img,house_img)
        plus_pressed = False
    elif minus_pressed&(n>1):
        n=n-1
        pombos,casas = create_pombos(n,windown,pombo_img,house_img)
        minus_pressed = False
    for obj in casas:
        windown.screen.blit(obj.image, obj.rect)
    for obj in pombos:
        windown.screen.blit(obj.image, obj.rect)
    pg.display.update()