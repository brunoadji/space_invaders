from PPlay.sprite import *
from PPlay.window import *
from PPlay.mouse import *
from PPlay.keyboard import *
from fisica import *
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
    
    def select(self):
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
        
    def select(self):
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

class Ranking():
    def __init__(self, janela):
        pass

class Jogar():
    def __init__(self, janela, tiro):
        self.fps = 0
        self.frame = 0
        self.tempo = 0
        self.janela = janela
        self.nave = Sprite("imagens/nave.png")
        self.tiro = tiro
        self.nave.x = janela.width/2 - self.nave.width/2
        self.nave.y = janela.height - self.nave.height - 10
        self.keyboard = Window.get_keyboard()
        self.monstro = Monstro(janela)
    def select(self):
        self.nave.draw()
        self.monstro.run(self.nave)
        
        self.tempo += self.janela.delta_time()
        self.frame += 1
        if self.tempo >= 1:
            self.fps = self.frame
            self.frame = 0
            self.tempo = 0
        
        self.janela.draw_text(str(self.fps), 10, 10, 24, (255, 255, 255), "Arial")
        
        if global_information.CoolDown:
            if global_information.Tempo >= global_information.TimeCoolDown:
                global_information.CoolDown = False
                global_information.Tempo = 0
            else:
                global_information.Tempo += self.janela.delta_time()
        
        if self.keyboard.key_pressed("SPACE") and not global_information.CoolDown:
            self.tiro.add_shot(self.nave)
            global_information.CoolDown = True
        if self.keyboard.key_pressed("D"):
            if self.nave.x < self.janela.width - self.nave.width:
                self.nave.x += global_information.Speed_x * self.janela.delta_time()
                
        if self.keyboard.key_pressed("A"):
            if self.nave.x > 0:
                self.nave.x += -global_information.Speed_x * self.janela.delta_time()

        if self.keyboard.key_pressed("ESC"):
            global_information.Scene = 1
        
        if global_information.Loss:
            global_information.Scene = 1

        self.tiro.update(self.monstro.monsters)