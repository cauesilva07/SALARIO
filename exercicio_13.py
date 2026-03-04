import os

os.system("cls")

media = float(input("Digite a média do aluno: "))
faltas = int(input("Digite o número de faltas:"))

if media >= 7 and faltas <= 40:
    print("Aluno aprovado!")

else:
    print("Aluno reprovado.")
    