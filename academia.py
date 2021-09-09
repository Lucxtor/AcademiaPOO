from aluno import Aluno
from professor import Professor
from aparelho import Aparelho
from lib import validaHorarioAluno, lerMatrizHorarios

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
        cadastroAluno = validaHorarioAluno(self.aparelhos, idade, horario, self.qtdeAlunosDiaTurno, self.qtdeProfsDiaTurno, self.capacidadeMaximaLocal)                                                                 #Chama função para verificar se o aluno pode usar está grade de horarios
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
    
    def imprimeListaAlunos(self):
        for index,aluno in enumerate(self.listaAlunos):
            print(f'{index+1}-{aluno.nome}')

    def imprimeListaProfessores(self):
        for index,professor in enumerate(self.listaProfessores):
            print(f'{index+1}-{professor.nome}')
            
    def editaAluno(self, nome):
        for i in self.listaAlunos:
            if i.nome == nome:
                while True:
                    menuAluno = input('''\nDigite 1 para editar o nome do aluno
Digite 2 para editar idade
Digite 3 para editar cpf
Digite 4 para editar a matriz de horários
Digite 5 para editar peso
Digite 6 para editar altura
Digite 7 para editar objetivo
Digite 8 para sair: ''')
            
                    if menuAluno == '1':
                        i.nome = input('Digite o novo nome do aluno: ').capitalize()
                    elif  menuAluno == '2':
                        i.idade = input('Digite a nova idade do aluno: ')
                        #Validar idade maior que 0
                    elif  menuAluno == '3':
                        i.cpf = input('Digite o novo cpf do aluno: ')
                    elif  menuAluno == '4':
                        for i in range(6):  # Repete 6 vezes linha 70-86
                            for j in range(3):  # Repete 3 vezes linha 71-86
                                self.qtdeAlunosDiaTurno[i][j] -= i.horario[i][j]  # remove os antigos horários escolhidos pelo aluno na matriz de horários de alunos
                        matrizHorarios = lerMatrizHorarios()
                        atualizaAluno = validaHorarioAluno(self.aparelhos, i.idade, i.horario, self.qtdeAlunosDiaTurno, self.qtdeProfsDiaTurno, self.capacidadeMaximaLocal)
                        if atualizaAluno:
                            i.horario = matrizHorarios
                    elif  menuAluno == '5':
                        i.peso = input('Digite o novo peso do aluno: ')
                        #Validar maior que 0
                    elif  menuAluno == '6':
                        i.altura = input('Digite a nova altura do aluno: ')
                        #Validar maior que 0
                    elif  menuAluno == '7':
                        i.objetivo = input('Digite o novo peso do aluno: ')
                    else:
                        break
                    i.imprimir()
            break
        
    def editaProfessor(self, nome):
        for i in self.listaProfessores:
            if i.nome == nome:
                while True:
                    menuProfessor = input('''\nDigite 1 para editar o nome do aluno
Digite 2 para editar idade
Digite 3 para editar cpf
Digite 4 para editar a matriz de horários
Digite 5 para editar número CTPS
Digite 6 para sair: ''')

                    if menuProfessor == '1':
                        i.nome = input('Digite o novo nome do professor: ').capitalize()
                    elif menuProfessor == '2':
                        i.idade = input('Digite a nova idade do professor: ')
                        #Validar maior que 0
                    elif menuProfessor == '3':
                        i.cpf = input('Digite o novo cpf do professor: ')
                    elif menuProfessor == '4':
                        matrizHorarios = lerMatrizHorarios()
                        i.horario = matrizHorarios
                    elif menuProfessor == '5':
                        i.numeroCarteira = input('Digite o novo número de CTPS do professor: ')
                    else:
                        break
                    i.imprimir()
            break

    def removePessoa(self, nome):
        for pessoa in self.listaPessoas:
            if pessoa['Nome'] == nome:
                if pessoa['tipoPessoa'] == 'Aluno':
                    for aluno in self.listaAlunos:
                        if aluno.nome == nome:
                            for i in range(6):  # Repete 6 vezes linha 70-86
                                for j in range(3):  # Repete 3 vezes linha 71-86
                                    self.qtdeAlunosDiaTurno[i][j] -= aluno.horario[i][j]  # Remove os horários escolhidos anteriormente pelo aluno na matriz de horários de alunos
                            self.listaAlunos.remove(aluno)
                else:
                    for professor in self.listaProfessores:
                        if professor.nome == nome:
                            for i in range(6):  # Repete 6 vezes linha 70-86
                                for j in range(3):  # Repete 3 vezes linha 71-86
                                    self.qtdeProfsDiaTurno[i][j] -= professor.horario[i][j]  # Remove os horários escolhidos anteriormente pelo professor na matriz de horários de professores
                            self.listaProfessores.remove(professor)
                self.listaPessoas.remove(pessoa)

    def consultaPessoa(self, nome):
        for pessoa in self.listaPessoas:
            if pessoa['Nome'] == nome:
                if pessoa['tipoPessoa'] == 'Aluno':
                    for aluno in self.listaAlunos:
                        if aluno.nome == nome:
                            aluno.imprimir()
                else:
                    for professor in self.listaProfessores:
                        if professor.nome == nome:
                            professor.imprimir()
        #Retornar caso não encontre nenhuma pessoa cadastrada