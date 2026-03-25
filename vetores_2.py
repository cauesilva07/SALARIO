import os

os.system("cls")

# Criando um vetor.
vetor_notas = []
QUANTIDADE_NOTAS = 3

print("Adicionando 3 notas ao vetor")
for i in range(QUANTIDADE_NOTAS):
    nota = float(input(f"Informe a nota {i+1}: "))
    vetor_notas.append(nota)

print("\nExibindo as notas informadas") 
for uma_nota in vetor_notas:
    print(f"Nota: {uma_nota}")

    