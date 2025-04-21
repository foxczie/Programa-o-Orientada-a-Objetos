class Imovel:
    def __init__(self, endereco, preco):
        self.endereco = endereco
        self.preco = preco
    
class ImovelNovo(Imovel):
    def __init__(self, endereco, preco, adcpreco):
        super().__init__(endereco, preco)
        self.adcpreco = adcpreco

class ImovelVelho(Imovel):
    def __init__(self, endereco, preco, descpreco):
        super().__init__(endereco, preco)
        self.descpreco = descpreco


        


