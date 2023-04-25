import pygame as pg
from screeninfo import get_monitors

class Screen:
    def __init__(self,size_scale,color):
        for monitor in get_monitors():
            if monitor.is_primary:
                screen_width = monitor.width
                screen_height = monitor.height
        size_scale=0.8
        screen_width=screen_width*size_scale
        screen_height=screen_height*size_scale
        self.width=screen_width
        self.height=screen_height
        self.screen = pg.display.set_mode((screen_width,screen_height))
        self.bg_color = color
    def title(self,title):
        pg.display.set_caption(title)

class img_Button:
    def __init__(self, image, pos, callback):
        '''
            Create a animated button from images
            self.callback is for a funtion for the button to do - set to None
        '''
        self.image = image
        self.rect = self.image.get_rect(topleft=pos)
        self.callback = callback
    def position(self,pos):
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        