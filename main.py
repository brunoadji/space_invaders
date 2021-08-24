from PPlay.window import *
from cenas import *
from monster import *
from shot import *
import global_information
janela = Window(1000, 800)

menu = Menu(janela)
dificuldade = Dificuldade(janela)
ranking = Ranking(janela)
adicionar_tiro = Tiro(janela)
jogo = Jogar(janela, adicionar_tiro)

while True:
    janela.set_background_color([100, 100, 100])
    if global_information.ChangeScene:
        global_information.ChangeScene = False

    if global_information.Scene == 1:
        menu.select()
    if global_information.Scene == 2:
        dificuldade.select()
    if global_information.Scene == 3:
        pass
    if global_information.Scene == 4:
        jogo.select()
    if global_information.Scene == 5:
        exit()
        
    janela.update()