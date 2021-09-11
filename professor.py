from pessoa import Pessoa
from lib import diaSemana

class Professor(Pessoa):                                                                                       
    def __init__(self, nome, idade, CPF, horario, numeroCarteira):                                            #Método construtor, iniciado quando um professor é instanciado
        Pessoa.__init__(self, nome, idade, CPF, horario)                                                      #Método construtor da superclasse Pessoa, iniciado quando um professor é instanciado
        self.numeroCarteira = numeroCarteira                                                                  #Variável usada para gravar o número da CTPS do professor instanciado
    
    def imprimir(self): #Polimorfismo
        print(f'\nNome: {self.nome}\nIdade: {self.idade}\nCPF: {self.CPF}\nNúmeroCTPS: {self.numeroCarteira}')#Imprime nome, idade, cpf, número da CTPS, 
        print('\n         M T N')                                                                             #Impresão pra ajudar na leitura da matriz
        for i in range (6):                                                                                   #Linha 13-18 imprime a matriz pulando linha a cada dia que passa
            if i > 0:
                print('')
            print(diaSemana[i], end='  ')
            for j in range(3):
                print(self.horario[i][j], end=' ')
        print()