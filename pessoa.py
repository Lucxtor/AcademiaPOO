from lib import diaSemana

class Pessoa:
    def __init__(self,nome, idade, CPF, horario):
        self.nome = nome
        self.idade = idade
        self.CPF = CPF
        self.horario = horario

    def imprimir(self): #Polimorfismo
        print(f'Nome: {self.nome}\nIdade: {self.idade}\nCPF: {self.CPF}\nHorário:')
        print('\n         M T N')
        for i in range (6):
            if i > 0:
                print('')
            print(diaSemana[i], end='  ')
            for j in range(3):
                print(self.horario[i][j], end=' ')