class Voice:
    # Construtor e Atributos já declarados
    def __init__(self, nome, sexo):
        self.nome = nome
        self.sexo = sexo

    #Métodos Getters e Setters
    def set_nome(self, nome):
        self.nome = nome

    def set_sexo(self, sexo):
        self.sexo = sexo

    def get_nome(self):
        return self.nome
    
    def get_sexo(self):
        return self.sexo
    
    def ouvinte(resposta):
        if resposta == "raiva":
            print("Expressão puto")
        else:
            print(None)