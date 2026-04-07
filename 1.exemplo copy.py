import os

#Limpa o terminal
# Cabeçalho.
#Função.
#Sem retorno
# Sem parâmetros.
def logo_senai() :
    os.system("cls")
    print("======  ======")
    print(" SENAI - BAHIA ")
    print("=====  ======")

# Chamar a função.
logo_senai()
nome = input("Digite seu nome: ")

logo_senai()
idade = int (input("Digite a sua idade: "))

logo_senai()
peso = float (input("Digite o seu peso: "))