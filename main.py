from PPlay.window import *
from cenas import *
from fisica import *
import global_information
janela = Window(1000, 800)

menu = Menu(janela)
dificuldade = Dificuldade(janela)
ranking = Ranking(janela)
adicionar_tiro = Tiro(janela)
jogo = Jogar(janela, adicionar_tiro)

while True:
    print("loop works")
    janela.set_background_color([0, 0, 0])
    if global_information.ChangeScene:
        global_information.ChangeScene = False

    if global_information.Scene == 1:
        menu.select()
    if global_information.Scene == 2:
        dificuldade.select()
    if global_information.Scene == 3:
        pass
    if global_information.Scene == 4:
        jogo.select(janela)
    if global_information.Scene == 5:
        exit()
        
    janela.update()