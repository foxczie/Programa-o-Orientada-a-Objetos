#Implemente uma classe Carro com atributos para
#marca, modelo, ano e quilometragem. Inclua métodos para
#aumentar a quilometragem, e outro método
#para exibir informações do carro.

class Carro:
    def __init__(self, marca, modelo, ano, km):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.km = km
        
    def aumentar(self, km):
        self.km += km

    def infos(self):
        print(f'Seu carro é um {self.modelo}, da marca {self.marca}, do ano {self.ano} e possui quilometragem {self.km}.')
            
ver = Carro('Marcona', 'Modelo foda', '2020', 200)
ver.aumentar(2)
ver.infos()

    