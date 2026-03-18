import os

os.system("cls")

while True:
    login = input("Digite o login: ")
    senha = input("Digite a senha: ")

    if login == "admin" and senha == "1234":
        print("Acesso permitido!")
        break
    else:
        print("Login ou senha incorretos. Tente novamente.")