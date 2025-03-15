# Desenvolva uma classe Livro com atributos para título,
# autor, ano de publicação e disponibilidade. Adicione métodos
# para emprestar e devolver o livro, alterando seu status de
# disponibilidade.

class Livro:
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.disp = True

    def emprestar(self):
        if self.disp:
            print('Livro disponivel. Foi pego emprestado com sucesso.')
            self.disp = False
        else:
            print('Livro Indisponível para empréstimo.')

    def devolver(self):
        if self.disp:
            print('Você não pegou esse livro.')
        else:
            print('Livro devolvido com sucesso.')
            self.disp = True
  
livro1 = Livro('Livrasso','Mamae','2000')
livro1.emprestar()
livro1.devolver()
livro1.devolver()