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

while True:
    menu = input('''\nDigite 1 para entrar na academia
Digite 2 para sair da academia
Digite 3 para cadastrar uma pessoa
Digite 4 para editar uma pessoa
Digite 5 para excluir uma pessoa
Digite 6 para cadastrar um aparelho
Digite 7 para encerrar o programa: ''')

    while menu not in '1234567':
        print(f'\nNúmero inválido, tente novamente:')
        menu = input('''\nDigite 1 para entrar na academia
Digite 2 para sair da academia
Digite 3 para cadastrar uma pessoa
Digite 4 para editar uma pessoa
Digite 5 para excluir uma pessoa
Digite 6 para cadastrar um aparelho
Digite 7 para encerrar o programa: ''')    
    
    
    if menu == '1':
        nomeEntrada = input('\nDigite o seu nome: ').capitalize()
        academia.entrar(nomeEntrada)

    elif menu == '2':
        nomeSaida = input('\nDigite o seu nome: ').capitalize()
        academia.sair(nomeSaida)

    elif menu == '3':
        nome = input('\nDigite o seu nome: ').capitalize()
        cpf = input('Digite o seu CPF: ')
        idade = int(input('Digite a sua idade: '))
        while idade < 0:
            print('\nNúmero inválido, a idade precisa ser maior do que 0')
            idade = int(input('Digite a sua idade: '))        
        
        print("\nInforme 1 para o dia e turno que deseja frequentar a academia e 0 para os dias que não deseja: ")
        for i in range(6):
            for j in range(3):
                matrizHorarios[i][j] = int(input(f'{listaDiasSemana[i]} de {listaTurnos[j]}: '))
                while matrizHorarios[i][j] != 0 and matrizHorarios[i][j] != 1:
                    print('\nNúemro inválido, utilize apenas 0 ou 1')
                    matrizHorarios[i][j] = int(input(f'{listaDiasSemana[i]} de {listaTurnos[j]}: '))
                    
        menuCadastro = input('''Digite 1 para cadastrar aluno \nDigite 2 para cadastrar professor: ''')
        while menuCadastro != '1' and menuCadastro != '2':
            print('\nNúemro inválido, utilize apenas 1 ou 2.Tente novamente')
            menuCadastro = input('''Digite 1 para cadastrar aluno \nDigite 2 para cadastrar professor: ''')
        
        if menuCadastro == '1':
            peso = float(input('Digite o seu peso em kg[Para separar a parte inteira da parte fracionária, utilize "."]: '))
            altura = float(input('Digite a sua altura em m[Para separar a parte inteira da parte fracionária, utilize "."]: '))
            objetivo = input('Digite o seu objetivo: ')
            auxAluno = academia.cadastrarAluno(nome, idade, cpf, matrizHorarios, peso, altura, objetivo)
            
        elif menuCadastro == '2':
            numeroCTPS = input('Digite o número da sua carteira de trabalho: ')
            auxProfessor = academia.cadastrarProfessor(nome, idade, cpf, matrizHorarios, numeroCTPS)
        
    elif menu == '6':
        nomeAparelho = input('\nDigite o nome do aparelho: ').capitalize()
        restricaoIdade = bool(input('Digite 0 se o aparelho puder ser usado por menores de 16 anos ou 1 se não puder: '))
        while restricaoIdade != 0 and restricaoIdade != 1:
                print('\nNúemro inválido, utilize apenas 0 ou 1')
                restricaoIdade = bool(input('Digite 0 se o aparelho puder ser usado por menores de 16 anos ou 1 se não puder: '))
                
        auxAparelho = academia.cadastrarAparelho(nomeAparelho,restricaoIdade)
        
    elif menu == '7':
        print('\nFIM !')
        break