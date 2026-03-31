import os

os.system("cls")

# Inicializa o vetor vazio
vetor = []

# Loop para preencher o vetor com 5 números
for i in range(5):
    numero = float(input(f"Digite o {i+1}º número: "))
    vetor.append(numero)

# Inicializa contadores
quantidade_negativos = 0
soma_positivos = 0

# Percorre o vetor para contar negativos e somar positivos
for numero in vetor:
    if numero < 0:
        quantidade_negativos += 1
    elif numero > 0:
        soma_positivos += numero

# Exibe os resultados
print(f"Quantidade de números negativos: {quantidade_negativos}")
print(f"Soma dos números positivos: {soma_positivos}")