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

    def cadastrarAluno(self, nome, idade, CPF, horario, peso, altura, objetivo):                             #Método de cadastro de aluno, recebendo como parâmetros nome, idade, CPF, horario, peso, altura, objetivo
        maxAparelhos = 0                                                                                     #Variável usada pra verificar quantos aparelhos o aluno pode usar 
        cadastroAluno = True                                                                                 #Por padrão, o cadastro é válido
        for i in self.aparelhos:                                                                             #Repetir(tamanho da lista de aparelhos)vezes linha 59-61
            maxAparelhos += 1                                                                                #Adiciona 1 a variável maxAparelhos
            if idade < 16 and i.restricaoIdade:                                                              #Verifica se a idade do aluno é menor do q 16 e se o aparelho tem restrição de idade
                maxAparelhos -= 1                                                                            #Decrementa em 1 a variável maxAparelhos
        for i in range(6):                                                                                   #Repete 6 vezes linha 63-66
            for j in range(3):                                                                               #Repete 3 vezes linha 64-66
                if horario[i][j] + self.qtdeAlunosDiaTurno[i][j] > self.qtdeProfsDiaTurno[i][j] * 8 or horario[i][j] + self.qtdeAlunosDiaTurno[i][j] > maxAparelhos or horario[i][j] + self.qtdeAlunosDiaTurno[i][j] > self.capacidadeMaximaLocal:
                                                                                                             #Verifica se o horário escolhido pelo aluno é válido, comparando com o número de profs em cada horário, número de aparelhos e capacidade do local           
                    cadastroAluno = False                                                                    #Se for inválido, torna o cadastro inválido

        if cadastroAluno:                                                                                    #Se passar pelas verificações
            for i in range(6):                                                                               #Repete 6 vezes linha 70-86
                for j in range(3):                                                                           #Repete 3 vezes linha 71-86
                    self.qtdeAlunosDiaTurno[i][j] += horario[i][j]                                           #Adiciona os horários escolhidos pelo aluno na matriz de horários de alunos      
            dicionarioAluno = {'Nome': nome, 'tipoPessoa': 'Aluno'}                                          #Criação de dicionário com nome do aluno e tipo de pessoa = Aluno
            a = Aluno(nome, idade, CPF, horario, peso, altura, objetivo)                                     #Instancia um aluno
            self.listaAlunos.append(a)                                                                       #Adiciona o aluno instanciado a listade alunos
            self.listaPessoas.append(dicionarioAluno)                                                        #Adiciona o dicionário criado a lista de pessoas
            a.imprimir()                                                                                     #Invoca o método imprimir para o aluno instanciado
            if idade < 16:                                                                                   #Verifica se a idade do aluno é <16
                print("\nO aluno cadastrado não pode utilizar os seguintes aparelhos: ")                     #Caso a idade seja <16, imprime a mensagem "O aluno cadastrado não pode utilizar os seguintes aparelhos: "
                for i in self.aparelhos:                                                                     #Repete(tamanho da lista de aparelhos)vezes linha 80-81
                    if i.restricaoIdade:                                                                     #Verifica se o aparelho tem restrição
                        print(i.nomeAparelho)                                                                #Caso tenha, imprime o nome do aparelho
            print('\nAluno cadastrado com sucesso')                                                          #Imprime a mensagem "Aluno cadastrado com sucesso"
            return a                                                                                         #Retorna o aluno instanciado

        else:                                                                                                #Caso o cadastro tenha sido inválidado
            print('Impossível cadastrar nesses dias e horários. Tente novamente')                            #Imprime a mensagem "Impossível cadastrar nesses dias e horários. Tente novamente"

    def cadastrarProfessor(self, nome, idade, CPF, horario, numeroCarteira):                                 #Método de cadastro de professor, recebendo como parâmetros nome, idade, CPF, horario, numeroCarteira
        p = Professor(nome, idade, CPF, horario, numeroCarteira)                                             #Instancia um professor
        for i in range(6):                                                                                   #Repete 6 vezes linha 91-92
            for j in range(3):                                                                               #Repete 3 vezes linha 92
                self.qtdeProfsDiaTurno[i][j] += horario[i][j]                                                #Adiciona horários escolhidos pelo professor na matriz de horário de profs
        self.listaProfessores.append(p)                                                                      #Adiciona o professor instanciado na lista de professores
        dicionarioProfessor = {'Nome': nome, 'tipoPessoa': 'Professor'}                                      #Criação de dicionário com nome do professor e tipo de pessoa = Professor
        self.listaPessoas.append(dicionarioProfessor)                                                        #Adiciona o dicionário criado na lista de pessoas
        p.imprimir()                                                                                         #Invoca o método impriimir do professor instanciado
        print('\nProfessor cadastrado com sucesso!')                                                         #Imprime a mensagem "Professor cadastrado com sucesso"
        return p                                                                                             #Retorna o professor instanciado

    def cadastrarAparelho(self, nomeAparelho, restricaoIdade):                                               #Método de cadastro de aparelho, recebendo como parâmetro o nome do aparelho e restrição de idade
        a = Aparelho(nomeAparelho, restricaoIdade)                                                           #Instancia aparelho
        self.aparelhos.append(a)                                                                             #Adiciona o aparelho instanciado na lista de aparelhos
        print("\nAparelho cadastrado com sucesso!")                                                          #Imprime mensagem "Aparelho cadastrado com sucesso!"
        return a                                                                                             #Retorna o aparelho instanciado
