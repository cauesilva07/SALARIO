import os

os.system("clear")

while True:
    idade = int(input("Digite a idade: "))
    if idade < 18:
        print("Acesso negado.")
        print("Tente novamente.")
    else:
        print("Acesso permitido.")
        break

print("Programa encerrado.")