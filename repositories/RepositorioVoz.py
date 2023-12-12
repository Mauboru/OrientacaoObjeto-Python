from entities.voz import Voice

class RepositorioVoice:
    def cadastrar(self, nome, genero):
        if nome == "" or genero == "":
            return ValueError("Nenhuma das variáveis pode ser nula")

        nova_voz = Voice(nome, genero)
        return self.nova_voz