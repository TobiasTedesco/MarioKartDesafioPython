import estruturaPersonagens
import personagens
import random

class Dado:
    @staticmethod
    def jogarDado():
        resultado = random.randint(1, 6)
        return resultado

    @staticmethod
    def jogadaDeDado(jogador1, PcPLayer):
        roladaDeDadoPlayer = Dado.jogarDado()
        roladaDeDadoPC = Dado.jogarDado()

        print(f'O {jogador1} tirou {roladaDeDadoPlayer} no dado 🎲')
        print(f'O {PcPLayer} tirou {roladaDeDadoPC} no dado 🎲')

        return roladaDeDadoPlayer, roladaDeDadoPC