Como rodar o Servidor SOAP:

Passo 1: Instalar o Java 8 no Codespaces, rode o comando:
sudo apt update && sudo apt install openjdk-8-jdk -y

Passo 2: Compilar e Rodar com o Java 8, rode o comando:
/usr/lib/jvm/java-8-openjdk-amd64/bin/javac CalculadoraIFRN.java

Passo 3: Após compilar, execute o servidor, rode o comando:
/usr/lib/jvm/java-8-openjdk-amd64/bin/java CalculadoraIFRN

Passo 4: Abra um novo terminal, conecte-se com o venv e vá ate a pasta SOAP

Passo 5: Instale o "zeep" no terminal, rode o comando:
pip install zeep 

Passo 6: Rode o cliente python pelo terminal, usando:
python cliente_ifrn.py