import asyncio
import websockets
import json

# Armazena os clientes conectados (uso do set pra não ter duplicatas e ajudar a remover)
clientes_conectados = set()

async def gerenciar_conexao(websocket):
    # Adiciona o cliente a lista de conectados
    clientes_conectados.add(websocket)
    
    # Identificador do cliente (id do objeto websocket)
    cliente_id = id(websocket)
    print(f"[Conexão Aberta] Cliente conectado: {cliente_id}")

    try:
        # Loop ouvindo mensagens deste cliente
        async for mensagem in websocket:
            print(f"[Mensagem Recebida] de {cliente_id}: {mensagem}")
            
            # Formato de mensagem: JSON com campo "pedido"
            dados = json.loads(mensagem)
            
            # Cria a mensagem de broadcast para todos os clientes conectados
            resposta = json.dumps({
                "remetente": cliente_id,
                "texto": f"Novo pedido recebido: {dados['pedido']}"
            })
            
            # Broadcast: Envia para todos os clientes conectados simultaneamente
            websockets.broadcast(clientes_conectados, resposta)
            
    except websockets.exceptions.ConnectionClosed:
        # O cliente desconectou, o loop é quebrado e o cliente é removido
        pass
    finally:
        # Quando o loop quebra (cliente desconectou), remove do conjunto
        clientes_conectados.remove(websocket)
        print(f"[Conexão Encerrada] Cliente desconectado: {cliente_id}")

async def main():
    print("Servidor WebSocket rodando em ws://localhost:8765")
    # Inicia o servidor na porta 8765
    async with websockets.serve(gerenciar_conexao, "localhost", 8765):
        await asyncio.Future()  # Mantém o servidor rodando para sempre

if __name__ == "__main__":
    asyncio.run(main())