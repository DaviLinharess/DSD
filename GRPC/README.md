# Sistema gRPC - Biblioteca

Projeto desenvolvido utilizando gRPC e Protocol Buffers para demonstrar a comunicação remota entre um cliente e um servidor.

## Instalar as dependências

```bash
pip install -r requirements.txt
```

## Gerar os stubs

Windows

```bash
python -m grpc_tools.protoc ^
-I proto ^
--python_out=. ^
--grpc_python_out=. ^
proto/livros.proto
```

Linux / macOS

```bash
python -m grpc_tools.protoc \
-I proto \
--python_out=. \
--grpc_python_out=. \
proto/livros.proto
```

Os seguintes arquivos serão gerados automaticamente:

- `livros_pb2.py`
- `livros_pb2_grpc.py`

## Executar o servidor

```bash
python server.py
```

## Executar o cliente

```bash
python client.py
```