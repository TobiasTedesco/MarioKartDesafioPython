class Corredores:
    def __init__(self, nome, velocidade, manobrabilidade, poder, pontos = 0):
        self.nome = nome
        self.velocidade = velocidade
        self.manobrabilidade = manobrabilidade
        self.poder = poder
        self.pontos = pontos
    
    def get_infos(self):
        print(f'Jogador selecionado: {self.nome} \n \n Velocidade {self.velocidade} \n Manobrabilidade: {self.manobrabilidade} \n Poder: {self.poder} \n Pontuação:{self.pontos}\n')

    def __str__(self):
        return self.nome