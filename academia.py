from aluno import Aluno
from professor import Professor
from aparelho import Aparelho

class Academia:
 
    
    def __init__(self, nome, capacidadeMaximaLocal, aparelhos=0, professores=[], alunos=[]):
        self.nome = nome
        self.capacidadeMaximaLocal = capacidadeMaximaLocal
        self.aparelhos = aparelhos
        self.professores = professores
        self.alunos = alunos
        self.listaAlunos = []
        self.listaProfessores = []
        self.listaPessoas = []
        self.alunosDentro = 0
        self.professoresDentro = 0
        self.cadastroAluno = True
        self.qtdeProfsDiaTurno = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
        self.qtdeAlunosDiaTurno = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
        # auxCapacidadeMaximaProfessores = 0
        # auxCapacidadeMaximaAparelhos = 0
        # for i in aparelhos:
        #     auxCapacidadeMaximaAparelhos += int(i.nPessoasTurno)
        # for i in ['M', 'T', 'N']:
        #    for j in ['seg', 'ter', 'qua', 'qui', 'sex', 'sab']:
        #         for p in professores:
        #             for ip in p.diasTrabalho:
        #                 for jp in p.turnosTrabalho:
        #                     if i == ip and j == jp:
        #                         auxCapacidadeMaximaProfessores += 8
        #         for a in aparelhos:
        #             auxCapacidadeMaximaAparelhos += int(a.nPessoasTurno)

    def entrar(self, nome):
        for i in range(len(listaPessoas)):
            if self.nome == listaPessoas[i][Nome]:
                if listaPessoas[i]['Tipo pessoa'] == 'Aluno':
                    if self.alunosDentro + 1 <= self.professoresDentro * 8 and self.alunosDentro + 1 <= aparelhos:
                        self.alunosDentro += 1
                        print('\nEntrada realizada com sucesso!')
                    else:
                        print('\nAcademia com lotação máxima. Entrada negada. Tente novamente mais tarde')
    
                elif listaPessoas[i]['Tipo pessoa'] == 'Professor':
                    professoresDentro += 1
                    print('\nEntrada realizada com sucesso!')
    
    def sair(self, nome):
        for i in range(len(listaPessoas)):
            if self.nome == listaPessoas[i][Nome]:
                if listaPessoas[i]['Tipo pessoa'] == 'Aluno':
                    self.alunosDentro -= 1
                    print('\nSaída realizada com sucesso!')
               
                elif listaPessoas[i]['Tipo pessoa'] == 'Professor':
                    professoresDentro -= 1
                    print('\nSaída realizada com sucesso!')
    

    
    
    def cadastrarAluno(self, aluno):
        for i in range (6):
            for j in range(3):
                if self.horarios[i][j]+self.qtdeAlunosDiaTurno[i][j] > self.qtdeProfDiaTurno[i][j]*8 or self.horarios[i][j]+self.qtdeAlunosDiaTurno[i][j] > self.aparelhos:
                    cadastroAluno = False
                    
        if cadastroAluno == True:
            for i in range (6):
                for j in range(3):
                    self.qtdeAlunosDiaTurno[i][j] = self.horarios[i][j] + self.qtdeAlunosDiaTurno[i][j]
            dicionarioAluno = {'Nome':self.nome,'CPF':self.cpf,'Idade':self.idade,'Dias Semana':self.diaSemana,'Turno':turno,'Peso':self.peso,'Altura':self.altura,'Objetivo':self.objetivo, 'Tipo pessoa':'Aluno'}
            listaAlunos.append = dicionarioAluno
            listaPessoas.append = dicionarioAluno
            print('\nAluno cadastrado com sucesso')
            
        else: 
            print('Impossível cadastrar nesses dias e horários. Tente novamente')
                

        
        #Verificar se tem restrição de aparelhos
            #Se tiver, imprimir quais são os aparelhos disponíveis
            #Se não, imprimir o nome de todos os apelhos

    def cadastrarProfessor(self, professor):
        dicionarioProfessor = {'Nome':self.nome,'CPF':self.cpf,'Idade':self.idade,'Dias Semana':self.diaSemana,'Turno':turno,'Peso':self.peso,'Altura':self.altura,'Objetivo':self.objetivo, 'Tipo pessoa':'Professor'}
        capacidadeMaximaDiaTurno += self.horario
        listaProfessores.append = dicionarioAluno
        listaPessoas.append = dicionarioProfessor
        for i in range(6):
            for j in range (3):
                self.capacidadeMaximaDiaTurno[i][j] = self.capacidadeMaximaDiaTurno[i][j] + self.horario[i][j]
        print('\nProfessor cadastrado com sucesso!')
        
    def somaAparelho(self):
        self.aparelhos += 1
