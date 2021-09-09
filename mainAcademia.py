from aluno import Aluno
from aparelho import Aparelho
from academia import Academia
from pessoa import Pessoa
from professor import Professor

listaTurnos = ['Manhã', 'Tarde', 'Noite']
listaDiasSemana = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sabado']
matrizHorarios = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
academia = Academia('Academia do Luis e Olavo',500)
academia.cadastrarAparelho("supino", True)
academia.cadastrarAparelho("Cross-over", False)
academia.cadastrarProfessor("Olavo", 19, 123, [[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]], 123)
academia.cadastrarAluno("Luis", 19, 321, [[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [0, 0, 0]], 80, 1.8, "Fica shapado")
academia.cadastrarAluno("Pedro", 15, 321, [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [1, 1, 1]], 80, 1.8, "Fica shapado")

print("-="*50)
print(" "*(50-(round(len(academia.nome)/2))),academia.nome)
print("-="*50)

while True:                                                                                                 #Enquanto o programa não encerrado pelo usuário, repete linha 22-91                                                
    menu = input('''\nDigite 1 para entrar na academia                                                               
Digite 2 para sair da academia
Digite 3 para cadastrar uma pessoa
Digite 4 para editar uma pessoa
Digite 5 para excluir uma pessoa
Digite 6 para cadastrar um aparelho
Digite 7 para consultar uma pessoa
Digite 8 para encerrar o programa: ''')                                                                     #Entrada da variável menu

    while menu not in '1 2 3 4 5 6 7 8':                                                                      #Enquanto o número digitado pelo usuário não for uma das opções possíveis, repete linha 31-38
        print(f'\nNúmero inválido, tente novamente:')                                                       #Caso entre no laço, imprime a mensagem "Número inválido, tente novamente:"
        menu = input('''\nDigite 1 para entrar na academia                                                  
Digite 2 para sair da academia
Digite 3 para cadastrar uma pessoa
Digite 4 para editar uma pessoa
Digite 5 para excluir uma pessoa
Digite 6 para cadastrar um aparelho
Digite 7 para consultar uma pessoa
Digite 8 para encerrar o programa: ''')                                                                     #Nova entrada da variável menu
    
    
    if menu == '1':                                                                                         #Se a opção escolhida for = 1, tenta entrar na academia
        nomeEntrada = input('\nDigite o seu nome: ').capitalize()                                           #Entrada de nome digitado pelo usuário
        academia.entrar(nomeEntrada)                                                                        #Invoca o método para entrar na academia

    elif menu == '2':                                                                                       #Se a opção escolhida for = 2 tenta sair da academia
        nomeSaida = input('\nDigite o seu nome: ').capitalize()                                             #Entrada de nome digitado pelo usuário
        academia.sair(nomeSaida)                                                                            #Invoca o método para sair da academia

    elif menu == '3':                                                                                       #Se a opção escolhida for = 3, tenta cadastrar pessoa
        nome = input('\nDigite o seu nome: ').capitalize()                                                  #Entrada de nome digitado pelo usuário
        cpf = input('Digite o seu CPF: ')                                                                   #Entrada de CPF digitado pelo usuário
        idade = int(input('Digite a sua idade: '))                                                          #Entrada de idade, número inteiro digitado pelo usuário
        while idade < 0:                                                                                    #Enquanto a idade for < 0 repete linha 54-55
            print('\nNúmero inválido, a idade precisa ser maior do que 0')                                  #Imprime mensagem "Número inválido, a idade precisa ser maior do que 0"
            idade = int(input('Digite a sua idade[Deve ser um número inteiro > 0]: '))                      #Entrada de idade, número inteiro digitado pelo usuário
        
        print("\nInforme 1 para o dia e turno que deseja frequentar a academia e 0 para os dias que não deseja: ") #Imprime mensagem para indicar como preenche os horários
        for i in range(6):                                                                                  #Repete 6 vezes linha 59-63
            for j in range(3):                                                                              #Repete 3 vezes linha 60-63 
                matrizHorarios[i][j] = int(input(f'{listaDiasSemana[i]} de {listaTurnos[j]}: '))            #Entrada de 0 ou 1 pelo usuário
                while matrizHorarios[i][j] != 0 and matrizHorarios[i][j] != 1:                              #Enquanto a entrada for diferente de 0 e 1 repete linha 62-63
                    print('\nNúemro inválido, utilize apenas 0 ou 1')                                       #Imprime mensagem "Núemro inválido, utilize apenas 0 ou 1"
                    matrizHorarios[i][j] = int(input(f'{listaDiasSemana[i]} de {listaTurnos[j]}: '))        #Entrada de 0 ou 1 pelo usuário
                    
        menuCadastro = input('''Digite 1 para cadastrar aluno \nDigite 2 para cadastrar professor: ''')     #Entrada para a variável menuCadastro
        while menuCadastro != '1' and menuCadastro != '2':                                                  #Enquanto a entrada =! de 1 ou 2 repete linha 67-68
            print('\nNúemro inválido, utilize apenas 1 ou 2.Tente novamente')                               #Imprime mensagem "Núemro inválido, utilize apenas 1 ou 2"
            menuCadastro = input('''Digite 1 para cadastrar aluno \nDigite 2 para cadastrar professor: ''') #Nova entrada para a variável menuCadastro
        
        if menuCadastro == '1':                                                                                                 #Se a opção 1 for escolhida, cadastra aluno
            peso = float(input('Digite o seu peso em kg[Para separar a parte inteira da parte fracionária, utilize "."]: '))    #Entrada de peso digitada pelo usuário
            altura = float(input('Digite a sua altura em m[Para separar a parte inteira da parte fracionária, utilize "."]: ')) #Entrada de altura digitada pelo usuário
            objetivo = input('Digite o seu objetivo: ')                                                                         #Entrada de objetivo digitada pelo usuário
            auxAluno = academia.cadastrarAluno(nome, idade, cpf, matrizHorarios, peso, altura, objetivo)                        #Variável usada para invocar o método de cadastro de aluno
            
        elif menuCadastro == '2':                                                                           #Se a opção 2 for escolhida, cadastra professor       
            numeroCTPS = input('Digite o número da sua carteira de trabalho: ')                             #Entrada de número CTPS digitada pelo usuário
            auxProfessor = academia.cadastrarProfessor(nome, idade, cpf, matrizHorarios, numeroCTPS)        #Variável usada para invocar o método de cadastro de professor
    
    elif menu == '4':
        menuCadastroEdicao = input('\nDigite 1 para editar um aluno\nDigite 2 para editar um professor: ')
        
        while menuCadastroEdicao != '1' and menuCadastroEdicao != '2':                                            #Enquanto a entrada =! de 1 ou 2 repete linha 85-86
            print('\nNúemro inválido, utilize apenas 1 ou 2.Tente novamente')                               #Imprime mensagem "Núemro inválido, utilize apenas 1 ou 2"
            menuCadastroEdicao = input('''Digite 1 para editar aluno \nDigite 2 para editar professor: ''') #Nova entrada para a variável menuCadastro
        
        if menuCadastroEdicao == '1':
            academia.imprimeListaAlunos()
            escolheAluno = input('\nDigite o nome do aluno em que deseja-se fazer alterações: ')
            academia.editaAluno(escolheAluno)
        else:
            academia.imprimeListaProfessores()
            escolheProfessor = input('\nDigite o nome do professor em que deseja-se fazer alterações: ')
            academia.editaProfessor(escolheProfessor)
            
    elif menu == '5':
        pass
    
    elif menu == '6':                                                                                                              #Se a opção 6 for escolhida, cadastra Aaparelho
        nomeAparelho = input('\nDigite o nome do aparelho: ').capitalize()                                                         #Entrada de nome do aparelho digitada pelo usuário
        restricaoIdade = bool(input('Digite 0 se o aparelho puder ser usado por menores de 16 anos ou 1 se não puder: '))          #Entrada de 0 ou 1 para indicar se o aparelho tem restrição de idade
        while restricaoIdade != 0 and restricaoIdade != 1:                                                                         #Equanto entrada =! de 0 ou 1 repete linha 84-85
            print('\nNúemro inválido, utilize apenas 0 ou 1')                                                                  #Imprime mensagem "Núemro inválido, utilize apenas 0 ou 1"
            restricaoIdade = bool(input('Digite 0 se o aparelho puder ser usado por menores de 16 anos ou 1 se não puder: '))  #Nova entrada de 0 ou 1 para indicar se o aparelho tem restrição de idade
                
        auxAparelho = academia.cadastrarAparelho(nomeAparelho,restricaoIdade)                               #Variável usada para invocar método de cadastro de aparelho
        
    elif menu == '8':                                                                                       #Se a opção for 8, encerra o programa
        print('\nFIM !')                                                                                    #Imprime mensagem de encerramento do programa 
        break                                                                                               #Quebra do laço do programa