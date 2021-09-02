from aluno import Aluno
from professor import Professor
from aparelho import Aparelho

class Academia:
 
    
    def __init__(self, nome, capacidadeMaximaLocal, aparelhos=[], professores=[], alunos=[]):
        self.nome = nome
        self.capacidadeMaximaLocal = capacidadeMaximaLocal
        self.aparelhos = aparelhos
        self.professores = professores
        self.alunos = alunos
        self.listaAlunos = []
        self.listaProfessores = []
        self.capacidadeMaximaDiaTurno = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
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
        pass
        #Verificar se é aluno ou professor, fazendo uma busca nas listas de aluno e professor
            #Se estiver, verificar se alunosDentro+1 é <= do que professoresDentro*8 e se alunosDentro+1 < aparelhos 
                #Se for, adicionar +1 em alunos dentro e imprimir 'Entrada realizada com sucesso'
                #Se não for, imprimir 'Academia com lotação máxima. Entrada negada!'
            #Se não estiver, imprimir 'Aluno não cadastrado'
            
            #Verificar se o nome do professor está na lista de professores
                #Se estiver, +1 em professoresDentro
                #Se não, imprimir mensagem 'Professor não cadastrado'

    def cadastrarAluno(self, aluno):
        pass
        #Verificar se nos dias e turnos desejados, alunosCadastrados+1 <= professoresCadastrados*8 e se alunosCadastrados+1 <= aparelhos
            #Se for, conclui o cadastro dos alunos e imprime 'Aluno cadastrado com sucesso'
            #Se não for, imprime 'Impossível cadastrar nesses dias e horários. Tente novamente'
        #Verificar se tem restrição de aparelhos
            #Se tiver, imprimir quais são os aparelhos disponíveis
            #Se não, imprimir o nome de todos os apelhos

    def cadastrarProfessor(self, professor):
        pass

    def cadastrarAparelho(self, nome, restricaoIdade, nPessoasTurno):
        self.aparelhos.append(Aparelho.__init__(nome, restricaoIdade, nPessoasTurno))
    
