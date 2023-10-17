class Face:
    # Construtor e Atributos já declarados
    def __init__(self, nome, expressao):
        self.nome = nome
        self.expressao = expressao

    #Métodos Getters e Setters
    def set_nome(self, nome):
        self.nome = nome

    def set_expressao(self, expressao):
        self.expressao = expressao

    def get_nome(self):
        return self.nome
    
    def get_expressao(self):
        return self.expressao
    
    def resposta(self, resposta):
        if resposta == "chato":
            return "raiva"
        else:
            return None
        
class Voice:
    # Construtor e Atributos já declarados
    def __init__(self, nome, genero):
        self.nome = nome
        self.genero = genero

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