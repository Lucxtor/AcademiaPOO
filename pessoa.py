from lib import diaSemana

class Pessoa:
    def __init__(self,nome, idade, CPF, horario):                                   #Método construtor, iniciado quando um aluno ou professor é instanciado
        self.nome = nome                                                            #Variável usada pra gravar nome da pessoa instanciada
        self.idade = idade                                                          #Variável usada pra gravar idade da pessoa instanciada
        self.CPF = CPF                                                              #Variável usada pra gravar CPF da pessoa instanciada
        self.horario = horario                                                      #Variável usada pra gravar matriz de horário da pessoa instanciada

    def imprimir(self): #Polimorfismo
        print(f'Nome: {self.nome}\nIdade: {self.idade}\nCPF: {self.CPF}\nHorário:') #Imprime nome, idade, cpf e horário da pessoa
        print('\n         M T N')                                                   #Impresão pra ajudar na leitura da matriz
        for i in range (6):                                                         #Linha 13-18 imprime a matriz pulando linha a cada dia que passa
            if i > 0:
                print('')
            print(diaSemana[i], end='  ')
            for j in range(3):
                print(self.horario[i][j], end=' ')