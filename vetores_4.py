import os

os.system("cls")

vetor_notas = []
quantidade_notas = 4

print("Adicionando 4 notas ao vetor")
for i in range(quantidade_notas):
    nota = float(input(f"Digite a {i+1}ª nota: "))
    vetor_notas.append(nota)

media = sum(vetor_notas) / quantidade_notas

print("\nExibindo as notas informadas")

for uma_nota in vetor_notas:
    print(f"Nota: {uma_nota}")

print(f"Média: {media}")

if media >= 7:
    print("Aprovado")
elif media < 5:
    print("Em recuperação")
else:
    print("Reprovado")