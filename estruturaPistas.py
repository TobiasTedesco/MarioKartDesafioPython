import utilities
import random

class Pistas:
    @staticmethod
    def reta(jogador1, PcPLayer, roladaDeDadoPlayer, roladaDeDadoPC):
        jogador1.velocidade += roladaDeDadoPlayer
        PcPLayer.velocidade += roladaDeDadoPC

        if jogador1.velocidade > PcPLayer.velocidade:
            jogador1.pontos += 1
            print(f'{jogador1} ganhou 1 ponto')

        elif jogador1.velocidade == PcPLayer.velocidade:
            print(f'{jogador1} e {PcPLayer} empataram')

        else:
            print(f'{PcPLayer} ganhou 1 ponto')
            PcPLayer.pontos += 1

        return "Reta"

    @staticmethod
    def curva(jogador1, PcPLayer, roladaDeDadoPlayer, roladaDeDadoPC):
        jogador1.manobrabilidade += roladaDeDadoPlayer
        PcPLayer.manobrabilidade += roladaDeDadoPC

        if jogador1.manobrabilidade > PcPLayer.manobrabilidade:
            jogador1.pontos += 1
            print(f'{jogador1.nome} ganhou 1 ponto')

        elif jogador1.manobrabilidade == PcPLayer.manobrabilidade:
            print(f'{jogador1.nome} e {PcPLayer.nome} empataram')

        else:
            print(f'{PcPLayer.nome} ganhou 1 ponto')
            PcPLayer.pontos += 1

        return "Curva"

    @staticmethod
    def confronto(jogador1, PcPLayer, roladaDeDadoPlayer, roladaDeDadoPC):
        jogador1.poder += roladaDeDadoPlayer
        PcPLayer.poder += roladaDeDadoPC

        if jogador1.poder > PcPLayer.manobrabilidade:
            if PcPLayer.pontos > 0:
                PcPLayer.pontos -= 1
                print(f'{PcPLayer.nome} perdeu 1 ponto')

        elif jogador1.poder == PcPLayer.poder:
            print(f'{jogador1.nome} e {PcPLayer.nome} empataram')

        else:
            if jogador1.pontos > 0:
                print(f'{jogador1.nome} perdeu 1 ponto')
                jogador1.pontos -= 1

        return "Confronto"

    @staticmethod
    def pistas(jogador1, PcPLayer):
        # roladaDeDadoPlayer, roladaDeDadoPC = utilities.Dado.jogadaDeDado(jogador1, PcPLayer)

        pistaAleatoria = [
            Pistas.curva,
            Pistas.reta,
            Pistas.confronto
        ]

        pistaEscolhida = random.choice(pistaAleatoria)

        nomePista = pistaEscolhida(jogador1, PcPLayer, roladaDeDadoPlayer, roladaDeDadoPC)

        return nomePista