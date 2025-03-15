#Implemente uma classe Evento com atributos para
#nome do evento, data e número de participantes. Adicione
#métodos para alterar a data do evento e outro para exibir as
#informações do evento.

class Evento:
    def __init__(self, nome, data, participantes):
        self.nome = nome
        self.data = data
        self.participantes = participantes

    def mudardata(self, data):
        self.data = data

    def infos(self):
        print(f'O nome do evento é {self.nome}, será na data {self.data} e terá {self.participantes} participantes.')
            
ver = Evento('BGS', 2020, 100)
ver.mudardata(2019)
ver.infos()