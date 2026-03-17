import os
import time

os.system("cls")

a = int(input("Digite um número: "))
b = int(input("Digite outro número: "))
c = int(input("Digite mais um número: "))

media = (a + b + c) / 3

if media >= 7:
    print("Aluno aprovado com média ")
elif media >= 4:
    print("Aluno em recuperação com média ")