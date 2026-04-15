# Variáveis para armazenar os números
numero1 = int(input("Digite o 1º número: "))
numero2 = int(input("Digite o 2º número: "))
numero3 = int(input("Digite o 3º número: "))
numero4 = int(input("Digite o 4º número: "))
numero5 = int(input("Digite o 5º número: "))

# Lista com todos os números para facilitar o processamento
numeros = [numero1, numero2, numero3, numero4, numero5]

# Variáveis para armazenar as estatísticas
quantidade_pares = 0
quantidade_impares = 0
quantidade_positivos = 0
quantidade_negativos = 0
soma_pares = 0
soma_impares = 0
soma_geral = 0

maior_numero = numeros[0]
menor_numero = numeros[0]

# Processando cada número
for numero in numeros:
    # Pares e ímpares
    if numero % 2 == 0:
        quantidade_pares += 1
        soma_pares += numero
    else:
        quantidade_impares += 1
        soma_impares += numero

    # Positivos e negativos
    if numero > 0:
        quantidade_positivos += 1
    elif numero < 0:
        quantidade_negativos += 1

    # Maior e menor número
    maior_numero = max(maior_numero, numero)
    menor_numero = min(menor_numero, numero)

    # Soma geral
    soma_geral += numero

# Calculando médias (opcional)
media_geral = soma_geral / len(numeros) if numeros else 0
media_pares = soma_pares / quantidade_pares if quantidade_pares else 0
media_impares = soma_impares / quantidade_impares if quantidade_impares else 0

# Imprimindo as estatísticas
print("\nEstatísticas dos números:")
print(f"Quantidade de pares: {quantidade_pares}")
print(f"Quantidade de ímpares: {quantidade_impares}")
print(f"Quantidade de positivos: {quantidade_positivos}")
print(f"Quantidade de negativos: {quantidade_negativos}")
print(f"Maior número: {maior_numero}")
print(f"Menor número: {menor_numero}")
print(f"Soma geral: {soma_geral}")
print(f"Média geral: {media_geral:.2f}")
print(f"Média dos pares: {media_pares:.2f}")
print(f"Média dos ímpares: {media_impares:.2f}")