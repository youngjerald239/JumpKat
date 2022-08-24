import pygame
from tiles import AnimatedTile

class Enemy(AnimatedTile):
    def __init__(self,size,x,y):
        super().__init__(size,x,y,'./graphics/enemy/run')
        self.rect.y += size - self.image.get_size()[1]