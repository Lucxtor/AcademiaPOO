diaSemana = ['Segunda','Terça  ','Quarta ','Quinta ','Sexta  ','Sábado ']
listaTurnos = ['Manhã', 'Tarde', 'Noite']
listaDiasSemana = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sabado']
matrizHorarios = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]

def validaHorarioAluno(aparelhos, idade, horario, qtdeAlunosDiaTurno, qtdeProfsDiaTurno, capacidadeMaximaLocal):
    maxAparelhos = len(aparelhos)                                                                                     #Variável usada pra verificar quantos aparelhos o aluno pode usar
    cadastroAluno = True
    for i in aparelhos:                                                                             #Repetir(tamanho da lista de aparelhos)vezes linha 59-61
        if idade < 16 and i.restricaoIdade:                                                              #Verifica se a idade do aluno é menor do q 16 e se o aparelho tem restrição de idade
            maxAparelhos -= 1                                                                            #Decrementa em 1 a variável maxAparelhos
    for i in range(6):                                                                                   #Repete 6 vezes linha 63-66
        for j in range(3):                                                                               #Repete 3 vezes linha 64-66
            if horario[i][j] + qtdeAlunosDiaTurno[i][j] > qtdeProfsDiaTurno[i][j] * 8 or horario[i][j] + qtdeAlunosDiaTurno[i][j] > maxAparelhos or horario[i][j] + qtdeAlunosDiaTurno[i][j] > capacidadeMaximaLocal:
                                                                                                         #Verifica se o horário escolhido pelo aluno é válido, comparando com o número de profs em cada horário, número de aparelhos e capacidade do local
                cadastroAluno = False                                                                    #Se for inválido, torna o cadastro inválido
    return cadastroAluno

def lerMatrizHorarios():
    print(
        "\nInforme 1 para o dia e turno que deseja frequentar a academia e 0 para os dias que não deseja: ")  # Imprime mensagem para indicar como preenche os horários
    for i in range(6):                                                                                        # Repete 6 vezes linha 59-63
        for j in range(3):                                                                                    # Repete 3 vezes linha 60-63
            i.matrizHorarios[i][j] = int(
                input(f'{listaDiasSemana[i]} de {listaTurnos[j]}: '))                                         # Entrada de 0 ou 1 pelo usuário
            while matrizHorarios[i][j] != 0 and matrizHorarios[i][
                j] != 1:                                                                                      # Enquanto a entrada for diferente de 0 e 1 repete linha 62-63
                print(
                    '\nNúemro inválido, utilize apenas 0 ou 1')                                               # Imprime mensagem "Núemro inválido, utilize apenas 0 ou 1"
                i.matrizHorarios[i][j] = int(
                    input(f'{listaDiasSemana[i]} de {listaTurnos[j]}: '))                                     # Entrada de 0 ou 1 pelo usuário
    return matrizHorarios