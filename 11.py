import os

os.system("cls")

soma_salario = 0
contador_pessoas = 0
maior_idade = 0
menor_idade = 0
mulheres_salario5k = 0

opção = 0

while True:
    print("""
          --- MENU DA PESQUISA ---
1 - Adicionar pessoa
2 - Exibir resultados
    3 - Sair

    """)
    opção = int(input("Digite a opção desejada: "))

    match opção:
        case 1:
            idade = int(input("Digite a idade da pessoa: "))
            sexo = input("Digite o sexo da pessoa (M/F): ")
            salario = float(input("Digite o salário da pessoa: R$ "))

            soma_salario += salario
            contador_pessoas += 1

            maior_idade = max(maior_idade, idade)
            menor_idade = min(menor_idade, idade) 
            
            if sexo == "F" and salario > 5000:
                mulheres_salario5k += 1

            print("Pessoa adicionada com sucesso!")
        
        case 2:
            if contador_pessoas == 0:
                print("Nenhuma pessoa cadastrada.")
            else:
                media_salario = soma_salario / contador_pessoas
            
                print(f"Média de salário: R$ {media_salario:.2f}")
                print(f"Maior idade: {maior_idade}")
                print(f"Menor idade: {menor_idade}")
                print(f"Quantidade de mulheres com salário acima de R$ 5.000,00: {mulheres_salario5k}")
        case 3:
            print("Saindo do programa...")
            break
        case _:
            print("Opção inválida.")
