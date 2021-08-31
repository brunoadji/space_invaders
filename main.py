from PPlay.window import *
from cenas.jogo import *
from cenas.dificuldade import *
from cenas.menu import *
from cenas.ranking import *
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

switcher = {
    1: menu.run,
    2: dificuldade.run,
    3: ranking.run,
    4: jogo.run
}

while global_information != 5:
    janela.set_background_color([100, 100, 100])
    if global_information.ChangeScene:
        global_information.ChangeScene = False
        
    switcher[global_information.Scene]()
    
    janela.update()