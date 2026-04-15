import os

# Função sem retorno que limpa a tela e mostra o logo
def logo_senai():
    os.system("cls || clear")
    print("=== SENAI ===\n")

# Função para cadastrar usuários e preencher as listas
def cadastrar_usuarios(nomes, idades, alturas, pesos):
    while True:
        logo_senai()
        nome = input("Digite o nome do usuário (ou digite 'sair' para encerrar): ")
        if nome.lower() == 'sair':
            break
        try:
            idade = int(input("Digite a idade do usuário: "))
            altura = float(input("Digite a altura do usuário (em metros): "))
            peso = float(input("Digite o peso do usuário (em quilogramas): "))
        except ValueError:
            print("Entrada inválida! Digite números válidos.")
            input("Pressione Enter para continuar...")
            continue

        nomes.append(nome)
        idades.append(idade)
        alturas.append(altura)
        pesos.append(peso)

# Função para exibir os usuários cadastrados
def exibir_usuarios(nomes, idades, alturas, pesos):
    logo_senai()
    print("Dados dos usuários:\n")
    for i in range(len(nomes)):
        print(f"Usuário {i+1}:")
        print("Nome:", nomes[i])
        print("Idade:", idades[i])
        print("Altura:", alturas[i], "metros")
        print("Peso:", pesos[i], "quilogramas")
        print()

# Função principal
def main():
    nomes = []
    idades = []
    alturas = []
    pesos = []

    cadastrar_usuarios(nomes, idades, alturas, pesos)
    exibir_usuarios(nomes, idades, alturas, pesos)

# Execução do programa
if __name__ == "__main__":
    main()