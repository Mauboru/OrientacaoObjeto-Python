class Voice:
    def __init__(self, nome, genero):
        self.__nome = nome
        self.__genero = genero

    #Métodos Getters e Setters
    def set_nome(self, nome):
        self.nome = nome

    def set_sexo(self, sexo):
        self.sexo = sexo

    def get_nome(self):
        return self.nome
    
    def get_sexo(self):
        return self.sexo
    
    def ouvinte(self, resposta):
        if resposta == "raiva":
            print("Expressão puto")
        else:
            print(None)