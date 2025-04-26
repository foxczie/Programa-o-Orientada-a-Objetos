class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @property
    def idade(self):
        return self._idade
    
    @idade.setter
    def idade(self, nova_idade):
        while nova_idade < 18:
            nova_idade = int(input('Idade insuficiente. Digite novamente: '))
        self.__idade = nova_idade

class Funcionario(Pessoa):
    def __init__(self, nome, idade, salario):
        self.salario = salario
        super().__init__(nome, idade)

    @property
    def salario(self):
        print(f'Seu salário mensal é de R${self.__salario}.')
        return self.__salario

    @salario.setter
    def salario(self, novo_salario):
        self.novo_salario = novo_salario
        self.__salario = novo_salario

    def calcular_salario_anual(self):
        mensal = self.__salario * 12 
        return mensal

class Departamento:
    def __init__(self):
        self.__funcionarios = []
        
    def adicionar_funcionario(self, novo_funcionario):
        self.__funcionarios.append(novo_funcionario)
            
    def calcular_total_salarios(self):
        total_salario = 0
        for pessoa in self.__funcionarios:
            total_salario += pessoa.calcular_salario_anual()
        print(f'O total gasto com salários é de R${total_salario}')
        return total_salario

    def listar_funcionarios(self):
        for funcionario in self.__funcionarios:
            print(f'Funcionário: {funcionario.nome}\n Salário anual: R${funcionario.calcular_salario_anual()}. ')

funcionario1 = Funcionario('Amanda', 19, 2000)
funcionario2 = Funcionario('Leonardo', 25, 3000)
funcionario3 = Funcionario('Jorge', 17, 4000)

departamento = Departamento()

departamento.adicionar_funcionario(funcionario1)
departamento.adicionar_funcionario(funcionario2)
departamento.adicionar_funcionario(funcionario3)

departamento.listar_funcionarios()

departamento.calcular_total_salarios()

               
        