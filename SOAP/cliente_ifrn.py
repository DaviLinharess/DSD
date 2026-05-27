from zeep import Client
from zeep.exceptions import Fault

url_wsdl = "http://localhost:8080/ws/calculadora?wsdl"
client = Client(url_wsdl)

print("=== Aluno Aprovado Direto ===")
# Notas: 70 no primeiro bimestre (peso 2) e 80 no segundo (peso 3) -> Média 76
media1 = client.service.calcularMediaParcial(70, 80)
situacao1 = client.service.verificarSituacao(media1, 0)
print(f"Média Parcial calculada: {media1}")
print(f"Situação no SUAP: {situacao1}\n")


print("=== Aluno em Prova Final e Aprovado ===")
# Notas: 40 e 50 -> Média Parcial 46 (Ficou entre 20 e 60)
media2 = client.service.calcularMediaParcial(40, 50)
situacao2_antes = client.service.verificarSituacao(media2, 0)
print(f"Média Parcial calculada: {media2} -> Status: {situacao2_antes}")

# Aluno faz a Prova Final e tira 75 -> (46 + 75) / 2 = 60.5 (Aprovado)
situacao2_depois = client.service.verificarSituacao(media2, 75)
print(f"Após realizar a Prova Final (Nota 75): {situacao2_depois}\n")


print("=== Teste de Erro (Nota Inválida) ===")
try:
    # Forçando uma nota estourada para disparar a exceção (SOAP Fault)
    client.service.calcularMediaParcial(120, 50)
except Fault as erro:
    print(f"Sucesso na validação do erro!")
    print(f"Mensagem do Servidor Java: {erro.message}")