import os

# Função sem parametros e sem retorno.
def logo():
    os.system("cls")
    print("=======")
    print(" SENAI ")
    print("=======")

# Função com parametros e com retorno.
def somar(a, b):
    return a + b

# Função com parametros e com retorno.
def subtrair(a, b):
    return a - b


# Função com parametros e sem retorno.
def multiplicar(a, b):
    multiplicação = a * b
    print(f"Multiplicação: {multiplicação}")


#Função com parametros e sem retorno.
def dividir(a, b):
    divisão = a / b
    print(f"Divisão: {divisão}")


logo()
print(" - Solicitando dados")
n1 = int(input("Digite o primeiro numero: "))
n2 = int(input("Digite o segundo numero: "))

soma = somar(n1, n2)
subtração = subtrair(n1, n2)



logo()
print(" - Exibindo dados ")
print(f"Soma: {soma}")
print(f"Subtração: {subtração}")
multiplicar(n1, n2)
dividir(n1, n2)