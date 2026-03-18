import os

os.system("cls")

def ler_nota(mensagem):
    while True:
        nota = float(input(mensagem))
        if 0 <= nota <= 10:
            return nota
        else:
            print("Valor inválido! Digite uma nota entre 0 e 10.")

nota1 = ler_nota("Digite a primeira nota: ")
nota2 = ler_nota("Digite a segunda nota: ")
nota3 = ler_nota("Digite a terceira nota: ")

media = (nota1 + nota2 + nota3) / 3

print("Média:", media)

if media >= 7:
    print("Situação: Aprovado")
elif media >= 5:
    print("Situação: Recuperação")
else:
    print("Situação: Reprovado")