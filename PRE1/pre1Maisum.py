class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.set_idade(idade)

    def set_idade(self, nova_idade):
        self.nova_idade = nova_idade
        if nova_idade < 18:
            nova_idade = int(input(f'Digite outra idade: '))
        self.idade = nova_idade

class Funcionario(Pessoa):
    def __init__(self, nome, idade, salario):
        super().__init__(nome, idade)
        self.set_salario(salario)

    def set_salario(self, novo_salario):
        while novo_salario <= 0:
            novo_salario = float(input(f'Digite um salário maior que zero.'))
        self.__salario = novo_salario

    def get_salario(self):
        return self.__salario

    def calcular_salario_anual(self):
        return self.__salario * 12
    
class Departamento:
    def __init__(self, nome):
        self.nome = nome
        self.funcionarios = []

    def adicionar_funcionario(self, novo_funcionario):
        self.novo_funcionario = novo_funcionario
        self.funcionarios.append(novo_funcionario)

    def calcular_total_salarios(self):
        total = 0
        for funcionario in self.funcionarios:
            total += funcionario.calcular_salario_anual()
        print(f'O total gasto com salários é R${total}')

    def listar_funcionarios(self):
        for funcionario in self.funcionarios:
            print(f'Nome do funcionário: {funcionario.nome}\nTotal anual: R${funcionario.calcular_salario_anual()}')

funcionario1 = Funcionario('alo', 20, 1)
funcionario2 = Funcionario('oi', 18, 100)
funcionario3 = Funcionario('ola', 20, 100)

departamento = Departamento('matematica')

departamento.adicionar_funcionario(funcionario1)
departamento.adicionar_funcionario(funcionario2)
departamento.adicionar_funcionario(funcionario3)

departamento.listar_funcionarios()




        