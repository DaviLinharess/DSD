from concurrent import futures
import grpc

import livros_pb2
import livros_pb2_grpc


class LivroService(livros_pb2_grpc.LivroServiceServicer):

    def __init__(self):
        self.livros = []
        self.proximo_id = 1

    def CadastrarLivro(self, request, context):

        livro = livros_pb2.Livro(
            id=self.proximo_id,
            titulo=request.titulo,
            autor=request.autor,
            ano=request.ano
        )

        self.livros.append(livro)
        self.proximo_id += 1

        return livros_pb2.LivroResponse(livro=livro)

    def ListarLivros(self, request, context):

        return livros_pb2.ListaLivros(
            livros=self.livros
        )


def serve():

    server = grpc.server(
        futures.ThreadPoolExecutor(max_workers=10)
    )

    livros_pb2_grpc.add_LivroServiceServicer_to_server(
        LivroService(),
        server
    )

    server.add_insecure_port("localhost:50051")

    server.start()

    print("Servidor iniciado na porta 50051.")

    server.wait_for_termination()


if __name__ == "__main__":
    serve()