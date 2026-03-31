import os

os.system("cls")

# Inicializa o vetor vazio
vetor = []

# Loop para receber 5 números
while True:
    if len(vetor) == 5:  # verifica se já temos 5 números
        break
    try:
        numero = float(input(f"Digite o {len(vetor)+1}º número: "))
        if numero < 0:
            numero = 0  # substitui negativos por 0
        vetor.append(numero)
    except ValueError:
        print("Por favor, digite um número válido.")

# Exibe os valores do vetor
print("Valores do vetor:")
for i, valor in enumerate(vetor):
    print(f"Posição {i}: {valor}") 

    