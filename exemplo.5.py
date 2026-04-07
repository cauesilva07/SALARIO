import os

os.system("cls")


# Função para calcular a média
def calcular_media(nota1, nota2):
    return (nota1 + nota2) / 2

# Função para informar aprovação
def verificar_aprovacao(media):
    if media >= 7:
        return "Aprovado"
    else:
        return "Reprovado"

# Programa principal
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = calcular_media(nota1, nota2)
resultado = verificar_aprovacao(media)

print(f"Média: {media}")
print(f"Situação: {resultado}")
