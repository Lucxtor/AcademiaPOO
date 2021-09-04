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

    def entrar(self, nome):
        if len(self.listaPessoas) == 0:
            print("Primeiramente faça seu cadastro!")
        for i in range(len(self.listaPessoas)):
            if nome == self.listaPessoas[i]['Nome']:
                if self.listaPessoas[i]['tipoPessoa'] == 'Aluno':
                    if self.alunosDentro + 1 <= self.professoresDentro * 8:
                        self.alunosDentro += 1
                        print('\nEntrada realizada com sucesso!')
                        print(f'Bem-vindo {nome}!')
                    else:
                        print('\nAcademia com lotação máxima. Entrada negada. Tente novamente mais tarde')
                    break
                else:
                    self.professoresDentro += 1
                    print('\nEntrada realizada com sucesso!')
                    print(f'Bem-vindo prof. {nome}!')
                    break
            elif i + 1 == range(len(self.listaPessoas)):
                print("\nCadastro não encontrado, verifique o nome inserido ou então realize seu cadastro: ")


    def sair(self, nome):
        for i in range(len(self.listaPessoas)):
            if nome == self.listaPessoas[i]['Nome']:
                if self.listaPessoas[i]['tipoPessoa'] == 'Aluno':
                    self.alunosDentro -= 1
                    print('\nSaída realizada com sucesso!')
                    print(f'Bom descanso {nome}!')
                else:
                    self.professoresDentro -= 1
                    print('\nSaída realizada com sucesso!')
                    print(f'Bom descanso prof. {nome}!')

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
