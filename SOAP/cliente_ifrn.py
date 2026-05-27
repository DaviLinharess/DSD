from zeep import Client
from zeep.exceptions import Fault

# Conecta ao servidor SOAP
url_wsdl = "http://localhost:8080/ws/calculadora?wsdl"
client = Client(url_wsdl)

print("=========================================")
print("         CALCULADORA DO IFRN-CNAT        ")
print("=========================================\n")

try:
    # Entrada de dados
    n1 = float(input("Digite a nota do 1º Bimestre (0 a 100): "))
    n2 = float(input("Digite a nota do 2º Bimestre (0 a 100): "))

    # Cálculo da média parcial
    media_parcial = client.service.calcularMediaParcial(n1, n2)
    print(f"\n Média Parcial Calculada pelo Servidor: {media_parcial:.1f}")

    # Verifica a situação inicial (passando 0 na PF)
    situacao = client.service.verificarSituacao(media_parcial, 0)
    print(f" Status Atual: {situacao}")

    # Se o aluno estiver de Prova Final
    # Lê o retorno do Java e decide se precisa pedir mais um input
    if "Apto a fazer a Prova Final" in situacao:
        print("\n-----------------------------------------")
        nota_pf = float(input("Digite a nota obtida na Prova Final (0 a 100): "))
        print("-----------------------------------------")
        
        # Reenvia os dados para a Operação 2, agora com a nota da PF calculada
        situacao_final = client.service.verificarSituacao(media_parcial, nota_pf)
        print(f"\n Resultado Final: {situacao_final}")

except Fault as erro:
    # Captura a exceção tratada lá no Java (digitar <0 ou >100)
    print(f"\n Erro de Validação do Servidor SOAP:")
    print(f" {erro.message}")

except ValueError:
    # Se digitar letras em vez de números
    print("\n Erro: Por favor, digite apenas valores numéricos válidos.")

print("\n=========================================")