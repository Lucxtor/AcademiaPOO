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
        print(f'''\nNome: {self.nome}\nIdade: {self.idade}\nCPF: {self.CPF}\nPeso: {self.peso}\nAltura: {self.altura}\nObjetivo: {self.objetivo}\n''')
        print('         M T N')
        for i in range(6):
            if i > 0:
                print('')
            print(self.diaSemana[i], end='  ')
            for j in range(3):
                print(self.horario[i][j], end=' ')
        print()
