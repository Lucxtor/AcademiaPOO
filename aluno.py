from pessoa import Pessoa

class Aluno(Pessoa):
    def __init__(self, nome, idade, CPF, diaSemana, peso, altura, objetivo):
        Pessoa.__init__(self, nome, idade, CPF)
        self.diaSemana = diaSemana
        self.peso = peso
        self.altura = altura
        self.objetivo = objetivo

    def editarAluno(self):
        pass
    
    def removerAluno(self):
        
    def imprimir(self): #Polimorfismo