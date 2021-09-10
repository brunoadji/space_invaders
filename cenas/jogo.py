from PPlay.sprite import *
from PPlay.window import *
import global_information
from monster import *
from cenas.ranking import add

class Jogar():
    def __init__(self, janela, tiro):
        self.cooldownEnergyTrue = False
        self.cooldownEnergy = 3
        self.cooldownEnergyTime = 0
        self.cooldownLife = 2
        self.cooldownTime = 0
        
        self.cooldownShip = 0.2
        self.cooldownShipTime = 0
        
        self.fps = 0
        self.frame = 0
        self.tempo = 0
        self.navenoshot = Sprite("imagens/nave_nova.png")
        self.nave = Sprite("imagens/nave.png")
        self.nave.x = janela.width/2 - self.nave.width/2
        self.nave.y = janela.height - self.nave.height - 10
        self.janela = janela
        self.tiro = tiro
        self.keyboard = Window.get_keyboard()
        self.monstro = Monstro(janela, self.nave)

    def loss(self):
        name = input()
        self.monstro.reset()
        add(global_information.Pontos, name)
        global_information.reset()
        global_information.Scene = 1
        if not self.nave.drawable:
            self.nave.unhide()
            
    def win(self):
        global_information.Win = False
        self.monstro.create_monsters()
        self.monstro.chance *= 1.05
        

    def loss_life(self):
        if self.cooldownTime == 0:
            global_information.Lifes -= 1
        if global_information.Lifes == 0:
            return self.loss()
        if self.cooldownTime >= self.cooldownLife:
            self.cooldownTime = 0
            global_information.LossLife = False
            if not self.nave.drawable:
                self.nave.unhide()
        else:
            self.cooldownTime += self.janela.delta_time()
            if self.cooldownShipTime >= self.cooldownShip:
                if self.nave.drawable:
                    self.nave.hide()
                    self.cooldownShipTime = 0
                elif not self.nave.drawable:
                    self.nave.unhide()
                    self.cooldownShipTime = 0
            else:
                self.cooldownShipTime += self.janela.delta_time()

    def run(self):
        if self.keyboard.key_pressed("SPACE"):
            self.janela.draw_text("espaço pressionado", 10, self.janela.height/2, 24, (255, 255, 255), "Arial")
        self.navenoshot.x = self.nave.x
        self.navenoshot.y = self.nave.y
        if self.cooldownEnergyTrue:
            self.navenoshot.draw()
            self.cooldownEnergyTime += self.janela.delta_time()
            if self.cooldownEnergyTime >= self.cooldownEnergy:
                self.cooldownEnergyTime = 0
                self.cooldownEnergyTrue = False
        else:
            self.nave.draw()
        self.monstro.run()
        
        self.tempo += self.janela.delta_time()
        self.frame += 1
        if self.tempo >= 1:
            self.fps = self.frame
            self.frame = 0
            self.tempo = 0
        
        self.janela.draw_text(str(self.fps), 10, 10, 24, (255, 255, 255), "Arial")
        self.janela.draw_text(str(global_information.Pontos), self.janela.width/2, 10, 24, (0, 0, 255), "Arial")
        self.janela.draw_text(str(global_information.Lifes), self.janela.width - 34, 10, 24, (255, 255, 0), "Arial")
        
        if global_information.CoolDown:
            if global_information.Tempo >= global_information.TimeCoolDown[global_information.Difficulty]:
                global_information.CoolDown = False
                global_information.Tempo = 0
            else:
                global_information.Tempo += self.janela.delta_time()
        
        if self.keyboard.key_pressed("SPACE") and not global_information.CoolDown and not self.cooldownEnergyTrue:
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

        if global_information.LossLife:
            self.loss_life()

        if global_information.Win:
            self.win()
        
        if global_information.Loss:
            self.loss()
        
        if self.tiro.quantity == 10:
            self.tiro.quantity = 0
            self.cooldownEnergyTrue = True
        
        self.tiro.update(self.monstro)