import os

os.system("cls")

def verificar_valor(valor):
    if valor > 0:
        return "O valor é positivo."
    elif valor < 0:
        return "O valor é negativo."
    else:
        return "O valor é zero."

# Exemplo de uso:
numero = int(input("Digite um número inteiro: "))
resultado = verificar_valor(numero)
print(resultado)