# Sistema de Pedidos com RabbitMQ (MOM)

## Descrição

Este projeto demonstra o uso de Middleware Orientado a Mensagens (MOM) utilizando o paradigma de **Filas de Mensagens (Message Queue)**.

O estudo de caso escolhido foi um **Sistema de Pedidos de Lanchonete**, no qual um produtor envia pedidos para uma fila no RabbitMQ e dois consumidores processam esses pedidos de forma assíncrona.

Cada pedido é processado por apenas um consumidor, demonstrando o funcionamento do modelo ponto-a-ponto.

---

## Tecnologias Utilizadas

* Python
* RabbitMQ
* Docker
* Biblioteca pika

---

## Estrutura do Projeto

```text
MOM/

├── producer.py
├── consumer1.py
├── consumer2.py
├── requirements.txt
├── docker-compose.yml
└── README.md
```

---

## Como Executar

### 1. Iniciar o RabbitMQ

```bash
docker compose up -d
```

O painel administrativo estará disponível em:

http://localhost:15672

Login:

```
Usuário: guest
Senha: guest
```

---

### 2. Instalar as dependências

```bash
pip install -r requirements.txt
```

---

### 3. Executar os consumidores

Abra dois terminais.

Terminal 1:

```bash
python consumer1.py
```

Terminal 2:

```bash
python consumer2.py
```

---

### 4. Executar o produtor

Em outro terminal:

```bash
python producer.py
```

---

## Funcionamento

O produtor envia 10 pedidos para a fila denominada **pedidos**.

Os consumidores ficam aguardando novas mensagens.

Cada mensagem é entregue para apenas um consumidor, caracterizando o modelo de Filas de Mensagens.

Caso um consumidor seja encerrado durante a execução, o outro continuará processando todas as novas mensagens enviadas para a fila.

---

## Justificativa da Escolha

Foi utilizada a abordagem de **Filas de Mensagens (Message Queue)** porque o cenário representa uma situação em que cada pedido deve ser processado apenas uma vez. O RabbitMQ distribui automaticamente as mensagens entre os consumidores, permitindo balanceamento de carga e continuidade do processamento caso um consumidor fique indisponível.

---

## Paradigma Utilizado

* Middleware Orientado a Mensagens (MOM)
* Filas de Mensagens (Message Queue)