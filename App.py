from entities.voz import Voice
from entities.face import Face
# from repositories.RepositorioFace import RepositorioFace
from repositories.RepositorioVoz import RepositorioVoice
import os

if __name__ == '__main__':
    # Funções
    def menu():
        os.system('cls')
        print('------------ MENU -----------')
        print('| 1 - Cadastrar             |')
        print('| 2 - Listar                |')
        print('| 3 - Editar                |')
        print('| 4 - Excluir               |')
        print('| 5 - Sair                  |')
        print('-----------------------------')

    def cadastrar():
        os.system('cls')
        print('---------- CADASTRO ---------')
        print('| 1 - Cadastrar Voz        |')
        print('| 2 - Cadastrar Rosto      |')
        print('| 3 - Voltar ao Menu       |')
        print('-----------------------------')
        opcao_cadastro = int(input('Escolha uma opção de cadastro: '))

        if opcao_cadastro == 1:
            nome = input('Digite o nome: ')
            genero = input('Digite o genero da voz: ')
            RepositorioVoice.cadastrar(nome, genero)

        elif opcao_cadastro == 2:
            nome = input('Digite o nome: ')
            # Chame o repositório aqui para salvar o rosto
            # repository.salvar_rosto(Face(nome))

    def listar():
        return 1

    def editar():
        os.system('cls')
        print('---------- EDITAR -----------')
        print('| 1 - Editar Voz           |')
        print('| 2 - Editar Rosto         |')
        print('| 3 - Voltar ao Menu       |')
        print('-----------------------------')
        opcao_edicao = int(input('Escolha uma opção de edição: '))

    def excluir():
        os.system('cls')
        print('---------- EXCLUIR ----------')
        print('| 1 - Excluir Voz          |')
        print('| 2 - Excluir Rosto        |')
        print('| 3 - Voltar ao Menu       |')
        print('-----------------------------')
        opcao_exclusao = int(input('Escolha uma opção de exclusão: '))

    while True:
        menu()
        opcao = int(input('Escolha uma opção: '))

        if opcao == 1:
            cadastrar()
        elif opcao == 2:
            listar()
        elif opcao == 3:
            editar()
        elif opcao == 4:
            excluir()
        elif opcao == 5:
            print('Saindo')
            break
        else:
            input("Opção inválida!. Pressione ENTER para continuar")