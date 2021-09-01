from pessoa import Pessoa

class Professor(Pessoa):
    def __init__(self, nome, idade, CPF, numeroCarteira, diasTrabalho, turnosTrabalho):
        Pessoa.__init__(self, nome, idade, CPF)
        self.numeroCarteira = numeroCarteira
        self.diasTrabalho = diasTrabalho
        self.turnosTrabalho = turnosTrabalho

    def editar(self):
        pass