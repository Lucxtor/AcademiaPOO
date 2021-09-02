from pessoa import Pessoa

class Aluno(Pessoa):
    def __init__(self, nome, idade, CPF, horario, peso, altura, objetivo):
        Pessoa.__init__(self, nome, idade, CPF, horario)
        self.peso = peso
        self.altura = altura
        self.objetivo = objetivo

    def editarAluno(self):
        pass
    
    def removerAluno(self):
        pass
        
    def imprimir(self): #Polimorfismo
        pass
