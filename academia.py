from aluno import Aluno
from professor import Professor
from aparelho import Aparelho
from lib import validaHorarioAluno, lerMatrizHorarios

class Academia:

    def __init__(self, nome, capacidadeMaximaLocal, aparelhos=[], professores=[], alunos=[]):                #Método construtor, iniciado quado uma academia é instanciada
        self.nome = nome                                                                                     #Variável usada para armazenar o nome da academia
        self.capacidadeMaximaLocal = capacidadeMaximaLocal                                                   #Variável usada para armazenar capacidade máxima de pessoas da academia
        self.aparelhos = aparelhos                                                                           #Lista usada para armazenar todos os aparelhos instanciados
        self.listaAlunos = alunos                                                                            #Lista usada para armazenar todos os alunos instanciados
        self.listaProfessores = professores                                                                  #Lista usada para armazenar todos os professores instanciados
        self.listaPessoas = []                                                                               #Lista usada para armazenar todas as pessoas cadastradas e se são alunos ou professores
        self.alunosDentro = 0                                                                                #Variável usada pra armazenar a quantidade de alunos dentro da academia 
        self.professoresDentro = 0                                                                           #Variável usada pra armazenar a quantidade de professores dentro da academia
        self.qtdeProfsDiaTurno = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]          #Matriz usada para verificar quantos professores tem em cada dia e turno
        self.qtdeAlunosDiaTurno = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]         #Matriz usada para verificar quantos alunos tem em cada dia e turno

    def entrar(self, nome):                                                                                  #Método de entrada na academia, recebendo um nome digitado como parâmetro
        if len(self.listaPessoas) == 0:                                                                      #Caso não tenha ninguém cadastrado, não entra no for 
            print("Primeiramente faça seu cadastro!")                                                        #Imprime mensagem "Primeiramente faça seu cadastro!"
        for i in range(len(self.listaPessoas)):                                                              #Repete(o número de elementos da listaPessoas)vezes o código da linha 24-39
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


    def sair(self, nome):                                                                                        #Método de saída da academia, recebendo um nome digitado como parâmetro
        if self.alunosDentro == 0 and self.professoresDentro == 0:                                               #Caso não tenha nenhuma pessoa na academia
            print('\nNão tem nenhuma pessoa dentro da academia que possa sair')                                  #Imprime mensagem de erro
        else:                                                                                                    #Caso tenha(m) pessoa(s)
            for i in range(len(self.listaPessoas)):                                                              #Repete(o número de elementos da listaPessoas)vezes o código da linha 46-59
                if nome == self.listaPessoas[i]['Nome']:                                                         #Verifica se o nome digitado é igual ao nome da posição i da listaPessoas
                    if self.listaPessoas[i]['tipoPessoa'] == 'Aluno':                                            #Verifica se tipo de pessoa relacionado ao nome da posição i da listaPessoas é aluno
                        self.alunosDentro -= 1                                                                   #Decrementa 1 da variável alunosDentro
                        print('\nSaída realizada com sucesso!')                                                  #Imprime mensagem "Saída realizada com sucesso!"
                        print(f'Bom descanso {nome}!')                                                           #Imprime mensagem "Bom descanso {nome}!"
                        break
                    else:                                                                                        #Caso o tipo de pessoa que quer entrar não seja aluno, então é professor
                        self.professoresDentro -= 1                                                              #Decrementa 1 da variável professoresDentro
                        print('\nSaída realizada com sucesso!')                                                  #Imprime mensagem "Saída realizada com sucesso!"
                        print(f'Bom descanso prof. {nome}!')                                                     #Imprime mensagem "Bom descanso {nome}!"
                        break
                elif i == (len(self.listaPessoas)-1):                                                            #Caso chegue na última posição e não encontre o nome
                    print('\nPessoa não encontrada nos cadastros da academia, verifique e tente novamente!')     #Imprime mensagem de erro
            
    def cadastrarAluno(self, nome, idade, CPF, horario, peso, altura, objetivo):                             #Método de cadastro de aluno, recebendo como parâmetros nome, idade, CPF, horario, peso, altura, objetivo
        cadastroAluno = validaHorarioAluno(self.aparelhos, idade, horario, self.qtdeAlunosDiaTurno, self.qtdeProfsDiaTurno, self.capacidadeMaximaLocal)                                                                 #Chama função para verificar se o aluno pode usar está grade de horarios
        if cadastroAluno:                                                                                    #Se passar pelas verificações
            for i in range(6):                                                                               #Repete 6 vezes linha 65-66
                for j in range(3):                                                                           #Repete 3 vezes linha 66
                    self.qtdeAlunosDiaTurno[i][j] += horario[i][j]                                           #Adiciona os horários escolhidos pelo aluno na matriz de horários de alunos      
            dicionarioAluno = {'Nome': nome, 'tipoPessoa': 'Aluno'}                                          #Criação de dicionário com nome do aluno e tipo de pessoa = Aluno
            a = Aluno(nome, idade, CPF, horario, peso, altura, objetivo)                                     #Instancia um aluno
            self.listaAlunos.append(a)                                                                       #Adiciona o aluno instanciado a listade alunos
            self.listaPessoas.append(dicionarioAluno)                                                        #Adiciona o dicionário criado a lista de pessoas
            a.imprimir()                                                                                     #Invoca o método imprimir para o aluno instanciado
            if idade < 16:                                                                                   #Verifica se a idade do aluno é <16
                print("\nO aluno cadastrado não pode utilizar os seguintes aparelhos: ")                     #Caso a idade seja <16, imprime a mensagem "O aluno cadastrado não pode utilizar os seguintes aparelhos: "
                for i in self.aparelhos:                                                                     #Repete(tamanho da lista de aparelhos)vezes linha 75-76
                    if i.restricaoIdade:                                                                     #Verifica se o aparelho tem restrição
                        print(i.nomeAparelho)                                                                #Caso tenha, imprime o nome do aparelho
            print('\nAluno cadastrado com sucesso')                                                          #Imprime a mensagem "Aluno cadastrado com sucesso"
            return a                                                                                         #Retorna o aluno instanciado

        else:                                                                                                #Caso o cadastro tenha sido inválidado
            print('Impossível cadastrar nesses dias e horários. Tente novamente')                            #Imprime mensagem de erro

    def cadastrarProfessor(self, nome, idade, CPF, horario, numeroCarteira):                                 #Método de cadastro de professor, recebendo como parâmetros nome, idade, CPF, horario, numeroCarteira
        p = Professor(nome, idade, CPF, horario, numeroCarteira)                                             #Instancia um professor
        for i in range(6):                                                                                   #Repete 6 vezes linha 86-87
            for j in range(3):                                                                               #Repete 3 vezes linha 87
                self.qtdeProfsDiaTurno[i][j] += horario[i][j]                                                #Adiciona horários escolhidos pelo professor na matriz de horário de profs
        self.listaProfessores.append(p)                                                                      #Adiciona o professor instanciado na lista de professores
        dicionarioProfessor = {'Nome': nome, 'tipoPessoa': 'Professor'}                                      #Criação de dicionário com nome do professor e tipo de pessoa = Professor
        self.listaPessoas.append(dicionarioProfessor)                                                        #Adiciona o dicionário criado na lista de pessoas
        p.imprimir()                                                                                         #Invoca o método impriimir do professor instanciado
        print('\nProfessor cadastrado com sucesso!')                                                         #Imprime a mensagem "Professor cadastrado com sucesso"
        return p                                                                                             #Retorna o professor instanciado

       
    def imprimeListaAlunos(self):                                                                            #Método usado para imprimir lista de alunos
        print('')                                                                                            #Pula uma linha na impresão
        for index,aluno in enumerate(self.listaAlunos):                                                      #Percorre lista de alunos                            
            print(f'{index+1}-{aluno.nome}')                                                                 #Imprime o nome dos alunos

    def imprimeListaProfessores(self):                                                                       #Método usado para imprimir lista de alunos
        print('')                                                                                            #Pula uma linha na impresão
        for index,professor in enumerate(self.listaProfessores):                                             #Percorre lista de professores 
            print(f'{index+1}-{professor.nome}')                                                             #Imprime o nome dos professores
            
    def editaAluno(self, nome):                                                                              #Método usado para editar aluno, recebe um nome como parâmetro
        for index,aluno in enumerate (self.listaAlunos):                                                     #Perccore lista de alunos
            if aluno.nome == nome:                                                                           #Se o nome digitado for igual a um nome cadastrado
                while True:                                                                                  #Enquanto o usuário não sair do menu
                    menuAluno = input('''\nDigite 1 para editar o nome do aluno
Digite 2 para editar idade
Digite 3 para editar cpf
Digite 4 para editar a matriz de horários
Digite 5 para editar peso
Digite 6 para editar altura
Digite 7 para editar objetivo
Digite 8 para sair: ''').strip()                                                                             #Entrada de variável para menu de edição do aluno
            
                    if menuAluno == '1':                                                                     #Se o usuário quiser editar o nome
                        novoNome = input('\nDigite o novo nome do aluno: ').capitalize()                     #Entrada do novo nome 
                        for pessoa in self.listaPessoas:                                                     #Percorre lista de pessoas
                            if aluno.nome == pessoa['Nome']:                                                 #Encontra posição do nome encontrado na lista de pessoas
                                pessoa['Nome'] = novoNome                                                    #Atribui novo nome ao nome da lista de pessoas                                        
                                aluno.nome = novoNome                                                        #Atribui novo nome ao nome da lista de alunos            
                                nome = novoNome                                                              #Atribui novo nome a varíavel nome, para que consiga permanecer no laço do menu 
                    elif  menuAluno == '2':                                                                  #Se o usuário quiser editar idade do aluno
                        aluno.idade = int(input('\nDigite a nova idade do aluno: '))                         #Variável que armazena idade recebe entrada de nova idade
                        while aluno.idade < 1:                                                               #Enquanto a idade digitada for menor do q 1
                            print('\nIdade inválida, o número deve ser > 0')                                 #Imprime mensagem de eero
                            aluno.idade = int(input('\nDigite a nova idade do aluno: '))                     #Nova entrada de idade
                    elif  menuAluno == '3':                                                                  #Se o usuário quiser editar o cpf do aluno
                        aluno.CPF = input('\nDigite o novo cpf do aluno: ')                                  #Variável que armazena idade recebe entrada de nova idade
                    elif  menuAluno == '4':                                                                  #Se o usuário quiser editar a matriz de horários do aluno                        
                        for j in range(6):                                                                   #Repete 6 vezes linha 135-136
                            for k in range(3):                                                               #Repete 3 vezes linha 136
                                self.qtdeAlunosDiaTurno[j][k] -= aluno.horario[j][k]                         #Remove os antigos horários escolhidos pelo aluno na matriz de horários de alunos
                        matrizHorarios = lerMatrizHorarios()                                                 #Invoca método para preencher matriz
                        atualizaAluno = validaHorarioAluno(self.aparelhos, aluno.idade, aluno.horario, self.qtdeAlunosDiaTurno, self.qtdeProfsDiaTurno, self.capacidadeMaximaLocal)
                        #Invocação de método para validar horário digitado
                        if atualizaAluno:                                                                    #Se os horários passados forem validados
                            aluno.horario = matrizHorarios                                                   #Adiciona os horários na lista de horários
                        else:                                                                                #Se não
                            print('\nImpossível cadastrar nesses dias e horários. Tente novamente')          #Imprime mensagem de erro
                            
                    elif  menuAluno == '5':                                                                  #Se o usuário quiser editar o peso
                        aluno.peso = float(input('\nDigite o novo peso do aluno: '))                         #Variável que armazena peso recebe entrada de novo peso
                        while aluno.peso < 1:                                                                #Enquanto a entrada for < 1, repete  linhas 148-149
                            print('\nPeso inválido, o número deve ser > 0')                                  #Imprime mensagem de erro
                            aluno.peso = float(input('\nDigite o novo peso do aluno: '))                     #Nova entrada de peso
                    elif  menuAluno == '6':                                                                  #Se o usuário quiser editar a altura
                        aluno.altura = float(input('\nDigite a nova altura do aluno: '))                     #Variável que armazena altura recebe entrada de nova altura
                        while aluno.altura < 0:                                                              #Enquanto a entrada for < 1, repete linhas 153-154
                            print('\nAltura inválida, o número deve ser > 0')                                #Imprime mensagem de erro
                            aluno.altura = float(input('\nDigite a nova altura do aluno: '))                 #Nova entrada de altura
                    elif  menuAluno == '7':                                                                  #Se o usuário quiser editar o objetivo
                        aluno.objetivo = input('\nDigite o novo objetivo do aluno: ')                        #Variável que armazena objetivo recebe entrada de novo objetivo
                    else:                                                                                    #Se o usuário quiser sair do menu
                        break                                                                                #"Quebra" laço do menu                         
                    aluno.imprimir()                                                                         #Depois da edição, invoca o método pra imprimir todas as informações atualizadas do aluno
                break                                                                                        #"Quebra laço do for"
            elif index == len(self.listaAlunos)-1:                                                           #Caso já esteja na última posição da lista, e não tenha encontrado o aluno                                          
                print('\nNome digitado não encontrado, tente novamente!')                                    #Imprime mensagem de erro
                break
        
    def editaProfessor(self, nome):                                                                          #Método usado para editar professor, recebe um nome como parâmetro
        for index, professor in enumerate (self.listaProfessores):                                           #Perccore lista de professores
            if professor.nome == nome:                                                                       #Se o nome digitado for igual a um nome cadastrado, entra no menu de edição do professor
                while True:                                                                                  #Enquanto não for encerrado, repete linhas 169-205
                    menuProfessor = input('''\nDigite 1 para editar o nome do professor
Digite 2 para editar idade
Digite 3 para editar cpf
Digite 4 para editar a matriz de horários
Digite 5 para editar número CTPS
Digite 6 para sair: ''').strip()                                                                            #Entrada de variável para menu de edição do professor                                      

                    if menuProfessor == '1':                                                                #Se o usuário quiser editar o nome
                        novoNome = input('\nDigite o novo nome do professor: ').capitalize()                #Entrada do novo nome 
                        for pessoa in self.listaPessoas:                                                    #Percorre lista de pessoas
                            if professor.nome == pessoa['Nome']:                                            #Encontra posição do nome encontrado na lista de pessoas
                                pessoa['Nome'] = novoNome                                                   #Atribui novo nome ao nome da lista de pessoas 
                                professor.nome = novoNome                                                   #Atribui novo nome ao nome da lista de professores
                    elif menuProfessor == '2':                                                              #Se o usuário quiser editar a idade
                        professor.idade = int(input('\nDigite a nova idade do professor: '))                #Variável que armazena idade recebe entrada de nova idade
                        while professor.idade < 1:                                                          #Enquanto a entrada for < 1, repete linha 185-186
                            print('\nIdade inválida, o número deve ser > 0')                                #Imprime mensagem  de eero 
                            professor.idade = int(input('\nDigite a nova idade do professor: '))            #Recebe nova entrada de idade
                    elif menuProfessor == '3':                                                              #Se o usuário quiser editar o cpf
                        professor.CPF = input('\nDigite o novo cpf do professor: ')                         #Variável que armazena cpf recebe entrada de novo cpf
                    elif menuProfessor == '4':                                                              #Se o alunos quiser editar os horários do professor
                        for j in range(6):                                                                  #Repete 6 vezes linha 191-192
                            for k in range(3):                                                              #Repete 3 vezes linha 192
                                self.qtdeProfsDiaTurno[j][k] -= professor.horario[j][k]                     #Remove os antigos horários escolhidos pelo aluno na matriz de horários de alunos
                        matrizHorarios = lerMatrizHorarios()                                                #Invoca método para preencher matriz
                        
                        professor.horario = matrizHorarios                                                  #Adiciona horário na variável q armazena o horário do professor
                        
                    elif menuProfessor == '5':                                                              #Se o professor quiser editar o número da CTPS
                        professor.numeroCarteira = input('\nDigite o novo número de CTPS do professor: ')   #Variável que armazena CTPS recebe entrada de novo CTPS
                    else:                                                                                   #Se o usuário quiser sair do menu
                        break                                                                               #"Quebra" o laço do menu de edição do professor
                    professor.imprimir()                                                                    #Imprime todas as informações atualizadas do professor
                break                                                                                       #"Quebra" o laço do for
            elif index == len(self.listaProfessores)-1:                                                     #Caso já esteja na última posição da lista, e não tenha encontrado o professor            
                print('\nNome digitado não encontrado, tente novamente!')                                   #Imprime mensagem de erro
                break                                                                                       #"Quebra" laço do for

    def removePessoa(self, nome):
        for index, pessoa in enumerate(self.listaPessoas):                                 #Percorre lista de pessoas                    
            if pessoa['Nome'] == nome:                                                     #Se o nome digitado for igua ao nome do cadastro
                if pessoa['tipoPessoa'] == 'Aluno':                                        #Se for aluno
                    for aluno in self.listaAlunos:                                         #Percorre lista de alunos
                        if aluno.nome == nome:                                             #Se o nome digitado for igua ao nome do cadastro
                            for i in range(6):                                             #Repete 6 vezes linha 214-215
                                for j in range(3):                                         #Repete 3 vezes linha 215
                                    self.qtdeAlunosDiaTurno[i][j] -= aluno.horario[i][j]   #Remove os horários escolhidos anteriormente pelo aluno na matriz de horários de alunos
                            self.listaAlunos.remove(aluno)                                 #Remove o aluno da lista de alunos
                            print('\nAluno excluído com sucesso!')                         #Mensagem de sucesso!
                else:                                                                      #Se for professor
                    for professor in self.listaProfessores:                                #Percorre lista de professores
                        if professor.nome == nome:                                         #Se o nome digitado for igua ao nome do cadastro
                            for i in range(6):                                             #Repete 6 vezes linha 222-223
                                for j in range(3):                                         #Repete 3 vezes linha 223
                                    self.qtdeProfsDiaTurno[i][j] -= professor.horario[i][j]#Remove os horários escolhidos anteriormente pelo professor na matriz de horários de professores
                            self.listaProfessores.remove(professor)                        #Remove professor da lista de professores
                            print('\nProfessor excluído com sucesso!')                     #Mensagem de sucesso!
                self.listaPessoas.remove(pessoa)                                           #Remove aluno ou professor da lista de pessoas
                break                                                                      #"Quebra" o laço
            elif index == len(self.listaPessoas)-1:                                        #Caso já esteja na última posição da lista, e não tenha encontrado a pessoa
                print('\nNome digitado não encontrado, tente novamente!')                  #Imprime mensagem de erro
                break

    def consultaPessoa(self, nome):                                 #Métoda para consultar pessoa, recebendo o nome como parâmentro
        for index, pessoa in enumerate(self.listaPessoas):           #Percorre lista de pessoas
            if pessoa['Nome'] == nome:                              #Se o nome digitado for igua ao nome do cadastro
                if pessoa['tipoPessoa'] == 'Aluno':                 #Se for aluno
                    for aluno in self.listaAlunos:                  #Percorre lista de alunos
                        if aluno.nome == nome:                      #Se o nome digitado for igual ao cadastrado
                            aluno.imprimir()                        #Invoca o método para imprimir todas as informações do aluno
                            break                                   #"Quebra" o laço de repetição da linha 233
                else:                                               #Se for professor
                    for professor in self.listaProfessores:         #Percorre lista de professores  
                        if professor.nome == nome:                  #Se o nome digitado for igual ao cadastrado
                            professor.imprimir()                    #Invoca o método para imprimir todas as informações do professor
                            break                                   #"Quebra" o laço de repetição da linha 233
            elif index == len(self.listaPessoas)-1:                 #Caso já esteja na última posição da lista, e não tenha encontrado a pessoa
                print('\nNome digitado não encontrado')             #Imprime mensagem de erro
                            
    def cadastrarAparelho(self, nomeAparelho, restricaoIdade):          #Método de cadastro de aparelho, recebendo como parâmetro o nome do aparelho e restrição de idade
        a = Aparelho(nomeAparelho, restricaoIdade)                      #Instancia aparelho
        self.aparelhos.append(a)                                        #Adiciona o aparelho instanciado na lista de aparelhos
        print("\nAparelho cadastrado com sucesso!")                     #Imprime mensagem "Aparelho cadastrado com sucesso!"
        return a                                                        #Retorna o aparelho instanciado

                            
    def consultaAparelho(self):               
        print('')                                                                                              #Pula uma linha na impressão
        for index,aparelho in enumerate (self.aparelhos):                                                      #Percorre lista de aparelhos 
            print(f'{index} - {aparelho.nomeAparelho}\n    Tem restrição? {aparelho.restricaoIdade}')          #Imprime nome dos aparelhos e se tem restrição
            
        while True:                                                                                            #Enquanto quiser continuar removendo os aparelhos
            removeAparelho = input('Deseja remover algum dos aparelhos listados?[S/N]: ').upper()              #Entrada de S/N para remover algum aparelho
            while removeAparelho not in 'S N':
                print('Dígito inválido Digite S para remover algum dos aparelhos ou N para encerrar a remoção')#Imprime mensagem de erro
                removeAparelho = input('Deseja remover algum dos aparelhos listados?[S/N]: ').upper()          #Nova entrada de S/N para remover algum aparelho
            if removeAparelho == 'S':                                                                          #Caso queira remover
                nomeAparelho = input('Digite o nome do aparelho que deseja remover: ').capitalize()            #Entrada de nome do aparelho que será removido
                for index, aparelho in enumerate(self.aparelhos):                                              #Percorre lista de aparelhos
                    if nomeAparelho == aparelho.nomeAparelho:                                                  #Caso o nome digitado seja igual ao nome cadastrado
                        self.aparelhos.remove(aparelho)                                                        #Remove aparelho da lista de aparelhos
                        print(f'\nAparelho {nomeAparelho} removido com sucesso!')                              #Imprime mensagem de sucesso
                        break                                                                                  #"Quebra" o laço
                    elif index == len(self.aparelhos)-1:                                                       #Caso já esteja na última posição da lista, e não tenha encontrado o aparelho
                        print(f'\nAparelho {nomeAparelho} não encontrado na lista de aparelhos da academia')   #Imprime mensagem de erro
            else: 
                break
        
