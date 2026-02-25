import os

os.system("cls || clear")

primeiro_numero = int(input("Digite o primeiro número: "))
segundo_numero = int(input("Digite o segundo número: "))

print(" - solicitando dados -")

maior = max(primeiro_numero, segundo_numero)
menor = min(primeiro_numero, segundo_numero)

print(" - Exibindo dados -")
print(f"Maior: {maior}")
print(f"Menor: {menor}") 
