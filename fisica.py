from PPlay.sprite import *
class Tiro():
    def __init__(self, janela):
        self.janela = janela
        self.tiros = []

    def add_shot(self, nave):
        tiro = Sprite("imagens/tiro.jpg")
        tiro.set_position(nave.x + nave.width/2, nave.y - tiro.height)
        self.tiros.append(tiro)
    
    def draw_shots(self):
        for i in range(len(self.tiros)):
            self.tiros[i].draw()

    def update(self):
        variacao = 0
        for i in range(len(self.tiros)):
            self.tiros[i-variacao].y = self.tiros[i-variacao].y - 300 * self.janela.delta_time()
            if self.tiros[i-variacao].y <= -self.tiros[i-variacao].height:
                self.tiros.pop(i-variacao)
                variacao += 1
        self.draw_shots()

class Monstro():
    def __init__(self, janela):
        self.janela = janela
        self.monsters = []
        self.row = 3
        self.column = 5
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
        for i in range(self.row):
            for j in range(self.column):
                self.monsters[i][j].draw()
    
    def down_monsters(self):
        if self.countDown >= 50:
            self.countDown = 0
            self.down = False
        else:
            for i in range(self.row):
                for j in range(self.column):
                    self.monsters[i][j].y += 50 * self.janela.delta_time()
            self.countDown += 50 * self.janela.delta_time()
    
    # def align_monster_right(self):
    #     for i in range(self.row):
    #         for j in range(self.column-1, -1, -1):
    #             if j == self.column-1:
    #                 self.monsters[i][j].x = self.janela.width - self.monsters[i][j].width
    #             else:
    #                 self.monsters[i][j].x = self.monsters[i][j+1].x - self.monsters[i][j].width - self.monsters[i][j].width/2
    
    # def align_monster_left(self):
    #     for i in range(self.row):
    #         for j in range(self.column):
    #             if j == 0:
    #                 self.monsters[i][j].x = 0
    #             else:
    #                 self.monsters[i][j].x = self.monsters[i][j-1].x + self.monsters[i][j].width + self.monsters[i][j].width/2
    
    def run(self):
        self.draw_monsters()
        max_side_left = False
        max_side_right = False
        for i in range(self.row):
            for j in range(self.column):
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
            # self.align_monster_left()
            
        if max_side_right:
            self.speed_x = self.speed_x * -1
            max_side_right = False
            self.down = True
            # self.align_monster_right()
            
        if self.down:
            self.down_monsters()