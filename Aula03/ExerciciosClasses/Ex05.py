#Crie uma classe Aluno com atributos para nome,
#matrícula e curso. Adicione métodos para mudar o curso do
#aluno e outro para exibir as informações do aluno.

class Aluno:
    def __init__(self, nome, matricula, curso):
        self.nome = nome
        self.matricula = matricula
        self.curso = curso

    def mudarcurso(self, curso):
        self.curso = curso

    def infos(self):
        print(f'O nome do aluno é {self.nome}, sua matrícula é {self.matricula} e seu curso é {self.curso}')
            
ver = Aluno('Marcos', '2020202', 'ADS')
ver.mudarcurso('matematica')
ver.infos()