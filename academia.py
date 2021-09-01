from aluno import Aluno
from professor import Professor
from aparelho import Aparelho

class Academia:
    def __init__(self, nome, capacidadeMaxima, aparelhos=[], professores=[], alunos=[]):
        self.nome = nome
        self.capacidadeMaxima = capacidadeMaxima
        self.aparelhos = aparelhos
        self.nProfessores = professores
        self.nAlunos = alunos

    def entrar(self, nome):
        pass

    def cadastrarAluno(self, aluno):
        pass

    def cadastrarProfessor(self, professor):
        pass

    def cadastrarAparelho(self, nome, restricaoIdade, nPessoasTurno):
        self.aparelhos.append(Aparelho.__init__(nome, restricaoIdade, nPessoasTurno))
