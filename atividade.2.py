import os
os.system("cls")

# def inflacionar (preço)
#    return preço * 1.20 if preço >= 100 else preço * 1.10

def calcular_inflação(preço):
    if preço < 100:
    #inflação de 10%
        novo_preço * 1.10
    else:
# inflação de 20%
        novo_preço = preço *  1.20
    return novo_preço

preço_inicial = float(input("digite seu preço inicial:  "))
preço_final = calcular_inflação(preço_inicial)

print(f"O preço inflacionado é  R$ {preço_final:.2f}")