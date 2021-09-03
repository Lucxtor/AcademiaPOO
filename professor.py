from pessoa import Pessoa

class Professor(Pessoa):
    def __init__(self, nome, idade, CPF, horario, numeroCarteira):
        Pessoa.__init__(self, nome, idade, CPF, horario)
        self.numeroCarteira = numeroCarteira

    def editarProfessor(self):
        pass
    
    def removerProfessor(self):
        pass
    
    def imprimir(self): #Polimorfismo
        print(f'\nNome:{self.nome}\nIdade:{self.idade}\nCPF: {self.CPF}\nNúmeroCTPS: {self.numeroCarteira}')
        print('\n         M T N')
        for i in range (6):
            if i > 0:
                print('')
            print(self.diaSemana[i], end='  ')
            for j in range(3):
                print(horário[i][j], end=' ')