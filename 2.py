import os
os.system("cls || clear")

def ler_nota(ordem):
    print("===== Solicitando dados =====")
    while True:
        try:
            nota = float(input(f"Digite a nota do aluno {ordem} nota (0 a 10): "))
            if 0 <= nota <= 10:
                return nota
            else:
                print("Nota inválida. Digite um valor entre 0 e 10.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")

def calcular_media(nota1, nota2):
    media = (nota1 + nota2) / 2
    print(f"A média é: {media}")
    return media

def verificar_aprovacao(media):
    if media >= 7:
        print("Aluno aprovado!")
    else:
        print("Aluno reprovado!")

nota1 = ler_nota(1)
nota2 = ler_nota(2)

media = calcular_media(nota1, nota2)
print("_" * 20)
print(f"A média do aluno é: {media:.2f}")
