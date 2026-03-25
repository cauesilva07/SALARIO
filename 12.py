import os
os.system("cls")

# Variáveis para armazenar dados
total_familias = 0
soma_salarios = 0
soma_filhos = 0
maior_salario = 0
menor_salario = 0

while True:
    print("\n--- PESQUISA PREFEITURA")
    print("1. Cadastrar família")
    print("2. Relatório")
    print("3. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        # Cadastrar família
        salario = float(input("Informe o salário da família: "))
        num_filhos = int(input("Informe o número de filhos: "))

        # Atualizar variáveis
        total_familias += 1
        soma_salarios += salario
        soma_filhos += num_filhos

        if total_familias == 1:
            maior_salario = salario
            menor_salario = salario
        else:
            if salario > maior_salario:
                maior_salario = salario
            if salario < menor_salario:
                menor_salario = salario

    elif opcao == "2":
        # Relatório
        if total_familias > 0:
            media_salarios = soma_salarios / total_familias
            media_filhos = soma_filhos / total_familias
            print("\n--- RELATÓRIO ---")
            print(f"Total de famílias: {total_familias}")
            print(f"Média de salários: R$ {media_salarios:.2f}")
            print(f"Média de filhos: {media_filhos:.2f}")
            print(f"Maior salário: R$ {maior_salario:.2f}")
            print(f"Menor salário: R$ {menor_salario:.2f}")
        else:
            print("Nenhuma família cadastrada.")
            