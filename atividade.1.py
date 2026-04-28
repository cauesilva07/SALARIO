import os
os.system("cls")

usuarios = {}

def criar_usuario():
    nome = input("Digite o nome do usuário: ")
    if nome in usuarios:
        print("Usuário já existe!")
    else:
        usuario = nome
        print("Usuário criado com sucesso!")

def sacar():
    nome = input("Nome do usuário: ")
    if nome in usuarios:
        valor = float(input("Valor para saque: "))
        if usuarios[nome] >= valor:
            usuarios[nome] -= valor
            print("Saque realizado!")
        else:
            print("Saldo insuficiente!")
    else:
        print("Usuário não encontrado!")

def depositar():
    nome = input("Nome do usuário: ")
    if nome in usuarios:
        valor = float(input("Valor para depósito: "))
        usuarios[nome] += valor
        print("Depósito realizado!")
    else:
        print("Usuário não encontrado!")

def ver_saldo():
    nome = input("Nome do usuário: ")
    if nome in usuarios:
        print(f"Saldo: R$ {usuarios[nome]:.2f}")
    else:
        print("Usuário não encontrado!")

def menu():
    while True:
        print("\n=== BANCO SENAI DIGITAL ===")
        print("1 - Criar usuário")
        print("2 - Sacar")
        print("3 - Depositar")
        print("4 - Saldo")
        print("5 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            criar_usuario()
        elif opcao == "2":
            sacar()
        elif opcao == "3":
            depositar()
        elif opcao == "4":
            ver_saldo()
        elif opcao == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

menu()