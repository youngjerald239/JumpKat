import pygame

class UI:
    def __init__(self,surface):

        # setup
        self.display_surface = surface

        # health
        self.health_bar = pygame.image.load('./graphics/ui/health_bar.png')
        # coins
        self.coin = pygame.image.load('./graphics/ui/coin.png')

    def show_health(self,current,full):
        self.display_surface.blit(self.health_bar,(20,10))
    
    def show_coins(self,amount):
        pass