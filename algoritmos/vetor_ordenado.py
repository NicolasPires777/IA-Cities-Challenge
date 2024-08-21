import numpy as np

class VetorOrdenado:
    def __init__(self,capacidade):
        self.capacidade = capacidade
        self.ultima_posicao = -1
        self.valores = np.empty(self.capacidade, dtype=object)

    def insere(self, vertice):
        if self.ultima_posicao == self.capacidade - 1:
            print('Espaço em memória reservado já esgotou, limite de ',self.capacidade,' cidades.')
            return
        posicao = 0
        for i in range(self.ultima_posicao+1):
            posicao = i
            if self.valores[i].distancia_objetivo > vertice.distancia_objetivo:
                break
            if i == self.ultima_posicao:
                posicao = i+1
        x = self.ultima_posicao
        while x >= posicao:
            self.valores[x+ 1] = self.valores[x]
            x -= 1
        self.valores[posicao] = vertice
        self.ultima_posicao += 1

    def imprime(self):
        if self.ultima_posicao == -1:
            print('Vetor vazio')
        else:
            for i in range(self.ultima_posicao + 1):
                print(i, ' - ', self.valores[i].rotulo, ' - ', self.valores[i].distancia_objetivo)