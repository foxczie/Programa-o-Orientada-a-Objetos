# Implemente uma classe Produto com atributos para
# nome, preço e quantidade em estoque. Adicione métodos para
# adicionar e remover produtos do estoque, e um método para
# imprimir as informações do produto.

class Produto:
    # Construtor é um método que sempre é executado quando a classe(molde) é criada ou instanciada.
    def __init__(self, nome, preco, qtd):
        self.nome = nome
        self.preco = preco
        self.qtd = qtd

    def adicionar(self, qtd):
        if qtd >= 0:
            self.qtd += qtd
        else:
            print('Quantidade Negativa!!!')

    def remover(self, qtd):
        if self.qtd < qtd:
            print('Quantidade insuficiente!!!')
        else:
            self.qtd -= qtd

    def info(self):
        print(f'Nome:{self.nome}')
        print(f'Preço:{self.preco}')
        print(f'Qtd:{self.qtd}')

carro = Produto('oi', '20', '1') #objeto
carro.info()

