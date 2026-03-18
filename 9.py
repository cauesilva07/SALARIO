import os

os.system("cls")

soma = 0
contador = 0

valor = int(input("Digite um valor: "))

while valor >= 0:
    soma += valor
    contador += 1
    valor = int(input("Digite um valor: "))

media = soma / contador

print("Média:", media)