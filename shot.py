from PPlay.sprite import *
import global_information
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

    def update(self, monsters):
        variacao = 0
        for shot in self.tiros:
            shotted = False
            shot.y = shot.y - 300 * self.janela.delta_time()
            
            if shot.y <= 0 - shot.height:
                self.tiros.remove(shot)
                variacao += 1
            if shot.y <= monsters[-1][-1].y + monsters[-1][-1].height:
                for m in range(len(monsters)):
                    if shotted:
                        break
                    for monster in monsters[m]:
                        if shot.collided(monster):
                            monsters[m].remove(monster)
                            self.tiros.remove(shot)
                            variacao += 1
                            if len(monsters[m]) == 0:
                                monsters.pop(m)
                            shotted = True
                            global_information.Pontos += 100

        self.draw_shots()