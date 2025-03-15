#Crie uma classe ContaBancaria com atributos para o
#titular da conta, número da conta e saldo. Inclua métodos para
#depositar e sacar dinheiro, além de um método para exibir as
#informações da conta.

class ContaBancaria:
    def __init__(self, titular, numero, saldo):
        self.titular = titular
        self.numero = numero
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
 
    def sacar(self, valor):
        self.saldo -= valor

    def infos(self):
        print(f'O titular da conta é {self.titular}, o número da conta é {self.numero} e seu saldo é de {self.saldo}')

banco = ContaBancaria('Diogo', 20, 100)
banco.sacar(20)
banco.infos()
