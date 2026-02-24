import os

# Limpa o terminal.
os.system("cls")

print("- Solicitando dados -")
nome = input("Digite seu nome: ")

primeira_nota = float(input("Digite a primeira nota: "))
segunda_nota = float(input("Digite a segunda nota: "))

# Calcule.
media = (primeira_nota + segunda_nota) / 2

# Mostre o nome e a média.
print(f"Nome:  {nome}")
print(f"Média: {media}") 

# Verifique a situação do aluno.
if media >= 7:
    print("Aprovado")
else:
    print("Reprovado") 