from PPlay.mouse import *
from PPlay.sprite import *
import global_information

class Dificuldade():
    def __init__(self, janela):
        self.janela = janela
        self.backbutton = Sprite("imagens/backbutton.png")
        self.easybutton = Sprite("imagens/easybutton.png")
        self.mediumbutton = Sprite("imagens/mediumbutton.png")
        self.hardbutton = Sprite("imagens/hardbutton.png")
        self.mouse = Mouse()
        self.set_position()

    def set_position(self):
        self.backbutton.x = self.janela.width/2 - self.backbutton.width/2
        self.backbutton.y = 300
        self.easybutton.x = self.janela.width/2 - self.easybutton.width/2
        self.easybutton.y = self.backbutton.y + 80
        self.mediumbutton.x = self.janela.width/2 - self.mediumbutton.width/2
        self.mediumbutton.y = self.easybutton.y + 80
        self.hardbutton.x = self.janela.width/2 - self.hardbutton.width/2
        self.hardbutton.y = self.mediumbutton.y + 80
    
    def draw_buttons(self):
        self.backbutton.draw()
        self.easybutton.draw()
        self.mediumbutton.draw()
        self.hardbutton.draw()

    def run(self):
        self.draw_buttons()
        if self.mouse.is_over_object(self.backbutton):
            if self.mouse.is_button_pressed(1):
                global_information.Scene = 1
        if self.mouse.is_over_object(self.easybutton):
            if self.mouse.is_button_pressed(1):
                global_information.Difficulty = 1
        if self.mouse.is_over_object(self.mediumbutton):
            if self.mouse.is_button_pressed(1):
                global_information.Difficulty = 2
        if self.mouse.is_over_object(self.hardbutton):
            if self.mouse.is_button_pressed(1):
                global_information.Difficulty = 3