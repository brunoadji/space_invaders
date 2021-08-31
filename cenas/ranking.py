from PPlay.sprite import *
import sys

class Ranking():
    def __init__(self, janela):
        self.janela = janela
        self.backbutton = Sprite("imagens/backbutton.png")
        self.backbutton.x = self.janela.width/2 - self.backbutton.width/2
        self.backbutton.y = 200
    
    def add(self, pontos, nome):
        rank = open("ranking.txt", "r")
        string = rank.read()
        rank.close()
        string += ";" + nome + "#" + str(pontos)
        rank = open("ranking.txt", "w")
        rank.write(string)
        rank.close()
        self.update()

    def return_info(self):
        ranks = open("ranking.txt", "r")
        ranking = ranks.read()
        ranks.close()
        ranking = ranking.split(";")
        for i in range(len(ranking)):
            ranking[i] = ranking[i].split("#")
        return ranking
    
    def update(self):
        rank = open("ranking.txt", "r")
        linhas = rank.read()
        linhas = linhas.split(";")
        for i in range(len(linhas)):
            if "\n" in linhas[i]:
                linhas[i] = linhas[i][:len(linhas[i])-1]
        rank.close()
        remove = "something#" + str(sys.maxsize)
        
        while len(linhas) > 5:
            for i in range(len(linhas)-1, -1, -1):
                nome, pontos = linhas[i].split("#")
                if int(remove.split("#")[1]) > int(pontos):
                    remove = linhas[i]
            linhas.remove(remove)
        contador = 0
        while contador <= 4:
            mod = linhas[contador]
            for i in range(contador+1, len(linhas)):
                if int(linhas[i].split("#")[1]) > int(mod.split("#")[1]):
                    linhas[contador] = linhas[i]
                    linhas[i] = mod
                    break
            contador += 1
        string = ""
        for i in range(len(linhas)):
            if i < len(linhas)-1:
                string += linhas[i] + ";"
            else:
                string += linhas[i]
        rank = open("ranking.txt", "w")
        rank.write(string)
        rank.close()
    
    def run(self):
        self.backbutton.draw()
        ranking = self.return_info()
        y_start = 300
        x_start = self.janela.width/2-100
        for i in range(len(ranking)):
            self.janela.draw_text(ranking[i][0], x_start, y_start + i * 50, 24, [255, 0, 0], "Arial")
            self.janela.draw_text(ranking[i][1], x_start + 200, y_start + i * 50, 24, [255, 0, 0], "Arial")