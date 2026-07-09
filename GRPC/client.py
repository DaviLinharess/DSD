import grpc

import livros_pb2
import livros_pb2_grpc


def menu():

    channel = grpc.insecure_channel("localhost:50051")

    stub = livros_pb2_grpc.LivroServiceStub(channel)

    while True:

        print("\n===== Biblioteca =====")
        print("1 - Cadastrar livro")
        print("2 - Listar livros")
        print("0 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":

            titulo = input("Título: ")
            autor = input("Autor: ")
            ano = int(input("Ano: "))

            resposta = stub.CadastrarLivro(

                livros_pb2.LivroRequest(
                    titulo=titulo,
                    autor=autor,
                    ano=ano
                )

            )

            print("\nLivro cadastrado!")
            print(f"ID: {resposta.livro.id}")

        elif opcao == "2":

            resposta = stub.ListarLivros(
                livros_pb2.Empty()
            )

            print("\n===== Livros =====")

            if not resposta.livros:
                print("Nenhum livro cadastrado.")
            else:
                for livro in resposta.livros:
                    print("-----------------------")
                    print(f"ID: {livro.id}")
                    print(f"Título: {livro.titulo}")
                    print(f"Autor: {livro.autor}")
                    print(f"Ano: {livro.ano}")

        elif opcao == "0":
            break

        else:
            print("Opção inválida.")


if __name__ == "__main__":
    menu()