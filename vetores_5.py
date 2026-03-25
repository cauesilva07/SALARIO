import os

os.system("cls")

vetor_numeros = []
quantidade_numeros = 4

for i in range(quantidade_numeros):
    numero = float(input(f"Digite o  número {i+1}: "))
    vetor_numeros.append(numero)

    if len(vetor_numeros) > 0:
        maior_numero = max(vetor_numeros)
        menor_numero = min(vetor_numeros)
        
        print(f"O maior número é: {maior_numero}")
        print(f"O menor número é: {menor_numero}")
