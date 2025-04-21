
class Pessoa:
    def __init__ (self, nome, idade):
        self.nome = nome
        self.idade = idade

        @property
        def idade(self):
            return self.idade
        
        @idade.setter
        def idade(self, nova_idade):
            while nova_idade < 16:
                nova_idade = int(input('Idade insuficiente.'))
            self.idade = nova_idade

class Instrutor(Pessoa):
    def __init__(self, nome, idade, salario):
        super().__init__(nome, idade)
        self.salario = salario

    @property
    def salario(self):
        return self.__salario

    @salario.setter
    def salario(self, novo_salario):
        while novo_salario < 0:
            novo_salario = float(input('Salário inválido.'))
        self.__salario = novo_salario

class Aluno(Pessoa):
    def __init__(self, nome, idade, nota_final = None):
        super().__init__(nome, idade)
        self.nota_final = nota_final

    @property
    def nota_final(self):
        return self.__nota_final
    
    @nota_final.setter
    def nota_final(self, nova_nota_final):
        while nova_nota_final < 0 or nova_nota_final > 10:
            nova_nota_final = float(input('Nota inválida.'))
        self.__nota_final = nova_nota_final

    def aprovado(self):
        if self.__nota_final >= 6:
            return True
        else:
            return False
        
class Curso:
    def __init__(self, nome, instrutor):
        self.nome = nome
        self.instrutor = instrutor
        self.alunos = []

    def adicionar_alunos(self, novo_aluno):
        if novo_aluno not in self.alunos:
            self.alunos.append(novo_aluno)
    
    def listar_alunos(self):
        for aluno in self.alunos:
            print(f'Nome do aluno: {aluno.nome}')

    def exibir_detalhes(self):
        print(f'Nome do curso: {self.nome}\n Nome do instrutor: {self.instrutor.nome}\n Quantidade de alunos matriculados: {len(self.alunos)}')

instrutor1 = Instrutor('Diogo', 99, 1)
instrutor2 = Instrutor('Bia', 20, 9)

aluno1 = Aluno('Maria', 20, 6)
aluno2 = Aluno('Jose', 19, 10)
aluno3 = Aluno('Jesus', 4, 2)

curso = Curso('matematica', instrutor1)

curso.adicionar_alunos(aluno1)
curso.adicionar_alunos(aluno2)
curso.adicionar_alunos(aluno3)

curso.exibir_detalhes()

print(f'{aluno1.nome}: Aprovado') if aluno1.aprovado() else print(f'{aluno1.nome}: Reprovado')
print(f'{aluno2.nome}: Aprovado') if aluno2.aprovado() else print(f'{aluno2.nome}: Reprovado')
print(f'{aluno3.nome}: Aprovado') if aluno3.aprovado() else print(f'{aluno3.nome}: Reprovado')




    


        
                
            
