class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome 
        self.idade = self.set_idade(idade)
        
    def set_idade(self, nova_idade):
        if nova_idade < 18:
            nova_idade = int(input(f'Digite outra idade.'))
        self.idade = nova_idade

class Funcionario(Pessoa):
    def __init__(self, nome, idade, salario):
        self.__salario = salario
        super().__init__(nome, idade)

    def get_salario(self):
        return self.__salario
    
    def set_salario(self, novo_salario):
        novo_salario = float(input(f'Digite o novo salário.'))
        self.__salario = novo_salario

    def calcular_salario_anual(self):
        self.__salario * 12
        return self.__salario
    
class Departamento:
    def __init__(self, nome):
        self.nome = nome
        self.funcionarios = []

    def adicionar_funcionario(self, novo_funcionario):
        self.novo_funcionario = novo_funcionario
        self.funcionarios.append(novo_funcionario)

    def calcular_total_salarios(self):
        total_salarios = 0
        for funcionario in self.funcionarios:
            total_salarios += funcionario.calcular_salario_anual()
        print(f'O total gasto com salários nesse departamento é de R${total_salarios}')

    def listar_funcionarios(self):
        for funcionario in self.funcionarios:
            print(f'Nome do funcionário: {funcionario.nome}\n Salário anual: R${funcionario.calcular_salario_anual()}')

funcionario1 = Funcionario('alo', 18, 10)
funcionario2 = Funcionario('ola', 17, 100)
funcionario3 = Funcionario('pare', 20, 200)

departamento = Departamento('matematica')

departamento.adicionar_funcionario(funcionario1)
departamento.adicionar_funcionario(funcionario2)
departamento.adicionar_funcionario(funcionario3)

departamento.listar_funcionarios()

departamento.calcular_total_salarios()

print(funcionario1.idade)
        

