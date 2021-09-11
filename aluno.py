from pessoa import Pessoa
from lib import diaSemana

class Aluno(Pessoa):
    def __init__(self, nome, idade, CPF, horario, peso, altura, objetivo):  #Método construtor, iniciado quando um aluno é instanciado
        Pessoa.__init__(self, nome, idade, CPF, horario)                    #Método construtor da superclasse Pessoa, iniciado quando um aluno é instanciado
        self.peso = peso                                                    #Variável usada pra armazenar peso do aluno instanciado
        self.altura = altura                                                #Variável usada pra armazenar altura do aluno instanciado
        self.objetivo = objetivo                                            #Variável usada pra armazenar objetivo do aluno instanciado
        
    def imprimir(self): #Polimorfismo
        print(f'''\nNome: {self.nome}\nIdade: {self.idade}\nCPF: {self.CPF}\nPeso: {self.peso}\nAltura: {self.altura}\nObjetivo: {self.objetivo}\n''')
                                                                             #Imprime nome, idade, cpf, peso, altura e objetivo 
        print('\n         M T N')                                            #Impresão pra ajudar na leitura da matriz
        for i in range (6):                                                  #Linha 14-21 imprime a matriz pulando linha a cada dia que passa
            if i > 0:
                print('')
            print(diaSemana[i], end='  ')
            for j in range(3):
                print(self.horario[i][j], end=' ')
        print()
