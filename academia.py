from aluno import Aluno
from professor import Professor
from aparelho import Aparelho


class Academia:

    def __init__(self, nome, capacidadeMaximaLocal, aparelhos=[], professores=[], alunos=[]):
        self.nome = nome
        self.capacidadeMaximaLocal = capacidadeMaximaLocal
        self.aparelhos = aparelhos
        self.listaAlunos = alunos
        self.listaProfessores = professores
        self.listaPessoas = []
        self.alunosDentro = 0
        self.professoresDentro = 0
        self.cadastroAluno = True
        self.qtdeProfsDiaTurno = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.qtdeAlunosDiaTurno = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]

    def entrar(self, nome):                                                                                  #Método de entrada na academia, recebendo um nome digitado como parâmetro
        if len(self.listaPessoas) == 0:                                                                      #Caso não tenha ninguém cadastrado, não entra no for 
            print("Primeiramente faça seu cadastro!")                                                        #Imprime mensagem "Primeiramente faça seu cadastro!"
        for i in range(len(self.listaPessoas)):                                                              #Repete(o número de elementos da listaPessoas)vezes o código da linha 25-40
            if nome == self.listaPessoas[i]['Nome']:                                                         #Verifica se o nome digitado é igual ao nome da posição i da listaPessoas
                if self.listaPessoas[i]['tipoPessoa'] == 'Aluno':                                            #Verifica se tipo de pessoa relacionado ao nome da posição i da listaPessoas é aluno
                    if self.alunosDentro + 1 <= self.professoresDentro * 8:                                  #Verifica se o número de alunos dentro + 1 é ≤ ao número de profs dentro                           
                        self.alunosDentro += 1                                                               #Se passar pela condição, adiciona 1 aos alunos dentro
                        print('\nEntrada realizada com sucesso!')                                            #Imprime mensagem "Entrada realizada com sucesso!"
                        print(f'Bem-vindo {nome}!')                                                          #Imprime mensagem "Bem-vindo {nome}!"
                    else:                                                                                    #Caso o número de alunos dentro + 1 seja > profs dentro * 8
                        print('\nAcademia com lotação máxima. Entrada negada. Tente novamente mais tarde')   #Imprime a mensagem "Academia com lotação máxima. Entrada negada. Tente novamente mais tarde"
                    break                                                                                    #'Quebra' o laço
                else:                                                                                        #Caso o tipo de pessoa que quer entrar não seja aluno, então é professor
                    self.professoresDentro += 1                                                              #Adiciona 1 aos professores dentro
                    print('\nEntrada realizada com sucesso!')                                                #Imprime mensagem "Entrada realizada com sucesso!"
                    print(f'Bem-vindo prof. {nome}!')                                                        #Imprime mensagem "Bem-vindo {nome}!"
                    break                                                                                    #'Quebra' o laço
            elif i+1 == (len(self.listaPessoas)):                                                            #Caso o nome não tenha sido encontrado e a lista já estiver na última posição
                print("\nCadastro não encontrado, verifique o nome inserido ou então realize seu cadastro: ")#Imprime a mensagem "Cadastro não encontrado, verifique o nome inserido ou então realize seu cadastro:" 


    def sair(self, nome):                                                                                    #Método de saída da academia, recebendo um nome digitado como parâmetro
        for i in range(len(self.listaPessoas)):                                                              #Repete(o número de elementos da listaPessoas)vezes o código da linha 45-53
            if nome == self.listaPessoas[i]['Nome']:                                                         #Verifica se o nome digitado é igual ao nome da posição i da listaPessoas
                if self.listaPessoas[i]['tipoPessoa'] == 'Aluno':                                            #Verifica se tipo de pessoa relacionado ao nome da posição i da listaPessoas é aluno
                    self.alunosDentro -= 1                                                                   #Decrementa 1 da variável alunosDentro
                    print('\nSaída realizada com sucesso!')                                                  #Imprime mensagem "Saída realizada com sucesso!"
                    print(f'Bom descanso {nome}!')                                                           #Imprime mensagem "Bom descanso {nome}!"
                else:                                                                                        #Caso o tipo de pessoa que quer entrar não seja aluno, então é professor
                    self.professoresDentro -= 1                                                              #Decrementa 1 da variável professoresDentro
                    print('\nSaída realizada com sucesso!')                                                  #Imprime mensagem "Saída realizada com sucesso!"
                    print(f'Bom descanso prof. {nome}!')                                                     #Imprime mensagem "Bom descanso {nome}!"

    def cadastrarAluno(self, nome, idade, CPF, horario, peso, altura, objetivo):
        maxAparelhos = 0
        cadastroAluno = True
        for i in self.aparelhos:
            maxAparelhos += 1
            if idade < 16 and i.restricaoIdade:
                maxAparelhos -= 1
        for i in range(6):
            for j in range(3):
                if horario[i][j] + self.qtdeAlunosDiaTurno[i][j] > self.qtdeProfsDiaTurno[i][j] * 8 or horario[i][j] + self.qtdeAlunosDiaTurno[i][j] > maxAparelhos or horario[i][j] + self.qtdeAlunosDiaTurno[i][j] > self.capacidadeMaximaLocal:
                    cadastroAluno = False

        if cadastroAluno:
            for i in range(6):
                for j in range(3):
                    self.qtdeAlunosDiaTurno[i][j] += horario[i][j]
            dicionarioAluno = {'Nome': nome, 'tipoPessoa': 'Aluno'}
            a = Aluno(nome, idade, CPF, horario, peso, altura, objetivo)
            self.listaAlunos.append(a)
            self.listaPessoas.append(dicionarioAluno)
            a.imprimir()
            if idade < 16:
                print("\nO aluno cadastrado não pode utilizar os seguintes aparelhos: ")
                for i in self.aparelhos:
                    if i.restricaoIdade:
                        print(i.nomeAparelho)
            print('\nAluno cadastrado com sucesso')
            return a

        else:
            print('Impossível cadastrar nesses dias e horários. Tente novamente')

    def cadastrarProfessor(self, nome, idade, CPF, horario, numeroCarteira):
        p = Professor(nome, idade, CPF, horario, numeroCarteira)
        for i in range(6):
            for j in range(3):
                self.qtdeProfsDiaTurno[i][j] += horario[i][j]
        self.listaProfessores.append(p)
        dicionarioProfessor = {'Nome': nome, 'tipoPessoa': 'Professor'}
        self.listaPessoas.append(dicionarioProfessor)
        p.imprimir()
        print('\nProfessor cadastrado com sucesso!')
        return p

    def cadastrarAparelho(self, nomeAparelho, restricaoIdade):
        a = Aparelho(nomeAparelho, restricaoIdade)
        self.aparelhos.append(a)
        print("\nAparelho cadastrado com sucesso!")
        return a
