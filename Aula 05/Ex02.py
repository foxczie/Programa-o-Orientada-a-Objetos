class Animal:
    def __init__(self, nome, cor, numero_patas):
        self.nome = nome
        self.cor = cor
        self.numero_patas = numero_patas
    
class Cachorro(Animal):
    def __init__(self, nome, cor, numero_patas, raca):
        super().__init__(nome, cor, numero_patas)
        self.raca = raca

    def exibir_dados(self):
        print(f'Nome: {self.nome} \n Cor: {self.cor} \n Numero de patas: {self.numero_patas} \n Raça: {self.raca}')

auau = Cachorro('junior', 'rosa', '5', 'cachorro')
auau.exibir_dados()


