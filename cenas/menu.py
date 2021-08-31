from PPlay.sprite import *
from PPlay.mouse import *
import global_information

class Menu():
    def __init__(self, janela):
        self.janela = janela
        self.startbutton = Sprite("imagens/startbutton.jpg")
        self.difficultybutton = Sprite("imagens/difficultybutton.png")
        self.rankingbutton = Sprite("imagens/rankingbutton.png")
        self.exitbutton = Sprite("imagens/exitbutton.png")
        self.mouse = Mouse()
        self.set_position()
    
    def set_position(self):
        self.startbutton.x = self.janela.width/2 - self.startbutton.width/2
        self.startbutton.y = 300
        self.difficultybutton.x = self.janela.width/2 - self.difficultybutton.width/2
        self.difficultybutton.y = self.startbutton.y + 80
        self.rankingbutton.x = self.janela.width/2 - self.rankingbutton.width/2
        self.rankingbutton.y = self.difficultybutton.y + 80
        self.exitbutton.x = self.janela.width/2 - self.exitbutton.width/2
        self.exitbutton.y = self.rankingbutton.y + 80
    
    def draw_buttons(self):
        self.startbutton.draw()
        self.difficultybutton.draw()
        self.rankingbutton.draw()
        self.exitbutton.draw()
    
    def run(self):
        self.draw_buttons()
        if self.mouse.is_over_object(self.startbutton):
            if self.mouse.is_button_pressed(1):
                global_information.ChangeScene = True
                global_information.Scene = 4
        if self.mouse.is_over_object(self.difficultybutton):
            if self.mouse.is_button_pressed(1):
                global_information.ChangeScene = True
                global_information.Scene = 2
        if self.mouse.is_over_object(self.rankingbutton):
            if self.mouse.is_button_pressed(1):
                global_information.ChangeScene = True
                global_information.Scene = 3
        if self.mouse.is_over_object(self.exitbutton):
            if self.mouse.is_button_pressed(1):
                global_information.ChangeScene = True
                global_information.Scene = 5
