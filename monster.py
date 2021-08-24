from PPlay.sprite import *
import global_information
import random

class Monstro():
    def __init__(self, janela, ship):
        self.time = 0
        self.cooldown = False
        self.timecooldown = 2
        self.ship = ship
        self.janela = janela
        self.monsters = []
        self.shots = []
        self.row = 5
        self.column = 7
        self.speed_x = 100
        self.countDown = 0
        self.next_side = "right"
        self.create_monsters()
        self.down = False
    
    def create_monsters(self):
        height = 10
        for i in range(self.row):
            tmp2 = []
            for j in range(self.column):
                monster = Sprite("imagens/alien.png")
                if j == 0:
                    pos = 10
                else:
                    pos = tmp2[j-1].x + monster.width + monster.width/2
                monster.x = pos
                monster.y = height
                tmp2.append(monster)
            height += 60
            self.monsters.append(tmp2)

    def draw_monsters(self):
        for i in range(len(self.monsters)):
            for j in range(len(self.monsters[i])):
                self.monsters[i][j].draw()

    def down_monsters(self):
        if self.countDown >= 60:
            self.countDown = 0
            self.down = False
        else:
            for i in range(len(self.monsters)):
                for j in range(len(self.monsters[i])):
                    self.monsters[i][j].y += 60 * self.janela.delta_time()
            self.countDown += 60 * self.janela.delta_time()

    def add_shot(self, monster):
        pass
        tiro = Sprite("imagens/tiro.jpg")
        tiro.x = monster.x + monster.width/2
        tiro.y = monster.y + monster.height - tiro.height
        self.shots.append(tiro)

    def update_shots(self):
        for shot in self.shots:
            shot.y += 330 * self.janela.delta_time()
            if shot.y + shot.height >= self.ship.y:
                if shot.x + shot.width > self.ship.x and self.ship.x + self.ship.width > shot.x and not global_information.LossLife:
                    self.ship.x = self.janela.width/2 - self.ship.width/2
                    global_information.LossLife = True
                    self.shots.remove(shot)
                if shot.y >= self.janela.height:
                    self.shots.remove(shot)

    def draw_shots(self):
        for shot in self.shots:
            shot.draw()

    def run(self):
        if len(self.monsters) == 0:
            global_information.Win = True
        else:
            self.draw_monsters()
            self.draw_shots()
            self.update_shots()
            
            max_side_left = False
            max_side_right = False
            
            if self.cooldown:
                if self.time >= self.timecooldown:
                    self.cooldown = False
                    self.time = 0
                else:
                    self.time += self.janela.delta_time()

            for i in range(len(self.monsters)):
                for m in self.monsters[i]:
                    if not self.cooldown:
                        #10% de chance de gerar o tiro
                        if random.randint(0, 9) == 1:
                            self.cooldown = True
                            self.add_shot(m)

            for i in range(len(self.monsters)):
                for j in range(len(self.monsters[i])):
                    self.monsters[i][j].x += self.speed_x * self.janela.delta_time()
                    if self.monsters[i][j].x <= 0 and self.next_side == "left":
                        self.next_side = "right"
                        max_side_left = True
                    if self.monsters[i][j].x >= self.janela.width - self.monsters[i][j].width and self.next_side == "right":
                        self.next_side = "left"
                        max_side_right = True

            if max_side_left:
                self.speed_x = self.speed_x * -1
                max_side_left = False
                self.down = True
                
            if max_side_right:
                self.speed_x = self.speed_x * -1
                max_side_right = False
                self.down = True
            
            if self.down:
                self.down_monsters()

            if self.monsters[-1][0].y + self.monsters[-1][0].height >= self.ship.y:
                global_information.Loss = True