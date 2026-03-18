import os

os.system("cls")

n1 = float(input())
while n1 < 0 or n1 > 10:
    n1 = float(input())

n2 = float(input())
while n2 < 0 or n2 > 10:
    n2 = float(input())

n3 = float(input())
while n3 < 0 or n3 > 10:
    n3 = float(input())

media = (n1 + n2 + n3) / 3

if media >= 7:
    print("Aprovado")
elif media >= 5:
    print("Recuperação")
else:
    print("Reprovado")