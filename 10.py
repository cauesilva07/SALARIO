import os

os.system("cls")

soma_total = 0
soma_pares = 0
contador_total = 0
contador_pares = 0
contador_impares = 0

numero = int(input("Digite um número (0 para sair): "))

while numero != 0:
    soma_total += numero
    contador_total += 1

    if numero % 2 == 0:
        soma_pares += numero
        contador_pares += 1
    else:
        contador_impares += 1

    numero = int(input("Digite um número (0 para sair): "))

media_geral = soma_total / contador_total if contador_total > 0 else 0
media_pares = soma_pares / contador_pares if contador_pares > 0 else 0

print("Quantidade de números pares:", contador_pares)
print("Quantidade de números ímpares:", contador_impares)
print("Média dos valores pares:", media_pares)
print("Média geral:", media_geral)