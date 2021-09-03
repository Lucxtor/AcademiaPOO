from aluno import Aluno
from aparelho import Aparelho
from academia import Academia
from pessoa import Pessoa
from professor import Professor


listaTurnos = ['Manhã', 'Tarde', 'Noite']
listaDiasSemana = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sabado']
matrizHorarios = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]

while True:
    menu = input('''\nDigite 1 para entrar na academia
Digite 2 para sair da academia
Digite 3 para cadastrar uma pessoa
Digite 4 para editar uma pessoa
Digite 5 para excluir uma pessoa
Digite 6 para cadastrar um aparelho:
Digite 7 para encerrar o programa: ''')

    if menu == '1':
        nomeEntrada = input('\nDigite o seu nome: ').capitalize()
        entrar(nomeEntrada)

    elif menu == '2':
        nomeSaida = input('\nDigite o seu nome: ').capitalize()
        sair(nomeSaida)

    elif menu == '3':
        nome = input('Digite o seu nome: ').capitalize()
        cpf = input('Digite o seu CPF: ')
        idade = int(input('Digite a sua idade: '))
        print("Informe 1 para o dia e turno que deseja frequentar a academia e 0 para os dias que não deseja: ")
        for i in range(6):
            for j in range(3):
                matrizHorarios[i][j] = input(f'{listaDiasSemana[i]} de {listaTurnos[j]}: ')
        menuCadastro = input('''Digite 1 para cadastrar aluno \nDigite 2 para cadastrar professor: ''')
        
        if menuCadastro == '1':
            peso = float(input('Digite o seu peso em kg: '))
            altura = float(input('Digite a sua altura em m: '))
            objetivo = input('Digite o seu objetivo: ')
            a1 = cadastrarAluno(nome, idade, CPF, matrizHorarios, peso, altura, objetivo)
            
        elif menuCadastro == '2':
            numeroCTPS = input('Digite o número da sua carteira de trabalho: ')
            p1 = Academia('Academia do Luis e Olavo',500)
            p1 = cadastrarProfessor(nome, idade, CPF, matrizHorarios, numeroCTPS)
        
    elif menu == '6':
        nomeAparelho = input('\nDigite o nome do aparelho: ').capitalize()
        restricaoIdade = bool(input('Digite 0 se o aparelho puder ser usado por menores de 16 anos ou 1 se não puder: '))
        aparelho1 = Aparelho(nomeAparelho,restricaoIdade)
        aparelhoCadastrado = aparelho1.cadastrarAparelho(nomeAparelho,restricaoIdade)
        if aparelhoCadastrado:
            aparelhoAcademia = Academia('Academia do Luis e Olavo',500)
            aparelhoAcademia.somaAparelho()    
        
        
    elif menu == '7':
        print('\nFIM !')
        break