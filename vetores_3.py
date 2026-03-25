import os

os.system("cls")

# Criando um vetor.
vetor_notas = []
QUANTIDADE_NOTAS = 3

print("Adicionando 3 notas ao vetor")
for i in range(QUANTIDADE_NOTAS):
    nota = float(input(f"Digite a {i+1}ª nota: "))
    # Adicionando a nota ao vetor
    vetor_notas.append(nota)
    
# sum (vetor) = soma todas os valores no vetor.
media = sum(vetor_notas) / QUANTIDADE_NOTAS

print("\nExibindo as notas informadas")
# ForEach = percorre o vetor sem informar a quantidade.
# enumerate = através da variável i, numera a quantidade de repetições.
for i, uma_nota in enumerate(vetor_notas , start=1):
    print(f"{i}ª nota: {uma_nota}")

print(f"Média: {media}")

