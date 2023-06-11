import pygame as pg
from settings import *

class ObjectRenderer:
    def __init__(self, game):
        self.game = game
        self.creen = game.screen
        self.wall_textures = self.load_wall_textures()
            
    @staticmethod
    def get_textures(path, res=(TEXTURE_SIZE, TEXTURE_SIZE)):
        texture = pg.image.load(path).convert_alpha()
        return pg.transform.scale(texture, res)
    
    def load_wall_textures(self):
        return {
            1: self.get_textures('resources/texturas/1.png'),
            2: self.get_textures('resources/texturas/2.png'),
            4: self.get_textures('resources/texturas/4.png'),
        }