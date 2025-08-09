import personagens
import utilities
import estruturaPistas
import telaFinal
import random
import time

voltas = 0

listaPersonagens = {
    "Mario" : personagens.Mario,
    "Peach" : personagens.Peach,
    "Yoshi" : personagens.Yoshi,
    "Bowser" : personagens.Bowser,
    "Luigi" : personagens.Luigi,
    "Donkey Kong" : personagens.DonkeyKong
}

selecPlayer = input('Selecione o seu personagem: ')
if selecPlayer in listaPersonagens:
    jogador1 = listaPersonagens[selecPlayer]
    jogador1.get_infos()

    SelectPcPlayer = random.choice(list(listaPersonagens.values()))
    PcPLayer = SelectPcPlayer
    PcPLayer.get_infos()
    
else:
    print('Escolha inválida ❌')

while voltas < 5:

    nomePista = estruturaPistas.Pistas.pistas(jogador1, PcPLayer)
    
    print(f'A pista escolhida foi: {nomePista} \n')
    
    
    voltas += 1
    print(f'Número de voltas: {voltas}🏎️🏁')
    time.sleep(3)

telaFinal.fim(jogador1, PcPLayer)