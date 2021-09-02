from pessoa import Pessoa

class Professor(Pessoa):
    def __init__(self, nome, idade, CPF, horario, numeroCarteira):
        Pessoa.__init__(self, nome, idade, CPF, horario)
        self.numeroCarteira = numeroCarteira

    def editarProfessor(self):
        pass
    
    def removerProfessor(self):
        pass