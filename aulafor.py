# lista_produtos = ["faca", "garfo", "panela", "frigideira", "flavorstone"]

# for produto in lista_produtos:
#     print(produto)


# lista_preco = [10, 10, 200, 50, 300] 

# for preco in lista_preco:
#     print(preco)

# produtos = {
#     "faca": 10,
#     "garfo": 10,
#     "panela": 200,
#     "frigideira": 50,
#     "flavorstone": 300,
# }

# for produto in produtos:
#     print(produto)
#     print(produtos[produto])


# for i in range(5):
#     print("cleiton.simon33@gmail.com")

# print(range(5))    


with open("../vendaloja.txt", "r") as arquivo:
    texto = arquivo.read()
print(texto.split("\n"))    

faturamento = 0

lista_texto = lista_texto[1:] # type: ignore

for linha in lista_texto:
    posicao_pv = linha.find(";")
    valor = float(linha[posicao_pv+1 : ])
    faturamento += valor
print(faturamento)

#excluir a 1ª linha
# para cada linha do meu arquivo 
#somar o valor que itvr depois do ;