# Crie uma classe Pessoa com atributos para nome,
# idade e endereço. Inclua métodos para alterar o endereço e
# outro para exibir todas as informações da pessoa.

class Pessoa:
    def __init__(self, nome, idade, endereco):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco

    def alterar(self):
        self.endereco = input('Endereço?: ')

    def exibir(self):
        print(f'Seu nome é {self.nome}, sua idade é {self.idade} e seu endereço é {self.endereco}')

pessoa = Pessoa('Maria', '18', 'Rua batata')
pessoa.alterar()





