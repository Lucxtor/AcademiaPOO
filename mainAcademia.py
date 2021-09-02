listaTurnos = ['Manhã', 'Tarde', 'Noite']
listaDiasSemana = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sabado']
matrizHorarios = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]


menu = input('''Digite 1 para entrar na academia
Digite 2 para sair da academia
Digite 3 para fazer um novo cadastro
Digite 4 para editar uma pessoa
Digite 5 para excluir uma pessoa: ''')

if menu == '1':
    pass
    #Verificar se é aluno ou professor pelo nome
    #Se for professor, só entra
    #Se for aluno, alunosDentro+1 <= professores*8 e alunosDentro+1 <= máximo da academia 
    
elif menu == '2':
    pass
    #Pedir nome do aluno
    #Invocar método 'Sair'
elif menu == '3':
    nome = input('Digite o seu nome: ').capitalize()
    cpf = input('Digite o seu CPF: ')
    idade = int(input('Digite a sua idade: '))
    print("Informe 1 para o dia e turno que deseja frequentar a academia e 0 para os dias que não deseja: ")
    for i in range(6):
        for j in range(3):
            matrizHorarios[i][j] = input(f'{listaDiasSemana[i]} de {listaTurnos[j]}: ')
    menuCadastro = input('''Digite 1 para cadastrar aluno 
Digite 2 para cadastrar professor: ''')
    if menuCadastro == '1':
        # diaSemana = input('Digite quais dias da semana o aluno irá a academia [Os dias devem estar separados por espaço][Ex:seg ter qua]').lower().split()
        # turno = input('Digite M para manhã, T para tarde, N para noite: ')
        peso = float(input('Digite o seu peso em kg: '))
        altura = float(input('Digite a sua altura em m: '))
        objetivo = input('Digite o seu objetivo: ')
        #dicionarioAluno = {'Nome':nome,'CPF':cpf,'Idade':idade,'Dias Semana':diaSemana,'Turno':turno,'Peso':peso,'Altura':altura,'Objetivo':objetivo}
        #listaAlunos.append = dicionarioAluno
        #Invocar método criaAluno
    elif menuCadastro == '2':
        # diaSemana = input('Digite quais dias da semana o aluno irá a academia [Os dias devem estar separados por espaço][Ex:seg ter qua]').lower().split()
        # turno = input('Digite M para manhã, T para tarde, N para noite: ')
        numeroCTPS = input('Digite o número da sua carteira de trabalho: ')
        #dicionarioProfessor = {'Nome':nome,'CPF':cpf,'Idade':idade,'Dias Semana':diaSemana,'Turno Trabalho':turno,'N Carteira Trabalho'numeroCTPS}
        #listaProfessores.append(dicionarioProfessor)
        #Invocar método criaProfessor