import estruturaPistas
import personagens

def fim(jogador1, PcPLayer):
    if jogador1.pontos > PcPLayer.pontos:
        print(f'{jogador1} foi o grande vencedor!!! 🏆')

    elif PcPLayer.pontos > jogador1.pontos:
                print(f'{PcPLayer} foi o grande vencedor!!! 🏆')

    else:
        print(f'Pela primeira vez na história da Copa Pistão temos um empate duplo! 🏆🏁')