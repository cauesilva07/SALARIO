import os

os.system("cls")   

soma = 0
contador = 0

while True:
    nota = float(input("Digite a nota: "))
    soma += nota
    contador += 1

    resp = input("Deseja inserir outra nota? (S/N): ")

    if resp.upper() == "N":
        break

media = soma / contador

print("Média:", media)