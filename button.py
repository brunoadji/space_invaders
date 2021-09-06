import pygame
class button():
    def __init__(self, text, font):
        self.x = 0
        self.y = 0
        self.width = 0
        self.height = 0
        self.text = text
        self.font = pygame.font.Font("space_invaders.ttf")
        self.textcolor = (255, 255, 255)
        self.surfacecolor = (0, 0, 0)