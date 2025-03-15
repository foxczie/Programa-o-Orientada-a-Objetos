#Desenvolva uma classe AnimalDeEstimacao com
#atributos para nome, espécie e idade. Inclua métodos para
#alterar a idade do animal e outro para exibir as informações do
#animal.

class AnimalDeEstimacao:
    def __init__(self, nome, especie, idade):
        self.nome = nome
        self.especie = especie
        self.idade = idade

    def mudaridade(self, idade):
        self.idade = idade

    def infos(self):
        print(f'O nome do animal é {self.nome}, ele é da espécie {self.especie} e tem {self.idade} anos.')
            
ver = AnimalDeEstimacao('Jorge', 'Tartaruga', 19)
ver.mudaridade(20)
ver.infos()