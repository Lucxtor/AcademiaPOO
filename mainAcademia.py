from aluno import Aluno
from aparelho import Aparelho
from academia import Academia
from pessoa import Pessoa
from professor import Professor
from lib import lerMatrizHorarios

academia = Academia('Academia do Luis e Olavo', 500)
def cadastrarDadosBase():
    academia.cadastrarAparelho("Supino", True)
    academia.cadastrarAparelho("Cross-over", False)
    academia.cadastrarProfessor("Olavo", 19, 123, [[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]], 123)
    academia.cadastrarAluno("Luis", 19, 321, [[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [0, 0, 0]], 80, 1.8, "Fica shapado")
    academia.cadastrarAluno("Pedro", 15, 321, [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [1, 1, 1]], 80, 1.8, "Fica shapado")

cadastrarDadosBase()  #Função para instanciar academia e algumas informações para facilitar os testes

print("-="*50)
print(" "*(50-(round(len(academia.nome)/2))),academia.nome)
print("-="*50)

while True:                                                                                                #Enquanto o programa não for encerrado pelo usuário, repete linha 22-149                                              
    menu = input('''\nDigite 1 para entrar na academia                                                               
Digite 2 para sair da academia
Digite 3 para cadastrar uma pessoa
Digite 4 para editar uma pessoa
Digite 5 para remover uma pessoa
Digite 6 para cadastrar um aparelho
Digite 7 para consultar uma pessoa
Digite 8 para consultar aparelho
Digite 9 para encerrar o programa: ''').strip()                                                            #Entrada da variável menu

    while menu not in '1 2 3 4 5 6 7 8 9':                                                                 #Enquanto o número digitado pelo usuário não for uma das opções possíveis, repete linha 34-43
        print('\nNúmero inválido, tente novamente:')                                                       #Caso entre no laço, imprime a mensagem "Número inválido, tente novamente:"
        menu = input('''\nDigite 1 para entrar na academia                                                  
Digite 2 para sair da academia
Digite 3 para cadastrar uma pessoa
Digite 4 para editar uma pessoa
Digite 5 para remover uma pessoa
Digite 6 para cadastrar um aparelho
Digite 7 para consultar uma pessoa
Digite 8 para consultar aparelho
Digite 9 para encerrar o programa: ''').strip()                                                             #Nova entrada da variável menu
    
    #ENTRAR
    if menu == '1':                                                                                         #Se a opção 1 for escolhida, tenta entrar na academia
        nomeEntrada = input('\nDigite o seu nome: ').capitalize()                                           #Entrada de nome digitado pelo usuário
        academia.entrar(nomeEntrada)                                                                        #Invoca o método para entrar na academia
    #SAIR
    elif menu == '2':                                                                                       #Se a opção 2 for escolhida, tenta sair da academia
        nomeSaida = input('\nDigite o seu nome: ').capitalize()                                             #Entrada de nome digitado pelo usuário
        academia.sair(nomeSaida)                                                                            #Invoca o método para o nome  digitado sair da academia
    #CADASTRAR PESSOA
    elif menu == '3':                                                                                       #Se a opção 3 for escolhida, tenta cadastrar pessoa
        nome = input('\nDigite o seu nome: ').capitalize()                                                  #Entrada de nome digitado pelo usuário
        cpf = input('Digite o seu CPF: ')                                                                   #Entrada de CPF digitado pelo usuário
        idade = int(input('Digite a sua idade: '))                                                          #Entrada de idade, número inteiro digitado pelo usuário
        while idade < 0:                                                                                    #Enquanto a idade for < 0 repete linha 54-55
            print('\nNúmero inválido, a idade precisa ser maior do que 0')                                  #Imprime mensagem "Número inválido, a idade precisa ser maior do que 0"
            idade = int(input('Digite a sua idade[Deve ser um número inteiro > 0]: '))                      #Entrada de idade, número inteiro digitado pelo usuário
        
        matrizHorarios = lerMatrizHorarios()                                                                #Variável recebe o método lerMatrizHorários(usado para fazer o preenchimento da matriz)
                    
        menuCadastro = input('''\nDigite 1 para cadastrar aluno \nDigite 2 para cadastrar professor: ''').strip()   #Entrada para a variável menuCadastro
        while menuCadastro != '1' and menuCadastro != '2':                                                          #Enquanto a entrada for =! de 1 ou 2 repete linha 66-67
            print('\nNúemro inválido, utilize apenas 1 ou 2.Tente novamente')                                       #Imprime mensagem "Núemro inválido, utilize apenas 1 ou 2"
            menuCadastro = input('''Digite 1 para cadastrar aluno \nDigite 2 para cadastrar professor: ''').strip() #Nova entrada para a variável menuCadastro
        #CADASTRAR ALUNO
        if menuCadastro == '1':                                                                                                    #Se a opção 1 for escolhida, cadastra aluno
            peso = float(input('\nDigite o seu peso em kg[Para separar a parte inteira da parte fracionária, utilize "."]: '))     #Entrada de peso digitada pelo usuário
            while peso <= 0:                                                                                                       #Enquanto o peso digitado for < 0 repete linhas 72-73
                print('\nPeso inválido, o número precisa ser > 0')                                                                 #Mensagem de erro
                peso = float(input('\nDigite o seu peso em kg[Para separar a parte inteira da parte fracionária, utilize "."]: ')) #Nova entrada de peso digitada pelo usuário
            altura = float(input('Digite a sua altura em m[Para separar a parte inteira da parte fracionária, utilize "."]: '))    #Entrada de altura digitada pelo usuário
            while altura <= 0:                                                                                                     #Enquanto a altura digitado for < 0 repete linhas 76-77
                print('\nAltura inválida, o número precisa ser > 0')                                                               #Mensagem de erro
                altura = float(input('Digite a sua altura em m[Para separar a parte inteira da parte fracionária, utilize "."]: '))#Nova entrada de altura digitada pelo usuário
            objetivo = input('Digite o seu objetivo: ')                                                                            #Entrada de objetivo digitada pelo usuário
            auxAluno = academia.cadastrarAluno(nome, idade, cpf, matrizHorarios, peso, altura, objetivo)                           #Variável auxiliar usada para invocar o método de cadastro de aluno
        #CADASTRAR PROFESSOR  
        elif menuCadastro == '2':                                                                           #Se a opção 2 for escolhida, cadastra professor       
            numeroCTPS = input('Digite o número da sua carteira de trabalho: ')                             #Entrada de número CTPS digitada pelo usuário
            auxProfessor = academia.cadastrarProfessor(nome, idade, cpf, matrizHorarios, numeroCTPS)        #Variável auxiliar usada para invocar o método de cadastro de professor
    #EDITAR PESSOA
    elif menu == '4':                                                                                       #Se a opção 4 for escolhida, tenta editar uma pessoa
        menuCadastroEdicao = input('''\nDigite 1 para editar um aluno
Digite 2 para editar um professor
Digite 3 para sair: ''').strip()                                                                            #Entrada para escolher se vai editar prof ou aluno
        
        while menuCadastroEdicao != '1' and menuCadastroEdicao != '2' and menuCadastroEdicao != '3':        #Enquanto a entrada for =! de 1, 2 ou 3 repete linha 91-92
            print('\nNúemro inválido, utilize apenas 1,2 ou 3.Tente novamente')                             #Imprime mensagem de erro
            menuCadastroEdicao = input('''\nDigite 1 para editar aluno
Digite 2 para editar professor
Digite 3 para sair: ''').strip()                                                                            #Nova entrada para a variável menuCadastro
        #EDITAR ALUNO
        if menuCadastroEdicao == '1':                                                                                 #Se a opção aluno for escolhida
            academia.imprimeListaAlunos()                                                                             #Invoca um método pra imprimir a lista de alunos cadastrados
            escolheAluno = input('\nDigite o nome do aluno em que deseja-se fazer alterações: ').capitalize()         #Entrada para decidir em qual aluno se fará alterações
            academia.editaAluno(escolheAluno)                                                                         #Invocação de método pra pra editar o aluno digitado acima 
        #EDITAR PROFESSOR
        elif menuCadastroEdicao == '2':                                                                               #Caso a opção professor for escolhida
            academia.imprimeListaProfessores()                                                                        #Invoca um método pra imprimir a lista de professores cadastrados
            escolheProfessor = input('\nDigite o nome do professor em que deseja-se fazer alterações: ').capitalize() #Entrada para decidir em qual professor se fará alterações
            academia.editaProfessor(escolheProfessor)                                                                 #Invocação de método pra pra editar o professor escolhido acima 
    #REMOVER PESSOA
    elif menu == '5':                                                                                       #Se a opção 5 for escolhida, tenta remover pessoa
        print('\nAlunos')                                                                                   #Imprime lista de Alunos
        academia.imprimeListaAlunos()
        print('\nProfessores')                                                                              #Imprime lista de professores
        academia.imprimeListaProfessores() 
        nome = input("\nDigite o nome da pessoa que deseja remover: ").capitalize()                         #Entrada para receber nome da pessoa q será removida
        academia.removePessoa(nome)                                                                         #Invoca método pra remover a pessoa recebida acima
    #CADASTRAR APARELHO
    elif menu == '6':                                                                                                          #Se a opção 6 for escolhida, cadastra Aaparelho
        nomeAparelho = input('\nDigite o nome do aparelho: ').capitalize()                                                     #Entrada de nome do aparelho digitada pelo usuário
        restricaoIdade = bool(input('Digite 0 se o aparelho puder ser usado por menores de 16 anos ou 1 se não puder: '))      #Entrada de 0 ou 1 para indicar se o aparelho tem restrição de idade
        while restricaoIdade != 0 and restricaoIdade != 1:                                                                     #Equanto entrada =! de 0 ou 1 repete linha 118-119
            print('\nNúemro inválido, utilize apenas 0 ou 1')                                                                  #Imprime mensagem "Núemro inválido, utilize apenas 0 ou 1"
            restricaoIdade = bool(input('Digite 0 se o aparelho puder ser usado por menores de 16 anos ou 1 se não puder: '))  #Nova entrada de 0 ou 1 para indicar se o aparelho tem restrição de idade
                
        auxAparelho = academia.cadastrarAparelho(nomeAparelho,restricaoIdade)                               #Variável auxiliar usada para invocar método de cadastro de aparelho
    #CONSULTAR PESSOA
    elif menu == '7':                                                                                       #Caso a opção 7 seja escolhida, tenta consultar as informações das pessoas cadastradas
        while True:                                                                                         #Enquanto não tentarem encerrar o menu de consulta, repete linhas 125-143
            menuConsulta = input('''\nDigite 1 para exibir a lista de alunos                                                               
Digite 2 para exibir a lista de professores
Digite 3 para buscar pelo nome
Digite 4 para sair: ''')                                                                                       #Menu para decidir quem vai consultar
            while menuConsulta != '1' and menuConsulta != '2' and menuConsulta != '3' and menuConsulta != '4': #Enquanto a opção escolhida for inválida, repetelinha 130-133
                print('\nNúmero digitado inválido! Digite 1, 2, 3 ou 4')      
                menuConsulta = input('''\nDigite 1 para exibir a lista de alunos                                                               
Digite 2 para exibir a lista de professores
Digite 3 para buscar pelo nome: ''')                                                                            #Nova entrada no menu

            if menuConsulta == '1':                                                                             #Se decidirem imprimir a listar de alunos
                academia.imprimeListaAlunos()                                                                   #Invoca o método para imprimir a lista de alunos 
            elif menuConsulta == '2':                                                                           #Se decidirem imprimir a listar de professores
                academia.imprimeListaProfessores()                                                              #Invoca o método para imprimir a lista de alunos 
            elif menuConsulta == '3':                                                                           #Se decidirem nuscar pelo nome de uma pessoa
                nome = input("Digite o nome da pessoa que deseja buscar: ")                                     #Entrada para recber nome da pessoa que será impressa
                academia.consultaPessoa(nome)                                                                   #Invoca método pra consultar a pessoa digitada acima
            else:
                break
    #CONSULTAR/REMOVER APARELHO        
    elif menu == '8':                                                                                       #Se a opção de consultar aparelho for escolhida
        academia.consultaAparelho()                                                                         #Invoca método para consultar aparelho
    #ENCERRAR PROGRAMA
    elif menu == '9':                                                                                       #Se a opção for encerrar o programa
        print('\nFIM !')                                                                                    #Imprime mensagem de encerramento do programa 
        break                                                                                               #Quebra do laço do programa